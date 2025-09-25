# Stock Assistant

An interactive Streamlit application that combines stock visualization and text summarization capabilities.

## Features

- **Stock Price Dashboard**
  - Interactive stock price visualization
  - Technical indicators (moving averages)
  - Volume analysis
  - CSV export functionality

- **Text Summarizer**
  - Paste text or input URL
  - Adjustable summary length
  - Support for both extractive and transformer-based summarization
  - Word count statistics

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd stock-assistant
```

2. Create and activate virtual environment:
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## Usage

### Stock Dashboard
- Enter a stock symbol (e.g., AAPL, GOOGL)
- Select date range
- Toggle technical indicators
- Export data as needed

### Text Summarizer
- Paste text or enter URL
- Adjust summary length using the slider
- Choose summarization method
- View original and summarized text side by side

## Data Storage

The application maintains a history of:
- Recent stock searches
- Recent text summaries

This data is stored locally in `data/history.json`

## Dependencies

See `requirements.txt` for full list of dependencies:
- streamlit
- yfinance
- pandas
- plotly
- nltk
- transformers
- beautifulsoup4

## License

This project is licensed under the MIT License - see the LICENSE file for details.