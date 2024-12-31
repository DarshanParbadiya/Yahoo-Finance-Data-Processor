import yfinance as yf
import pandas as pd
from utils.constants import COUNTRY_MAPPING, MODIFICATIONS
class PriceFetcher:
    def get_yesterday_price(self, ticker_symbol):
        try:
            ticker = yf.Ticker(ticker_symbol)
            historical_data = ticker.history(period='5d', interval='1d')
            
            yesterday = pd.Timestamp.today() - pd.Timedelta(days=1)
            yesterday_close = historical_data.loc[yesterday.strftime('%Y-%m-%d')]['Close']
            return yesterday_close
        except Exception as e:
            print(f"Error retrieving price for {ticker_symbol}: {e}")
            return None

    def update_prices(self, df):
        for index, row in df.iterrows():
            ticker = row['Final Ticker']
            if not ticker:
                continue
            
            try:
                yesterday_price = self.get_yesterday_price(ticker)
                if yesterday_price is not None:
                    difference = round(float(yesterday_price) - float(row['Local Price']), 3)
                    df.at[index, 'Yahoo Finance'] = round(yesterday_price, 3)
                    df.at[index, 'Difference'] = difference
            except Exception as e:
                print(f"Error processing row {index}: {e}")
        
        return df
