import pytest
from src.services.pdf_loader import PDFLoader

def test_pdf_loader_loads_pdf():
    pdf_loader = PDFLoader()
    text = pdf_loader.load("data/pdfs/sample.pdf")  # Assuming a sample PDF exists in the data/pdfs directory
    assert text is not None
    assert len(text) > 0

def test_pdf_loader_invalid_file():
    pdf_loader = PDFLoader()
    with pytest.raises(FileNotFoundError):
        pdf_loader.load("data/pdfs/non_existent.pdf")