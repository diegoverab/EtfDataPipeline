import requests, os, time
import polars as pl
from config import API_KEY, ETF_LIST_FILE, HISTORICAL_DIR

def fetch_historical(start='2022-01-01', end='2024-12-31'):
    os.makedirs(HISTORICAL_DIR, exist_ok=True)
    tickers = pl.read_csv(ETF_LIST_FILE)['Code'].to_list()

    for i, ticker in enumerate(tickers):
        url = f'https://eodhd.com/api/eod/{ticker}?from={start}&to={end}&api_token={API_KEY}&period=d&fmt=json'
        try:
            r = requests.get(url)
            if r.status_code == 200:
                df = pl.DataFrame(r.json())
                df.write_csv(f'{HISTORICAL_DIR}/{ticker}.csv')
        except Exception as e:
            print(f"Error con {ticker}: {e}")
        time.sleep(1)
        print(f'{i+1}/{len(tickers)} - {ticker}')
