import pdfplumber
from typing import Tuple, Dict, Any

class PDFExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        content = ""
        metadata = {}
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                content += page.extract_text() + "\n"
            metadata['page_count'] = len(pdf.pages)
        return content, metadata
