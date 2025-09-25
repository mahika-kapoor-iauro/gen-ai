import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

def stock_dashboard():
    st.header("Stock Price Dashboard")
    
    # Stock symbol input
    symbol = st.text_input("Enter Stock Symbol", "AAPL").upper()
    
    # Date range selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=365))
    with col2:
        end_date = st.date_input("End Date", datetime.now())
    
    # Technical indicators
    show_ma20 = st.checkbox("Show 20-day Moving Average")
    show_ma50 = st.checkbox("Show 50-day Moving Average")
    
    try:
        # Fetch stock data
        stock = yf.Ticker(symbol)
        df = stock.history(start=start_date, end=end_date)
        
        if not df.empty:
            # Create price chart
            fig = go.Figure()
            
            # Add candlestick chart
            fig.add_trace(go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name='Stock Price'
            ))
            
            # Add moving averages if selected
            if show_ma20:
                ma20 = df['Close'].rolling(window=20).mean()
                fig.add_trace(go.Scatter(x=df.index, y=ma20, name='20-day MA', line=dict(color='orange')))
            
            if show_ma50:
                ma50 = df['Close'].rolling(window=50).mean()
                fig.add_trace(go.Scatter(x=df.index, y=ma50, name='50-day MA', line=dict(color='blue')))
            
            fig.update_layout(
                title=f'{symbol} Stock Price',
                yaxis_title='Price',
                xaxis_title='Date'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Volume chart
            volume_fig = go.Figure()
            volume_fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'))
            volume_fig.update_layout(
                title=f'{symbol} Trading Volume',
                yaxis_title='Volume',
                xaxis_title='Date'
            )
            st.plotly_chart(volume_fig, use_container_width=True)
            
            # Export button
            if st.button("Export to CSV"):
                csv = df.to_csv().encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f'{symbol}_stock_data.csv',
                    mime='text/csv'
                )
                
            # Add to recent stocks
            if symbol not in st.session_state.recent_stocks:
                st.session_state.recent_stocks.insert(0, symbol)
                st.session_state.recent_stocks = st.session_state.recent_stocks[:5]
                
        else:
            st.error("No data found for this symbol")
            
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")