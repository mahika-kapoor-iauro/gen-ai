import os
from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ============================================================================
# STEP 1: CONFIGURE DOCUMENT SOURCE
# ============================================================================
# This tells the program where to find your legal documents
DOCUMENTS_FOLDER = "/Users/mahikakapoor/Documents/works/gen ai/gen ai data"
SUPPORTED_FORMATS = [".pdf", ".txt"]

# ============================================================================
# STEP 2: DOCUMENT LOADER FUNCTION
# ============================================================================
def load_documents(folder_path: str) -> List:
    """
    Load all legal documents from a specified folder.
    
    This function:
    1. Scans the folder for PDF and TXT files
    2. Reads each file using the appropriate loader
    3. Returns a list of document objects that LangChain can work with
    
    Args:
        folder_path: Path to the folder containing your legal documents
        
    Returns:
        A list of loaded documents with their content
    """
    documents = []
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' does not exist.")
        print(f"Please create this folder and add your legal documents there.")
        return documents
    
    # Find all supported document files
    folder = Path(folder_path)
    files_found = list(folder.glob("*.pdf")) + list(folder.glob("*.txt"))
    
    if not files_found:
        print(f"⚠️  No documents found in '{folder_path}'")
        print(f"Supported formats: {SUPPORTED_FORMATS}")
        return documents
    
    print(f"📄 Found {len(files_found)} document(s) to process...\n")
    
    # Load each document
    for file_path in files_found:
        try:
            if file_path.suffix.lower() == ".pdf":
                # For PDF files, use PyPDFLoader
                loader = PyPDFLoader(str(file_path))
                loaded_docs = loader.load()
                documents.extend(loaded_docs)
                print(f"✅ Loaded PDF: {file_path.name} ({len(loaded_docs)} pages)")
                
            elif file_path.suffix.lower() == ".txt":
                # For text files, use TextLoader
                loader = TextLoader(str(file_path))
                loaded_docs = loader.load()
                documents.append(loaded_docs[0])
                print(f"✅ Loaded TXT: {file_path.name}")
                
        except Exception as e:
            print(f"❌ Error loading {file_path.name}: {str(e)}")
    
    return documents

# ============================================================================
# STEP 3: TEXT CLEANING FUNCTION
# ============================================================================
def clean_document_text(text: str) -> str:
    """
    Clean and normalize the extracted text.
    
    This function:
    1. Removes extra whitespace and line breaks
    2. Removes special characters that might confuse the AI
    3. Normalizes spacing to make text consistent
    
    Args:
        text: Raw text extracted from the document
        
    Returns:
        Cleaned text ready for analysis
    """
    # Replace multiple line breaks with single ones
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    
    # Replace multiple spaces with single space
    while "  " in text:
        text = text.replace("  ", " ")
    
    # Remove form feed characters and other control characters
    text = text.replace("\f", "")
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text

# ============================================================================
# STEP 4: DOCUMENT CHUNKING FUNCTION
# ============================================================================
def chunk_documents(documents: List, chunk_size: int = 1000, 
                   chunk_overlap: int = 200) -> List:
    """
    Break large documents into smaller, manageable pieces.
    
    Why we do this:
    - AI models work better with smaller text chunks
    - Allows us to find relevant information more efficiently
    - Prevents the AI from being overwhelmed by huge documents
    
    Args:
        documents: List of loaded documents
        chunk_size: Number of characters per chunk (1000 = ~200 words)
        chunk_overlap: Number of characters repeated between chunks
                      (helps maintain context between chunks)
        
    Returns:
        List of smaller document chunks ready for analysis
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    
    chunks = splitter.split_documents(documents)
    return chunks

# ============================================================================
# STEP 5: MAIN PREPARATION FUNCTION
# ============================================================================
def prepare_documents_for_review(folder_path: str = DOCUMENTS_FOLDER) -> List:
    """
    Main function that orchestrates the entire document preparation process.
    
    This does everything in order:
    1. Load documents from the folder
    2. Clean the text
    3. Split into manageable chunks
    4. Return processed documents ready for analysis
    
    Args:
        folder_path: Path to folder containing legal documents
        
    Returns:
        List of processed and chunked documents
    """
    print("=" * 70)
    print("🔍 CONTRACT REVIEW AGENT - DOCUMENT PREPARATION")
    print("=" * 70)
    print()
    
    # Step 1: Load documents
    print("📥 STEP 1: Loading documents from folder...")
    print(f"   Location: {folder_path}\n")
    documents = load_documents(folder_path)
    
    if not documents:
        print("\n⚠️  No documents were loaded. Exiting.")
        return []
    
    print(f"\n✅ Total documents loaded: {len(documents)}\n")
    
    # Step 2: Clean documents
    print("🧹 STEP 2: Cleaning document text...")
    for doc in documents:
        doc.page_content = clean_document_text(doc.page_content)
    print("✅ Text cleaned and normalized\n")
    
    # Step 3: Chunk documents
    print("✂️  STEP 3: Splitting documents into chunks...")
    chunks = chunk_documents(documents)
    print(f"✅ Documents split into {len(chunks)} chunks\n")
    
    # Display sample information
    if chunks:
        print("📊 Sample chunk (first 300 characters):")
        print("-" * 70)
        print(chunks[0].page_content[:300] + "...\n")
    
    print("=" * 70)
    print("✅ Document preparation complete!")
    print("=" * 70)
    
    return chunks

# ============================================================================
# STEP 6: ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    # Run the document preparation
    prepared_documents = prepare_documents_for_review()
    
    # Store for use by the analysis chains
    print(f"\n💾 Ready to analyze {len(prepared_documents)} document chunks")
    print("   Next step: Extract obligations, dates, and risks")
