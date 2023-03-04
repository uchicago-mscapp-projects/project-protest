import codecs
import webbrowser

f = open('index.html', 'w')

html_template = """
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>Project Protest: Analysis of the Black Lives Matter Movement after the
    George Floyd Murder
    </title>
    <link rel="stylesheet" href="styles_main.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
    <style>
        body {font-family: "Lato"}
    </style>
  </head>
  <body>
    <h1> "Project Protest: Analysis of the Black Lives Matter Movement after the
    George Floyd Murder" </h1> 
    <p> "On May 25, Minneapolis police officers arrested George Floyd, a 46-year-old black man,
     after a convenience store employee called 911 and told the police that Mr. Floyd had bought cigarettes with a 
     counterfeit $20 bill. Seventeen minutes after the first squad car arrived at the scene, Mr. Floyd was unconscious 
     and pinned beneath three police officers, showing no signs of life. <a title="NYT news" 
     href="https://www.nytimes.com/2020/05/31/us/george-floyd-investigation.html">  </a>"</p>
     <p> "The murder of George Floyd lead to a series of protest nationwide regarding
     the role of police in (...) </p>
     <p> "In this project, we are analyzing (...)" </p>
    <img
  src="ADD a picture.jpeg" 
  alt="page_icon" height="250" width="150"
  opacity = 0.3>
    <ul>
        <li>
            <a title="Number of protests" href="2023/index.html"> 2023! </a>
        </li>
        <li>
            <a title="Budget Analysis" href="2022/index.html"> 2022! </a>
        </li>
        <li>
            <a title="Newspaper analysis" href="2021/index.html"> 2021! </a>
        </li>
    </ul>
    <h2> "Number of protests (...)" </h2> 
    <p> "Description of first analysis: Heatmap of number of protests"
    </p>
    <h2> "Budget Analysis" </h2> 
    <p> "Description of second analysis: Budgets"    </p>
    <h2> "Newspaper Analysis"  </h2> 
    <p> "Description of third analysis: Newspapers"    </p>
    
    </body>
</html>
"""

f.write(html_template)
f.close()

file = codecs.open("index.html", 'r', "utf-8")
webbrowser.open('index.html')