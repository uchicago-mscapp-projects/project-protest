import time
import requests
import json


def create_url(tags, begin_date, end_date, page):
    """
    Create request url for API based on query search parameters passed to the
        function.
    
    Inputs:
        tags (lst): list of tags to look for. The tags to filter for are looked
            in the body, headline and byline of the articles.
        begin_date (str): 8 digits (YYYYMMDD) string that specify the begin date
            or from when to start looking for articles.
        end_date (str): 8 digits (YYYYMMDD) string that specify the end date or
            until when to stop looking for articles.
        page (str): number of page string that states where to look for articles.

    Return (str): URL string with query to send request to NYT Article Search 
        API
    """

    endpoint = "https://api.nytimes.com/svc/search/v2/articlesearch.json?" 

    ## Create the fq query parameter

    # IDK IF IT'S NECCESARY TO DO A DEEP COPY FOR THIS LIST OR NOT
    tags_copy = tags[:]
    
    # We add "'" to the beggining and end of each tag on the list cause we need
    # them in apostrophes to be able to do the query search
    for i,tag in enumerate(tags_copy):
        tags_copy[i] = "\"" + tag + "\""

    fq = "fq=(" + " OR ".join(tags_copy) + ")"

    api_key = "4AA7GDZ7giaN7m3rh8ULH5A60EWNlJHB"

    url = endpoint + fq + "&begin_date=" + begin_date + "&end_date=" + end_date +\
            "&page=" + page + "&api-key=" + api_key

    return url


def make_request(tags, begin_date, end_date, page = "0"):
    """
    Make a GET request to the NYT Article Search API with a request delay of 6
        seconds to avoid reaching request limit of 60 requests per minute.

    Inputs:
        tags (lst): list of tags to look for. The tags to filter for are looked
            in the body, headline and byline of the articles.
        begin_date (str): 8 digits (YYYYMMDD) string that specify the begin date
            or from when to start looking for articles.
        end_date (str): 8 digits (YYYYMMDD) string that specify the end date or
            until when to stop looking for articles.
        page (str): number of page string that states where to look for articles.
    
    Return (Response): API request response with specified query parameters
    """

    url = create_url(tags, begin_date, end_date, page)
    
    time.sleep(6)
    
    resp = requests.get(url)

    return resp

def get_json(tags, begin_date = "20180101", end_date = "20230201"):
    """
    Create json files from articles that meet query search parameters

    Inputs:
        tags (lst): list of tags to look for. The tags to filter for are looked
            in the body, headline and byline of the articles.
        begin_date (str): 8 digits (YYYYMMDD) string that specify the begin date
            or from when to start looking for articles.
        end_date (str): 8 digits (YYYYMMDD) string that specify the end date or
            until when to stop looking for articles.
    """

    resp = make_request(tags, begin_date, end_date)
    
    # Convert response to json format
    resp_json = json.loads(resp.text)

    # Save first json
    with open("nyt_0.json", "w") as f:
        json.dump(resp_json, f, indent=1)
        f.close()

    # Get number of articles that match our query search parameters
    hits = resp_json["response"]["meta"]["hits"]

    # Get maximum number of pages we can query
    max_pages = int(hits / 10)

    # Query everything and save the jsons
    for page_n in range(1, max_pages + 1):
        page_str = str(page_n)
        resp = make_request(tags, begin_date, end_date, page_str)
        resp_json = json.loads(resp.text)
        file_name = "nyt_" + page_str + ".json"
        
        with open(file_name, "w") as f:
            json.dump(resp_json, f, indent=1)
            f.close()

