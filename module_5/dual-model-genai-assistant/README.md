# Dual-Model GenAI Assistant

This project is a dual-model GenAI Assistant that integrates with Claude and OpenAI APIs to provide research assistance and summary generation functionalities.

## Project Structure

```
dual-model-genai-assistant
├── src
│   ├── main.py                # Entry point of the application
│   ├── config                 # Configuration settings
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models                 # API interaction models
│   │   ├── __init__.py
│   │   ├── claude.py          # Claude Assistant API client
│   │   └── openai.py          # OpenAI API client
│   ├── services               # Business logic and orchestration
│   │   ├── __init__.py
│   │   ├── assistant.py        # Assistant service for managing interactions
│   │   └── prompt_manager.py   # Prompt management for both models
│   ├── utils                  # Utility functions and classes
│   │   ├── __init__.py
│   │   ├── logger.py           # Logging functionality
│   │   └── validators.py       # Input and response validation
│   └── types                  # Data models and types
│       ├── __init__.py
│       └── models.py          # Data schemas for API outputs
├── tests                      # Unit tests for the application
│   ├── __init__.py
│   ├── test_claude.py         # Tests for ClaudeClient
│   ├── test_openai.py         # Tests for OpenAIClient
│   └── test_assistant.py      # Tests for AssistantService
├── .env.example               # Environment variable template
├── .gitignore                 # Files to ignore in version control
├── requirements.txt           # Project dependencies
├── pytest.ini                 # Pytest configuration
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd dual-model-genai-assistant
   ```

2. **Create a virtual environment:**
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and fill in your API keys and other necessary configurations.

## Usage

To run the application, execute the following command:

```
python src/main.py
```

You can interact with the assistant by providing research topics or requesting summaries.

## Features

- **Claude Integration:** Send research topics and receive structured outputs.
- **OpenAI Integration:** Generate summaries and creative outputs based on Claude's research results.
- **Prompt Management:** Ensure clear and structured prompts for both models.
- **Logging:** Track events and errors during execution.
- **Validation:** Ensure user inputs and API responses meet expected formats.

## Testing

To run the tests, use the following command:

```
pytest
```

This will execute all unit tests and provide a report on the results.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.