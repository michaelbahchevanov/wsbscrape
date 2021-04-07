import os.path
import requests
from requests.exceptions import RequestException
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

url = 'https://finance.yahoo.com/quote/'
tickers_raw = ['./data/nasdaq_screener_1617441070940.csv', './data/nasdaq_screener_1617441128021.csv', './data/nasdaq_screener_1617441157210.csv']

def hui(url, tickers):
    requests.get(url)

def get_tickers(*csvs, driver=None):
    """Accepts a collection of file paths
       ----------------------------------
       File output goes to ./data/nasdaq_tickers as a csv file
       ----------------------------------
       Returns a pandas DataFrame"""
    
    path = './data/nasdaq_tickers.csv'
    result = []
    
    if(os.path.isfile(path)):
        return pd.read_csv(path)
    else:
        with ThreadPoolExecutor(max_workers=42) as executor:
            total = [symbol for symbol in pd.concat([pd.read_csv(csv)['Symbol'] for csv in csvs[0]])]
            #for ticker in total:
            #is_link = url + ticker + '?p=' + ticker
            all_links = [url + ticker + '?p=' + ticker for ticker in total]
            try:
                executor.map(requests.get, all_links)
                print('vkarah: ')
            except RequestException:
                print('ebaha mi mameto')
                pass
    print(result)

def main():
    get_tickers(tickers_raw)

if __name__ == '__main__':
    main()