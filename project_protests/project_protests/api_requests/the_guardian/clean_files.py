import json
import pandas as pd
import os 
import re
#from .. import sentiment_analysis

##Author: JP Martinez
##Task: Clean The Guardian json files
##Last update: 02.26.23

def open_clean_data(json_file):
    """
    Open json_files created in py file "make_requests" and clean them
    Input 
    """
    #Open Json-files into dictionary
    df = pd.read_json(json_file)
    df = df.from_dict(df.loc["results", "response"])
    
    #Structure df and clean_data

    df.rename(columns = {"webPublicationDate":"date","webUrl": "url", "sectionId":"section",
    "pillarName":"category", "webTitle" : "headline"}, inplace = True)
    df = df.drop(columns = ["sectionName","isHosted", "pillarId"])

    df["lead"] = df["fields"].apply(pd.Series) ##Change to trailText

    df["date"] = df["date"].astype(str)
    df["date"] = df["date"].str.extract(r"(\d{4}-\d{2}-\d{2})")
    df["date"] = pd.to_datetime(df["date"],format= "%Y/%m/%d")

    df = standarized_clean(df,["section", "headline"])

    return df

def standarized_clean(df,varlist):
    """
    Do standarized cleaning for a dataframe in which for each variable in
    var_list it removes leading and trailing whitespace and lower case
    
    Input:
    df (Dataframe): Dataframed to which the cleaning is going to be applied
    varlist: List of columns to be cleaned

    Return:
        Dataframed with cleaned specified columns 
    """
    for var in varlist:
        df[var] = df[var].astype(str)
        df[var] = df[var].str.lower()
        df[var] = df[var].str.strip()

    return df

def create_news_df():
    """
    Create dataframe with all the news information obtained 
    from the The Guardian API  
    Inputs:
    - none, it uses the json_files obtained from 
    """
    json_directory = "json_files"
    df = open_clean_data("{}/the_guardian_1.json".format(json_directory))

    number_of_files = len(os.listdir(json_directory))

    for i in range(2, number_of_files + 1):
        df = pd.concat([df,open_clean_data("{}/the_guardian_{}.json".format(json_directory,i))]
        ,ignore_index = True)

    df.to_csv("data/the_guardian_compiled", index = False)