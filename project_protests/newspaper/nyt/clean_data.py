import pandas as pd
import json
import os
# from ...collecting_news import create_dirs
# from ...query_params import query_lst, from_date, to_date, filters_lst

query_lst = ["blm", "black lives matter", "police brutality", "defund police",
                "blue lives matter", "George Floyd", "Breonna Taylor",
                "Tyre Nichols", "Eric Garner", "Ahmaud Arbery", "Tamir Rice"]
tags_list = None
from_date = "2017-01-01"
to_date = "2023-01-31"
page_size = 50
page = 1
filters_lst = ["headline", "lead_paragraph"]


def create_csv(tags = query_lst, filters = filters_lst):
    """
    Create csv file with news articles related to BLM protests

    Inputs:
        tags (lst): list of tags to look for. The tags to filter for are looked
            in the body, headline and byline of the articles.
        filters (lst): list of filters where to look tags. They can be "headline",
            "lead_paragraph" and/or "body"
        begin_date (str): 8 digits (YYYYMMDD) string that specify the begin date
            or from when to start looking for articles.
        end_date (str): 8 digits (YYYYMMDD) string that specify the end date or
            until when to stop looking for articles.
    """
    ### ADD CREATE DIRS FUNCTION SO THIS FUNCTION DETONATES ALL THE PROCESS
    #create_dirs(tags, filters, begin_date, end_date)
    
    d = {"id": [], "date": [], "url": [], "headline": [], "abstract": [],
        "lead_paragraph": [], "type_of_material": [], "section_name": []}

    current_dir = os.path.dirname(os.path.realpath(__file__))
    new_dir = os.path.join(current_dir, "raw_data")
    year_lst = os.listdir(new_dir)
    
    # Add conditional in case there already existed a csv file and we're replacing
    # without having to eliminate all the jsons and previous csv file before
    # with the create_dirs function of the collecting_news module

    if 'nyt_articles.csv' in year_lst:
        year_lst.remove("nyt_articles.csv")
    
    ## CHECK IF THERE'S A WAY TO LIST ALL FILES INSIDE PARENT SUBDIRECTORIES
    # THOUGHT THAT WITH SOMETHING LIKE os.walk(root) BUT I WOULD STILL HAVE TO
    # ITERATE OVER THE SUBDIRECTORIES AND FILES OF THAT

    # MAYBE WE SHOULD CREATE ALL THE JSON FILES IN ONE DIRECTORY WITH NAMES LIKE
    # "[YEAR]_[MONTH]_[JSON ID].json"

    for year in year_lst:
        year_dir = os.path.join(new_dir, year)
        month_lst = os.listdir(year_dir)
        
        for month in month_lst:
            month_dir = os.path.join(year_dir, month)
            file_lst = os.listdir(month_dir)

            for file_name in file_lst:
                file_path = os.path.join(month_dir, file_name)
                f = open(file_path)
                data = json.load(f)
                update_dict(d, data)

    ## CHECK IF I RETURN JUST THE DATAFRAME OBJECT
    ## CHECK IF SPLITTING THIS IN ANOTHER CREATE_DATAFGRAME FUNCTION

    df = create_df(d, tags, filters)
     
    df.to_csv(os.path.join(new_dir, "nyt_articles.csv"), index=False)

def create_df(d, tags, filters):
    """
    Create dataframe based on articles' dictionary

    Inputs:
        d (dict):  dictionary with keys and values to create dataframe
        tags (lst): list of tags to look for. The tags to filter for are looked
            in the body, headline and byline of the articles.
        filters (lst): list of filters where to look tags. They can be "headline",
            "lead_paragraph" and/or "body"

    Return (DataFrame): dataframe with NYT articles data
    """
    df = pd.DataFrame(data=d)

    df = df.astype('string')
    df["date"] = df["date"].astype('datetime64')

    for tag in tags:
        df[tag] = False
        for fil in filters:
            for index, row in df.iterrows():
                #print(index, fil)
                if pd.isna(row[fil]):
                    continue
                if tag.lower() in row[fil].lower():
                    df[tag][index] = True

    return df

def update_dict(d, json):
    """
    Update a dictionary with the columns and observations for our csv file
    
    Inputs:
        d (dict):  dictionary just with keys and no values
        json (dict): json with news articles

    Return (dict): dictionary with added values for each key
    """

    for article in json["response"]["docs"]:
        d["id"].append(article["_id"][14:])
        d["date"].append(article["pub_date"][0:10]) # get only the date without time
        d["url"].append(article["web_url"])
        d["headline"].append(article["headline"]["main"])
        d["abstract"].append(article["abstract"])
        d["lead_paragraph"].append(article["lead_paragraph"])
        # Add get method to set to default value in case "type_of_material" is
        # not a key in the json dictionary
        d["type_of_material"].append(article.get("type_of_material", "NaN"))
        d["section_name"].append(article.get("section_name", "NaN"))