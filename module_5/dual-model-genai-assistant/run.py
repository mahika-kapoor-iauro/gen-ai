import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config.settings import settings
from src.services.assistant import DualModelAssistant

def main():
    # Validate environment
    try:
        settings.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        sys.exit(1)
    
    assistant = DualModelAssistant()
    
    if len(sys.argv) < 2:
        print("Usage: python3 run.py <topic> [format]")
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

if __name__ == "__main__":
    main()
