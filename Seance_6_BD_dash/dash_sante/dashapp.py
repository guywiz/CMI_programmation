import model.data
import view.GUI

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])

# styling the sidebar
SIDEBAR_STYLE = {
	"position": "fixed",
	"top": 0,
	"left": 0,
	"bottom": 0,
	"width": "16rem",
	"padding": "2rem 1rem",
	"background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
	"margin-left": "18rem",
	"margin-right": "2rem",
	"padding": "2rem 1rem",
}

sidebar = html.Div(
	[
		html.H2("CMI ISI", className="display-4"),
		html.Hr(),
		html.P(
			"Données de santé", className="lead"
		),
		dbc.Nav(
			[
				dbc.NavLink("Histogramme", href="/", active="exact"),
			],
			vertical=True,
			pills=True,
		),
	],
	style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
	dcc.Location(id="url"),
	sidebar,
	content
])

@app.callback(
	Output("page-content", "children"),
	[Input("url", "pathname")]
)
def render_page_content(pathname):
	if pathname == "/":
		dropdown = view.GUI.build_dropdown_menu(model.data.get_pathologies())
		graph = view.GUI.init_graph()
		return [
			html.Div([
				dropdown, graph
			])
		]

	else:
		return html.Div(
			[
				html.H1("404: Not found", className="text-danger"),
				html.Hr(),
				html.P(f"The pathname {pathname} was not recognised..."),
			]
		)

@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(patho_name):
    df, attributes = model.data.extract_patho_data(patho_name)
    return view.GUI.build_figure(df, attributes)

if __name__=='__main__':
	app.run_server(debug=False)