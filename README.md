# Newzer
This is my first Django project.

Main Function
----------------
This website is all about news.News that users want,whether they want to read news on some topic or they just want to get the latest headlines on sports,entertainment,health etc.

News Source
------------
Behind the scenes, the website calls the news API to get the news.

/news
------
Displays the news about a specific term that you mention.For eg there is a form in this page that asks you on what specific entity,topic (or just about anything) you want to get the news.
After filling the form and clicking on submit it shows you the news about that query (if it exists).

/top_headlines
-----------------
Displays the latest headlines.You can choose from the categories whether it be health,entertainment or sports etc.

Database used
--------------
There is no database required for this type of application however to help the user navigate between pages SQLLite3 has been used that stores the sessions of the users.
