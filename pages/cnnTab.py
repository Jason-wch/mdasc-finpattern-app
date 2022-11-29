import dash_html_components as html
import dash_core_components as dcc
from data_prep import parent_img_path

def create_page(cdl_words):

    data_struct_intro = cdl_words.data_struct_intro

    return html.Div(
        className='control-tab', 
        children=[
            
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