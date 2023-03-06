# Project Protest

## Team
Lisette Solis, Josemaria Macedo, JP Martinez, Monica Nimmagadda

## Description
In 2020, millions of people participated in Black Lives Matter Protests throughout the USA and the world1. These protests sparked by the murder of George Floyd are some of the largest in USA history. 

Our project focuses on understanding these protests and their impact in relationship to media coverage and changes to municipal budgets. 

We were particularly interested in better understanding the extent of coverage on the protests and the tone of the stories, and in turn whether there is a relationship between the number protests, type of media coverage, and changes to municipal budgets.

## Data Sources & Method for Analysis
More information on our data collection and analysis can be found on the HTML site once the project is run.

## Instructions to Run
To run the project the following steps need to be followed: 
1. Clone repository  
2. Run ```poetry install``` to install the neccesary packages 
3. Run ```poetry shell``` to activate the virtual environment
4. From the directory *“30122-project-project-protest"* run from the command line ```poetry run project_protest <arguments>``` 

When running the last command, up to two arguments can be called: 
1. ```compile_news```: Using the json files obtained from scraping data from The New York Times and The Guardian, it cleans and compile to create a compiled csv with the newspaper information. This argument can be combined with collect_data. 
2. ```dashboard```: This argument runs the dashboard application Specifying this argument is equivalent as specifying no arguments, and can only be called as a standalone argument. 
3. ```run```: This argument performs the two tasks described in compile_news and dashboard. This argument can be combined with collect_data.  
4. ```collect_data```: This argument collect the data from The Guardian and The New York Times API and store the json files obtained from the requests. This argument can only be called combined with either compile_news or run and can only be included as the last argument. (The approximate run time for this argument when using the default query arguments is approximate 25 minutes). Before running the command with this argument, you should include a config.py file (sent privately) with the API keys for the New York Times and The Guardian API in the "project_protest" package directory.

## Output
The output of the above instructions will create an HTML site with two tabs:
1. Home - interactive visualizations of our data
  - Protest:
    - number of protests per year (2017-2023)
  - Newspaper: 
    - number of news stories per year (2017-2023)
    - correlation matrix between number of newsstories and number of protests
  - Sentiment Analysis:
    - sentiment scores of news stories per year (2017-2023)
    - similarity scores of words related to "police" (2017-2022) 
2. Data Sources and Analysis
  - Description and shortcomings of our data sources
  - Method of analysis


