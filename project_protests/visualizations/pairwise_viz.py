# Task: Visualization for word similarity
# Author: Monica Nimmagadda
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import pathlib
from sentiment_analysis.pairwise_correlation import word_similarity

def visualize_similarity():
    '''
    This function takes in the similarity words list and creates bar charts
    by year for each set of words and score. 
    The resulting plot is a 2x3 chart of each year 2017-2022 and their corresponding
    top words related to "police" as seen in NYT and the Guardian data.
    '''
    police_df = word_similarity("police")
    df = pd.DataFrame(police_df, columns=["word", "score", "year"])
    fig = make_subplots(rows=2,cols=3, subplot_titles=['2017', '2018', '2019', '2020', '2021', '2022'])
    for idx, year in enumerate(df['year'].unique()):
        chart = px.scatter(df[df['year']==year], x="word", y="score")
        chart.update_layout(title=str(year))
        if idx < 3:
            fig.append_trace(chart.data[0], row=1, col=idx+1)
        else:
            fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
   
    return fig