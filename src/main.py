import sys
import os

# Dynamically add the 'src' directory to PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(src_dir)

from services.file_handler import FileHandler
from services.ticker_processor import TickerProcessor
from services.price_fetcher import PriceFetcher
from config.settings import CSV_INPUT_PATH, CSV_OUTPUT_PATH

def main():
    # Load the CSV file
    file_handler = FileHandler(CSV_INPUT_PATH)
    df = file_handler.load_csv()
    
    # Process tickers
    ticker_processor = TickerProcessor()
    df = ticker_processor.process_tickers(df)

    # Fetch prices and calculate differences
    price_fetcher = PriceFetcher()
    df = price_fetcher.update_prices(df) 
    # Save the modified CSV
    file_handler.save_csv(df, CSV_OUTPUT_PATH)
    print("Processing complete. Modified CSV saved.")

if __name__ == "__main__":
    main()
