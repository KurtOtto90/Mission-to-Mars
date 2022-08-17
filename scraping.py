# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hemisphere_image_urls():
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
    return hemisphere_image_urls

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())