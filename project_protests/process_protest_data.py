import os
import pandas as pd
import glob
from itertools import chain

def load_data():
    folder_dir = "/home/monican/capp30122/30122-project-project-protest/project_protests/count_data"
    csv_files = glob.glob(os.path.join(folder_dir, "*.csv"))
    li = []
    for filename in csv_files:
        df = pd.read_csv(filename)
        li.append(df)
    df = (pd.concat(li, axis=0, ignore_index=True)).fillna('')
    # combine EstimateLow and size_low cols into new col Estimate_Low. 
    # Drop old cols EstimateLow and size_low cols
    df['Estimate_Low'] = df['EstimateLow'].astype(str) + df['size_low'].astype(str)
    pd.to_numeric(df['Estimate_Low'], errors='coerce')
    df = df.drop('size_low', axis=1)
    df = df.drop('EstimateLow', axis=1)

    # combine EstimateHigh and size_high cols into new col Estimate_High. 
    # Drop old cols EstimateLow and size_low cols
    df['Estimate_High'] = df['EstimateHigh'].astype(str) + df['size_high'].astype(str)
    pd.to_numeric(df['Estimate_High'], errors='coerce')
    df = df.drop('EstimateHigh', axis=1)
    df = df.drop('size_high', axis=1)

    #remove Source columns
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

    # merge claim columns
    df['Claim Description'] = df['Claim'].astype(str) + df['claims'].astype(str)
    df = df.drop('Claim', axis=1)
    df = df.drop('claims', axis=1)

    # merging city cols
    df['CityTown'] = df['CityTown'].replace('nan', '')
    df['City/Town'] = df['City/Town'].replace('nan', '')
    df['CityTown'].fillna('')
    df['City/Town'].fillna('')
    df['City_Town'] = df['CityTown'].astype(str) + df['City/Town'].astype(str)
    df = df.drop('CityTown', axis=1)
    df = df.drop('City/Town', axis=1)
    for col in df.columns:
        print(col)
    
    return df
