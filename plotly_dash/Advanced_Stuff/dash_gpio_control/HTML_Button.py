import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_html_ui_utility import button_util
from gpiozero import LED
from time import sleep

# def make_button_style(
#     background_color=None,
#     color=None,
#     height=None,               
#     width=None,               
#     margin_top=None,               
#     margin_left=None
# ):

# # white_button_style = {'background-color': 'white',
# #                       'color': 'black',
# #                       'height': '50px',
# #                       'width': '100px',
# #                       'margin-top': '10px',
# #                       'margin-left': '10px'}

# # red_button_style = {'background-color': 'red',
# #                     'color': 'white',
# #                     'height': '50px',
# #                     'width': '100px',
# #                     'margin-top': '10px',
# #                     'margin-left': '10px'}

#     button_style = dict()
#     button_style['background-color'] = background_color               
#     button_style['color'] = color               
#     button_style['height'] = height               
#     button_style['width'] = width               
#     button_style['margin-top'] = margin_top               
#     button_style['margin-left'] = margin_left

#     return button_style

MACHINE_ON = True

led = LED(17)

app = dash.Dash(__name__)

btn_util = button_util()

white_button_style = btn_util.make_button_style('white', 'black', '50px', '100px', '10px', '10px', '8px')
red_button_style = btn_util.make_button_style('red', 'white', '50px', '100px', '10px', '10px', '8px')

app.layout = html.Div([
    html.Div(id='machine_status',
            children=[
                html.H2(
                    children=["LED Status: OFF"],
                    style={
                        'background-color':'Aqua',
                        'width':'200px'
                    }
                )
            ],      
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
    global led

    if n_clicks % 2 > 0:
        MACHINE_ON = True
        led.on()
        status = html.H2(
            children=["LED Status: ON"],
            style={
                'background-color':'red',
                'width':'200px'
            }
        )
        return red_button_style, ['OFF'], [status]
    else:
        MACHINE_ON = False
        led.off()
        status = html.H2(
            children=["LED Status: OFF"],
            style={
                'background-color':'Aqua',
                'width':'200px'
            }
        )        
        return white_button_style, ['ON'], [status]

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0', port='8085')