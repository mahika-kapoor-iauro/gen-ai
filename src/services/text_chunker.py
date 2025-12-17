import os
from typing import List, Tuple
from src.utils.logger import setup_logger
from src.config.settings import CHUNK_SIZE, CHUNK_OVERLAP, OUTPUT_FOLDER_PATH

logger = setup_logger(__name__)

class TextChunker:
    def __init__(self, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
        """
        Initialize the text chunker.
        
        Args:
            chunk_size: Size of each chunk in characters
            chunk_overlap: Number of characters to overlap between chunks
        """
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be less than chunk_size")
        
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        logger.info(f"⚙️  TextChunker initialized | Size: {chunk_size}, Overlap: {chunk_overlap}")
    
    def chunk_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks.
        
        Args:
            text: The text to chunk
        
        Returns:
            List of text chunks
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk.strip())
            
            # Move start position for next chunk, accounting for overlap
            start = end - self.chunk_overlap
        
        logger.info(f"✂️  Text chunked successfully | Created {len(chunks)} chunks")
        return chunks
    
    def save_chunks_to_file(self, chunks: List[str], filename: str) -> str:
        """
        Save chunks to a text file for visual verification.
        
        Args:
            chunks: List of chunks to save
            filename: Name of the output file (without extension)
        
        Returns:
            Path to the saved file
        """
        output_file = os.path.join(OUTPUT_FOLDER_PATH, f"{filename}_chunks.txt")
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Total Chunks: {len(chunks)}\n")
                f.write(f"Chunk Size: {self.chunk_size}\n")
                f.write(f"Chunk Overlap: {self.chunk_overlap}\n")
                f.write("=" * 80 + "\n\n")
                
                for idx, chunk in enumerate(chunks, 1):
                    f.write(f"--- CHUNK {idx} ---\n")
                    f.write(chunk)
                    f.write("\n\n")
            
            logger.info(f"💾 Chunks saved to {output_file}")
            return output_file
        
        except Exception as e:
            logger.error(f"❌ Error saving chunks to file: {str(e)}")
            raise