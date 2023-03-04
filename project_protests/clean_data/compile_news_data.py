import json
import pandas as pd
from .collecting_news import create_json ##Check with chema
from .clean_data import create_csv
from ../project_protests/api_requests/the_guardian/make_requests import get_json_files #Check correct syntax
from ../project_protests/api_requests/the_guardian/clean_files import create_news_df

def compile_news_data(api_keys, collect_data = False):
    """
    Obtain the data from both NYT and The Guardian and compile it into one csv
    Inputs:
    api_keys (tuple): Tuple where the first item is the NYT api key and
    the second item is The Guardian api key 
    collect_data (bool): If True collect_json files, if False skip and move on to 
    compilling csv files
    Return:
    None - saves a csv that compiles the information of both newspapers
    """

    #Create json files:
    if collect_data:
        nyt_api_key, the_guardian_api_key = api_keys
        create_json(nyt_api_key) ##Give default parameters to all functions in collecting news
        get_json_files(the_guardian_api_key)

    #Save json files as csv's
    create_csv()
    create_news_df()

    #Compile csv's and save data
    nyt_df = pd.read_csv("nyt.csv") ##Add correct path for data
    the_guardian_df = pd.read_csv("the_guardian.csv")

    the_guardian_df["newspaper"] = "The Guardian"
    nyt_df["newspaper"] = "New York Times"
    nyt_df.rename(columns = {"type_of_material":"type"}, inplace = True)

    news_df = pd.concat([nyt_df,the_guardian_df])

    news_df.to_csv("news_clean_data/news_compiled.csv", index = False)




