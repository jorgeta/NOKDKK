import pandas as pd
import yfinance as yf
import fire
import os
from yahoofinancials import YahooFinancials

from configs.config_utils import read_yaml

class App:
    
    def __init__(self):
        cd = str(os.path.dirname(os.path.abspath(__file__)))
        self.root = f'{cd}/../..'
        self.config = read_yaml(f'{self.root}/config.yaml')
    
    def update_data(self):
        ticker = self.config.data.ticker
        period = self.config.data.period
        interval = self.config.data.interval
        
        df = yf.download(ticker, period=period, interval=interval)
        df.to_csv(f'{self.root}/data/{ticker}-{interval}-{period}.csv')


def main():
    fire.Fire(App)

if __name__ == '__main__':
    main()