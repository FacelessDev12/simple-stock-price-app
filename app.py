
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown below are the stock **Closing Price** and **Volume** of Google (GOOGL)!
""")

# Define ticker symbol
tickerSymbol = 'GOOGL'

# Fetch data
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices
tickerDf = tickerData.history(start='2010-05-31', end='2020-05-31')

# Display Closing Price Chart
st.write("## Closing Price")
st.line_chart(tickerDf.Close)

# Display Volume Chart
st.write("## Volume")
st.line_chart(tickerDf.Volume)

