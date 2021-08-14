import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_ui_utility import button_util

btn_util = button_util()
white_button_style = btn_util.make_button_style('white', 'black', '50px', '100px', '10px', '10px')

button = html.Div(
    [
        dbc.Button(
            children=["Click me"], 
            id="example-button", 
            className="mr-2", 
            n_clicks=0,
            style=white_button_style

        ),
        html.Span(id="example-output", style={"verticalAlign": "middle"}),
    ]
)

app = dash.Dash(__name__)

app.layout = html.Div([button])

@app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."


if __name__ == '__main__':
    app.run_server(debug=True)