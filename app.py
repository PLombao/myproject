import plotly.graph_objs as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

markdown_text = '''
# Descripción:

Aquí podemos poñer una descripción en formato Markdown.
'''




app.layout = html.Div([
    html.H1(
        children='Triple Alpha Innovation',
        style={'textAlign': 'center'}
    ),
    
    html.Div(children='Esto é unha demo en Dash', 
        style={'textAlign': 'center'}
    ),
    
    dcc.Markdown(children=markdown_text),
    
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
            
    dcc.Dropdown(
        options=[
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'Africa', 'value': 'Africa'},
            {'label': 'Americas', 'value': 'Americas'},
            {'label': 'Oceania', 'value': 'Oceania'}
        ],
        
        value='Europe'
    )
            
    
])

if __name__ == '__main__':
    app.run_server(debug=True)