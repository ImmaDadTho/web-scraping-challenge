# web-scraping-challenge

In this activity I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page, and using the application creates a database in MongoDB and stores the information that was scraped in a table. There are two parts to this ativity the first part is `scraping` the second part is `MongoDB and Flask application`.

I have also created another repo to fulfill part 3 of the assignment that will just have the Jupyter notebook containing the scraping code used and some screenshots of the final application.
https://github.com/ImmaDadTho/MarsWSsubmission

# Scraping

I started by creating a jupyter notebook file to scrape and analyze different information pertaining to the mission to mars, the information gathered are as follows:


* Scraping the Mars News Site and collecting the latest News Title and Paragraph Text. 
* Use splinter to navigate the site and find the image URL for the current Featured Mars Image.
* Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet.
  * Use Pandas to convert the data to a HTML table string.
  
![Alt text](missions_to_mars/screenshots/jupyterFactspythontoHtml.jpg?raw=true "Title")

* Visit the astrogeology site to obtain high-resolution images for each hemisphere of Mars.
  * Use splinter to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
  
  
# MongoDb and Flask Application

In this part of the activity I use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above, the steps were as follows:

* Started by converting my Jupyter notebook into a Python script called scrape_mars.py by using a function called scrape. 
* Created a route called '/scrape' that will import my scrape_mars.py script and call the scrape function.
  * Store the return value in Mongo as a Python dictionary.
  
![Alt text](missions_to_mars/screenshots/MongoDbScreenshot.jpg?raw=true "Title")

* Created a root route '/' that will query the Mongo database and pass the Mars data into an HTML template for displaying the data.
* Created a template HTML file called index.html that will take the Mars data dictionary and display all the data in the appropriate HTML elements. 

![Alt text](missions_to_mars/screenshots/indexpagescreenshot.jpg?raw=true "Title")
