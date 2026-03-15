from typing import Dict, Any, Optional
import json
import sqlite3
from pathlib import Path

class StorageBackend:
    def __init__(self, db_path: str = 'doc_check.db', json_path: str = 'doc_check.json'):
        self.db_path = db_path
        self.json_path = json_path
        self._init_sqlite()

    def _init_sqlite(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                id TEXT PRIMARY KEY,
                firm_name TEXT,
                data TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def save_case(self, case_id: str, firm_name: str, data: Dict[str, Any]):
        conn = sqlite3.connect(self.db_path)
        data_json = json.dumps(data)
        conn.execute('INSERT OR REPLACE INTO cases (id, firm_name, data) VALUES (?, ?, ?)', 
                     (case_id, firm_name, data_json))
        conn.commit()
        conn.close()

    def get_case(self, case_id: str) -> Optional[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT data FROM cases WHERE id = ?', (case_id,))
        result = cursor.fetchone()
        conn.close()
        return json.loads(result[0]) if result else None

    def update_status(self, case_id: str, status: str):
        conn = sqlite3.connect(self.db_path)
        conn.execute('UPDATE cases SET status = ? WHERE id = ?', (status, case_id))
        conn.commit()
        conn.close()

    def save_to_json(self, data: Dict[str, Any]):
        Path(self.json_path).write_text(json.dumps(data, indent=2))
