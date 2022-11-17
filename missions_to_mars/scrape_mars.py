from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
import datetime as dt
import time

# scrape all function
def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = scrape_news(browser)

    #build dictionary from scrape info 
    MarsDat = {
        'newsTitle':news_title,
        'newsParagraph': news_paragraph,
        'MarsFeaturedImage': scrape_feature_pic(browser),
        'MarsVSEarth':scrape_facts(browser),
        'MarsHemispheres':scrape_hemis(browser),
        'Current_As_Of':dt.datetime.now()
    }

    browser.quit()
    #print("Scrape Scrape")
    #browser.quit()
    return MarsDat
# scrape the mars news page 
def scrape_news(browser):
    # syntax used to visit the mars site 
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    #creates a delay to properly get data from scraping 
    browser.is_element_present_by_css('div.list_text', wait_time=1.5)

    souphtml = browser.html
    marsnewssoup = soup(souphtml, 'html.parser')

    sections = marsnewssoup.select_one('div.list_text')

    news_title = sections.find('div', class_='content_title').get_text()

    news_p = sections.find('div', class_="article_teaser_body").get_text()

    return news_title, news_p

# scrape the featured image page 
def scrape_feature_pic(browser):
    featuredurl = 'https://spaceimages-mars.com/'
    browser.visit(featuredurl)

    #clicks on full size image button 

    fullsizeimage = browser.find_by_tag('button')[1]
    fullsizeimage.click()

    # pulls html from 'https://spaceimages-mars.com/'
    featuredhtml = browser.html
    dustysoup = soup(featuredhtml, 'html.parser')

    # locates the featured image in full size
    image_url = dustysoup.find('img', class_="headerimage fade-in").get('src')

    # save featured full image in a variable 
    featured_image_url = f'https://spaceimages-mars.com/{image_url}'

    return featured_image_url

# scrape the facts page 
def scrape_facts(browser):
    marsfactsurl = 'https://galaxyfacts-mars.com/'
    browser.visit(marsfactsurl)

    # pulls the html from 'https://galaxyfacts-mars.com/'
    galaxyhtml = browser.html
    galaxysoup = soup(galaxyhtml, 'html.parser')

    #locates the diagram of mars vs earth 
    VStable = galaxysoup.find('div', class_="diagram mt-4")

    #locates the table in the diagram
    marsVSearth = VStable.find('table')

    #create a string to store the facts 
    facts = ""

    #inputs the facts into the string using the table data 
    facts += str(marsVSearth)

    return facts

#scrape hemispheres page 
def scrape_hemis(browser):
    hemispheresurl = 'https://marshemispheres.com/'
    browser.visit(hemispheresurl)

    # create a list to hold images and titles
    hemispheresImages = []

    #get a list of all the hemispheres
    hemihtml = browser.find_by_css('a.product-item img')

    #loop though the links, click on link, find the sample anchor, return the href
    for i in range(4):
        #hemisphere dictionary
        hemisphereDict = {}
        
        #find elements on each loop 
        browser.find_by_css('a.product-item img')[i].click()
        time.sleep(1)
        #find the sample image anchor tag
        sample = browser.find_by_text('Sample').first
        hemisphereDict['img_url'] = sample['href']
        
        #get hemisphere title
        hemisphereDict['title'] = browser.find_by_css('h2.title').text

        #append hemisphere object to list
        hemispheresImages.append(hemisphereDict)
        
        #navigate backwards
        browser.back()
        time.sleep(1)

    return hemispheresImages

if __name__ == '__main__':
    print(scrape_all())