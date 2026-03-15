from bs4 import BeautifulSoup
from typing import Tuple, Dict, Any

class HTMLExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            content = soup.get_text()
            metadata = {'title': soup.title.string if soup.title else 'Untitled'}
        return content, metadata
