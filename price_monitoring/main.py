import requests
import lxml
import bs4
import re
import pandas as pd

''' Handle all sorts of URL formats and correctly merge them'''
from urllib.parse import urljoin


# Base URL of the site
base_url = 'https://books.toscrape.com/'

# Single page URL
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

result = requests.get(url)

# Scrap single-book data
soup = bs4.BeautifulSoup(result.content,"lxml")

product_page_url = [url]
product_upc = [soup.find_all("td")[0].getText()]
book_title = [soup.find("li", class_="active").getText()]
price_including_tax = [soup.find_all("td")[3].getText()]
price_excluding_tax = [soup.find_all("td")[2].getText()]
quantity_available = [re.search(r"\d+",soup.find_all("td")[5].getText()).group()]
product_description = [soup.select(".product_page > p")[0].getText()]
category = [soup.select(".breadcrumb > li")[2].getText().strip()]
review_rating = [soup.find_all("td")[6].getText()]
image_url = [urljoin(base_url,soup.select("img")[0]["src"])]

# Define a Dictionary with the data collected
data = {}

data["product_page_url"] = product_page_url
data["product_upc"] = product_upc
data["book_title"] = book_title
data["price_including_tax"] = price_including_tax
data["price_excluding_tax"] = price_excluding_tax
data["quantity_available"] = quantity_available
data["product_description"] = product_description
data["category"] = category
data["review_rating"] = review_rating
data["image_url"] = image_url


all_books_urls = []
pages_base_url= "https://books.toscrape.com/catalogue/page-{}.html"
#Loop to every page to collect the Books URLs
def books_urls():
    links = []
    page = 1
    print("Searching...")
    
    while True: 
        result = requests.get(pages_base_url.format(page))
        
        soup = bs4.BeautifulSoup(result.content,"lxml")
        
        # Find out of range pages
        no_pages = soup.find_all(string="404 Not Found")

        if "404 Not Found" in no_pages:
            break
            
        anchors = soup.select(".image_container > a")

        # Collect all the URLs from one page and build a complete URL
        hrefs = [urljoin(base_url,anchor['href']) for anchor in anchors]

        links.extend(hrefs)

        page += 1

    all_books_urls.extend(links)

    return all_books_urls
    
books_urls()