# Yahoo Finance Data Processor

This project processes financial data from a CSV file, fetches current and historical prices using Yahoo Finance, and calculates the price difference. The processed data is saved to an output CSV file.

---

## Features

- Reads and processes financial data from a CSV file.
- Cleans and validates tickers and numeric fields.
- Fetches historical prices using Yahoo Finance API.
- Calculates price differences and appends them to the output.
- Outputs the processed data to a new CSV file.

---

## Project Structure

```plaintext
src/
├── config/
│   ├── settings.py        # Configuration for file paths and other |||||||├── utils/ 
│   ├── constants
├── services/
│   ├── file_handler.py    # Handles file operations (reading, writing)
│   ├── ticker_processor.py # Processes tickers and data cleaning
│   ├── price_fetcher.py   # Fetches prices using Yahoo Finance API
├── main.py                # Main script to orchestrate the processing
README.md                  # Instructions for setting up and running the project
requirements.txt           # Required Python libraries
```
# Installation

### Clone the repository:
```bash
git clone https://github.com/yourusername/yahoo-finance-processor.git
cd yahoo-finance-processor
```

### Install required Python libraries:
```bash
pip install -r requirements.txt
```

### Ensure your `config/settings.py` file has the correct paths for input and output files:
```python
CSV_INPUT_PATH = r"path_to_your_input_file.csv"
CSV_OUTPUT_PATH = r"path_to_your_output_file.csv"
```

---

# Usage

### Navigate to the `src` directory:
```bash
cd src
```

### Run the main script:
```bash
python main.py
```

The output will be saved to the file specified in `CSV_OUTPUT_PATH` in `config/settings.py`.

---

# Input and Output Format

### Input File (CSV):  
Ensure the input CSV file contains the following columns:
- `Ticker`
- `Security Description 1`
- `Country Code`
- `Local Price`
- `ISIN`
- `Acct Base Currency Code`
- `Issue Currency Code`
- `Segment`

### Output File (CSV):  
The processed output file will include:
- All original columns
- `Final Ticker` (processed ticker)
- `Yahoo Finance` (fetched price)
- `Difference` (price difference)

---

# Troubleshooting

### Common Issues

#### 1. **ModuleNotFoundError**  
Ensure you are running the script from the correct directory (`src`).  
If issues persist, set `PYTHONPATH` to include the `src` directory:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

#### 2. **Invalid File Paths**  
Ensure that the input and output paths in `config/settings.py` are correct and accessible.

#### 3. **Non-Numeric Values in CSV**  
Check your input file for non-numeric values in columns like `Local Price`.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contact

For any questions or issues, please contact:
**Email:** [darshanparbadiya@gmail.com](mailto:darshanparbadiya@gmail.com)
