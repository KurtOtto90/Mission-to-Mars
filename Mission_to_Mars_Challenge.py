#!/usr/bin/env python
# coding: utf-8

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
driver = webdriver.Chrome("C:/Users/kurto/Documents/Data Analyst Bootcamp/Module 10 - Web Scraping with HTML-CSS/Mission-to-Mars/chromedriver.exe")
#driver.implicitly_wait(5)
driver.get(url)
#links = img_soup2.find_all('a',)
#links
cerberus = driver.find_element("link text", "Cerberus Hemisphere Enhanced")
cerberus.click()
cerb_url = driver.current_url
driver.get(cerb_url)
cerberus_Hem_pic = driver.find_element("link text", "Sample")
cerberus_Hem_pic.click()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[1])
cerb_pic_url = driver.current_url
hemisphere_image_urls.append({'img_url': cerb_pic_url, 'title': 'Cerberus Hemisphere Enhance'})

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(5)
driver.get(url)

schiaparelli = driver.find_element("link text", "Schiaparelli Hemisphere Enhanced")
schiaparelli.click()
schiap_url = driver.current_url
driver.get(schiap_url)
schiap_Hem_pic = driver.find_element("link text", "Sample")
schiap_Hem_pic.click()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[1])
schiap_pic_url = driver.current_url
hemisphere_image_urls.append({'img_url': schiap_pic_url, 'title': 'Schiaparelli Hemisphere Enhance'})

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(5)
driver.get(url)

syrtis = driver.find_element("link text", "Syrtis Major Hemisphere Enhanced")
syrtis.click()
syrtis_url = driver.current_url
driver.get(syrtis_url)
syrtis_Hem_pic = driver.find_element("link text", "Sample")
syrtis_Hem_pic.click()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[1])
syrtis_pic_url = driver.current_url
hemisphere_image_urls.append({'img_url': syrtis_pic_url, 'title': 'Syrtis Major Hemisphere Enhance'})


driver.close()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(5)
driver.get(url)

valles = driver.find_element("link text", "Valles Marineris Hemisphere Enhanced")
valles.click()
valles_url = driver.current_url
driver.get(valles_url)
valles_Hem_pic = driver.find_element("link text", "Sample")
valles_Hem_pic.click()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[1])
valles_pic_url = driver.current_url
hemisphere_image_urls.append({'img_url': valles_pic_url, 'title': 'Valles Marineris Hemisphere Enhance'})

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()


# In[ ]:




