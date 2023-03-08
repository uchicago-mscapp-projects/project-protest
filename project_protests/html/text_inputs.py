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
    "Title" : """Project Protest: Analysis of the impact of Black Lives Matter protest 2017-2023""", 
    "subtitles": {"Number of protest":"Protests",
    "Police":"Impact on Police Budget",
    "News":"Analyzing News Coverage",
    "Sentiment_analysis":"Analyzing perception in news coverage",
    "Conclusion":"Conclusion",
    "Sentiment_Score": "Sentiment Scores of News Headlines",
    "Pairwise": "Most Similar Words to Police"},
    "sub_subtitles": {"coverage": "News_coverage", "sentiment":"Sentiment Analysis",
    "pairwise": "Pairwise correlations"},
    "paragraphs": {
        "team": "Team: Josemaria Macedo, JP Martinez, Monica Nimmagadda, Lisette Solis", 
        "introduction": """
        In 2020, millions of people participated in Black Lives Matter Protests throughout the USA and the world. These protests sparked by the murder of George Floyd some of the largest in USA history. Our project focuses on understanding these protests and their impact in relationship to media coverage and changes to municipal budgets. We were particularly interested in better understanding the extent of coverage on the protests and the tone of the stories, and in turn whether there is a relationship between the number protests, type of media coverage, and changes to municipal budgets.
        """
    }, 
    "graph_info": {
        "protest": "There is a clear spike in the number of protests in the years 2020 and 2021 following the high-profile murders of George Floyd, Breonna Taylor, and Ahmaud Arbery. However, some of this spike may also be due to the Crowd Counting Consortium growing as an organization and developing their data collection methods. If this dataset were complete, we would likely expect to see the spike in 2020 rather than 2021.", 
        "sentiment": "Part of the initial scope of the project was to perform a sentiment analysis on newspaper data to determine the tone of the stories regarding the Black Lives Matter movement. The first approach taken was to calculate the sentiment scores in the headline and lead paragraph of the news collected from The Guardian and The New York Times using a pre-trained model from the package nltk which results are presented in the following figure.",
        "sentiment_2": "In these results is possible to see observe that the distribution of scores is centered at 0 and highly skewed to the left leaning to negative scores which makes sense regarding the issue that is being covered with the tags utilized. While using the headline is not possible to see a clear change in the distribution of scores, it is possible to see a shift toward negative scores when using the lead paragraph.", 
        "sentiment_3": "During the analysis we discovered that there were important limitations in applying this model to the data. Given the complexity of the issue, the results of the sentiment score are highly likely to not be reflective of the level of support for the Black Lives Matter movements and the reforms being pursued by them which could be solved by training our own data to determine which stories are associated with support and opposition to the Black Lives Matter movement which could not be included due to capacity and time constraints.",
        "news": "There is a clear spike in 2020 of the number of stories from The New York Times and The Guardian covering the Black Lives Matter movement. Both newspapers reached around 750 stories each (1,513 in total). This makes sense because protests related to the movement also increased during the same year after the killings of George Floyd, Breonna Taylor, and Ahmaud Arbery. However, there is a decrease in the coverage in 2021 and 2022 from both newspapers and an increase of protests related to the Black Lives Matter movement in the same period of time. The decrease in number of stories could be due to diminishing attention to the movement and less stories to cover. The increase in protests may be due to Crowd Counting Consortium still developing their data collection methods during 2020 and improving their methods in 2021. ", 
        "budget": "The main effort behind the Black Lives Matter movement is to defund the police and use this funding for community services such as housing, parks, or healthcare. The chart below visualizes the budget per capita in eight different cities with major protest involvement. The budget per capita has steadily increased since FY2016. Some cities like Minneapolis and Detroit decreased their budget after FY2020, but still increased their budget in the years after. This demonstrates that the calls to defund the police has not affected local budgets in these cities. ",
        "pairwise": "The graph below shows the words most similar to the term, police, per year from 2017-2022. The scores designate similarity from 1 being the exact same to -1 being the exact opposite. Because of the selective filtering we did on the initial newspaper dataset, the words usually surrounding “police” are related to the BLM movement. There is a noticeable trend of words related to George Floyd in 2020 and 2021. You can also see the decrease in score before 2020 and after 2021 as more articles were produced around the Floyd protests in 2020. The impact of George Floyd on articles around BLM and the police are clear as words like Floyd, Chauvin (officer who killed Floyd), Minneapolis show up even in 2022. In the future, understanding the perception of police in the media would require filtering for a more neutral sample of articles to build the model. "
    }, 
}

