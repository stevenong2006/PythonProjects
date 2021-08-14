import dash
import dash_html_components as html
from dash.dependencies import Input, Output

def make_button_style(
    background_color=None,
    color=None,
    height=None,               
    width=None,               
    margin_top=None,               
    margin_left=None
):

# white_button_style = {'background-color': 'white',
#                       'color': 'black',
#                       'height': '50px',
#                       'width': '100px',
#                       'margin-top': '10px',
#                       'margin-left': '10px'}

# red_button_style = {'background-color': 'red',
#                     'color': 'white',
#                     'height': '50px',
#                     'width': '100px',
#                     'margin-top': '10px',
#                     'margin-left': '10px'}

    button_style = dict()
    button_style['background-color'] = background_color               
    button_style['color'] = color               
    button_style['height'] = height               
    button_style['width'] = width               
    button_style['margin-top'] = margin_top               
    button_style['margin-left'] = margin_left

    return button_style

MACHINE_ON = True

app = dash.Dash(__name__)

white_button_style = make_button_style('white', 'black', '50px', '100px', '10px', '10px')
red_button_style = make_button_style('red', 'white', '50px', '100px', '10px', '10px')

app.layout = html.Div([
    html.H2(id='machine_status',
            children=["Machine Status: OFF"],
    ),
    html.Button(id='button',
                children=['OFF'],
                n_clicks=0,
                style=white_button_style
    )

])



@app.callback([
    Output('button', 'style'),
    Output('button', 'children'),
    Output('machine_status', 'children'),
    ], [Input('button', 'n_clicks')])
def change_button_style(n_clicks):

    global MACHINE_ON

    if n_clicks % 2 > 0:
        MACHINE_ON = True
        return red_button_style, ['OFF'], [f"Machine Status: ON -- n_clicks={n_clicks}"]
    else:
        MACHINE_ON = False
        return white_button_style, ['ON'], [f"Machine Status: OFF -- n_clicks={n_clicks}"]

if __name__ == '__main__':
    app.run_server(debug=True)