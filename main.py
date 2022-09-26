import json
import urllib.request
from urllib.request import urlretrieve as urlget
import csv
def main():
    aapl = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1632619273&period2=1664155273&interval=1d&events=history&includeAdjustedClose=true"
    urlget(aapl, 'aapl.csv')




if __name__ == '__main__':
    main()