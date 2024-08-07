import pandas as pd
import json

def process_stock_data(file_path):
    with open(file_path, 'r') as f:
        raw_data = json.load(f)

    time_series = raw_data['Time Series (Daily)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })
    df = df.astype(float)
    df.sort_index(inplace=True)
    return df

if __name__ == "__main__":
    file_path = 'data/raw/stock_data.json'
    df = process_stock_data(file_path)
    print(df.head())
    df.to_csv('data/processed/processed_stock_data.csv')
