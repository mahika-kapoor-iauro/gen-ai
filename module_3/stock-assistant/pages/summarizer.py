import streamlit as st
import yfinance as yf
from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def extractive_summarize(text, ratio=0.3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    word_freq = {}
    
    for word in words:
        if word not in stop_words and word.isalnum():
            word_freq[word] = word_freq.get(word, 0) + 1
            
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
                    
    num_sentences = max(1, int(len(sentences) * ratio))
    summary_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
    summary = ' '.join([s[0] for s in summary_sentences])
    return summary

def text_summarizer():
    st.header("Stock News Summarizer")
    
    # Input methods
    input_method = st.radio("Choose input method:", ["Enter Text", "Stock News"])
    
    if input_method == "Enter Text":
        text = st.text_area("Enter text to summarize:", height=200)
    else:
        symbol = st.text_input("Enter Stock Symbol:", "AAPL").upper()
        try:
            stock = yf.Ticker(symbol)
            news = stock.news
            if news:
                news_titles = [item['title'] for item in news]
                selected_news = st.selectbox("Select news to summarize:", news_titles)
                text = next(item['longBusinessSummary'] for item in news if item['title'] == selected_news)
            else:
                st.warning("No news found for this symbol")
                text = ""
        except Exception as e:
            st.error(f"Error fetching news: {str(e)}")
            text = ""
    
    if text:
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Text")
            st.write(text)
            st.info(f"Word count: {len(text.split())}")
        
        with col2:
            st.subheader("Summary")
            ratio = st.slider("Summary length (%)", 10, 50, 30) / 100
            
            use_transformers = st.checkbox("Use advanced summarization (slower)")
            
            if use_transformers:
                try:
                    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                    summary = summarizer(text, max_length=int(len(text.split()) * ratio), 
                                      min_length=30, do_sample=False)[0]['summary_text']
                except Exception as e:
                    st.error("Error with transformer model. Falling back to extractive summarization.")
                    summary = extractive_summarize(text, ratio)
            else:
                summary = extractive_summarize(text, ratio)
            
            st.write(summary)
            st.info(f"Word count: {len(summary.split())}")
            
            # Add to recent summaries
            if summary not in st.session_state.recent_summaries:
                st.session_state.recent_summaries.insert(0, summary)
                st.session_state.recent_summaries = st.session_state.recent_summaries[:5]