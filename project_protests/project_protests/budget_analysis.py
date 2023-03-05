import pandas as pandas
import re 
import pathlib
import pandas as pd

# Monica Nimmagadda #

def load_budget_data():
    budget_filepath = pathlib.Path(__file__).parent / "police_budget_by_city.csv"
    budget_df = pd.read_csv(budget_filepath)
    cols = budget_df.columns
    for col in cols[2:-1]:
        budget_df[col] = budget_df[col].astype(float)
    budget_df = project_population(budget_df)
    visualization
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

