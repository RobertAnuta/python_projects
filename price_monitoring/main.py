import requests
import lxml
import bs4
import re
import csv

''' Handle all sorts of URL formats and correctly merge them'''
from urllib.parse import urljoin


# Base URL of the site
base_url = 'https://books.toscrape.com/'

# Page URL
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

result = requests.get(url)

soup = bs4.BeautifulSoup(result.content,"lxml")

# Scrap the page content
product_page_url = url
product_upc = soup.find_all("td")[0].getText()
book_title = soup.find("li", class_="active").getText()
price_including_tax = soup.find_all("td")[3].getText()
price_excluding_tax = soup.find_all("td")[2].getText()
quantity_available = re.search(r"\d+",soup.find_all("td")[5].getText()).group()
product_description = soup.select(".product_page > p")[0].getText()
category = soup.select(".breadcrumb > li")[2].getText()
review_rating = soup.find_all("td")[6].getText()
image_url = urljoin(base_url, soup.select("img")[0]["src"])


