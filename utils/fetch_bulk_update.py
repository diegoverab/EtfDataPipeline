import requests, os, datetime
import polars as pl
from config import API_KEY, EXCHANGE, ETF_LIST_FILE, BULK_DIR

def fetch_bulk_update(date=None):
    os.makedirs(BULK_DIR, exist_ok=True)
    date = date or datetime.date.today().strftime('%Y-%m-%d')
    url = f'https://eodhd.com/api/eod-bulk-last-day/{EXCHANGE}?api_token={API_KEY}&date={date}&fmt=json'
    r = requests.get(url)
    bulk = pl.DataFrame(r.json())
    etfs = pl.read_csv(ETF_LIST_FILE)['Code'].to_list()
    df_etfs = bulk.filter(pl.col('code').is_in(etfs))
    path = f'{BULK_DIR}/eod_etfs_{date}.csv'
    df_etfs.write_csv(path)
    print(f'Descargado bulk EOD para {date}: {df_etfs.height} filas')
    return df_etfs
