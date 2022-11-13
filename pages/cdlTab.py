import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq

def create_page(cdl_words):

    cdl_intro = cdl_words.cdl_intro
    morning_star_intro = cdl_words.morning_star_intro

    return html.Div(
        className='control-tab', 
        children=[
            
            # Sub-header
            html.H4("Candlestick Pattern Analysis", className = "what-is"),
            
            # Common candlestick pattern
            html.H6("Common candlestick pattern"),
            html.Div(
                [
                    html.Img(
                        src = "./assets/cdl_basic.png",
                        style = {"width": "40%"}
                    ),
                    html.Img(
                        src = "./assets/morning_star.png",
                        style = {'width': "40%"}
                    )
                ]
            ),
            
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
            )
            
            
            # html.Div(
            #     className='app-controls-name',
            #     children='Color scheme'
            # ),
            # dcc.Dropdown(
            #     id='forna-color-scheme',
            #     options=[
            #         {'label': color_scheme,
            #             'value': color_scheme}
            #         for color_scheme in [
            #             'sequence', 'structure', 'positions', 'custom'
            #         ]
            #     ],
            #     value='sequence',
            #     clearable=False
            # ),
            # html.Div(
            #     className='app-controls-desc',
            #     id='forna-color-scheme-desc',
            #     children='Choose the color scheme to use.'
            # ),
            # html.Div(
            #     id='forna-custom-colorscheme',
            #     className='app-controls-block',
            #     children=[
            #         html.Hr(),
            #         html.Div(
            #             className='app-controls-name',
            #             children='Molecule name'
            #         ),
            #         dcc.Dropdown(
            #             id='forna-custom-colors-molecule'
            #         ),
            #         html.Div(
            #             className='app-controls-desc',
            #             children='Select the sequence to which the custom ' +
            #             'color scheme will be applied. If none is selected, ' +
            #             'the color scheme will be applied to all molecules.'
            #         ),
            #         html.Br(),
            #         html.Div(
            #             className='app-controls-name',
            #             children='Coloring range'
            #         ),
            #         daq.ColorPicker(
            #             id='forna-color-low',
            #             label='Low',
            #             labelPosition='top',
            #             value={'hex': '#BE0000'}
            #         ),
            #         daq.ColorPicker(
            #             id='forna-color-high',
            #             label='High',
            #             labelPosition='top',
            #             value={'hex': '#336AFF'}
            #         ),
            #         html.Div(
            #             className='fullwidth-app-controls-name',
            #             children='Coloring domain'
            #         ),
            #         html.Div(
            #             className='app-controls-desc',
            #             children='Specify a minimum and maximum value ' +
            #             'which will be used to calculate intermediate ' +
            #             'colors for nucleotides that have a numerical ' +
            #             'value specified below.'
            #         ),
            #         html.Br(),
            #         dcc.Input(
            #             id='forna-color-domain-low',
            #             type='number',
            #             value=1
            #         ),
            #         dcc.Input(
            #             id='forna-color-domain-high',
            #             type='number',
            #             value=100
            #         ),
            #         html.Br(),
            #         html.Br(),
            #         html.Div(
            #             className='fullwidth-app-controls-name',
            #             children='Colors map'
            #         ),
            #         html.Div(
            #             className='app-controls-desc',
            #             children='Specify the colors for each ' +
            #             'nucleotide by entering the position of ' +
            #             'the nucleotide into the left input box, ' +
            #             'and either a) a string representation ' +
            #             'of a color or b) a number within the ' +
            #             'range specified above. Then, press the ' +
            #             '"Submit" button,'
            #         ),
            #         html.Br(),
            #         dcc.Input(
            #             id='forna-color-map-nucleotide',
            #             type='number',
            #             min=1,
            #             placeholder=1
            #         ),
            #         dcc.Input(
            #             id='forna-color-map-color',
            #             placeholder='green'
            #         ),
            #         html.Br(),
            #         html.Br(),
            #         html.Button(
            #             id='forna-submit-custom-colors',
            #             children='Submit'
            #         )
                # ]
            # )
        ])