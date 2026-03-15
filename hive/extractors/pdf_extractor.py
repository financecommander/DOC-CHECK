from typing import Tuple, Dict, Any
import pdfplumber

class PDFExtractor:
    async def extract(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        """Extract text and metadata from a PDF file."""
        content = ""
        metadata = {}
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                content += page.extract_text() + "\n"
                if i == 0:  # First page metadata
                    metadata['page_count'] = len(pdf.pages)
        return content, metadata
