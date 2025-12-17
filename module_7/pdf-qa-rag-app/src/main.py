from src.services.pdf_loader import PDFLoader
from src.services.vector_store import VectorStore
from src.services.qa_engine import QAEngine
from src.config.settings import Settings

def main():
    # Load settings
    settings = Settings()

    # Load PDF files
    pdf_loader = PDFLoader(data_directory=settings.DATA_DIRECTORY)
    documents = pdf_loader.load_pdfs()

    # Create vector store
    vector_store = VectorStore()
    embeddings = vector_store.create_embeddings(documents)

    # Initialize QA engine
    qa_engine = QAEngine(vector_store=vector_store)

    # Example question
    question = "What is the main topic of the PDF?"
    answer = qa_engine.answer_question(question)

    print(f"Question: {question}")
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()