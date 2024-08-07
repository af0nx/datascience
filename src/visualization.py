import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(file_path):
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], marker='o', linestyle='-')
    plt.title('Fechamento Diário da Ação')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (USD)')
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = 'data/processed/processed_stock_data.csv'
    plot_stock_data(file_path)
