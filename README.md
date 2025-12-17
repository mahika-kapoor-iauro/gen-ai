# PDF Question-Answering RAG App

A locally-running Python application for extracting, chunking, and processing PDF documents using Retrieval Augmented Generation (RAG).

## Current Features

✅ PDF text extraction  
✅ Text chunking with configurable size and overlap  
✅ Chunk verification file generation  
⏳ Vector embeddings (coming next)  
⏳ LLM integration (coming next)  

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` to customize (or leave defaults):

```
PDF_FOLDER_PATH=./data/pdfs
OUTPUT_FOLDER_PATH=./data/chunks
CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

### 3. Add Your PDF Files

Place your PDF files in the `data/pdfs` folder:

```bash
mkdir -p data/pdfs
# Copy your PDF files here
```

### 4. Run the Pipeline

```bash
python run.py
```

## What Happens

The script will:

1. ✅ Find all PDF files in `data/pdfs`
2. ✅ Extract text from each PDF
3. ✅ Split text into chunks (500 characters with 100 character overlap by default)
4. ✅ Save chunks to `data/chunks/[filename]_chunks.txt` for visual verification

## Example Console Output

```
================================================================================
🚀 Starting PDF Ingestion and Chunking Pipeline
================================================================================

📖 Step 1: Loading PDF files...
🔍 Found 1 PDF file(s)
📄 PDF file 'example.pdf' opened successfully
📊 Total pages: 10
✅ PDF loaded successfully | Text extracted: 5234 characters

📋 Step 2: Processing 1 PDF(s)...

🔄 Processing: example.pdf
✂️  Text chunked successfully | Created 12 chunks
💾 Chunks saved to ./data/chunks/example_chunks.txt
✨ example.pdf processed successfully!
   └─ Chunks file: ./data/chunks/example_chunks.txt

================================================================================
✅ PDF Ingestion and Chunking Pipeline Complete!
================================================================================

💡 Tip: Check the chunks files in data/chunks/ folder to verify the output.
```

## Folder Structure

```
pdf-qa-rag-app/
├── src/
│   ├── config/
│   │   └── settings.py          # Configuration management
│   ├── services/
│   │   ├── pdf_loader.py        # PDF extraction
│   │   └── text_chunker.py      # Text chunking
│   ├── utils/
│   │   └── logger.py            # Logging setup
│   └── main.py                  # Main pipeline
├── data/
│   ├── pdfs/                    # Your PDF files go here
│   └── chunks/                  # Generated chunk files
├── run.py                       # Entry point
├── requirements.txt             # Dependencies
├── .env.example                 # Environment template
└── README.md                    # This file
```

## Troubleshooting

### "No PDF files found"
- Ensure your PDF files are in `data/pdfs/` folder
- Check file permissions
- Verify files have `.pdf` extension

### "No text could be extracted"
- The PDF might be image-based (scanned)
- Try another PDF file
- Check if the PDF is password-protected

### Import errors
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## Configuration Options

Edit `.env` or `src/config/settings.py`:

| Option | Default | Description |
|--------|---------|-------------|
| `CHUNK_SIZE` | 500 | Characters per chunk |
| `CHUNK_OVERLAP` | 100 | Overlapping characters between chunks |
| `PDF_FOLDER_PATH` | ./data/pdfs | Where to find PDFs |
| `OUTPUT_FOLDER_PATH` | ./data/chunks | Where to save chunks |

## Next Steps

After verifying chunks in `data/chunks/`, the next phase will:
- Convert chunks to vector embeddings
- Store embeddings in a vector database
- Integrate with an LLM for Q&A

## License

MIT