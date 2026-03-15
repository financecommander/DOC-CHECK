from typing import Tuple, Dict, Any
import pdfplumber
import asyncio

class PDFExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        """
        Extract text and metadata from a PDF file.
        """
        loop = asyncio.get_event_loop()
        content = await loop.run_in_executor(None, self._extract_content, file_path)
        metadata = await loop.run_in_executor(None, self._extract_metadata, file_path)
        return content, metadata

    def _extract_content(self, file_path: str) -> str:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            return text

    def _extract_metadata(self, file_path: str) -> Dict[str, Any]:
        return {'source': file_path, 'format': 'pdf'}
