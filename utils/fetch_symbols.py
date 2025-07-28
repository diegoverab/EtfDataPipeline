import requests
import polars as pl
from config import API_KEY, EXCHANGE, ETF_LIST_FILE

def fetch_etf_list():
    url = f'https://eodhd.com/api/exchange-symbol-list/{EXCHANGE}?api_token={API_KEY}&fmt=json'
    resp = requests.get(url)
    data = resp.json()
    etfs = [s for s in data if s.get('Type') == 'ETF']
    df = pl.DataFrame(etfs)
    df.write_csv(ETF_LIST_FILE)
    print(f'{len(df)} ETFs guardados en {ETF_LIST_FILE}')
    return df
