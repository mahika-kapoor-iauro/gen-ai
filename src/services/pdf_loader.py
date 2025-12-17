import os
from pathlib import Path
from PyPDF2 import PdfReader
from src.utils.logger import setup_logger
from src.config.settings import PDF_FOLDER_PATH

logger = setup_logger(__name__)

class PDFLoader:
    def __init__(self):
        self.pdf_folder = PDF_FOLDER_PATH
    
    def load_pdf(self, filename: str) -> str:
        """
        Load a single PDF file and extract text.
        
        Args:
            filename: Name of the PDF file (e.g., 'document.pdf')
        
        Returns:
            Extracted text from the PDF
        """
        file_path = os.path.join(self.pdf_folder, filename)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found at {file_path}")
        
        if not filename.lower().endswith('.pdf'):
            raise ValueError(f"File {filename} is not a PDF file")
        
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                num_pages = len(pdf_reader.pages)
                
                logger.info(f"📄 PDF file '{filename}' opened successfully")
                logger.info(f"📊 Total pages: {num_pages}")
                
                text = ""
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    extracted_text = page.extract_text()
                    if extracted_text:
                        text += extracted_text + "\n"
                
                if not text.strip():
                    raise ValueError("No text could be extracted from the PDF")
                
                logger.info(f"✅ PDF loaded successfully | Text extracted: {len(text)} characters")
                return text
                
        except Exception as e:
            logger.error(f"❌ Error loading PDF '{filename}': {str(e)}")
            raise
    
    def load_all_pdfs(self) -> dict:
        """
        Load all PDF files from the PDF folder.
        
        Returns:
            Dictionary with filename as key and extracted text as value
        """
        pdf_files = [f for f in os.listdir(self.pdf_folder) if f.lower().endswith('.pdf')]
        
        if not pdf_files:
            logger.warning(f"⚠️  No PDF files found in {self.pdf_folder}")
            return {}
        
        logger.info(f"🔍 Found {len(pdf_files)} PDF file(s)")
        
        all_texts = {}
        for filename in pdf_files:
            try:
                text = self.load_pdf(filename)
                all_texts[filename] = text
            except Exception as e:
                logger.error(f"Skipping {filename}: {str(e)}")
                continue
        
        return all_texts