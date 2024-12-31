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
    
    # def fetch_local_prices(self,df):
    #     # Iterate through each row and modify the ticker value if necessary
    #     for index, row in df.iterrows():
    #         print(f"Index: {index}, {row['Local Price']}, {row['ISIN']}, {row['Ticker']}")
            
    #         if pd.isna(row['Ticker']):
    #             print(f"Index: {index}, Ticker is NaN")
    #             ticker = None
    #         else:
    #             ticker = row['Ticker']
    #             # Check if any character in the ticker needs modification
    #             for key, value in MODIFICATIONS.items():
    #                 if key in row['Ticker']:
    #                     ticker = ticker.replace(key, value)
    #                     # print(f"Modified Ticker: {ticker}")
            
    #             try:
    #                 ticker_modification = "."+country_mapping[row['Country Code']]
    #                 # print(ticker_modification)
    #             except KeyError:
    #                 # print('No modification')
    #                 ticker_modification = ""
                
    #             final_ticker = ticker+ticker_modification
    #             # print(f'Final Ticker: {final_ticker}')
    #             df.at[index, 'Final Ticker'] = final_ticker
                
    #             try:
    #                 current_price = get_yesterday_price(final_ticker)
    #             except Exception as e:
    #                 print(f"Error retrieving current price for {row['Ticker']}: {e}")
    #                 current_price = None
    #             else:
    #                 if current_price is not None:
    #                     difference = float(current_price) - float(row['Local Price'])
    #                     print(row['Ticker'], row['Local Price'], current_price, difference)
    #                     df.at[index, 'Difference'] = difference
    #                     df.at[index, 'Yahoo Finance'] = current_price
    #                 else:
    #                     df.at[index, 'Difference'] = None
                
    #     # df['Yahoo Finance'] = df['Yahoo Finance'].round(3)
    #     # df['Difference'] = df['Difference'].round(3)        
    #     #     # Save the DataFrame to a CSV file
    #     # df.to_csv('modi`fied_tickers.csv', index=False)

    #     # print("The final tickers have been saved to modified_tickers.csv")
    #     return df 
                