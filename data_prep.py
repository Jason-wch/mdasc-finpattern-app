import pandas as pd
import os

# parent_path = '.' # local environment
# parent_img_path = '.'
# config_setting = {}

parent_path = '/home/Fpat/public_html/mdasc-finpattern-app'
parent_img_path = '/financial_big_data_analytics/FinPattern/mdasc-finpattern-app'
config_setting = {
        'url_base_pathname':'/financial_big_data_analytics/FinPattern/mdasc-finpattern-app/',
        'routes_pathname_prefix':'/financial_big_data_analytics/FinPattern/mdasc-finpattern-app/',
        'requests_pathname_prefix':'/financial_big_data_analytics/FinPattern/mdasc-finpattern-app/'
    }

# stock_dir = './input/Stock Price/'
stock_dir  = f'{parent_path}/input/Stock Price/'
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
