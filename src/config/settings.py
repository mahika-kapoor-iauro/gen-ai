import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PDF_FOLDER_PATH = os.getenv("PDF_FOLDER_PATH", str(BASE_DIR / "data" / "pdfs"))
OUTPUT_FOLDER_PATH = os.getenv("OUTPUT_FOLDER_PATH", str(BASE_DIR / "data" / "chunks"))

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))

# Create folders if they don't exist
Path(PDF_FOLDER_PATH).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER_PATH).mkdir(parents=True, exist_ok=True)

class Settings:
    """Central configuration for API keys and model settings"""
    
    # API Keys
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Claude Settings
    CLAUDE_MODEL = "claude-3-5-sonnet-20241022"
    CLAUDE_MAX_TOKENS = 2048
    
    # OpenAI Settings
    OPENAI_MODEL = "gpt-4o"
    OPENAI_MAX_TOKENS = 1024
    
    # Validation
    @staticmethod
    def validate():
        if not Settings.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY not set in .env")
        if not Settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set in .env")

settings = Settings()
