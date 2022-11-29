import dash_html_components as html
import dash_core_components as dcc
from data_prep import *

def create_page():

    return html.Div(
        className='control-tab', 
        children=[
            html.H4(className='what-is',
                    children='FinPattern'),
            dcc.Markdown('''
            Beginning in the 1600s, the first stock market opened in Amsterdam and market participants started to trade stocks in the open market. Over the years of the development of stock markets and advancements in technology, practitioners and academics have employed different tools and approaches with an aim to study and predict stock momentum. In the past, researchers forecast the stock momentum by the means of technical analysis indicators and candlestick patterns and managed to make profits from their prediction. However, those studies could not assess the validity of the indicators and did not allow to take the market sentiment into consideration. With the lack of transaction data and technology, it is difficult for researchers to comprehensively validate their hypothesis on stock momentum prediction.
            
            This study aims to handle the complexity of evaluation on technical analysis, candlestick patterns as well as incident sentiment in parallel, and develop an advanced convolutional neural network (CNN) model to predict the stock momentum in consideration of the above dimensions. We have performed feature importance analysis to identify the relevant indicators, conducted sentiment analysis on the news, incidents, and COVID-19-related events to generate the sentiment score factors, as well as considering the above information along with the candlestick patterns, cross industries, and time-lag dimensions to construct a 3D data structure and train the CNN models for prediction. 
            
            Our interim result shows the proposed CNN model outperforms the baseline model which is trained by Logistic Regression with candlestick patterns only. In the future, we would also consider the trading rules, COVID-19, and natural disaster factors, and continue to fine-tune our CNN model to enhance the model performance. We believe our project could provide insight to practitioners to further study the interaction between technical analysis, candlestick patterns, and industry sentiment so as to provide a comprehensive view of stock market movement.

            '''),
            html.Div(
                html.Img(
                    className='align-self-center', 
                    src = f'{parent_img_path}/assets/main.png', 
                    style={'width': "50%"}
                ),
                style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
            ),

            html.H4(className='what-is',
                    children='Stock Price Movement'),
            dcc.Dropdown(id='stock_dropdown', multi=False, clearable=True,
                            options=[{'label': f, 'value': f}
                                    for f in stocks],
                            value=list(dict_stock.keys())[0], searchable=True, style={'width': '65%'}),
            dcc.Dropdown(id='stock_metric_dropdown', multi=True, clearable=True, style={
                            'width': '100%'}),
            dcc.Graph(id='stock-graph')
        ])