from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome(ChromeDriverManager().install())
s = Service('C:/Users/.../chromedriver.exe')
driver = webdriver.Chrome(service=s)

# scrape all function
def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    #print("Scrape Scrape")
    browser.quit()

# scrape the mars news page 

# scrape the featured image page 

# scrape the facts page 

#scrape hemispheres page 
if __name__ == '__main__':
    print(scrape_all())