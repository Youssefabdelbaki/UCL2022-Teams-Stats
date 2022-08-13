import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go


goal = pd.read_csv('goals.csv')
attempt = pd.read_csv('attempts.csv')
disc = pd.read_csv('disciplinary.csv')
att = pd.read_csv('attacking.csv')
dist = pd.read_csv('distributon.csv')
defending = pd.read_csv('defending.csv')

app = Dash(__name__,external_stylesheets=[dbc.themes.FLATLY])
server = app.server


clubs = goal['club'].unique()


app.layout = html.Div([

    dbc.Row([
        dbc.Col([
            html.Br(),

            html.Img(src=app.get_asset_url('UEFA BALL.png'), style={'height':200})
        ], width={'size':2,'offset':1}, style={'textAlign':'left'}),

        dbc.Col([
            html.H1('Champion League Title 2022',style={'marginTop':80,'font-weight':'bold','font-family':'Calibri'}),

            html.H2("Teams' Stats",style={'font-family':'Calibri'})
        ], width={'size':6},style={'textAlign':'center'}),

        dbc.Col([
            html.Br(),

            html.Img(src=app.get_asset_url('UEFA-CL.png'),style={'height':200})
        ], width={'size':2}, style={'textAlign':'right'})
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([

                dcc.Dropdown(clubs, 'Real Madrid', id='Team_List',style={'backgroundColor':'#cfd6da','font-family':'Calibri','fontSize':20})
            ],color='black', outline=True)

        ], width={'size':10, 'offset':1})
    ]),

    html.Br(),

    dbc.Row([
        html.Div([
            html.Br(),

            html.P('Total Goals', style={'fontSize':18, 'font-family':'Arial'}),

            html.P(id='total_goals',style={'fontSize':30, 'font-family':'Arial','font-weight':'bold'}),

            html.Br()
        ], style={'textAlign':'center','backgroundColor':'white','width':'20%','height':120,'marginLeft':'9%'}),

        html.Div([
            html.Br(),

            html.P('Total Attempts on Target', style={'fontSize':18, 'font-family':'Arial'}),

            html.P(id='total_attempts',style={'fontSize':30, 'font-family':'Arial','font-weight':'bold'}),

            html.Br()
        ],style={'textAlign':'center','backgroundColor':'white','width':'20%','height':120,'marginLeft':'0.677%'}),

        html.Div([
            html.Br(),

            html.P('Total Yellow Cards', style={'fontSize':18, 'font-family':'Arial'}),

            html.P(id='yellow_cards',style={'fontSize':30, 'font-family':'Arial','font-weight':'bold'}),

            html.Br()
        ],style={'textAlign':'center','backgroundColor':'white','width':'20%','height':120,'marginLeft':'0.677%'}),

        html.Div([
            html.Br(),

            html.P('Total Red Cards', style={'fontSize':18, 'font-family':'Arial'}),

            html.P(id='red_cards',style={'fontSize':30, 'font-family':'Arial','font-weight':'bold'}),

            html.Br()
        ],style={'textAlign':'center','backgroundColor':'white','width':'20%','height':120,'marginLeft':'0.677%'} )
    ]),

    html.Br(),

    dbc.Row([
        html.Div([
            dcc.Graph(id='total_goals_graph',style={'width':'100%','height':'100%'})

        ], style={'backgroundColor':'white', 'width':'40%','height':400, 'marginLeft':'9%'}),

        html.Div([
            dcc.Graph(id='total_assists_graph', style={'width':'100%','height':'100%'})
        ], style={'backgroundColor':'white', 'width':'41%','height':400, 'marginLeft':'1%'})
    ]),

    html.Br(),

    dbc.Row([
        html.Div([
           dcc.Graph(id='total_attempts_graph',style={'width':'100%','height':'100%'})
        ], style={'backgroundColor':'white', 'width':'82%','height':500, 'marginLeft':'9%'})
    ]),

    html.Br(),

    dbc.Row([
        html.Div([
           dcc.Graph(id='tackles_graph',style={'width':'100%','height':'100%'})
        ], style={'backgroundColor':'white', 'width':'82%','height':400, 'marginLeft':'9%'}),
    ]),

    html.Br(),

    dbc.Row([
        html.Div([
            dcc.Graph(id='accuracy_graph',style={'width':'100%','height':'100%'})
        ],style={'backgroundColor':'white', 'width':'40%','height':1000, 'marginLeft':'9%'} ),

        html.Div([
            html.Div([
               dcc.Graph(id='dribbles_graph',style={'width':'100%','height':'100%'})
            ], style={'backgroundColor':'white', 'width':'100%','height':'50%', 'marginLeft':'1%', 'marginBottom':'1%'}),


            html.Div([
               dcc.Graph(id='cards_graph',style={'width':'100%','height':'100%'})
            ], style={'backgroundColor':'white', 'width':'100%','height':'49%', 'marginLeft':'1%'})
        ], style={'backgroundColor':'white', 'width':'41%','height':1000, 'marginLeft':'1%'})

    ]),

    html.Br(),

    dbc.Row([
        html.Div([
            dcc.Graph(id='Ball_recovered_graph',style={'width':'100%','height':'100%'})
        ],style={'backgroundColor':'white', 'width':'82%','height':500, 'marginLeft':'9%'} )
    ]),

    html.Br(),

    dbc.Row([
        html.Div([
            dcc.Graph(id='Clearance_graph',style={'width':'100%','height':'100%'})
        ],style={'backgroundColor':'white', 'width':'82%','height':500, 'marginLeft':'9%'} )
    ]),

    html.Br(),

    dbc.Row([
        html.Div([

        ])
    ])


],style={'backgroundColor':'#cfd6da','width':'100%','height':'100%'})

