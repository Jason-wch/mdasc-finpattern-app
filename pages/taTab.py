import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq


def create_page():

    return html.Div(className='control-tab', children=[
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
                                            placeholder="testing"
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
                                            placeholder="testing"
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