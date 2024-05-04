import requests
import lxml
import bs4
import re
import pandas as pd
import openpyxl
import os
import time
from urllib.parse import urljoin


def clear_console():
    os.system('cls')

# Base URL of the site
base_url = 'https://books.toscrape.com/'
book_base_url = 'https://books.toscrape.com/catalogue/'

all_books_urls = []
pages_base_url= "https://books.toscrape.com/catalogue/page-{}.html"

#Loop through every page to collect the URLs
def books_urls():
    '''
    Looking through every page of the website and collect the book's URLs to be scrapped     
    '''
    links = []
    page = 1
    
    while True: 
        result = requests.get(pages_base_url.format(page))
        
        soup = bs4.BeautifulSoup(result.content,"lxml")
        
        # Find out of range pages
        no_pages = soup.find_all(string="404 Not Found")

        if "404 Not Found" in no_pages:
            break
            
        anchors = soup.select(".image_container > a")

        # Collect all the URLs from one page and build a complete UT
        hrefs = [urljoin(book_base_url,anchor['href']) for anchor in anchors]

        links.extend(hrefs)

        page += 1
        print(f"Searching for links.. {len(links)}", end='\r')

    all_books_urls.extend(links)

    return all_books_urls
    

def generate_excel(all_books_urls):
    '''The function will loop through every books URLs and will write the details in a dictionary.
    All the values will be added into an excel sheet split into categories
    '''    
    print("Writing data...")

    all_books_data = []
    
    for url in all_books_urls:
        try:
            time.sleep(1)

            result = requests.get(url)
            
            soup = bs4.BeautifulSoup(result.content,"lxml")

            # Define a Dictionary with the data collected
            book_data = {
                "product_page_url" : url,
                "product_upc" : soup.select("table td")[0].getText(),
                "book_title" : soup.find("li", class_="active").getText(),
                "price_including_tax" : soup.select("table td")[3].getText(),
                "price_excluding_tax" : soup.select("table td")[2].getText(),
                "quantity_available" : re.search(r"\d+",soup.find_all("td")[5].getText()).group(),
                "product_description" : soup.find_all("meta")[2]["content"].strip(),
                "category" : soup.select(".breadcrumb > li")[2].getText().strip(),
                "review_rating" : soup.select("table td")[6].getText(),
                "image_url" : urljoin(base_url,soup.select("img")[0]["src"]),
            }

            # Append the book data to the list
            all_books_data.append(book_data)

            print(f"{len(all_books_data)}\{len(all_books_urls)}", end='\r')
            
        except requests.RequestException as e:
            print(f"Request error with {url}: {e}")
        except Exception as e:
            print(f"Error processing data from {url}: {e}") 

    #Convert dictionary to DataFrame
    data_frame = pd.DataFrame(all_books_data)
    
    # Write the DataFrame to Excel
    with pd.ExcelWriter("Price Monitoring.xlsx", engine="openpyxl") as writer:
        for category, group_df in data_frame.groupby('category'):
            group_df.to_excel(writer, sheet_name=category, index=False)

    clear_console()
    print("Data has been written to Excel successfully.")   

    
    # Define the path for the directory and check if the folder exists
    folder_path = os.getcwd() + "\images"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print("Saving images...")

    for book in all_books_data:
        image_link = requests.get(book["image_url"])
        f = open(f'.\images\{soup.select("table td")[0].getText()}', "wb")
        f.write(image_link.content)
        f.close()
    
    clear_console()
    print("Books images successfully saved!")


if __name__ == "__main__":
    # Generate URLs
    books_urls()
    # Loop through the URLs and collect the excel data
    generate_excel(all_books_urls[0:2])