@app.callback(
    Output('total_goals', 'children'),
    Output('total_attempts', 'children'),
    Output('yellow_cards', 'children'),
    Output('red_cards', 'children'),
    Output('total_goals_graph', 'figure'),
    Output('total_assists_graph', 'figure'),
    Output('total_attempts_graph','figure'),
    Output('tackles_graph','figure'),
    Output('accuracy_graph','figure'),
    Output('dribbles_graph','figure'),
    Output('cards_graph','figure'),
    Output('Ball_recovered_graph','figure'),
    Output('Clearance_graph','figure'),
    Input('Team_List','value'))


def update_figure(selected_team):
    filtered_goal = goal[goal['club'] == selected_team]
    filtered_attempt = attempt[attempt['club'] == selected_team]
    filtered_disc = disc[disc['club'] == selected_team]
    filtered_att = att[att['club'] == selected_team]
    filtered_dist = dist[dist['club'] == selected_team]
    filtered_defending = defending[defending['club'] == selected_team]


    child_1 = filtered_goal['goals'].sum()
    child_2 = filtered_attempt['on_target'].sum()
    child_3 = filtered_disc['yellow'].sum()
    child_4 = filtered_disc['red'].sum()

    fig_1 = px.bar(filtered_goal, x='player_name',y=['inside_area','outside_areas'], title='Team Total Goals',
                       template='simple_white',text_auto=True,
                       hover_data=['right_foot', 'left_foot', 'headers', 'others'],
                       labels={'value':'Goals','variable':'Legend'})

    fig_2 = px.bar(filtered_att, x='player_name',y='assists', title='Team Total Assists',
                       template='simple_white',text_auto=True,
                       labels={'variable':'Legend'})

    fig_3 = px.bar(filtered_attempt, x='player_name',y=['on_target','off_target','blocked'], title='Team Total Attempts',
                       template='simple_white',text_auto=True,
                       labels={'value':'Attempts','variable':'Legend'})

    fig_4 = px.bar(filtered_defending, x='player_name',y=['t_won','t_lost'], title='Team Tackles',
                       template='simple_white',text_auto=True,
                       labels={'value':'Tackles','variable':'Legend', 'Accuracy':'Accuracy(%)'})

    fig_5 = px.bar(filtered_dist, x=['pass_accuracy','cross_accuracy'],y='player_name', title='Team Pass and Cross Accuracy(%)',
                       template='simple_white',text_auto=True,
                       labels={'value':'Accuracy(%)','variable':'Legend'}, barmode='group')

    fig_6 = px.bar(filtered_att, x='player_name', y='dribbles', title='Team Dribbles',
                   template='simple_white', text_auto=True,
                   labels={'value': 'Dribbles', 'variable': 'Legend'})

    fig_7 = px.bar(filtered_disc, x='player_name', y=['yellow','red'], title='Team Total Cards',
                   template='simple_white', text_auto=True,
                   labels={'value': 'Cards', 'variable': 'Legend'})

    fig_8 = px.bar(filtered_defending, x='player_name', y='balls_recoverd', title='Team Ball Recovered',
                   template='simple_white', text_auto=True,
                   labels={'value': 'Ball Recovered', 'variable': 'Legend'})

    fig_9 = px.bar(filtered_defending, x='player_name', y='clearance_attempted', title='Team Clearance',
                   template='simple_white', text_auto=True,
                   labels={'value': 'Clearnace', 'variable': 'Legend'})

    return child_1, child_2, child_3, child_4, fig_1, fig_2, fig_3, fig_4, fig_5, fig_6, fig_7, fig_8, fig_9

if __name__ == "__main__":
    app.run_server(debug=True)