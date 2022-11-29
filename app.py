from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from plotly.subplots import make_subplots

import plotly.graph_objects as go

from layout_helper import run_standalone_app
from data_prep import *

from pages import (
    cdlTab,
    taTab,
    cnnTab,
    newsTab,
    aboutTab
)
from assets import (
    __cdl_words as cdl_words
)

# Configurations
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
    return 'DASC7600 - Fin Pattern Project'

# def layout():
#     return html.Div(
#         id = 'forna-body',
#         className = 'app-body',
#         style = {'height': '100vh'},
#         children = [
#             aboutTab.create_page(),
#             # taTab.create_page(),
#             # newsTab.create_page(),
#             cdlTab.create_page(cdl_words),
#             cnnTab.create_page(cdl_words)
#         ]
#     )


# Main layout with tabs
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

                        # Tab - About this project
                        dcc.Tab(
                            label='About this Project',
                            value='what-is',
                            children=aboutTab.create_page()
                        ),

                        # Tab - Technical Indicators
                        dcc.Tab(
                            label='Technical Indicators',
                            value='technical-indicators',
                            children=taTab.create_page()
                        ),
                        
                        # Unexpected News
                        dcc.Tab(
                            label='Unexpected News',
                            value='sentiment',
                            children=newsTab.create_page()
                        ),
                        
                        # Candlestick Pattern
                        # dcc.Tab(
                        #     label='Candlestick Pattern',
                        #     value='candlestick',
                        #     children=cdlTab.create_page(cdl_words)
                        # ),
                        
                        # 3D CNN Modeling
                        dcc.Tab(
                            label='Candlestick Pattern & 3D CNN Modeling',
                            value='cdl_cnn',
                            children=cnnTab.create_page(cdl_words)
                        )
                    ], 
                    style={'height': '50%'})
                ]),


            dcc.Store(id='forna-sequences', data=initial_sequences),
            # dcc.Store(id='forna-custom-colors')
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

    @_app.callback(
        Output('cdl-graph', 'figure'),
        [Input('stock_cdl_dropdown', 'value')],
        [Input('cdl_pattern_dropdown', 'value')])
    def updateCdlGraph(f, patterns = 'morning_star'):
        df_cdl = cnnTab.df_cdl
        temp = df_cdl[df_cdl['ticker'] == f].tail(200)
        temp = temp.set_index('report_date')
        print(patterns)

        if type(patterns) != list:
            patterns = [patterns]

        annotation_list = [dict(x = ind, y = row['high'], text = row['candlestick_label'].replace('_', ' ').capitalize())\
                   for ind, row in temp[temp['candlestick_label'].isin(patterns)].iterrows()]

        fig = go.Figure(
            data = [go.Candlestick(
                x = temp.index,
                open = temp['open'],
                high = temp['high'], 
                low = temp['low'],
                close = temp['close'],
                text = temp['candlestick_label']
            )]
        )

        fig.update_layout(
            xaxis_rangeslider_visible = False,
            annotations = annotation_list
        )

        return fig

    @_app.callback(
        Output('3d-graph', 'figure'),
        [Input('stock_3d_dropdown', 'value')],
        [Input('report_date', 'date')])
    def update3DGraph(f, report_date):
        df_cdl = cnnTab.df_cdl
        temp = df_cdl[df_cdl['ticker'] == f]
        temp = temp.set_index('report_date')
        annotation = [dict(x = report_date, text = report_date, y = temp['close'].median() / 2)]

        fig = go.Figure(
            data = [
                go.Line(
                    x = temp.index,
                    y = temp['close']
                )
            ]
        )

        fig.add_vline(x=report_date, line_width=3, line_dash="dash", line_color="green")

        fig.update_layout(
            xaxis_rangeslider_visible = False,
            annotations = annotation
        )

        return fig

    @_app.callback(
        Output('model-prediction', 'children'),
        [Input('stock_3d_dropdown', 'value')],
        [Input('report_date', 'date')])
    def updateModelPrediction(f, report_date):
        df_predict = cnnTab.df_predict
        print(f, report_date)

        temp = df_predict[(df_predict['stock'] == f)\
             & (df_predict['report_date'] == report_date)]
        print(temp)

        predict = 'Rise' if temp['predict'].iloc[0] == 1 else 'Drop'
        label = 'Rise' if temp['label'].iloc[0] == 1 else 'Drop'
    
        return [
            html.Div(f'Model Prediction after {report_date}: {predict}'),
            html.Div(f'Actual prediction after {report_date}: {label}')
        ]

    @_app.callback(
        Output('dd-output-container', 'children'),
        Input('conf-dropdown', 'value')
    )
    def update_output(value):
        return     html.Div(
                html.Img(
                    className='align-self-center', 
                    src = f'{parent_img_path}/assets/'+value+'.png', 
                    style={'width': "25%"}
                ))

    @_app.callback(
    Output('feature-graph', 'figure'),
     Input('feature-dropdown','value'))

#Figure Update
    def update_figure(feature):
        filtered_df = feature_df[feature_df['Attribute'].isin(feature)]
        fig = go.Figure(go.Bar(x=filtered_df['Attribute'], y=filtered_df['Importance']))
        fig.update_xaxes(title_text="Features")
        # Set y-axes titles
        fig.update_yaxes(title_text="Importance")
        fig.update_layout(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )  
                        
        return fig
        
    @_app.callback(
    Output('covid-graph', 'figure'),
     Input('covid-dropdown','value'))
#Figure Update
    def update_figure(locations):
        filtered_df = covid_df[covid_df['location'] == locations]
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_scatter(x=filtered_df['date'], y=filtered_df['total_cases'], name='Total Cases')
        fig.add_scatter(x=filtered_df['date'], y=filtered_df['total_deaths'], name='Total Deaths', secondary_y=True)
        fig.update_xaxes(title_text="Date")
        # Set y-axes titles
        fig.update_yaxes(title_text="# of Cases", secondary_y=False)
        fig.update_yaxes(title_text="# of Deaths", secondary_y=True)

        fig.update_layout(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )  
        return fig
    @_app.callback(
    Output('disaster-graph', 'figure'),
    Input('disaster-dropdown','value'))
#Figure Update
    def update_figure(continents):
        filtered_df = disaster_df[disaster_df['Continent'] == continents]
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_scatter(x=filtered_df['date'], y=filtered_df['Total Deaths'], name='Total Deaths')
        fig.update_xaxes(title_text="Date")
        # Set y-axes titles
        fig.update_yaxes(title_text="# of Deaths", secondary_y=False)

        fig.update_layout(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )  
        return fig

app = run_standalone_app(layout, callbacks, header_colors, __file__)
app.title = 'FinPattern'
app._favicon = (f'{parent_path}/dslab_logo.png')

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
    # app.run()
