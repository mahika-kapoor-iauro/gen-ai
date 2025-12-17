import sys
from src.config.settings import settings
from src.services.assistant import DualModelAssistant
from src.services.pdf_loader import PDFLoader
from src.services.text_chunker import TextChunker
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    # Validate environment
    try:
        settings.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        sys.exit(1)
    
    assistant = DualModelAssistant()
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <topic> [format]")
        print("Formats: report, blog, linkedin")
        return
    
    topic = ' '.join(sys.argv[1:-1]) if len(sys.argv) > 2 else sys.argv[1]
    output_format = sys.argv[-1] if len(sys.argv) > 2 and sys.argv[-1] in ["report", "blog", "linkedin"] else "report"
    
    result = assistant.research_and_summarize(topic, output_format)
    
    print(f"\n{'='*50}")
    print(f"SUMMARY ({result['summary'].format_type.upper()})")
    print(f"{'='*50}")
    print(result['summary'].summary)
    print(f"\nWord Count: {result['summary'].word_count}")

    """
    Main function to load PDF and create chunks.
    """
    try:
        logger.info("=" * 80)
        logger.info("🚀 Starting PDF Ingestion and Chunking Pipeline")
        logger.info("=" * 80)
        
        logger.info("\n📖 Step 1: Loading PDF files...")
        pdf_loader = PDFLoader()
        pdfs = pdf_loader.load_all_pdfs()
        
        if not pdfs:
            logger.warning("⚠️  No PDFs to process. Please add PDF files to the data/pdfs folder.")
            return
        
        logger.info(f"\n📋 Step 2: Processing {len(pdfs)} PDF(s)...")
        text_chunker = TextChunker()
        
        for filename, text in pdfs.items():
            logger.info(f"\n🔄 Processing: {filename}")
            chunks = text_chunker.chunk_text(text)
            base_name = filename.replace('.pdf', '')
            output_path = text_chunker.save_chunks_to_file(chunks, base_name)
            logger.info(f"✨ {filename} processed successfully!")
            logger.info(f"   └─ Chunks file: {output_path}")
        
        logger.info("\n" + "=" * 80)
        logger.info("✅ PDF Ingestion and Chunking Pipeline Complete!")
        logger.info("=" * 80)
        logger.info(f"\n💡 Tip: Check the chunks files in data/chunks/ folder to verify the output.")
        
    except Exception as e:
        logger.error(f"\n❌ Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
