from typing import Dict, List, Any
from dataclasses import dataclass
import asyncio

from hive.extractors.pdf_extractor import PDFExtractor

from hive.extractors.docx_extractor import DOCXExtractor

from hive.extractors.html_extractor import HTMLExtractor

@dataclass
class Document:
    content: str
    metadata: Dict[str, Any]
    type: str

class DocumentPipeline:
    def __init__(self):
        self.extractors = {
            'pdf': PDFExtractor(),
            'docx': DOCXExtractor(),
            'html': HTMLExtractor()
        }

    async def process_document(self, file_path: str, doc_type: str) -> Document:
        """
        Process a document based on its type and extract content.
        """
        if doc_type not in self.extractors:
            raise ValueError(f"Unsupported document type: {doc_type}")
        
        extractor = self.extractors[doc_type]
        content, metadata = await extractor.extract(file_path)
        return Document(content=content, metadata=metadata, type=doc_type)

    async def classify_document(self, document: Document) -> Dict[str, Any]:
        """
        Classify the document based on content and metadata.
        TODO: Implement ML-based classification or rule-based logic.
        """
        return {'category': 'general', 'confidence': 0.9}

    async def run_pipeline(self, file_path: str, doc_type: str) -> Dict[str, Any]:
        """
        Run the full pipeline: extract and classify.
        """
        doc = await self.process_document(file_path, doc_type)
        classification = await self.classify_document(doc)
        return {
            'document': doc,
            'classification': classification
        }
