from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/planet_mars_db'
mongo = PyMongo(app)

@app.route('/')
def index():
    return "You have arrived to The Milky Way,\
    please make your way to the red planet we call Mars!"

@app.route('/scrape')
def scrape():

    marsGoDb = mongo.db.marsdata

    #drop table if exists
    mongo.db.marsdata.drop()

    #activates the scrape mars py 
    mars_data = scrape_mars.scrape_all()
    
    #loads the dictionary into mongo DB
    marsGoDb.insert_one(mars_data)

    return (f"You have reached the planet Mars\n" %{mars_data})

if __name__ == "__main__":
    app.run()