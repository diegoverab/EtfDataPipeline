import os
from config import DATA_DIR
from utils.fetch_symbols import fetch_etf_list
from utils.fetch_fundamentals import fetch_fundamentals
from utils.fetch_historical import fetch_historical
from utils.fetch_bulk_update import fetch_bulk_update
from utils.merge_bulk_with_historical import merge_bulk_with_local

def main():
    # === Crear carpeta raíz si no existe ===
    os.makedirs(DATA_DIR, exist_ok=True)

    print('Paso 1: Descargar lista de ETFs')
    fetch_etf_list()

    print('\nPaso 2: Descargar fundamentos')
    fetch_fundamentals()

    print('\nPaso 3: Descargar históricos')
    fetch_historical(start='2024-01-01', end='2025-07-24')

    print('\nPaso 4: Descargar actualizaciones vía Bulk API')
    df_bulk = fetch_bulk_update(date='2025-07-25')

    print('\nPaso 5: Fusionar con históricos existentes')
    merge_bulk_with_local(df_bulk)

if __name__ == '__main__':
    main()
