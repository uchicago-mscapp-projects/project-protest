###Task: Add text used in dashboard appication
###Last modified 03.04.23
###While this is hardcoded and adapted according to the final text requirements,
###Allows for easier modification of the dashboard app and allows less conflict

#Description of dictionary keys
#Title: h1 tags related text
#subtitles: h2 tags related text
#subsubtitles: h3 tags related text  
#paragrahps: p tags related text

HTML_TEXT = { 
    "Title" : """Project Protest: Analysis of the Black Lives Matter Movement after the
    George Floyd Murder""", 
    "subtitles": {"Number of protest":"Protests",
    "Police":"Impact on Police Budget",
    "News":"Analying News Coverage",
    "Sentiment_analysis":"Analyzing perception in news coverage",
    "Conclusion":"Conclusion"},
    "sub_subtitles": {"coverage": "News_coverage", "sentiment":"Sentiment Analysis",
    "pairwise": "Pairwise correlations"},
    "paragraphs": {
        "introduction": """
        In 2020, millions of people participated in Black Lives Matter Protests throughout the USA and the world. These protests sparked by the murder of George Floyd some of the largest in USA history.1 Our project focuses on understanding these protests and their impact in relationship to media coverage and changes to municipal budgets. We were particularly interested in better understanding the extent of coverage on the protests and the tone of the stories, and in turn whether there is a relationship between the number protests, type of media coverage, and changes to municipal budgets.  
        """,
        "description": """In this project, we are analyzing (...)
        """
    }
}

DATA_TEXT = {"paragraphs":
{"p1":"Page description","p2":"News collection description",
"p3":"Protest data description","p4":"Police data description"},
"subtitles":{"news":"News data gathering descriprion","protest":"Protest data gathering description",
"police":"Police data gathering description"}}

METHODOLOGY_TEXT = {"paragraphs":{},"subtitles":{}}