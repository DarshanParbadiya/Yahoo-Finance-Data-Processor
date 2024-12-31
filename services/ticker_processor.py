import pandas as pd
from utils.constants import COUNTRY_MAPPING, MODIFICATIONS

class TickerProcessor:
    def process_tickers(self, df):
        # Filter and process rows
        df = df[['Ticker', 'Security Description 1', 'Country Code', 'Local Price', 'ISIN', 
                 'Acct Base Currency Code', 'Issue Currency Code', 'Segment']]
        df = df[df['Segment'] == 'EQUITIES']
        
        df['Final Ticker'] = df.apply(self.modify_ticker, axis=1)
        return df

    def modify_ticker(self, row):
        ticker = row['Ticker']
        if pd.isna(ticker):
            return None
        
        # Apply modifications
        for key, value in MODIFICATIONS.items():
            if key in ticker:
                ticker = ticker.replace(key, value)
        
        # Add country code suffix
        country_code = row.get('Country Code', '')
        ticker_suffix = COUNTRY_MAPPING.get(country_code, '')
        return f"{ticker}.{ticker_suffix}" if ticker_suffix else ticker
