from PyPDF2 import PdfReader

class TextProcessor:
    @staticmethod
    def get_pdf_text(pdf_docs):
        """Extract text from PDF documents"""
        text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    @staticmethod
    def get_text_chunks(text, chunk_size=1000, overlap=100):
        """Split text into overlapping chunks"""
        chunks = []
        start = 0
        text_length = len(text)
        
        while start < text_length:
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap
            
        return chunks 