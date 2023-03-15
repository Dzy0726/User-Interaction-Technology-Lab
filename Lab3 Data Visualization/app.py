import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

file = pd.read_csv('black-friday/BlackFriday.csv', )

sumPurchase = file['Purchase'].sum()
file['Purchase_Percent'] = round(file['Purchase'] / sumPurchase, 6)

app = dash.Dash(__name__)

categorys = ["Gender", "Age", "Occupation", "City_Category",
             "Stay_In_Current_City_Years", "Marital_Status"]

pie_category = ['Gender', 'Age', 'City_Category', "Stay_In_Current_City_Years", "Marital_Status"]
pie_values = ["Purchase", "Product_Category_1_Sales", "Product_Category_2_Sales", "Product_Category_3_Sales"]

app.layout = html.Div([
    html.H1(
        children='Black Friday Data Visualization',
        style={
            'textAlign': 'Center',
            'text-transform': 'uppercase',
        }
    ),
    html.P(
        children=" The dataset here is a sample of the transactions made in a retail store. The store wants to know "
                 "better the customer purchase behavior against different products.Specifically, here the problem is a "
                 "regression problem where we are trying to predict the dependent variable (the amount of purchase) "
                 "with the help of the information contained in the other variables.",
        style={
            'background-color': 'lightgrey',
            'border': '2px solid #ccc',
            'border-radius': '12px',
            'text-align': 'justify',
            'text-indent': '50px'
        }
    ),
    html.Div([
        html.H4(
            children='Sales of various products by',
            style={
                'padding-left': '10px',
            }
        ),
        html.Div([
            dcc.Dropdown(
                id="dropdown",
                options=[{"label": x, "value": x} for x in categorys],
                value=categorys[0],
                clearable=False,
                style={
                    'padding-left': '10px',
                },
            )
        ],
            style={
                'width': '49%',
                'display': 'inline-block',
            }
        ),
        dcc.Graph(id="bar-chart"),
    ]),

    html.Div([
        html.H4(
            children='Sunburst of Purchase',
            style={
                'padding-left': '10px'
            }
        ),
        html.Div([
            dcc.Graph(id="sunburst-chart"),
        ],
            style={
            }
        ),
    ],

    ),

    html.Div([
        html.H4(
            children='Pie-Chart:Displays the proportions by different categories',
        ),
        html.Div([
            html.P("Names:"),
        ],
            style={
                'padding-left': '20px',
            }
        ),
        html.Div([
            dcc.Dropdown(
                id='names',
                value=pie_category[0],
                options=[{'value': x, 'label': x}
                         for x in pie_category],
                clearable=False
            ),
        ],
            style={
                'width': '50%',
            }
        ),
        html.Div([
            html.P("Values:"),
        ],
            style={
                'padding-left': '20px',
            }
        ),
        html.Div([
            dcc.Dropdown(
                id='values',
                value=pie_values[0],
                options=[{'value': x, 'label': x}
                         for x in pie_values],
                clearable=False
            ),
        ],
            style={
                'width': '50%',
            }
        ),
        dcc.Graph(id="pie-chart"),
    ],
        style={
            'padding-left': '20px'
        }
    ),
    html.Div([
        html.H4(
            children='Shopping Star',
        ),
        dcc.Graph(id="table"),
    ],
        style={
            'padding-left': '20px',
        }
    ),
])


@app.callback(
    dash.dependencies.Output("bar-chart", "figure"),
    [dash.dependencies.Input("dropdown", "value")])
def update_bar_chart(category):
    group_result = file.groupby([category])[['Product_Category_1', 'Product_Category_2', 'Product_Category_3']].agg(
        'sum')
    y_name = file[category].unique()
    y_name.sort()

    return {
        'data': [
            go.Bar(name='Product_Category_1', x=y_name, y=group_result['Product_Category_1'][y_name]),
            go.Bar(name='Product_Category_2', x=y_name, y=group_result['Product_Category_2'][y_name]),
            go.Bar(name='Product_Category_3', x=y_name, y=group_result['Product_Category_3'][y_name])
        ],
        'layout':
            go.Layout(
                xaxis={
                    'title': category,
                },
                yaxis={
                    'title': 'Sales',
                }

            )

    }


@app.callback(
    dash.dependencies.Output("sunburst-chart", "figure"),
    dash.dependencies.Input("dropdown", "value")
)
def update_sunburst(self):
    fig = px.sunburst(file, path=['City_Category', 'Gender', 'Age'], values='Purchase_Percent')
    return fig



@app.callback(
    dash.dependencies.Output("pie-chart", "figure"),
    dash.dependencies.Input("names", "value"),
    dash.dependencies.Input("values", "value")
)
def update_piechart(names, values):
    if values == "Product_Category_1_Sales":
        values = "Product_Category_1"
    elif values == "Product_Category_2_Sales":
        values = "Product_Category_2"
    elif values == "Product_Category_3_Sales":
        values = "Product_Category_3"

    fig = px.pie(file, values=values, names=names)
    return fig


@app.callback(
    dash.dependencies.Output("table", "figure"),
    dash.dependencies.Input("names", "value")
)
def update_table(table_name):
    group = file.groupby(['User_ID'])[['Purchase']].agg('sum')
    res = group.sort_values(by='Purchase', ascending=False)
    id = []
    rank = []
    i = 0
    for tmp in res['Purchase']:
        if i < 10:
            rank.append(tmp)
            i = i + 1
    for i in range(0, 10):
        id.append(res[res['Purchase'] == rank[i]].index[0])
    fig = go.Figure(data=[go.Table(
        header=dict(values=['User ID', 'Total Cost']),
        cells=dict(values=[id, rank]))])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
