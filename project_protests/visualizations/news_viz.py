"""
Lisette Solis
"""
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pathlib
from project_protests.visualizations.protest_viz import protest_data

def news_counts():
    """
    Visualize the number of news stories with the number of protests 

    Return: Plotly figure
    """
    traces = []
    dropdowns = []
    buttons = []

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # add trade for Guardian data 
    g_df_pivot = pivot_guardian(guardian_data( ))
    fig.add_trace(go.Scatter(x=g_df_pivot["Year"], y=g_df_pivot['Count'], name="Guardian", mode="lines"), secondary_y=False)
    # add trace for NYT data 
    n_df_pivot = pivot_nyt(nyt_data())
    fig.add_trace(go.Scatter(x=n_df_pivot["Year"], y=n_df_pivot['Count'], name="NYT", mode="lines"), secondary_y=False)
    # add trace for protest data
    p_df = protest_data()
    p_df_pivot = p_df.groupby(['Year']).size().to_frame().reset_index()
    p_df_pivot.rename({0:'Count'}, axis='columns', inplace=True)
    fig.add_trace(go.Scatter(x=p_df_pivot["Year"], y=p_df_pivot['Count'], name="Normalized Protests", mode="lines"), secondary_y=True)

    fig.update_yaxes(title_text="News Stories (#)", secondary_y=False)
    fig.update_yaxes(title_text="Protests (#)", secondary_y=True)
    fig.update_layout(template="simple_white", 
        title="Number of News Stories and Number of Protests", title_x=0.5)
    
    colors = ['#98A4D7', '#7BAE82', '#1e4477']
    for i,_ in enumerate(fig.data):
        fig.data[i].marker.color = colors[i]
    return fig


def month_corr():
   """
   Correlation matrix between count of stories and protests 

   Return: Plotly figure
   """
   # add trace for newspaper data 
   df = guardian_data()
   nyt = nyt_data()
   df = pd.concat([df, nyt], ignore_index = True)

   #  pivot data by year 
   df_pivot = df.groupby(['Year', 'Month']).size().to_frame().reset_index()
   df_pivot.rename(columns={0:'Count'}, inplace=True)
   # pivot data for protests 
   p_df = protest_data()
   p_df_pivot = p_df.groupby(['Year', 'Month']).size().to_frame().reset_index()
   p_df_pivot.rename({0:'Count'}, axis='columns', inplace=True)

   join = pd.merge(p_df_pivot, df_pivot, how ='left', on =['Month', 'Year'])
   join.rename(columns={'Count_x':'Count Protests', 'Count_y':'Count News'}, inplace=True)

   fig = px.imshow(join.corr(), text_auto=True, color_continuous_scale='deep')
   fig.update_layout(title_text='Correlation Matrix', title_x=0.5) 
   return fig

def pivot_nyt(df): 
    """
    Helper function to pibvot the NY Times data 
 
    Return: Plotly figure
    """
    n_df_pivot = df.groupby(['Year']).size().to_frame().reset_index()
    n_df_pivot.rename(columns={0:'Count'}, inplace=True)
    return n_df_pivot

def nyt_data():
    """
    Create dataframe from CSV of NY Times data

    Return: Plotly figure
    """
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

def pivot_guardian(df):
    """
    Helper function to pivot the guardian data

    Return: Pandas DataFrame
    """
    g_df_pivot = df.groupby(['Year']).size().to_frame().reset_index()
    g_df_pivot.rename(columns={0:'Count'}, inplace=True)
    return g_df_pivot

def guardian_data():
    """
    Create dataframe from CSV of Guardian data

    Return: Plotly figure
    """
    filepath = pathlib.Path(__file__).parent.parent.parent / "project_protests/newspaper/the_guardian/data/the_guardian_compiled.csv"
    df = pd.read_csv(filepath)
    df['date']= pd.to_datetime(df['date'])
    df['Month'] = df['date'].dt.month
    df['Year'] = df['date'].dt.year 
    df['Newspaper'] = 'Guardian'
    return df

def tag_counts():
    """
    Visualization of the number of stories that can be filtered by tag
    Note: not in final HTML dashboard 

    Retunr: Plotly figure
    """
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
    df = guardian_data()
    nyt = nyt_data()
    df = pd.concat([df, nyt], ignore_index = True)
    # traces for each tag
    for i, tag in enumerate(tags):
        sub_df = df.loc[df[tag] == True]
        df_pivot = sub_df.groupby(['Year', tag]).size().to_frame().reset_index()
        df_pivot.rename(columns={0:'Count'}, inplace=True)
        trace = go.Scatter(x=df_pivot["Year"], y=df_pivot['Count'], name=tag, mode="lines")        
        traces.append(trace)
        dropdowns.append({'label': tag, 'value':trace})
    # add dropdown options
    for i in range(len(dropdowns)):
        visible = [False] * len(tags)
        visible[i] = True
        buttons.append({'args': [{'visible': visible}],
                        'label': dropdowns[i]['label'], \
                        'method': 'update'
                        })
    # define layout
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
    fig = go.Figure(data=traces, layout=initial_layout)
    fig.update_layout(
    title="Stories with Tags", 
    title_x=0.5, 
    template="simple_white"
    )
    return fig
