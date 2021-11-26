import plotly.express as px
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
# Load Data
df = px.data.tips()
# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H1("JupyterDash Demo"),
    dcc.Graph(id='graph'),
    html.Label([
        "colorscale",
        dcc.Dropdown(
            id='colorscale-dropdown', clearable=False,
            value='plasma', options=[
                {'label': c, 'value': c}
                for c in px.colors.named_colorscales()
            ])
    ]),
])
# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input("colorscale-dropdown", "value")]
)
def update_figure(colorscale):
    return px.scatter(
        df, x="total_bill", y="tip", color="size",
        color_continuous_scale=colorscale,
        render_mode="webgl", title="Tips"
    )
# Run app and display result inline in the notebook
# app.run_server(mode='jupyterlab')

# Run app and display result inline in the notebook
# app.run_server(mode='inline', , host='0.0.0.0', port='8050', dev_tools_ui=True, threaded=True )
# app.run_server(mode='jupyterlab', host='0.0.0.0', port='8050', dev_tools_ui=True, threaded=True)
# app.run_server(mode='external',host='0.0.0.0', port='8050', dev_tools_ui=True, threaded=True)
app.run_server(mode='external',host='0.0.0.0', port='8050', dev_tools_ui=True)
