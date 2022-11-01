from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import dash_bio
import plotly.graph_objects as go
import pandas as pd
from layout_helper import run_standalone_app
import os
from data_prep import *

def header_colors():
    return {
        'bg_color': '#005985',
        'font_color': 'white',
    }


initial_sequences = {
    'PDB_01019': {
        'sequence': 'AUGGGCCCGGGCCCAAUGGGCCCGGGCCCA',
        'structure': '.((((((())))))).((((((()))))))',
        'options': {
            'applyForce': True,
            'circularizeExternal': True,
            'avoidOthers': False,
            'labelInterval': 6,
            'name': 'PDB_01019'
        }
    }
}


def description():
    return 'RNA secondary structure analysis.'


def layout():
    return html.Div(
        id='forna-body',
        className='app-body',
        style={'height': '100vh'},
        children=[
            html.Div(
                id='forna-control-tabs',
                className='control-tabs',
                children=[
                    dcc.Tabs(id='forna-tabs', value='what-is', children=[
                        dcc.Tab(
                            label='About this Project',
                            value='what-is',
                            children=html.Div(className='control-tab', children=[
                                html.H4(className='what-is',
                                        children='FinPattern'),
                                dcc.Markdown('''
                                Beginning in the 1600s, the first stock market opened in Amsterdam and market participants started to trade stocks in the open market. Over the years of the development of stock markets and advancements in technology, practitioners and academics have employed different tools and approaches with an aim to study and predict stock momentum. In the past, researchers forecast the stock momentum by the means of technical analysis indicators and candlestick patterns and managed to make profits from their prediction. However, those studies could not assess the validity of the indicators and did not allow to take the market sentiment into consideration. With the lack of transaction data and technology, it is difficult for researchers to comprehensively validate their hypothesis on stock momentum prediction.
                                
                                This study aims to handle the complexity of evaluation on technical analysis, candlestick patterns as well as incident sentiment in parallel, and develop an advanced convolutional neural network (CNN) model to predict the stock momentum in consideration of the above dimensions. We have performed feature importance analysis to identify the relevant indicators, conducted sentiment analysis on the news, incidents, and COVID-19-related events to generate the sentiment score factors, as well as considering the above information along with the candlestick patterns, cross industries, and time-lag dimensions to construct a 3D data structure and train the CNN models for prediction. 
                                
                                Our interim result shows the proposed CNN model outperforms the baseline model which is trained by Logistic Regression with candlestick patterns only. In the future, we would also consider the trading rules, COVID-19, and natural disaster factors, and continue to fine-tune our CNN model to enhance the model performance. We believe our project could provide insight to practitioners to further study the interaction between technical analysis, candlestick patterns, and industry sentiment so as to provide a comprehensive view of stock market movement.





                                '''),
                                html.Img(
                                    className='align-self-center', src='./assets/main.png', style={'height': '20%'}),

                                html.H4(className='what-is',
                                        children='Stock Price'),
                                dcc.Dropdown(id='stock_dropdown', multi=False, clearable=True,
                                             options=[{'label': f, 'value': f}
                                                      for f in stocks],
                                             value=list(dict_stock.keys())[0], searchable=True, style={'width': '65%'}),
                                dcc.Dropdown(id='stock_metric_dropdown', multi=True, clearable=True, style={
                                             'width': '100%'}),
                                dcc.Graph(id='stock-graph')
                            ])
                        ),

                        dcc.Tab(
                            label='Technical Indicators',
                            value='add-sequence',
                            children=html.Div(className='control-tab', children=[
                                html.Div(
                                    title='Enter a dot-bracket string and a nucleotide sequence.',
                                    className='app-controls-block',
                                    children=[
                                        html.Div(className='fullwidth-app-controls-name',
                                                 children='Sequence'),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Specify the nucleotide sequence as a string.'
                                        ),
                                        dcc.Input(
                                            id='forna-sequence',
                                            placeholder=initial_sequences['PDB_01019']['sequence']
                                        ),

                                        html.Br(),
                                        html.Br(),

                                        html.Div(className='fullwidth-app-controls-name',
                                                 children='Structure'),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Specify the RNA secondary structure '
                                            'with a dot-bracket string.'
                                        ),
                                        dcc.Input(
                                            id='forna-structure',
                                            placeholder=initial_sequences['PDB_01019']['structure']
                                        ),

                                    ]
                                ),
                                html.Div(
                                    title='Change some boolean properties.',
                                    className='app-controls-block',
                                    children=[
                                        html.Div(className='app-controls-name',
                                                 children='Apply force'),
                                        daq.BooleanSwitch(
                                            id='forna-apply-force',
                                            on=True,
                                            color='#85002D'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Indicate whether the force-directed layout ' +
                                            'will be applied to this molecule.'
                                        ),
                                        html.Br(),
                                        html.Div(className='app-controls-name',
                                                 children='Circularize external'),
                                        daq.BooleanSwitch(
                                            id='forna-circularize-external',
                                            on=True,
                                            color='#85002D'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Indicate whether the external loops ' +
                                            'should be forced to be arranged in a circle.'
                                        ),
                                        html.Br(),
                                        html.Div(className='app-controls-name',
                                                 children='Avoid others'),
                                        daq.BooleanSwitch(
                                            id='forna-avoid-others',
                                            on=True,
                                            color='#85002D'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Indicate whether this molecule should ' +
                                            '"avoid" being close to other molecules.'
                                        ),
                                        html.Br(),
                                        html.Div(className='app-controls-name',
                                                 children='Label interval'),
                                        dcc.Slider(
                                            id='forna-label-interval',
                                            min=1,
                                            max=10,
                                            value=5,
                                            marks={i+1: str(i+1)
                                                   for i in range(10)}
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Indicate how often nucleotides are ' +
                                            'labelled with their number.'
                                        )

                                    ]
                                ),

                                html.Div(
                                    className='app-controls-block',
                                    children=[
                                        html.Div(className='fullwidth-app-controls-name',
                                                 children='ID'),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Specify a unique ID for this sequence.'
                                        ),
                                        dcc.Input(id='forna-id',
                                                  placeholder='PDB_01019')
                                    ]
                                ),

                                html.Hr(),

                                html.Div(id='forna-error-message'),
                                html.Button(id='forna-submit-sequence',
                                            children='Submit sequence'),
                            ])
                        ),
                        dcc.Tab(
                            label='Unexpected News',
                            value='sentiment',
                            children=html.Div(className='control-tab', children=[
                                html.Div(
                                    className='app-controls-block',
                                    children=[
                                        html.Div(
                                            className='fullwidth-app-controls-name',
                                            children='Sequences to display'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Choose the sequences to display by ID.'
                                        ),
                                        html.Br(),
                                        dcc.Dropdown(
                                            id='forna-sequences-display',
                                            multi=True,
                                            clearable=True,
                                            value=['PDB_01019']
                                        )
                                    ]
                                ),
                                html.Hr(),
                                html.Div(
                                    className='app-controls-block',
                                    children=[
                                        html.Div(
                                            className='app-controls-block',
                                            children=[
                                                html.Div(
                                                    className='fullwidth-app-controls-name',
                                                    children='Sequence information by ID'
                                                ),
                                                html.Div(
                                                    className='app-controls-desc',
                                                    children='Search for a sequence by ID ' +
                                                    'to get more information.'
                                                ),
                                                html.Br(),
                                                dcc.Dropdown(
                                                    id='forna-sequences-info-search',
                                                    clearable=True
                                                ),
                                                html.Br(),
                                                html.Div(
                                                    id='forna-sequence-info')
                                            ]
                                        )
                                    ]
                                )
                            ])
                        ),
                        dcc.Tab(
                            label='Candlestick Pattern',
                            value='candlestick',
                            children=html.Div(className='control-tab', children=[
                                html.Div(
                                    className='app-controls-name',
                                    children='Color scheme'
                                ),
                                dcc.Dropdown(
                                    id='forna-color-scheme',
                                    options=[
                                        {'label': color_scheme,
                                         'value': color_scheme}
                                        for color_scheme in [
                                            'sequence', 'structure', 'positions', 'custom'
                                        ]
                                    ],
                                    value='sequence',
                                    clearable=False
                                ),
                                html.Div(
                                    className='app-controls-desc',
                                    id='forna-color-scheme-desc',
                                    children='Choose the color scheme to use.'
                                ),
                                html.Div(
                                    id='forna-custom-colorscheme',
                                    className='app-controls-block',
                                    children=[
                                        html.Hr(),
                                        html.Div(
                                            className='app-controls-name',
                                            children='Molecule name'
                                        ),
                                        dcc.Dropdown(
                                            id='forna-custom-colors-molecule'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Select the sequence to which the custom ' +
                                            'color scheme will be applied. If none is selected, ' +
                                            'the color scheme will be applied to all molecules.'
                                        ),
                                        html.Br(),
                                        html.Div(
                                            className='app-controls-name',
                                            children='Coloring range'
                                        ),
                                        daq.ColorPicker(
                                            id='forna-color-low',
                                            label='Low',
                                            labelPosition='top',
                                            value={'hex': '#BE0000'}
                                        ),
                                        daq.ColorPicker(
                                            id='forna-color-high',
                                            label='High',
                                            labelPosition='top',
                                            value={'hex': '#336AFF'}
                                        ),
                                        html.Div(
                                            className='fullwidth-app-controls-name',
                                            children='Coloring domain'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Specify a minimum and maximum value ' +
                                            'which will be used to calculate intermediate ' +
                                            'colors for nucleotides that have a numerical ' +
                                            'value specified below.'
                                        ),
                                        html.Br(),
                                        dcc.Input(
                                            id='forna-color-domain-low',
                                            type='number',
                                            value=1
                                        ),
                                        dcc.Input(
                                            id='forna-color-domain-high',
                                            type='number',
                                            value=100
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.Div(
                                            className='fullwidth-app-controls-name',
                                            children='Colors map'
                                        ),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Specify the colors for each ' +
                                            'nucleotide by entering the position of ' +
                                            'the nucleotide into the left input box, ' +
                                            'and either a) a string representation ' +
                                            'of a color or b) a number within the ' +
                                            'range specified above. Then, press the ' +
                                            '"Submit" button,'
                                        ),
                                        html.Br(),
                                        dcc.Input(
                                            id='forna-color-map-nucleotide',
                                            type='number',
                                            min=1,
                                            placeholder=1
                                        ),
                                        dcc.Input(
                                            id='forna-color-map-color',
                                            placeholder='green'
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.Button(
                                            id='forna-submit-custom-colors',
                                            children='Submit'
                                        )
                                    ]
                                )
                            ])
                        ),
                        dcc.Tab(
                            label='3D CNN',
                            value='cnn',
                            children=html.Div(className='control-tab', children=[
                                html.Div(
                                    className='app-controls-block',
                                    children=[
                                        html.Div(className='fullwidth-app-controls-name',
                                                 children='Title pattern'),
                                        html.Div(
                                            className='app-controls-desc',
                                            children='Specify the information which will ' +
                                                     'be rendered on the mouse hover.'
                                        ),
                                        dcc.Input(id='forna-title-pattern',
                                                  placeholder='${structName}:${num}')
                                    ]
                                ),
                                html.Br(),
                                html.Button(
                                    id='forna-submit-title-pattern',
                                    children='Submit'
                                )
                            ])
                        )
                    ], style={'height': '50%'})
                ]),
            html.Div(id='forna-container', children=[

                # dash_bio.FornaContainer(
                #     id='forna',
                #     height=500,
                #     width=500
                # )
            ]),


            dcc.Store(id='forna-sequences', data=initial_sequences),
            dcc.Store(id='forna-custom-colors')
        ]
    )


