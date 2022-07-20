""" Dashboard main code."""

from dash import Dash
import components as c

app = Dash(__name__, suppress_callback_exceptions=True,
           title='ENVRI - State of the Environment')


# Layout
app.layout = c.main_layout

if __name__ == '__main__':
    app.run_server(debug=True)
