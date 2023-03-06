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
    "Conclusion":"Conclusion",
    "Sentiment_Score": "Sentiment Scores of News Headlines",
    "Pairwise": "Most Similar Words to Police"},
    "sub_subtitles": {"coverage": "News_coverage", "sentiment":"Sentiment Analysis",
    "pairwise": "Pairwise correlations"},
    "paragraphs": {
        "team": "Team: Lisette Solis, Josemaria Macedo, JP Martinez, Monica Nimmagadda", 
        "introduction": """
        In 2020, millions of people participated in Black Lives Matter Protests throughout the USA and the world. These protests sparked by the murder of George Floyd some of the largest in USA history. Our project focuses on understanding these protests and their impact in relationship to media coverage and changes to municipal budgets. We were particularly interested in better understanding the extent of coverage on the protests and the tone of the stories, and in turn whether there is a relationship between the number protests, type of media coverage, and changes to municipal budgets.
        """
    }, 
    "graph_info": {
        "protest": "There is a clear spike in the number of protests in the number of protests in the years 2020 and 2021 following the high-profile murders of George Floyd, Breonna Taylor, and Ahmaud Arbery. However, some of this spike may also be due to the Crowd Counting Consortium growing as an organization and developing their data collection methods. If this dataset were complete, we would likely expect to see the spike in 2020 rather than 2021.", 
        "sentiment": "Part of the initial scope of the project was to perform a sentiment analysis on newspaper data to determine the tone of the stories regarding the Black Lives Matter movement. The first approach taken was to calculate the sentiment scores in the headline and lead paragraph of the news collected from The Guardian and The New York Times using a pre-trained model from the package nltk which results are presented in the following figure.",
        "sentiment_2": "In these results is possible to see observe that the distribution of scores is centered at 0 and highly skewed to the left leaning to negative scores which makes sense regarding the issue that is being covered with the tags utilized. While using the headline is not possible to see a clear change in the distribution of scores, it is possible to see a shift toward negative scores when using the lead paragraph.", 
        "sentiment_3": "During the analysis we discovered that there were important limitations in applying this model to the data. Given the complexity of the issue, the results of the sentiment score are highly likely to not be reflective of the level of support for the Black Lives Matter movements and the reforms being pursued by them which could be solved by training our own data to determine which stories are associated with support and opposition to the Black Lives Matter movement which could not be included due to capacity and time constraints.",
        "news": "There is a clear spike in 2020 of the number of stories from The New York Times and The Guardian covering the Black Lives Matter movement. Both newspapers reached around 750 stories each (1,513 in total). This makes sense because protests related to the movement also increased during the same year after the killings of George Floyd, Breonna Taylor, and Ahmaud Arbery. However, there is a decrease in the coverage in 2021 and 2022 from both newspapers and an increase of protests related to the Black Lives Matter movement in the same period of time. The decrease in number of stories could be due to diminishing attention to the movement and less stories to cover. The increase in protests may be due to Crowd Counting Consortium still developing their data collection methods during 2020 and improving their methods in 2021. ", 
        "budget": "The main effort behind the Black Lives Matter movement is to defund the police and use this funding for community services such as housing, parks, or healthcare. The chart below visualizes the budget per capita in eight different cities with major protest involvement. The budget per capita has steadily increased since FY2016. Some cities like Minneapolis and Detroit decreased their budget after FY2020, but still increased their budget in the years after. This demonstrates that the calls to defund the police has not affected local budgets in these cities. ",
        "pairwise": "The graph below shows the words most similar to the term, police, per year from 2017-2022. The scores designate similarity from 1 being the exact same to -1 being the exact opposite. Because of the selective filtering we did on the initial newspaper dataset, the words usually surrounding “police” are related to the BLM movement. There is a noticeable trend of words related to George Floyd in 2020 and 2021. You can also see the decrease in score before 2020 and after 2021 as more articles were produced around the Floyd protests in 2020. The impact of George Floyd on articles around BLM and the police are clear as words like Floyd, Chauvin (officer who killed Floyd), Minneapolis show up even in 2022. In the future, understanding the perception of police in the media would require filtering for a more neutral sample of articles to build the model. "
    }, 
}

DATA_TEXT = {"paragraphs":
{"p1":"Page description","p2":"News collection description",
"p3":"Protest data description","p4":"Police data description"},
"subtitles":{"news":"News data gathering descriprion","protest":"Protest data gathering description",
"police":"Police data gathering description"}}

METHODOLOGY_TEXT = {"paragraphs":{},"subtitles":{}}