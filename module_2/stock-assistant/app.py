import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import json
from pathlib import Path

# Configure the Streamlit page
st.set_page_config(
    page_title="Stock Assistant",
    page_icon="📈",
    layout="wide"
)

# Initialize session state
if 'recent_stocks' not in st.session_state:
    st.session_state.recent_stocks = []
if 'recent_summaries' not in st.session_state:
    st.session_state.recent_summaries = []

# Load history from JSON if exists
def load_history():
    history_file = Path("data/history.json")
    if history_file.exists():
        with open(history_file) as f:
            return json.load(f)
    return {"stocks": [], "summaries": []}

# Save history to JSON
def save_history():
    history = {
        "stocks": st.session_state.recent_stocks,
        "summaries": st.session_state.recent_summaries
    }
    with open("data/history.json", "w") as f:
        json.dump(history, f)

# Main app layout
def main():
    st.title("Stock Assistant")
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Summarizer", "About"])
    
    # Load history
    history = load_history()
    st.session_state.recent_stocks = history["stocks"]
    st.session_state.recent_summaries = history["summaries"]
    
    # Page routing
    if page == "Dashboard":
        from pages.dashboard import stock_dashboard
        stock_dashboard()
    elif page == "Summarizer":
        from pages.summarizer import text_summarizer
        text_summarizer()
    else:
        st.write("About this app...")
    
    # Save history
    save_history()
    
    # Recent items in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("Recent Stocks")
    for stock in st.session_state.recent_stocks[:5]:
        st.sidebar.text(stock)
        
    st.sidebar.markdown("---")
    st.sidebar.subheader("Recent Summaries")
    for summary in st.session_state.recent_summaries[:5]:
        st.sidebar.text(summary[:50] + "...")

if __name__ == "__main__":
    main()