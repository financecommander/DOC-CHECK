from typing import Tuple, Dict, Any
from bs4 import BeautifulSoup
import asyncio

class HTMLExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        """
        Extract text and metadata from an HTML file.
        """
        loop = asyncio.get_event_loop()
        content = await loop.run_in_executor(None, self._extract_content, file_path)
        metadata = await loop.run_in_executor(None, self._extract_metadata, file_path)
        return content, metadata

    def _extract_content(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            return soup.get_text()

    def _extract_metadata(self, file_path: str) -> Dict[str, Any]:
        return {'source': file_path, 'format': 'html'}
