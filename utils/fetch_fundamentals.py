import requests, time, json
import polars as pl
from config import API_KEY, ETF_LIST_FILE, FUNDAMENTALS_FILE

def fetch_fundamentals():
    tickers = pl.read_csv(ETF_LIST_FILE)['Code'].to_list()
    data = {}

    for i, ticker in enumerate(tickers):
        url = f'https://eodhd.com/api/fundamentals/{ticker}?api_token={API_KEY}&fmt=json'
        try:
            r = requests.get(url)
            if r.status_code == 200:
                data[ticker] = r.json()
        except Exception as e:
            print(f"Error con {ticker}: {e}")
        time.sleep(1)
        print(f'{i+1}/{len(tickers)} - {ticker}')

    with open(FUNDAMENTALS_FILE, 'w') as f:
        json.dump(data, f)

    print(f'Datos fundamentales guardados en {FUNDAMENTALS_FILE}')
