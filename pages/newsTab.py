import dash_html_components as html
import dash_core_components as dcc
from data_prep import *


def create_page():

    return html.Div(className='control-tab', children=[
        html.Div(
            className='app-controls-block',
            children=[html.H4(className='what-is',
                              children='Unexpected News Analysis'),
                      dcc.Markdown('''
There were two main objectives in the unexpected news analysis. Firstly to propose a new ensembled sentiment model to predict the text sentiment of online financial news articles and secondly to investigate whether or not natural disaster or COVID-19 related data will have an impact in predicting stock price movements.

Financial news data of the S&P 500 stocks were first extracted and classified with 3 existing pre-trained sentiment models, Flair, VADER and BERT. A validation set was then created via manually labelling 385 pieces of news article. The performance of the 3 well-researched pretrained models are then compared with the 4 ensemble methods which includes majority voting, average voting, weighted ensemble and industry weighted ensemble. Based on the results on the validation set, the weighted ensemble methodology yielded the best performance in terms of F1 score and outperformed the base models by over 3%.

Secondly, the number of deaths in natural disaster that happened in America, as well as the number of deaths and cases caused by COVID-19 are also input as features to attempt to predict stock price movement via 5 commonly used machine learning models. In total, 35 models were created and tuned. It was observed that the introduction of natural disaster and COVID-19 data has indeed improved the performance of these stock prediction models. Eventually the logistic regression model trained with features combining all features provided the best F1 score on the validation set. Therefore, it can be concluded that all of the features extracted in the unexpected event are important towards stock movement prediction. These data were then passed onto the 3D CNN model for predictions.

            '''), html.Div(
                html.Img(
                    className='align-self-center',
                    src=f'{parent_img_path}/assets/wordcloud.png',
                    style={'width': "50%"}
                ), style={'textAlign': 'center'})

            ]
        ),
        html.Hr(),
        html.H4(className='what-is',
                children='Sentiment Analysis'),
        dcc.Markdown('''
An ensembling approach was adopted for the sentiment analysis. TThe weighted ensembling method defines a weight to each of the classifiers and derives a final probability score of the article being positive. The weight is defined by the following equation, where the weight illustrates the accuracy of each classifier.
weights the contribution of each of the base models positive probability predictions on the final prediction. A final probability of above 0.5 will be classified as a positive news article.
 '''),
        html.Div(
            html.Img(
                className='align-self-center',
                src=f'{parent_img_path}/assets/ensemble_formula.png',
                style={'width': "10%"}
            ), style={'textAlign': 'center'}),
        dcc.Markdown('''
The confusion matrix for 3 stocks are shown below with regards to the Sentiment Analysis:'''),

        html.Div([
            dcc.Dropdown(['AAPL', 'TSLA', 'MSFT'], 'AAPL',
                         id='conf-dropdown', style={'width': '40%', 'textAlign': 'center'}),
            html.Div(id='dd-output-container', style={'textAlign': 'center'})
        ], style={'textAlign': 'center'}),
        html.Hr(),

        html.H4(className='what-is',
                children='COVID-19 Data'),
        dcc.Markdown('''
Additionally, with the pandemic looming over the past 2 years, literature suggests that  COVID-19 has an adverse and predictive relationship with stock price. 
The COVID-19 data is collected from the Covid-19 Data Repository by the Center for Systems Science and Engineering at John Hopkins University. THe dataset contains a complete list of COVID-19 data and is updated daily. The data sources include the World Health Organization “WHO”, European Centre for Disease Prevention and Control “ECDC” and other various government organizations.  
 
 The graph below shows the number of COVID cases and deaths for each country over the past 2 years.'''), dcc.Dropdown(
            id='covid-dropdown',
            options=[{'label': i, 'value': i} for i in covid_countries],
            placeholder="Please select..",
            value='United States',
            searchable=True, multi=False
        ),            dcc.Graph(id='covid-graph'),
        html.Hr(),
        html.H4(className='what-is',
                children='Disasters Data'),
        dcc.Markdown('''
The Natural disasters data is collected from the International Disaster Database’s Emergency Events Database “EMDAT” launched by the Centre for Research on the Epidemiology for Disasters (CRED) in 1988. The dataset contains over 22,000 mass disasters from 1900 to the present day compiled from different sources such as UN agencies, non-governmental organisations and insurance companies.

The data contains the disaster date, location as well as severity metrics such as the number of deaths and total estimated damages in monetary terms. The disasters are filtered to include only disaster events in the Americas since it is deemed more appropriate when applying into stock predictions for American stocks in the S&P 500.

While the total deaths have been included as part of the features, the total damages has been excluded as the data quality was poor and there were significant missing data.
'''), dcc.Dropdown(
            id='disaster-dropdown',
            options=[{'label': i, 'value': i}
                     for i in disaster_continents],
            placeholder="Please select..",
            value='Americas',
            searchable=True, multi=False
        ),
        dcc.Graph(id='disaster-graph')


    ])
