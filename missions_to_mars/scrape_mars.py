from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# driver = webdriver.Chrome(ChromeDriverManager().install())
# s = Service('C:/Users/.../chromedriver.exe')
# driver = webdriver.Chrome(service=s)

# scrape all function
def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    scrape_news(browser)

    #print("Scrape Scrape")
    #browser.quit()

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

# scrape the facts page 

#scrape hemispheres page 
if __name__ == '__main__':
    print(scrape_all())