import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import pathlib
import seaborn as sns
from .protest_viz import protest_data
from project_protests.police_budget.budget_analysis import load_budget_data

def budget_viz():
    """"
    """
    df = load_budget_data()
    df.drop(df.index[(df["Type"] == "Total") | (df["Type"] == "Population")], inplace=True)
    df.drop(columns=["Type"], inplace=True)
    # df =  df.loc[(df['City'] == 'Atlanta')]
    df = df.melt(id_vars="City", value_name="Total")

    # create traces for figure 
    traces = []
    dropdowns = [] 
    buttons = []

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # add traces for cities
    cities = list(df["City"].unique())
    for city in cities:
        sub_df = df.loc[df['City'] == city]
        fig.add_trace(
            go.Bar( 
                x=sub_df['variable'],
                y=sub_df['Total'], 
                name=city
            ), secondary_y=False,
        )


    fig.update_yaxes(title_text="Per Capita Budget ($)", secondary_y=False)
    # fig.update_yaxes(title_text="Protests (#)", secondary_y=True)
    fig.update_layout(template="simple_white", 
        title="Per Capita Police Budget", title_x=0.5)

    return fig