import pandas as pd 
import plotly.express as px 

def protest_data():
    # change to the create path using parent wd so it's not specific to me 
    df = pd.DataFrame(pd.read_csv("/home/lisettesolis/30122-project-project-protest/project_protests/count_data/test_police-data.csv",on_bad_lines='skip'), columns = ['Location', 'Date', 'County', 'StateTerritory', \
        'City_Town'])
    # df = pd.DataFrame(pd.read_csv("/home/lisettesolis/30122-project-project-protest/project_protests/visualizations/test_police-data.csv",on_bad_lines='skip'), columns = ['Location', 'Date', 'County', 'StateTerritory', \
    #     'City_Town'])
    df['Year'] = df['Date'].str.split('/', 2).str[2]

    return df.head()

def city_counts():
    df = protest_data()
    df_pivot = pd.pivot_table(df, index='Year', values='Date',
                          aggfunc='count', margins=True, margins_name='Count')
    return df_pivot