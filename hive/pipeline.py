from typing import List, Dict, Any
from dataclasses import dataclass
from hive.extractors.pdf_extractor import PDFExtractor
from hive.extractors.docx_extractor import DOCXExtractor
from hive.extractors.html_extractor import HTMLExtractor

@dataclass
class Document:
    content: str
    metadata: Dict[str, Any]
    doc_type: str

class Pipeline:
    def __init__(self):
        self.extractors = {
            'pdf': PDFExtractor(),
            'docx': DOCXExtractor(),
            'html': HTMLExtractor()
        }

    async def ingest(self, file_path: str, doc_type: str) -> Document:
        """Ingest a document and extract content based on type."""
        if doc_type.lower() not in self.extractors:
            raise ValueError(f"Unsupported document type: {doc_type}")
        extractor = self.extractors[doc_type.lower()]
        content, metadata = await extractor.extract(file_path)
        return Document(content=content, metadata=metadata, doc_type=doc_type)

    async def classify(self, document: Document) -> Dict[str, Any]:
        """Classify document content (placeholder for ML model or rule-based logic)."""
        # TODO: Integrate with classification model or rule engine
        return {'category': 'financial', 'confidence': 0.95}

    async def process(self, file_path: str, doc_type: str) -> Dict[str, Any]:
        """Full pipeline: ingest and classify."""
        doc = await self.ingest(file_path, doc_type)
        classification = await self.classify(doc)
        return {
            'document': doc.metadata,
            'classification': classification,
            'content': doc.content[:500]  # Truncate for summary
        }
