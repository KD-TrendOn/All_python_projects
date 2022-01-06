import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# Get the data for the stock AAPL
data = yf.download('AAPL','2017-02-28','2019-08-01')
print(type(data['Adj Close']))
# Plot the close price of the AAPL
# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']
data = pd.DataFrame(columns=tickers_list)
# Fetch the data

plt.show()