import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import base64
import io
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("DataVizPro: Interactive Data Visualization Dashboard"),

    # File upload section
    html.Div([
        html.Label("Upload CSV or JSON File:"),
        dcc.Upload(
            id='upload-data',
            children=html.Button('Upload File'),
            multiple=False
        ),
    ]),

    # Visualization output section
    html.Div(id='output-data-upload')
])

# Callback to process uploaded data
@app.callback(
    dash.Output('output-data-upload', 'children'),
    [dash.Input('upload-data', 'contents')],
    [dash.State('upload-data', 'filename')]
)
def update_graph(contents, filename):
    if contents is None:
        return html.Div("Upload a CSV or JSON file to get started.")

    # Decode the uploaded file
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if filename.endswith('.csv'):
            # Use Pandas to read the CSV
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif filename.endswith('.json'):
            # Use Pandas to read the JSON
            df = pd.read_json(io.StringIO(decoded.decode('utf-8')))
        else:
            return html.Div("Invalid file format. Please upload a CSV or JSON file.")
    except Exception as e:
        return html.Div(f"Error reading file: {e}")

    # Create a Plotly figure (for example, a bar chart)
    fig = px.bar(df, x=df.columns[0], y=df.columns[1], title=f'{filename} Visualization')

    return html.Div([
        html.H5(f"Uploaded: {filename}"),
        dcc.Graph(figure=fig)
    ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
