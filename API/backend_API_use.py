import sys
import pandas as pd
import pprint
import json
import pandas_datareader.data as web
from pandas_datareader import data as pdr
import datetime
import yfinance as yf
import matplotlib.pyplot as plt  # Import matplotlib
import matplotlib.ticker as ticker
import candle


def main():
    """Main entry point for the script."""

    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.today()

    # apple = get_data('AAPL',start,end)
    # microsoft = get_data('MSFT', start, end)
    # google = get_data('GOOG', start, end)

    # stocks = pd.DataFrame({"AAPL": apple["Adj Close"],
    #                        "MSFT": microsoft["Adj Close"],
    #                        "GOOG": google["Adj Close"]})

    # print(stocks.head())  # adj close就是等于adjusted close

    msft = yf.Ticker("MSFT")
    data = msft.get_all()
    pprint.pprint(data)
    # get stock info
    # print(msft.cashflow)
    # print(msft.earnings)
    # print(msft.quarterly_cashflow)
    # print(msft.balance_sheet)
    # print(msft.balance_sheet.loc['Intangible Assets', '2019-06-30'].values)


def write_to_file(filename, my_data):
    try:
        with open(filename, 'w') as outfile:
            json.dump(my_data, outfile)
    except:
        print("An exception occurred")


def get_data(ticker, start, end):
    # <== that's all it takes :-) to get real time market information. Override
    yf.pdr_override()
    # both methods return identical result
    # result1 = web.get_data_yahoo(ticker, start, end)
    result2 = pdr.get_data_yahoo(ticker, start=start, end=end)

    return result2


def display_candle(my_dataframe):
    """
    :param my_dataframe: Pandas framework
    display candle stick diagram
    """
    candle.pandas_candlestick_ohlc(my_dataframe)
    my_dataframe["20d"] = pd.np.round(my_dataframe["Close"].rolling(window=20, center=False).mean(), 2)
    candle.pandas_candlestick_ohlc(my_dataframe.loc['2020-01-01':'2020-10-07', :], otherseries="20d")


def display_linechart_single_y(my_dataframe):
    """
    :param my_dataframe: Pandas framework
    shown regular linear chart. If contain stocks with huge price difference, try to use display_linechart_two_y
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    my_dataframe.plot(ax=ax, grid=True, legend=True).axhline(0.5, color='black', ls='--')
    formatter_left = ticker.FormatStrFormatter('$%1.2f')
    ax.yaxis.set_major_formatter(formatter_left)
    ax.set_ylabel("Price")
    plt.show()


def display_linechart_two_y(my_dataframe, secondaryY):
    """
    :param my_dataframe: Pandas framework
    :param secondaryY: example: ["AAPL", "MSFT"]
    """
    # plt.subplots()是一个函数，返回一个包含figure和axes对象的元组。因此，使用fig,ax = plt.subplots()将元组分解为fig和ax两个变量。
    fig, ax = plt.subplots(figsize=(10, 6))
    my_dataframe.plot(secondary_y=secondaryY, ax=ax, grid=True, legend=True)

    formatter_left = ticker.FormatStrFormatter('$%1.2f')
    formatter_right = ticker.FormatStrFormatter('$%1.0f')
    ax.yaxis.set_major_formatter(formatter_left)
    ax.right_ax.yaxis.set_major_formatter(formatter_right)
    ax.set_ylabel("Price")
    plt.show()


def display_value_change(my_dataframe):
    """
    :param my_dataframe: ["AAPL", "MSFT"]
    convert all stocks in the framework to compare total loss/return
    """
    stock_return = my_dataframe.apply(lambda x: ((x / x[0]) - 1) * 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    my_dataframe.plot(ax=ax, grid=True, legend=True).axhline(0.5, color='black', ls='--')
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=None, symbol='%', is_latex=False))
    ax.set_ylabel("Valuation Change")
    plt.show()
    # show_diagram(stock_return)


def display_logDifference(my_dataframe):
    stock_change = my_dataframe.apply(lambda x: pd.np.log(x) - pd.np.log(x.shift(1)))  # shift moves dates back by 1.
    stock_change.head()
    stock_change.plot(grid=True).axhline(y=0, color="black", lw=2)


def show_diagram(my_dataframe):
    """
    Plan to use this function for all function that needs to display a chart.
    :param my_dataframe:
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    my_dataframe.plot(ax=ax, grid=True, legend=True).axhline(0.5, color='black', ls='--')
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=None, symbol='%', is_latex=False))
    ax.set_ylabel("Valuation Change")
    plt.show()


if __name__ == '__main__':
    sys.exit(main())
