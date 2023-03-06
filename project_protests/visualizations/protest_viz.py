import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
import pathlib

def protest_data():
    """
    """
    # change to the create path using parent wd so it's not specific to me 
    filepath = pathlib.Path(__file__).parent.parent.parent / "project_protests/protest/police-data.csv"
    df = pd.DataFrame(pd.read_csv(filepath),\
        columns = ['Location', 'Date', 'County', 'StateTerritory','City_Town'])
    df['Date']= pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year 
    
    return df


def filtereable_cities():
    df = protest_data()
    # Agregate data at the national level 
    df_national = df.groupby(['Year']).size().to_frame().reset_index()
    df_national.rename(columns={0:'Count'}, inplace=True)

    # pivot data for cities
    cities = ['Baltimore', 'New York', 'Chicago', 'Detroit', 'Atlanta', 'Los Angeles', 'Minneapolis', 'Houston']
    cities.sort()
    df_cities = df.loc[df['City_Town'].isin(cities)]
    df_pivot = df_cities.groupby(['Year', 'City_Town']).size().to_frame().reset_index()
    df_pivot.rename(columns={0:'Count'}, inplace=True)
    
    # create traces for figure 
    trace = []
    dropdowns = []
    buttons = []

    # Add trace for national data
    t = (go.Scatter(x=df_national["Year"], y=df_national['Count'], name='National', mode="lines"))
    trace.append(t)
    dropdowns.append({'label': 'National', 'value':t})
    # Add trace for each city
    for i, city in enumerate(cities):
        sub_df = df_pivot.loc[df_pivot['City_Town'] == city]
        t = go.Scatter(x=sub_df["Year"], y=sub_df['Count'], name=city, mode="lines")        
        trace.append(t)
        dropdowns.append({'label': city, 'value':t})

    # Define the initial layout with the dropdown menu    
    for i, dropdown in enumerate(dropdowns):
        visible = [False] * len(dropdowns)
        visible[i] = True
        buttons.append({'args': [{'visible': visible}],
                        'label': dropdowns[i]['label'], \
                        'method': 'restyle'
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
        yaxis=dict(title='Count'),
        title="Protests by Year", title_x=0.5,
        template="simple_white", 
            )

    #Create the figure with the traces and initial layout
    fig = go.Figure(data=trace, layout=initial_layout)

    return fig
