import plotly.express as px

from dash import dcc
from dash import dash_table

def build_dropdown_menu(menu_items):
    return dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in menu_items],
        value=menu_items[-1],
        clearable=False,
    )

def init_graph():
    return dcc.Graph(id="bar-chart")

def build_figure(df, attributes):
    x, y = attributes
    fig = px.bar(df, x=x, y=y)
    return fig
