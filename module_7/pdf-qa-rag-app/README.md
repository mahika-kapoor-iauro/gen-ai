# PDF Question-Answering App (RAG)

This project is a PDF Question-Answering application that utilizes Retrieval-Augmented Generation (RAG) techniques to answer questions based on the content of PDF documents. The application loads PDF files, extracts text, and uses a language model to generate answers.

## Project Structure

```
pdf-qa-rag-app
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   └── llm.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── pdf_loader.py
│   │   ├── vector_store.py
│   │   └── qa_engine.py
│   ├── types
│   │   ├── __init__.py
│   │   └── models.py
│   └── utils
│       ├── __init__.py
│       └── logger.py
├── data
│   └── pdfs
├── tests
│   ├── __init__.py
│   ├── test_pdf_loader.py
│   ├── test_vector_store.py
│   └── test_qa_engine.py
├── .env.example
├── .gitignore
├── requirements.txt
├── pytest.ini
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd pdf-qa-rag-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Copy the `.env.example` file to `.env` and fill in the required values.

6. **Run the application:**

   ```bash
   python run.py
   ```

## Usage

1. Place your PDF files in the `data/pdfs` directory.
2. Start the application using the command above.
3. Follow the prompts to ask questions based on the content of the loaded PDFs.

## Testing

To run the tests, use the following command:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.