def callbacks(_app):

    @_app.callback(
        [Output('forna-sequences', 'data'),
         Output('forna-error-message', 'children')],
        [Input('forna-submit-sequence', 'n_clicks')],
        [State('forna-sequence', 'value'),
         State('forna-structure', 'value'),
         State('forna-apply-force', 'on'),
         State('forna-circularize-external', 'on'),
         State('forna-avoid-others', 'on'),
         State('forna-label-interval', 'value'),
         State('forna-id', 'value'),
         State('forna-sequences', 'data')]
    )
    def add_sequence(nclicks, sequence, structure, apply_force,
                     circularize_ext, avoid_others, label_interval,
                     seqid, current):

        if nclicks is None or nclicks == 0:
            raise PreventUpdate

        error_msg = html.P(
            'You already have a sequence with this ID. ' +
            'Please choose a different ID, or check the next tab ' +
            'to see which IDs have already been taken.',
            style={'color': 'red'}
        )

        if sequence is None or structure is None:
            raise PreventUpdate

        if current is None:
            current = {}

        if seqid not in current.keys():
            error_msg = html.P(
                'Successfully added {}!'.format(seqid),
                style={'color': 'green'}
            )
            current[seqid] = {
                'sequence': sequence,
                'structure': structure,
                'options': {
                    'applyForce': apply_force,
                    'circularizeExternal': circularize_ext,
                    'avoidOthers': avoid_others,
                    'labelInterval': label_interval,
                    'name': seqid
                }
            }

        return current, error_msg

    @_app.callback(
        Output('forna', 'hoverPattern'),
        [Input('forna-submit-title-pattern', 'n_clicks')],
        [State('forna-title-pattern', 'value')]
    )
    def update_hover_pattern(nclicks, hover_pattern):
        if nclicks is None or nclicks == 0:
            raise PreventUpdate

        return hover_pattern

    @_app.callback(
        Output('forna', 'colorScheme'),
        [Input('forna-color-scheme', 'value')]
    )
    def update_color_scheme(color_scheme):
        return color_scheme

    @_app.callback(
        Output('forna-custom-colorscheme', 'style'),
        [Input('forna-color-scheme', 'value')]
    )
    def show_hide_custom_colorscheme(color_scheme):
        return {'display': 'block' if color_scheme == 'custom' else 'none'}

    @_app.callback(
        Output('forna', 'customColors'),
        [Input('forna-custom-colors', 'data')]
    )
    def update_custom_colors(data):
        if data is None:
            raise PreventUpdate
        return data

    @_app.callback(
        Output('forna-custom-colors', 'data'),
        [Input('forna-submit-custom-colors', 'n_clicks'),
         Input('forna-color-low', 'value'),
         Input('forna-color-high', 'value')],
        [State('forna-color-domain-low', 'value'),
         State('forna-color-domain-high', 'value'),
         State('forna-color-map-nucleotide', 'value'),
         State('forna-color-map-color', 'value'),
         State('forna-custom-colors-molecule', 'value'),
         State('forna-custom-colors', 'data')]
    )
    def update_custom_colors_storage(nclicks, color_low, color_high,
                                     color_domain_low, color_domain_high,
                                     color_map_index, color_map_color,
                                     seq_id, current):
        if nclicks is None or nclicks == 0:
            raise PreventUpdate
        if color_low is None or color_high is None:
            raise PreventUpdate
        if color_domain_low is None or color_domain_high is None:
            raise PreventUpdate

        if color_map_index is None or color_map_color is None:
            raise PreventUpdate

        if seq_id is None:
            seq_id = ''

        try:
            color = float(color_map_color)
        except ValueError:
            color = color_map_color

        if current is None:
            current = {'domain': [], 'range': [], 'colorValues': {}}

        current['domain'] = [color_domain_low, color_domain_high]
        current['range'] = [color_low['hex'], color_high['hex']]

        if current['colorValues'].get(seq_id) is None:
            current['colorValues'][seq_id] = {}

        current['colorValues'][seq_id].update({color_map_index: color})

        return current

    @_app.callback(
        [Output('forna-sequences-display', 'options'),
         Output('forna-sequences-info-search', 'options'),
         Output('forna-custom-colors-molecule', 'options')],
        [Input('forna-sequences', 'data')]
    )
    def update_sequences(data):

        if data is None:
            raise PreventUpdate

        new_options = [
            {'label': sequence_id,
             'value': sequence_id}
            for sequence_id in data.keys()
        ]

        return new_options, new_options, new_options

    @_app.callback(
        Output('forna-sequence-info', 'children'),
        [Input('forna-sequences-info-search', 'value')],
        [State('forna-sequences', 'data')]
    )
    def update_sequence_info(sequence_id, data):
        if data is None or sequence_id is None:
            raise PreventUpdate

        return html.Div(
            [
                'Sequence: {}'.format(data[sequence_id]['sequence']),
                html.Br(),
                'Structure: {}'.format(data[sequence_id]['structure'])
            ] + [
                html.Div([
                    '{}: {}'.format(
                        option, data[sequence_id]['options'][option]
                    ),
                    html.Br()
                ])
                for option in data[sequence_id]['options'].keys()
            ]
        )

    @_app.callback(
        Output('forna', 'sequences'),
        [Input('forna-sequences-display', 'value')],
        [State('forna-sequences', 'data')]
    )
    def update_shown_sequences(selected_sequence_ids, stored_sequences):

        if selected_sequence_ids is None or stored_sequences is None:
            raise PreventUpdate

        sequences = []

        for sequence_id in selected_sequence_ids:
            sequences.append(
                stored_sequences[sequence_id]
            )

        return sequences

    @_app.callback(
        Output('stock_metric_dropdown', 'options'),
        [Input('stock_dropdown', 'value')])
    def update_date_dropdown(f):
        return [{'label': i, 'value': i} for i in dict_stock[f]]

    @_app.callback(
        Output('stock-graph', 'figure'),
        [Input('stock_metric_dropdown', 'value')],
        [State('stock_dropdown', 'value')])
    def updateGraph(channels, f):
        if channels:
            fig = go.Figure(data=[go.Scatter(
                x=dict_stock[f]['date'], y=dict_stock[f][i], name=i) for i in channels])
            title = f
            fig.update_layout(title=title,
                              xaxis_title='Date',
                              yaxis_title='$USD'
                              )
            return fig
        else:
            return go.Figure(data=[])


app = run_standalone_app(layout, callbacks, header_colors, __file__)
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
