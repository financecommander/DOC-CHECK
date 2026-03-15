from typing import List, Dict, Any
from dataclasses import dataclass
import asyncio

from hive.extractors.pdf import PDFExtractor

from hive.extractors.docx import DOCXExtractor

from hive.extractors.html import HTMLExtractor

@dataclass
class Document:
    content: str
    metadata: Dict[str, Any]
    type: str

class Pipeline:
    def __init__(self):
        self.extractors = {
            'pdf': PDFExtractor(),
            'docx': DOCXExtractor(),
            'html': HTMLExtractor()
        }

    async def process(self, file_path: str, doc_type: str) -> Document:
        """Process a document based on its type and extract content."""
        if doc_type not in self.extractors:
            raise ValueError(f"Unsupported document type: {doc_type}")
        
        extractor = self.extractors[doc_type]
        content, metadata = await extractor.extract(file_path)
        return Document(content=content, metadata=metadata, type=doc_type)

    async def classify(self, document: Document) -> Dict[str, Any]:
        """Classify the document content (placeholder for ML model integration)."""
        # TODO: Integrate with ML classification model
        return {'category': 'finance', 'confidence': 0.95}

    async def run(self, file_path: str, doc_type: str) -> Dict[str, Any]:
        """Run the full pipeline: extract and classify."""
        doc = await self.process(file_path, doc_type)
        classification = await self.classify(doc)
        return {
            'document': doc.metadata,
            'content': doc.content,
            'classification': classification
        }
