import yfinance as yf

# tickers = ['KC=F', 'SB=F', 'PL=F', 'CL=F']
# # KC=F : Coffee
# # SB=F : Sugar
# # PL=F : Platinum
# # CL=F : Crude Oil
# data_analyzed = yf.download(tickers, start='2014-08-26', end='2024-08-26')
# data_analyzed.to_csv('data.csv')


class Loader:
    def __init__(self, tickers, period):
        data_analyzed = yf.download(tickers, period=period)
        data_analyzed.to_csv('./data.csv')

    def read_data(self, name):
        pass
