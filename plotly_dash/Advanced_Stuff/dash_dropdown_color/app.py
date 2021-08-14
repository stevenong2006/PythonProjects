import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
# app = dash.Dash(__name__)
app.title = 'Example'
app.layout = dbc.Tabs([
    dbc.Tab(
        dbc.Card([
            dcc.Dropdown(
                id='dropdown',
                options=[
                    { 'label': 'Item 1', 'value': 'foo' },
                    { 'label': 'Item 2', 'value': 'bar' },
                    { 'label': 'Item 3', 'value': 'ha' },
                    { 'label': 'Item 4', 'value': 'weee' },
                ],
                style={'width': '40%'},
                placeholder="Pick one ..."
            ),
            html.Br(),
            html.Div(id='item-display'),
        ], body=True), label='Tab 1')
])

@app.callback(
    Output('item-display', 'children'),
    [Input('dropdown', 'value')]
)
def display_item(v):
    return dbc.Alert(f'You selected Item {v}', color='primary') 

if __name__ == '__main__':
    app.run_server(debug=True)