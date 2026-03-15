from typing import Tuple, Dict, Any
from bs4 import BeautifulSoup

class HTMLExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        """Extract text and metadata from an HTML file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            content = soup.get_text(separator='\n')
            metadata = {'title': soup.title.string if soup.title else 'Untitled'}
        return content, metadata
