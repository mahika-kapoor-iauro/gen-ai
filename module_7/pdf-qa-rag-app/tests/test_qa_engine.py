import pytest
from src.services.qa_engine import QAEngine
from src.services.pdf_loader import PDFLoader
from src.services.vector_store import VectorStore

@pytest.fixture
def setup_qa_engine():
    pdf_loader = PDFLoader()
    vector_store = VectorStore()
    qa_engine = QAEngine(vector_store=vector_store, pdf_loader=pdf_loader)
    return qa_engine

def test_qa_engine_initialization(setup_qa_engine):
    qa_engine = setup_qa_engine
    assert qa_engine is not None
    assert isinstance(qa_engine.pdf_loader, PDFLoader)
    assert isinstance(qa_engine.vector_store, VectorStore)

def test_answer_question(setup_qa_engine):
    qa_engine = setup_qa_engine
    pdf_loader = qa_engine.pdf_loader
    pdf_loader.load("data/pdfs/sample.pdf")  # Assuming a sample PDF exists
    question = "What is the main topic of the PDF?"
    answer = qa_engine.answer_question(question)
    assert answer is not None
    assert isinstance(answer, str)  # Ensure the answer is a string

def test_no_answer_for_unrelated_question(setup_qa_engine):
    qa_engine = setup_qa_engine
    question = "This question is unrelated to the PDF content."
    answer = qa_engine.answer_question(question)
    assert answer == "I'm sorry, I cannot answer that question."  # Assuming this is the expected response for unrelated questions