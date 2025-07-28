import polars as pl
import os
from config import HISTORICAL_DIR

def merge_bulk_with_local(df_bulk):
    for ticker in df_bulk['code'].unique():
        path = f"{HISTORICAL_DIR}/{ticker}.csv"
        if os.path.exists(path):
            df_local = pl.read_csv(path)
            df_nuevo = df_bulk.filter(pl.col("code") == ticker)
            df_nuevo = df_nuevo.rename({'code': 'ticker'})
            df_nuevo = df_nuevo['date', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume']
            df_merged = pl.concat([df_local, df_nuevo], how='vertical').unique(subset=['date'])
            df_merged.write_csv(path)
            print(f'Actualizado {ticker} con {df_nuevo.shape[0]} nuevas filas')
        else:
            print(f'{ticker}: histórico no encontrado, ignorado.')
