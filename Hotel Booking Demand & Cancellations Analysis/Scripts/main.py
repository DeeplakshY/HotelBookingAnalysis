# main.py
import pandas as pd
import os

# Paths
RAW_DATA_PATH = os.path.join("data", "raw", "hotel_bookings.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "hotel_bookings_cleaned.csv")

def load_data(path):
    """Load CSV data into a pandas DataFrame"""
    try:
        df = pd.read_csv(path)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

def preprocess_data(df):
    """Basic preprocessing: handle missing values and duplicates"""
    df = df.drop_duplicates()
    df = df.fillna(0)  # or any other logic
    print("Data preprocessing done.")
    return df

def save_data(df, path):
    """Save the processed data to a CSV"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Processed data saved to {path}")

def main():
    df = load_data(RAW_DATA_PATH)
    if df is not None:
        df_clean = preprocess_data(df)
        save_data(df_clean, PROCESSED_DATA_PATH)

if __name__ == "__main__":
    main()
