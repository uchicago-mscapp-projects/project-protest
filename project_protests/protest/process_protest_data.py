import os
import pandas as pd
import glob
from itertools import chain
import numpy as np
import pathlib
# Monica Nimmagadda # 

def process_protest_data():
    '''
    This function processes all of the protest data from the Crowd Consortium
    for protests between Jan 2017 and Jan 2023.
    '''
    filename = pathlib.Path(__file__).parent / "data"
    dir = list(filename.iterdir())
    li = []
    for item in dir:
        file = pd.read_csv(item)
        li.append(file)
    
    df = (pd.concat(li, axis=0, ignore_index=True)).fillna('')
    # combine columns and drop old columns
    df = combine_and_drop_cols(df, 'EstimateLow', 'size_low', 'Estimate_Low')
    df = combine_and_drop_cols(df, 'EstimateHigh', 'size_high', 'Estimate_High')
    df = combine_and_drop_cols(df, 'Claim', 'claims', 'Claim Description')

    df['CityTown'] = df['CityTown'].replace('nan', '')
    df['City/Town'] = df['City/Town'].replace('nan', '')
    df['CityTown'].fillna('')
    df['City/Town'].fillna('')
    df = combine_and_drop_cols(df, 'CityTown', 'City/Town', 'City_Town')

    #remove Source columns with different names
    for i in range(1,31):
        if i < 18:
            name_concat_cap = 'Source'+str(i)
            name_concat_lower = 'source'+str(i)
            df = df.drop(name_concat_cap, axis=1)
            df = df.drop(name_concat_lower, axis=1)
        else:
            name_concat_lower = 'source'+str(i)
            df = df.drop(name_concat_lower, axis=1)

    # remove unnamed cols
    unnamed_merge = chain(range(1,6), range(25, 45))
    for it in unnamed_merge:
        name_concat = 'Unnamed:' + " " + str(it)
        df = df.drop(name_concat, axis=1)


    # fill null values with another column value
    df = fill_null_another_col(df, 'City_Town', 'locality')
    df = fill_null_another_col(df, 'Date', 'date')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
    df = fill_null_another_col(df, 'StateTerritory', 'state')


    cols_to_drop = ['Pro(2)/Anti(1)', 'locality', 'ReportedArrests', 'ReportedParticipantInjuries', 'TownsCities', 'ReportedPoliceInjuries', 'ReportedPropertyDamage', 'Misc.','date', 'state', 'valence', 'notes', 'coder', 'Pro2Anti1','TearGas','protest','Crowd Counting Consortium', 'S1', 'S2', 'Pro2-Anti1', 'CountLove', 'AdHoc', 'Misc']
    df = drop_multiple_cols(df, cols_to_drop)

    # filter protests to related to Black Lives Matter and police
    police_terms = ['police', 'black lives', 'racial justice', 'criminal justice', 'racism', 'white supremacy']
    police_df = df[df['Claim Description'].str.contains('|'.join(police_terms))]
    
    # final output
    police_df.to_csv("police-data.csv")
    return None

def combine_and_drop_cols(df, col_1, col_2, new_col):
    '''
    This function combines columns of differently named columns between the sheets
    that have the same value. It also drops the old columns.
    Input: dataframe, col_1 and col_2 to combine, new_col to create
    Output: dataframe (changed in place)
    '''
    df[new_col] = df[col_1].astype(str) + df[col_2].astype(str)
    if col_1 == 'EstimateHigh' or col_1 == 'EstimateLow':
        pd.to_numeric(df[new_col], errors='coerce')
    df = df.drop(col_2, axis=1)
    df = df.drop(col_1, axis=1)
    return df

def drop_multiple_cols(df, cols_to_drop):
    '''
    This function drops columns that are in the passed in list.
    Input: dataframe, cols_to_drop (list)
    Output: dataframe (changed in place)
    '''
    final_columns = []
    for col in df.columns:
        if col not in cols_to_drop:
            final_columns.append(col)
    df.drop(columns=df.columns.difference(final_columns), inplace=True)
    return df

def fill_null_another_col(df, col, fill_col):
    '''
    This function fills null values of one col, with values of the given col
    Input: dataframe, col, fill_col
    Output: dataframe (changed in place)
    '''
    df[col] = df[col].replace(r'^\s*$', np.nan, regex=True)
    df[col] = df[col].fillna(df[fill_col])
    return df

