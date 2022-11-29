import dash_html_components as html
import dash_core_components as dcc
from data_prep import parent_img_path, parent_path
import pandas as pd
from datetime import date

df_cdl = pd.read_excel(f'{parent_path}/data/cdl.xlsx')
df_predict = pd.read_excel(f'{parent_path}/data/model_prediction.xlsx')
stock_list = list(df_cdl['ticker'].unique())
patterns = ['morning_star', 'evening_star', 'hammer',
       'inverted_hammer', 'bullish_engulfing', 'bearish_engulfing',
       'shooting_star', 'hanging_man']

print(df_cdl.shape)
print(stock_list)

default_date = df_predict['report_date'].iloc[50]

def create_page(cdl_words):

    data_struct_intro = cdl_words.data_struct_intro
    cdl_intro = cdl_words.cdl_intro
    morning_star_intro = cdl_words.morning_star_intro

    return html.Div(
        className='control-tab', 
        children=[
            
            # Candlestick pattern
            # Sub-header
            html.H4("Candlestick Pattern Analysis", className = "what-is"),
            
            # Common candlestick pattern
            html.H6("Common candlestick pattern"),
            html.Div(
                [
                    html.Img(
                        src = f"{parent_img_path}/assets/cdl_basic.png",
                        style = {"width": "40%"}
                    ),
                    html.Img(
                        src = f"{parent_img_path}/assets/morning_star.png",
                        style = {'width': "40%"}
                    )
                ]
            ),

            # Candlestick pattern demo
            html.H6("Candlestick pattern demo"),
            dcc.Dropdown(
                id = 'stock_cdl_dropdown',
                multi = False,
                clearable = True,
                options = [{'label': f, 'value': f} for f in stock_list],
                value = stock_list[0],
                searchable = True

            ),
            dcc.Dropdown(
                id = 'cdl_pattern_dropdown',
                multi = True,
                clearable = True,
                options = [{
                    'label': f.replace('_', ' ').capitalize(),
                    'value': f
                } for f in patterns],
                value = patterns[0],
                searchable = True
            ),

            dcc.Graph(id = 'cdl-graph'),
            
            # Description - cdl intro
            html.Div(
                [
                    html.H6("What is candlestick pattern?"),
                    html.Div(cdl_intro)
                ]
            ),

            # Example - morning star
            html.Div(
                [
                    html.H6("Common candlestick pattern example - Morning Star"),
                    html.Div(morning_star_intro)
                ]
            ),


            # Sub-header
            html.H4("3D CNN Modeling", className = "what-is"),
            
            # 3D Data Structure
            html.Div(
                [
                    html.H6("Preparation of 3D data sturcture"),
                    html.Img(
                        src = f'{parent_img_path}/assets/3D_data_structure.png',
                        style = {
                            "width": "70%"
                        }
                    ),
                    html.H6("What is the 3D data structure"),
                    html.Div(data_struct_intro)
                ]
            ),
            
            # 3D Data Structure & Prediction
            html.H6("3D Data Structure & Prediction demo"),
            dcc.Dropdown(
                id = 'stock_3d_dropdown',
                multi = False,
                clearable = True,
                options = [{'label': f, 'value': f} for f in stock_list],
                value = stock_list[0],
                searchable = True
            ),

            html.Div('Prediction Date: '),
            dcc.DatePickerSingle(
                id = 'report_date',
                min_date_allowed = date(2020,1,1),
                max_date_allowed = date(2022,6,30),
                initial_visible_month = default_date,
                date = default_date
            ),
            dcc.Graph(id = '3d-graph'),
            html.Div(id = 'model-prediction')


            
            
            # html.Div(
            #     className='app-controls-block',
            #     children=[
            #         html.Div(className='fullwidth-app-controls-name',
            #                     children='Title pattern'),
            #         html.Div(
            #             className='app-controls-desc',
            #             children='Specify the information which will ' +
            #                         'be rendered on the mouse hover.'
            #         ),
            #         dcc.Input(id='forna-title-pattern',
            #                     placeholder='${structName}:${num}')
            #     ]
            # ),
            # html.Br(),
            # html.Button(
            #     id='forna-submit-title-pattern',
            #     children='Submit'
            # )
        ])