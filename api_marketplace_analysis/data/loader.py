import yfinance as yf


class Loader:
    def __init__(self, ticker: str, interval: str):
        data_analyzed = yf.download(ticker, period=interval)
        data_analyzed.to_csv('./data.csv')
