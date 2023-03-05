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
    "subtitles": {"Number of protest":"Analysis of number of protests",
    "Police":"Analyzing changes in police budget",
    "News":"Analyzing changes in news coverage",
    "Sentiment_analysis":"Analyzing perception in news coverage",
    "Conclusion":"Conclusion"},
    "sub_subtitles": {"coverage": "News_coverage", "sentiment":"Sentiment Analysis",
    "pairwise": "Pairwise correlations"},
    "paragraphs": {
        "introduction": """
        On May 25, Minneapolis police officers arrested George Floyd, a 46-year-old black man,
     after a convenience store employee called 911 and told the police that Mr. Floyd had bought cigarettes with a 
     counterfeit $20 bill. Seventeen minutes after the first squad car arrived at the scene, Mr. Floyd was unconscious 
     and pinned beneath three police officers, showing no signs of life.
        """,
        "introduction_2": """
        The murder of George Floyd lead to several protest nationwide regarding
     the role of police in (...)
        """,
        "description": """In this project, we are analyzing (...)
        """
    }
}

DATA_TEXT = {"paragraphs":{"p1":"Page description","p2":"News collection description",
"p3":"Protest data description","p4":"Police data description"},
"subtitles":{"news":"News data gathering descriprion","protest":"Protest data gathering description",
"police":"Police data gathering description"}}

METHODOLOGY_TEXT = {"paragraphs":{},"subtitles":{}}