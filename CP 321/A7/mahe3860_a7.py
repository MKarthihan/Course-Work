
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load the dataset
df = pd.read_csv('world_cup_matches.csv')

# Preprocess winner counts
winner_counts = df['Winners'].value_counts().reset_index()
winner_counts.columns = ['Country', 'Wins']

# List of unique years and countries
years = sorted(df['Year'].unique())
countries = sorted(winner_counts['Country'].unique())

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("FIFA World Cup Winners Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.H2("Choropleth Map of Winning Countries", id='choropleth-map'),
        dcc.Graph(id='map-graph')
    ]),

    html.Div([
        html.H2("Select a Country to View Number of Wins"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': c, 'value': c} for c in countries],
            placeholder='Select a country'
        ),
        html.Div(id='country-output')
    ], style={'paddingTop': '30px'}),

    html.Div([
        html.H2("Select a Year to View Winner and Runner-Up"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': y, 'value': y} for y in years],
            placeholder='Select a year'
        ),
        html.Div(id='year-output')
    ], style={'paddingTop': '30px'}),

], style={'backgroundColor': 'white', 'padding': '40px'})

# Choropleth map callback
@app.callback(
    Output('map-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_map(selected_country):
    fig = px.choropleth(
        winner_counts,
        locations='Country',
        locationmode='country names',
        color='Country',  # Each country gets a unique color
        hover_name='Country',
        hover_data={'Wins': True, 'Country': False},  # Show Wins on hover
        title='World Cup Winning Countries',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white',
        coloraxis_showscale=False  # Hide scale bar (not useful for categories)
    )
    return fig

# Country selection callback
@app.callback(
    Output('country-output', 'children'),
    Input('country-dropdown', 'value')
)
def show_country_wins(country):
    if country is None:
        return ""
    wins = winner_counts[winner_counts['Country'] == country]['Wins'].values[0]
    return f"{country} has won the World Cup {wins} time(s)."

# Year selection callback
@app.callback(
    Output('year-output', 'children'),
    Input('year-dropdown', 'value')
)
def show_year_result(year):
    if year is None:
        return ""
    row = df[df['Year'] == year].iloc[0]
    return f"In {year}, {row['Winners']} won against {row['Runners-up']}."

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8051)