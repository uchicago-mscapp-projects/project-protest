##Author: JP Martinez
##Task: Clean The Guardian json files
##Last update: 03.1.23

import json
import pandas as pd
import os 
from bs4 import BeautifulSoup
import re
#from .make_request import base_query_list
#from .. import sentiment_analysis

base_query_list = ["Black Lives Matter", "BLM", "Police Brutality", \
"George Floyd", "Breonna Taylor", "Tyrel Nichols", "Ahmaud Abery", "Blue Lives Matter"]

def open_clean_data(json_file,query_list = base_query_list):
    """
    Open json_files created in py file "make_requests" and clean them
    Input 
    """
    ##Open Json-files into dictionary
    df = pd.read_json(json_file)
    df = df.from_dict(df.loc["results", "response"])
    
    ##Structure df and clean_data

    df.rename(columns = {"webPublicationDate":"date","webUrl": "url", "sectionId":"section",
    "pillarName":"category", "webTitle" : "headline"}, inplace = True)
    
    df["id"] = df["id"].apply(lambda x: x.split("/")[-1])
    df["body"] = df["fields"].apply(lambda x: dict(x)["body"])
    df["standfirst"] = df["fields"].apply(lambda x: dict(x)["standfirst"])

    ###Retrieve first paragraph and remove tags and hrefs
    df["lead_paragraph"] = df["body"].apply(lambda x: BeautifulSoup(x,"html.parser").p)
    df = retrieve_text_html(df,["lead_paragraph","standfirst"])

    df["date"] = df["date"].astype(str)
    df["date"] = df["date"].str.extract(r"(\d{4}-\d{2}-\d{2})")
    df["date"] = pd.to_datetime(df["date"],format= "%Y/%m/%d")
    
    ##Add dummy variables to identify which tags match
    for query_term in query_list:
        df[query_term] = df["headline"].apply(lambda x: query_term in x)

    #Drop unnecesary columns
    df = df.drop(columns = ["sectionName","isHosted", "pillarId","body","fields","apiUrl"])

    df = standarized_clean(df,["section", "headline","lead_paragraph"])

    return df

def standarized_clean(df,varlist):
    """
    Do standarized cleaning for a dataframe in which for each variable in
    var_list it removes leading and trailing whitespace and lower case
    
    Input:
    -df (Dataframe): Dataframed to which the cleaning is going to be applied
    -varlist: List of columns to be cleaned

    Return:
        Dataframed with cleaned specified columns 
    """
    for var in varlist:
        df[var] = df[var].astype(str)
        df[var] = df[var].str.lower()
        df[var] = df[var].str.strip()

    return df

def retrieve_text_html(df, varlist):
    """
    Retrieves the text from an html text by removing tags and hrefs
    Inputs:
    -df (Dataframe): Dataframed to which the cleaning is going to be applied
    -varlist: List of columns to be cleaned
    Return:
        Dataframed with cleaned specified columns 
    """
    for var in varlist:
        df[var] = df[var].astype(str)
        df[var] = df[var].apply(lambda x: re.sub(r"</?\w>?","",x))
        df[var] = df[var].apply(lambda x: re.sub(r"href=\S*?>","",x))

    return df

def create_news_df():
    """
    Create dataframe with all the news information obtained 
    from the The Guardian API  
    Inputs:
    - none, it uses the json_files obtained from 
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    json_directory = os.path.join(current_dir, "json_files")
    df = open_clean_data("{}/the_guardian_1.json".format(json_directory))

    number_of_files = len(os.listdir(json_directory))

    for i in range(2, number_of_files + 1):
        df = pd.concat([df,open_clean_data("{}/the_guardian_{}.json".format(json_directory,i))]
        ,ignore_index = True)

    df.to_csv(os.path.join(current_dir, "data/the_guardian_compiled.csv"), index = False)