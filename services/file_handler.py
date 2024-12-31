import pandas as pd

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        print(f"Loading CSV file: {self.file_path}")
        return pd.read_csv(self.file_path)

    def save_csv(self, df, output_path):
        print(f"Saving CSV file to: {output_path}")
        df.to_csv(output_path, index=False)
