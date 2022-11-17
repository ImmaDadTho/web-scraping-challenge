from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/planet_mars_db'
mongo = PyMongo(app)

@app.route('/')
def index():
    mars_data = mongo.db.marsdata.find_one()

    return render_template("index.html", mars = mars_data)


@app.route('/scrape')
def scrape():

    marsGoDb = mongo.db.marsdata

    #drop table if exists
    mongo.db.marsdata.drop()

    #activates the scrape mars py 
    mars_data = scrape_mars.scrape_all()

    #loads the dictionary into mongo DB
    marsGoDb.insert_one(mars_data)

    # return mars_data

    return redirect("/")

if __name__ == "__main__":
    app.run()