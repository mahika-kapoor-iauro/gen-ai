import os
from dotenv import load_dotenv

load_dotenv()

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
