from typing import List, Dict, Any
from dataclasses import dataclass
from hive.extractors.pdf import PDFExtractor
from hive.extractors.docx import DOCXExtractor
from hive.extractors.html import HTMLExtractor

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
        extractor = self.extractors.get(doc_type)
        if not extractor:
            raise ValueError(f"Unsupported document type: {doc_type}")
        content, metadata = await extractor.extract(file_path)
        return Document(content=content, metadata=metadata, doc_type=doc_type)

    async def classify(self, document: Document) -> Dict[str, Any]:
        # TODO: Implement ML-based classification or rule-based categorization
        return {'category': 'unclassified', 'confidence': 0.0}

    async def process(self, file_path: str, doc_type: str) -> Dict[str, Any]:
        doc = await self.ingest(file_path, doc_type)
        classification = await self.classify(doc)
        return {
            'document': doc,
            'classification': classification
        }
