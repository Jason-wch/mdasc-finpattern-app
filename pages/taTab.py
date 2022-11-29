import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from data_prep import *


def create_page():

    return html.Div(className='control-tab', children=[
                                html.Div(
                                    title='Enter a dot-bracket string and a nucleotide sequence.',
                                    className='app-controls-block',
                                    children=[ html.H4(className='what-is',
                              children='Feature Importance Analysis'),
                      dcc.Markdown('''3 major parts of the analysis and model training were conducted. Apart from the generation of renowned technical analysis indicators, we had quantified the trading strategies and signals as new indicators according to the indicative of technical analysis indicators and also the industry practice. 73 technical indicators or trading rules were created, quantified, and evaluated in the feature importance analysis. The technical indicators were divided into various categories such as overlap studies, momentum indicator, cycle pattern, trading rules etc. Factor importance analysis on technical indicators was performed to find out the top correlated technical indicators with respect to the stock momentum prediction and studied the significance of each category of technical analysis indicators in different industry sector models. By fitting the logistic regression with the labels created by the labelling method used in previous research, accuracy, precision, recall, and F1 score were used to evaluate the feature importance of the different categories of the technical indicators. In general, momentum indicators and trading rules were found to be the most important technical indicators in terms of statistical significance. We observed that the F-1 score is the highest when we considered all classes of technical analysis indicators in the preliminary modeling, which was basically in line with our expectations and objective after conducting literature research. 
 
In addition, it was observed that the distinctive characteristics of each industry can drive the above 2 categories of technical indicators to provide a dominant indication for prediction stock momentum, except the energy sector, which drives the volatility and volume indicators mostly. The energy sector is a special industry that possesses distinct features compared to other industries, like Communication Services, Financials, Industrials…etc. It is because the stock momentum is essentially not driven by historical momentum and trading rules, but it is inclined to be impacted by volume and volatility trends. The observation is aligned to the empirical study by Zhao, X. (2020). He revealed that the stock price of the energy sector is correlated to the policy uncertainty shocks and energy-specific demand shocks, which implied that policy uncertainty is an essential factor affecting the energy stock momentum rather than the historical momentum or trading rules.
 
Furthermore, we have further built LSTM models to assess the feature importance of each technical analysis indicator. Given the non-linearity of the LSTM model, we could not calculate the statistical significance of model factors directly; hence, we leveraged the permutation feature importance technique to evaluate the significance of each feature. We revealed both logistic regression and LSTM indicate the similar conclusion about the importance of the class of technical analysis indicators. For example, momentum indicators and trading rules are still dominating among a number of classes of technical analysis indicators. In particular, Will R% from the momentum category, the trend of the average directional index, and Bollinger bands from trading rules indicate the most significant predictive contribution to the model.

            '''),        html.Hr(),html.H4(className='what-is',
                              children='Feature Importance Chart'),
           dcc.Dropdown(
                id='feature-dropdown',
                options=[{'label': i, 'value': i} for i in features],
                placeholder="Please select..",
                value=['ema_5','mama','tema_30','ema_10','MA_10','ema_15', 'dema_30','ema_20','midprice','midpoint','T3ema','ema_25','ema_30','kama_30','ema_35','ema_40','fama','SMA_50','MA_50','SMA_30','HT','trima' ],
                searchable=True,multi=True
            ),
                        dcc.Graph(id='feature-graph'),

            
                                    ]
                                )])

                            #     html.Hr(),

                            #     html.Div(id='forna-error-message'),
                            #     html.Button(id='forna-submit-sequence',
                            #                 children='Submit sequence'),
                            # ])