import dash_html_components as html
import dash_core_components as dcc

def create_page():
    return html.Div(className='control-tab', children=[
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