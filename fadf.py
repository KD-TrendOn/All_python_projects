import yfinance as yf

msft = yf.Ticker("MSFT")
print('---------------------------')
# get stock info
print('msft.info')
print(msft.info)
print('---------------------------')
# get historical market data
print('msft.history(period="max")')
print(type(msft.history(period="max")))
print('---------------------------')
# show actions (dividends, splits)
print('msft.actions')
print(msft.actions)
print('---------------------------')
# show dividends
print('msft.dividends')
print(msft.dividends)
print('---------------------------')
# show splits
print('msft.splits')
print(msft.splits)
print('---------------------------')
# show financials
print('msft.financials')
print(msft.financials)
print('---------------------------')
print('msft.quarterly_financials')
print(msft.quarterly_financials)
print('---------------------------')
# show major holders
print('msft.major_holders')
print(msft.major_holders)
print(type(msft.major_holders))
print('---------------------------')
# show institutional holders
print('msft.institutional_holders')
print(msft.institutional_holders)
print('---------------------------')
# show balance sheet
print('msft.balance_sheet')
print(msft.balance_sheet)
print('---------------------------')
print('msft.quarterly_balance_sheet')
print(msft.quarterly_balance_sheet)
print('---------------------------')
# show cashflow
print('msft.cashflow')
print(msft.cashflow)
print('---------------------------')
print('msft.quarterly_cashflow')
print(msft.quarterly_cashflow)
print('---------------------------')
# show earnings
print('msft.earnings')
print(msft.earnings)
print('---------------------------')
print('msft.quarterly_earnings')
print(msft.quarterly_earnings)
print('---------------------------')
# show sustainability
print('msft.sustainability')
print(msft.sustainability)
print('---------------------------')
# show analysts recommendations
print('msft.recommendations')
print(msft.recommendations)
print('---------------------------')
# show next event (earnings, etc)
print('msft.calendar')
print(msft.calendar)
print('---------------------------')
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print('msft.isin')
print(msft.isin)
print('---------------------------')
# show options expirations
print('msft.options')
print(msft.options)
print('---------------------------')
# show news
print('msft.news')
print(msft.news)
print('---------------------------')
# get option chain for specific expiration
print("msft.option_chain('2021-12-10')")
print(msft.option_chain('2021-12-23'))
# data available via: opt.calls, opt.puts