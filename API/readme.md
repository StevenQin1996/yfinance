#Readme
##github 地址：https://github.com/StevenQin1996/yfinance.git
local repo consist patch that fixed bug: financial data fetch null from API.

To apply patch: 

1. pip uninstall yfinance,

2. installing with this command:
pip install git+https://github.com/StevenQin1996/yfinance.git
instead of:
pip install yfinance

#开发笔记
main:

display_linechart_single_y(stocks)

display_linechart_two_y(stocks, ["AAPL", "MSFT"])

display_value_change(stocks)

display_candle(apple)

data can also be retrieved using:

    data = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers = "AAPL MSFT",

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period = "ytd",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval = "1d",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by = 'ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust = True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost = True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads = True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy = None)


