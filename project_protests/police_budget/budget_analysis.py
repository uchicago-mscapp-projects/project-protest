import pandas as pandas
import re 
import pathlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Monica Nimmagadda #

def load_budget_data():
    budget_filepath = pathlib.Path(__file__).parent / "police_budget_by_city.csv"
    budget_df = pd.DataFrame(pd.read_csv(budget_filepath), 
        columns= ['City','Type','FY16', 'FY17', 'FY18', 'FY19', 'FY20', 'FY21', 'FY22', 'FY23'])
    budget_df.dropna(axis=0, how='all', inplace=True)
    cols = budget_df.columns
    for col in cols[2:-1]:
        budget_df[col] = budget_df[col].astype(float)
    budget_df = project_population(budget_df) 
    budget_df = normalize_population(budget_df)

    return budget_df

def project_population(df):
    for row in df.itertuples():
        if row.Type == 'Population':
            fy_21 = row.FY21
            fy_20 = row.FY20
            percent_change = (fy_21 - fy_20) / fy_20
            fy_22 = fy_21 + (fy_21 * percent_change)
            df.loc[row.Index, 'FY22'] = fy_22
            fy_23 = fy_22 + (fy_22 * percent_change)
            df.loc[row.Index, 'FY23'] = fy_23

    return df 
        
def normalize_population(df):
    cities = list(df['City'].unique())   
    for city in cities:
            # fill in missing budget values using the projected population totals 
            budget_22 = df.loc[(df['City'] == city) & (df['Type'] == 'Total')]['FY22']
            pop_22 = df.loc[(df['City'] == city) & (df['Type'] == 'Population')]['FY22']
            norm_22 = int(budget_22)/int(pop_22)
            df.loc[(df['City'] == city) & (df['Type'] == 'Normalized'), 'FY22'] = norm_22

            budget_23 = df.loc[(df['City'] == city) & (df['Type'] == 'Total')]['FY23']
            pop_23 = df.loc[(df['City'] == city) & (df['Type'] == 'Population')]['FY23']
            norm_23 = int(budget_23)/int(pop_23)
            df.loc[(df['City'] == city) & (df['Type'] == 'Normalized'), 'FY23'] = norm_23
    
    return df

def visualize_budget(df):
    df_population = df.loc[df['Type'] == 'Population']
    df_budget = df.loc[df['Type'] == 'Total']
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter( 
            x=df_budget['City'],
            y=df_budget[df_budget.columns[2:9]], 
            name="Budget"
        ), secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df_population['City'],
            y=df_population[df_population.columns[2:9]], 
            name="Population"
        ), secondary_y=True,
    )
    fig.update_yaxes(title_text="Budget ($)", secondary_y=False)
    fig.update_yaxes(title_text="Population (#)", secondary_y=True)
    fig.show()


