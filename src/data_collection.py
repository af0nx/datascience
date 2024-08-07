import requests

def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=compact"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return None

if __name__ == "__main__":
    SYMBOL = "IBM"  # Substitua pelo símbolo da ação desejada
    API_KEY = "YOUR_API_KEY"  # Substitua pela sua chave de API

    data = fetch_stock_data(SYMBOL, API_KEY)
    if data:
        print("Dados obtidos com sucesso!")
        with open('data/raw/stock_data.json', 'w') as f:
            import json
            json.dump(data, f, indent=4)
