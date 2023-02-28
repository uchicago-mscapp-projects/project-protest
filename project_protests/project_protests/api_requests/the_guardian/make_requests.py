import sys
import json
import lxml.html
import requests
#from urllib.parse import urllibparse
import urllib.parse

##Author: JP Martinez
##Task: Create querys and do requests for The Guardian API - Save JSON Files
##Last date updated: 02.27.23

def create_query_statement(key,list_parameters, inclusive = True):
    """
    Creates a query statement to add to the request
    Input:
    key (str):
    query_list (list): List of parameters to add to the query
    inclusive (Bool): True if the query parameter should include any of the terms in
    query list. If false, article must have all parameters in query_search
    """
    query_terms_encoded_list = []
    
    for query_term in list_parameters:
        encoded_query = "'" + urllib.parse.quote(query_term) + "'"
        query_terms_encoded_list.append(encoded_query)

    query = key + "=(" + " OR ".join(query_terms_encoded_list) + ")"

    return query

base_query_list = ["Black Lives Matter", "BLM", "Police Brutality", \
"George Floyd", "Breonna Taylor", "Tyrel Nichols", "Ahmaud Abery"]  


def request_the_guardian(api_key, search = True, query_list = base_query_list, tags_list = None,
 from_date = "2017-01-01", to_date = "2023-01-31",page_size = 50, pages = 1):
    """
    Makes a requests for The Guardian API and returns a JSON file
    Inputs:
    -api_key (str): Api key to be used for the request
    -search (Bool): If True, use search
    -query_list (list): List of items to search in content
    -tags_list(list): Tags to look for in content
    -from_date(str): Starting date for news retrieve 
    -to_date(str): End date for news retrieve
    - pages (int): The page to retrieve in the results 
    Return:
     Object with response

    For additional info on documentation, visit: https://open-platform.theguardian.com/documentation/
    """
    #Base for the request
    main_page = "https://content.guardianapis.com/"

    #Add parameters to the query
    parameters_list = []
    api_key_param = "api-key=" + api_key
    parameters_list.append(api_key_param)

    if search:
        search_param = "search?"
        query_statement = create_query_statement("q",query_list)
        parameters_list.append(query_statement)
        if tags_list != None:
            tags_statement = create_query_statement("tag",tags_list)
            parameters_list.append(tags_statement)
    else:
        search_param = "tags?"
        tags_statement = create_query_statement("q",tags_list)
        parameters_list.append(tags_statement)


    from_date_param = "from-date=" + from_date
    parameters_list.append(from_date_param)
    to_date_param = "to-date=" + to_date
    parameters_list.append(to_date_param)
    page_size_param = "page-size=" + str(page_size)
    parameters_list.append(page_size_param)
    show_field_param = "show-fields=trailText"
    parameters_list.append(show_field_param)

    #Join sections and request query
    full_query = main_page + search_param + "&".join(parameters_list)
    
    response = requests.get(full_query)

    return response

def get_json_files(api_key, search = True, query_list = base_query_list, tags_list = None,
 from_date = "2017-01-01", to_date = "2023-01-31", page_size = 50, pages = 1):
    """
    Get json files
    """
    #Make request and do json transformations
    response = request_the_guardian(api_key,search, query_list, tags_list,
    from_date,to_date,page_size,pages)

    response_json = json.loads(response.text)
    #Get number of pages to determine the number of requests to make
    n_pages = response_json["response"]["pages"]

    with open("{}/the_guardian_1.json".format("json_files"), "w") as f:
        json.dump(response_json, f, indent=1)
        f.close()

    for page in range(2,n_pages+1):
        response = request_the_guardian(api_key, search, query_list,tags_list,
    from_date,to_date,page_size,page)
        response_json = json.loads(response.text)
        print("saved page n° {}/{}".format(page,n_pages))
        
        with open("{}/the_guardian_{}.json".format("json_files",page),"w") as f:
            json.dump(response_json,f,indent=1)
            f.close()





