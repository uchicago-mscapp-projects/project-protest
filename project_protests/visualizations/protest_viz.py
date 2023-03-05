import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
import dash 
import os

def protest_data():
    """
    """
    # change to the create path using parent wd so it's not specific to me 
    df = pd.DataFrame(pd.read_csv("/home/lisettesolis/30122-project-project-protest/project_protests/count_data/police-data.csv",on_bad_lines='skip'),\
        columns = ['Location', 'Date', 'County', 'StateTerritory','City_Town'])
    df['Date']= pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year 
    
    return df


def count_all():
    """
    """
    df = protest_data()
    df_pivot = df.groupby(['Year']).size().to_frame().reset_index()
    df_pivot.rename({0:'Count'}, axis='columns', inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_pivot["Year"], y=df_pivot['Count'], name="All", mode="lines"))
    fig.update_layout(
        title="Number of Protests", template="simple_white"
    )
    
    return fig.show()


def go_cities():
    """"
    """
    df = protest_data()
    dfg = df.groupby(['Year', 'City_Town']).size().to_frame().sort_values([0], ascending = False).head(10).reset_index()
    cities = list(dfg['City_Town'].unique())
    df['Count'] = 1
    df = df.loc[df['City_Town'].isin(cities)]
    
    # pivot data by year 
    df_pivot = df.groupby(['Year', 'City_Town']).count().reset_index()
    
    # create traces for figure 
    trace = []
    dropdowns = []
    buttons = []
    
    for i, city in enumerate(cities):
        sub_df = df_pivot.loc[df_pivot['City_Town'] == city]
        t = go.Scatter(x=sub_df["Year"], y=sub_df['Count'], name=city, mode="lines")        
        trace.append(t)
        dropdowns.append({'label': city, 'value':t})

    # Define the initial layout with the dropdown menu
    buttons =[ ]
    
    for i in range(len(dropdowns)):
        visible = [False] * len(cities)
        visible[i] = True
        buttons.append({'args': [{'visible': visible}],
                        'label': dropdowns[i]['label'], \
                        'method': 'update'
                        })

    initial_layout = go.Layout(
        updatemenus=[{'buttons': buttons,
            'direction': 'down',
            'showactive': True,
            'x': 0.1,
            'y': 1.2
                }
            ],
        xaxis=dict(title='Year'),
        yaxis=dict(title='Count')
            )

    #Create the figure with the traces and initial layout
    fig = go.Figure(data=trace, layout=initial_layout)
    fig.update_layout(
    title="Cities with the most Protests", template="simple_white"
    )

    return fig.show()
