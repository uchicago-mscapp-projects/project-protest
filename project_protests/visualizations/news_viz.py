import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
import os
import pathlib
import seaborn as sns
from .protest_viz import protest_data

def nyt_data():
    # change to the create path using parent wd so it's not specific to me 
    filepath = pathlib.Path(__file__).parent.parent.parent / "project_protests/newspaper/nyt/raw_data/nyt_articles.csv"
    df = pd.read_csv(filepath)
    df['date']= pd.to_datetime(df['date'])
    df.rename({'black lives matter':'Black Lives Matter', 
                'police brutality': 'Police Brutality',
                'defund police':'Defund Police',
                'blue lives matter':'Blue Lives Matter',
                'blm' : 'BLM'}, axis='columns', inplace=True)
    df['Month'] = df['date'].dt.month
    df['Year'] = df['date'].dt.year
    df['Newspaper'] = 'NYT'

    return df

def guardian_data():
    filepath = pathlib.Path(__file__).parent.parent.parent / "project_protests/newspaper/the_guardian/data/the_guardian_compiled.csv"
    df = pd.read_csv(filepath)
    df['date']= pd.to_datetime(df['date'])
    df['Month'] = df['date'].dt.month
    df['Year'] = df['date'].dt.year 
    df['Newspaper'] = 'Guardian'

    return df

def news_counts():
    traces = []
    dropdowns = []
    buttons = []

    # add trade for Guardian data 
    g_df = guardian_data()
    g_df_pivot = g_df.groupby(['Year']).size().to_frame().reset_index()
    g_df_pivot.rename(columns={0:'Count'}, inplace=True)
    
    g_trace = (go.Scatter(x=g_df_pivot["Year"], y=g_df_pivot['Count'], name="Guardian", mode="lines"))
    traces.append(g_trace)
    dropdowns.append({'label': 'Guardian', 'value':g_trace})

    # add trace for NYT data 
    n_df = nyt_data()
    n_df_pivot = n_df.groupby(['Year']).size().to_frame().reset_index()
    n_df_pivot.rename(columns={0:'Count'}, inplace=True)
    
    n_trace = (go.Scatter(x=n_df_pivot["Year"], y=n_df_pivot['Count'], name="NYT", mode="lines"))
    traces.append(n_trace)
    dropdowns.append({'label': 'NYT', 'value':n_trace})
    
    # add trace for protest data
    p_df = protest_data()
    p_df_pivot = p_df.groupby(['Year']).size().to_frame().reset_index()
    p_df_pivot.rename({0:'Count'}, axis='columns', inplace=True)
    p_df_pivot['Normalized Counts'] = p_df_pivot['Count']/5

    p_trace = go.Scatter(x=p_df_pivot["Year"], y=p_df_pivot['Normalized Counts'], name="Normalized Protests", mode="lines")
    traces.append(p_trace)
    
    fig = go.Figure(data=traces)
    fig.update_layout(
    title="Number of News Stories and Number of Protests", template="simple_white"
    )

    return fig

def month_corr():
   
   # add trace for newspaper data 
   df = guardian_data()
   nyt = nyt_data()
   df = pd.concat([df, nyt], ignore_index = True)

   #  pivot data by year 
   df_pivot = df.groupby(['Year', 'Month']).size().to_frame().reset_index()
   df_pivot.rename(columns={0:'Count'}, inplace=True)

    # add trace for protest data
   p_df = protest_data()
   p_df_pivot = p_df.groupby(['Year', 'Month']).size().to_frame().reset_index()
   p_df_pivot.rename({0:'Count'}, axis='columns', inplace=True)

   join = pd.merge(p_df_pivot, df_pivot, how ='left', on =['Month', 'Year'])
   join.rename(columns={'Count_x':'Count Protests', 'Count_y':'Count News'}, inplace=True)

   fig = px.imshow(join.corr(), text_auto=True, color_continuous_scale='deep')
   fig.update_layout(title_text='Correlation Matrix', title_x=0.5)
   
   return fig

def tag_counts():
    traces = []
    dropdowns = []
    buttons = []

    tags = ['Black Lives Matter',
                'BLM',
                'Police Brutality',
                'George Floyd',
                'Breonna Taylor',
                'Tyre Nichols',
                'Ahmaud Arbery',
                'Blue Lives Matter']

    # add trace for Guardian data 
    df = guardian_data()
    nyt = nyt_data()
    df = pd.concat([df, nyt], ignore_index = True)

    for i, tag in enumerate(tags):
        sub_df = df.loc[df[tag] == True]
        df_pivot = sub_df.groupby(['Year', tag]).size().to_frame().reset_index()
        df_pivot.rename(columns={0:'Count'}, inplace=True)
        trace = go.Scatter(x=df_pivot["Year"], y=df_pivot['Count'], name=tag, mode="lines")        
        traces.append(trace)
        dropdowns.append({'label': tag, 'value':trace})
    
    # Define the initial layout with the dropdown menu
    buttons =[ ]

    for i in range(len(dropdowns)):
        visible = [False] * len(tags)
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
    fig = go.Figure(data=traces, layout=initial_layout)
    fig.update_layout(
    title="Stories with Tags", title_x=0.5, template="simple_white"
    )

    return fig
