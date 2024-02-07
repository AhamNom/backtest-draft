import yfinance as yf
import pandas as pd

symbol = input('stock symbol: ')
start_date = input('start date by yyyy-mm-dd: ')

data = yf.download(symbol, start=start_date, period='1d', interval='1m')
print(data.head())
data.to_csv(symbol + '.csv')
