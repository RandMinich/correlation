import yfinance as finance
import pandas


go = finance.Ticker('GOOGL')

h = go.history(period='max')