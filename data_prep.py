import pandas as pd
import os

parent_path = '.' # local environment
parent_img_path = '.'
config_setting = {}

# parent_path = '/home/Fpat/public_html/mdasc-finpattern-app'
# parent_img_path = '/financial_big_data_analytics/FinPattern/mdasc-finpattern-app'
# config_setting = {
#         'url_base_pathname':'/financial_big_data_analytics/FinPattern/mdasc-finpattern-app/',
#         'routes_pathname_prefix':'/financial_big_data_analytics/FinPattern/mdasc-finpattern-app/',
#         'requests_pathname_prefix':'/financial_big_data_analytics/FinPattern/mdasc-finpattern-app/'
#     }



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

feature_dir  = f'{parent_path}/input/feature_importance.csv'
feature_df = pd.read_csv(feature_dir,index_col=None)
features = list(feature_df['Attribute'])


covid_dir  = f'{parent_path}/input/filtered_covid.csv'
covid_df = pd.read_csv(covid_dir,index_col=None, usecols =['location', 'date', 'total_cases','total_deaths'])
covid_countries=list(covid_df['location'].unique())


disaster_dir  = f'{parent_path}/input/filtered_disaster.csv'
disaster_df = pd.read_csv(disaster_dir)
disaster_continents=list(disaster_df['Continent'].unique())
