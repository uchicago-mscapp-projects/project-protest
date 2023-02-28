import pandas as pd
import json
import os

# def import_json(filename):
#     """
#     Import json file from path

#     Inputs:
#         filename (str): file path
    
#     Return (dict): json object
#     """
    
#     file = open(filename)
#     data = json.load(file)

#     return data

def create_csv():
    """
    Create csv file with news articles related to BLM protests

    """
    d = {"id": [], "date": [], "url": [], "headline": [], "abstract": [], "lead_paragraph": [], "type_of_material": []}
    # d = {"id": [], "date": [], "url": [], "headline": [], "abstract": [], "lead_paragraph": []}


    # CHANGE PATH later to make dynamic path depending of parent
    parent_dir = os.path.join(os.getcwd(), "raw_data")
    year_lst = os.listdir(parent_dir)
    
    ## CHECK IF THERE'S A WAY TO LIST ALL FILES INSIDE PARENT SUBDIRECTORIES
    # THOUGHT THAT WITH SOMETHING LIKE os.walk(root) BUT I WOULD STILL HAVE TO
    # ITERATE OVER THE SUBDIRECTORIES AND FILES OF THAT

    # MAYBE WE SHOULD CREATE ALL THE JSON FILES IN ONE DIRECTORY WITH NAMES LIKE
    # "[YEAR]_[MONTH]_[JSON ID].json"

    for year in year_lst:
        year_dir = os.path.join(parent_dir, year)
        month_lst = os.listdir(year_dir)
        
        for month in month_lst:
            month_dir = os.path.join(year_dir, month)
            file_lst = os.listdir(month_dir)

            for file_name in file_lst:
                file_path = os.path.join(month_dir, file_name)
                f = open(file_path)
                data = json.load(f)
                update_dict(d, data)

    #return d

    df = pd.DataFrame(data=d)
    df.to_csv("raw_data/nyt_articles.csv", index=False)


def update_dict(d, json):
    """
    Update a dictionary with the columns and observations for our csv file
    
    Inputs:
        d (dict):  dictionary just with keys and no values
        json (dict): json with news articles

    Return (dict): dictionary with added values for each key
    """
    
    #print(json)

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

    


