import sys
import json
import lxml.html
import requests
import urllib.parse

##Author: JP Martinez
##Task: Create querys and do requests for The Guardian API - Save JSON Files
##Last date updated: 03.02.23

def create_query_statement(key,list_parameters):
    """
    Creates a query statement to add to the request
    Input:
    key (str): api-key
    list_parameters (list): List of parameters to add to the query
    Return: (str: encoded query statement to pass to the )
    """
    query_terms_encoded_list = []
    
    for query_term in list_parameters:
        encoded_query = '"' + urllib.parse.quote(query_term) + '"'
        query_terms_encoded_list.append(encoded_query)

    query = key + "=(" + " OR ".join(query_terms_encoded_list) + ")"

    return query

base_query_list = ["Black Lives Matter", "BLM", "Police Brutality", \
"George Floyd", "Breonna Taylor", "Tyre Nichols", "Ahmaud Arbery", "Blue Lives Matter"]


def request_the_guardian(api_key, search = True, query_list = base_query_list, tags_list = None,
 from_date = "2017-01-01", to_date = "2023-01-31",page_size = 50, page = 1):
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
    show_field_param = "show-fields=body,standfirst"
    parameters_list.append(show_field_param)
    current_page_param = "page=" + str(page)
    parameters_list.append(current_page_param)
    query_fields_param = "query-fields=headline,standfirst"
    parameters_list.append(query_fields_param)

    #Join sections and request query
    full_query = main_page + search_param + "&".join(parameters_list)
    response = requests.get(full_query)
    
    return response

def get_json_files(api_key, search = True, query_list = base_query_list, tags_list = None,
 from_date = "2017-01-01", to_date = "2023-01-31", page_size = 50, page = 1):
    """
    Get json files
    Inputs:
    -api_key (str): Api key to be used for the request
    -search (Bool): If True, use search
    -query_list (list): List of items to search in content
    -tags_list(list): Tags to look for in content
    -from_date(str): Starting date for news retrieve 
    -to_date(str): End date for news retrieve
    - page (int): The page to retrieve in the results 
    Return:
     None - it creates json-files for each of the pages in the request results
    """
    #Make request and do json transformations
    response = request_the_guardian(api_key,search, query_list, tags_list,
    from_date,to_date,page_size,page)

    response_json = json.loads(response.text)
    #Get number of pages to determine the number of requests to make
    n_pages = response_json["response"]["pages"]

    with open("{}/the_guardian_1.json".format("json_files"), "w") as f:
        json.dump(response_json, f, indent=1)
        f.close()
    print("saved page n° 1/{}".format(n_pages))

    for pag in range(2,n_pages+1):
        response = request_the_guardian(api_key, search, query_list,tags_list,
    from_date,to_date,page_size,pag)
        response_json = json.loads(response.text)
        print("saved page n° {}/{}".format(pag,n_pages))
        
        with open("{}/the_guardian_{}.json".format("json_files",pag),"w") as f:
            json.dump(response_json,f,indent=1)
            f.close()