DATA_TEXT = {"paragraphs":
{"p1":"""Protest data is from the database maintained by the Crowd Counting Consortium. 
The database was started by two political science professors and aggregates self-reported protest data and 
data scraped from newspapers and social media event pages. Protest data is available from January 1, 2017 – January 
31, 2023 and therefore the other data sources are limited to match these dates.  Protests were filtered based on whether 
the description included any of the following tags in the description.""",
"tags_protest":"Tags: ['police', 'black lives', 'defund police'  'racial justice', 'criminal justice', 'racism', 'white supremacy'] ",
"p2": "Newspaper data was pulled from the New York Times (NYT) and The Guardian API. Queries were limited to include stories published between January 1, 2017 – January 31, 2023, that include any of following tags in either the headline (both NYT and Guardian), lead paragraph (NYT) or abstract (Guardian). The difference in whether to search in the lead paragraph or the abstract is explained by the options available for each API. ",
"tags_news": "Tags: ['blm', 'black lives matter', 'police brutality', 'blue lives matter', 'George Floyd', 'Breonna Taylor', 'Tyre Nichols', 'Ahmaud Arbery']",
"p3": "Budget data was collected manually from publicly available budgets. Since this data was collected manually, it was only collected for the eight US cities with the highest police spending per capita.",
"p4": "The sentiment scores in the headline and lead paragraph of the news collected from The Guardian and The New York Times were calculated using a pre-trained model from the package nltk.",
"p5": "During the analysis we discovered that there were important limitations in applying the sentiment pre-trained model to the data. The pre-trained model assigns for each word a score from -1 to 1 and compounds it along a string to get a score, where words associated with negative sentiments are categorize with a score below 0 while those associated with positive sentiments are assigned a value over 0.",
"p6" : "Given the complexity of the issue, the results of the sentiment score are highly likely to not be reflective of the level of support for the Black Lives Matter movements and the reforms being pursued by them.  For example, an article could have a negative score explained by a story that supports the movement but uses words with a negative score due to anger to the killing of a person, which at the same time could not be distinguishable –in terms of final score– from a news article that does not support the movement and uses words to refer to protestors as rioters. ",
"p7": "To correct for this issue, it would have been preferable to train our own data to determine which stories are associated with support and opposition to the Black Lives Matter movement which could not be included due to capacity and time constraints. To perform this correctly, we would have needed to obtained newspaper data from other media sources to end with a diverse sample of stories that show support and opposition since the two media sources occupied are usually associated with being more progressive. ",
"p8":"Using the Word2Vec package, a model was created using a corpus of lead paragraphs from the New York Times and the Guardian articles with the tags and dates listed above. The model filtered to 5 words on either side of the given term (in this case, “police”) and mentioned 10 or more times for 2018-2022 and 5 times for 2017. This is because our corpus for 2017 was limited. The model mapped the distance between the given term, scoring them on a scale of –1 to 1. The more similar a word is to the given term, the closer it is to 1. ",
"p9":"To visualize this data, each year is plotted with their top 15 words related to 'police' and their similarity scores. Because of the selective filtering we did on the initial newspaper dataset, the words usually surrounding “police” are related to the BLM movement. There is a noticeable trend of words related to George Floyd in 2020 and 2021. You can also see the decrease in score before 2020 and after 2021 as more articles were produced around the Floyd protests in 2020. ",
"p10":"Creating a corpus with any articles mentioning police would give us a greater understanding of how description of police has changed over time. Given our limitations of article requests, we were unable to run a more neutral model. ",
"p11":"Our results were inconclusive about how the protests shaped news coverage and resulted in policy change. Our analysis was limited by limitations of the data available and packages we chose which we further explain in the Data and Methods section.  ",
"p12":"Looking forward, we hope to see more work done on understanding media portrayal of inherently difficult topics like police brutality. Media coverage of these events plays a significant role in shaping political will and mobilization to enact policy change. However, despite mass mobilization around Black Lives Matter, we did not notice a change in trend of municipal budgets after the 2020 protests. This prompts the question of how effective protests are in creating policy impact. "}}
