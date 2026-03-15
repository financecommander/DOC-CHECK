from typing import Tuple, Dict, Any
import docx
import asyncio

class DOCXExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        """
        Extract text and metadata from a DOCX file.
        """
        loop = asyncio.get_event_loop()
        content = await loop.run_in_executor(None, self._extract_content, file_path)
        metadata = await loop.run_in_executor(None, self._extract_metadata, file_path)
        return content, metadata

    def _extract_content(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    def _extract_metadata(self, file_path: str) -> Dict[str, Any]:
        return {'source': file_path, 'format': 'docx'}
