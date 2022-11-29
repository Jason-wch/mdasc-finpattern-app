import pandas as pd
import os

# stock_dir = './input/Stock Price/'
stock_dir  = '/home/Fpat/public_html/mdasc-finpattern-app/input/Stock Price/'
stock_paths = [f for f in os.listdir(stock_dir) if f != '.DS_Store']

stock_list = []
dict_stock = {}

for i in stock_paths:
    dir = stock_dir + '/'+i
    df = pd.read_csv(dir, index_col=0)
    df['date'] = df.index
    stock = i.split('_')[0]
    dict_stock[stock] = df

stocks = list(dict_stock.keys())
stock_channels = dict_stock[stocks[0]]
