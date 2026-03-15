import asyncio
from typing import Tuple, Dict, Any
import pdfplumber

class PDFExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        """Extract text and metadata from a PDF file."""
        loop = asyncio.get_event_loop()
        content, metadata = await loop.run_in_executor(None, self._extract_sync, file_path)
        return content, metadata

    def _extract_sync(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            metadata = {
                'page_count': len(pdf.pages),
                'file_path': file_path
            }
        return text, metadata
