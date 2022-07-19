""" Create a simple dashboard with plotly Dash. """

# Run this app with 'python run.py' and open the browser at 
# http://localhost:8050/

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


# Table
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div(
    children=[
        html.Div(
            style={
            'backgroundColor': colors['background']
            },
            children=[
                html.H1(
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    },
                    children='Hello Dash'
                ),

                html.Div(
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    },
                    children='''
                    Dash: A web application framework for your data.
                    '''
                ),

                dcc.Graph(
                    id='example-graph',
                    figure=fig
                ),
            ]
        ),
        html.Div(
            children = [ 
                html.H4(children='US Agriculture Exports (2011)'),
                generate_table(df),
            ]
        ),
        html.Div(
            children = [ 
                html.H4(children='Markdown'),
                html.Div(children=markdown_text),
            ]
        ),
        html.Div(
            style={
                'display': 'flex',
                'flex-direction': 'row'
            },
            children = [ 
                html.Div(
                    style={
                        'padding': 10,
                        'flex': 1
                    },
                    children=[
                        html.Label('Dropdown'),
                        dcc.Dropdown(
                            ['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

                        html.Br(),
                        html.Label('Multi-Select Dropdown'),
                        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
                                    ['Montréal', 'San Francisco'],
                                    multi=True),

                        html.Br(),
                        html.Label('Radio Items'),
                        dcc.RadioItems(
                            ['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
                    ]
                ),
                html.Div(
                    style={
                        'padding': 10,
                        'flex': 1
                    },
                    children=[
                        html.Label('Checkboxes'),
                        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                                    ['Montréal', 'San Francisco']
                        ),

                        html.Br(),
                        html.Label('Text Input'),
                        dcc.Input(value='MTL', type='text'),

                        html.Br(),
                        html.Label('Slider'),
                        dcc.Slider(
                            min=0,
                            max=9,
                            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
                            value=5,
                        ),
                    ]
                ),
            ]
        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
