from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

@app.route('/')
def index():
    return "You have arrived to The Milky Way,\
    please make your way to the red planet we call Mars!"

@app.route('/scrape')
def scrape():
    return "You reached the Planet Mars"
    # mars_data = scrape_mars.scrape_all()
    # print(mars_data)

if __name__ == "__main__":
    app.run()