import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


nokdkk_df = yf.download('NOKDKK=X', start='2019-01-01', end='2021-06-12', progress=False)

print(nokdkk_df.describe())