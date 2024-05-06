# Books to Scrape Web Scraper

This script is designed to scrape book information from [Books to Scrape](https://books.toscrape.com/). It collects details about each book, organizes them by category into different sheets in an Excel file, and downloads images of the books.

## Features

- Retrieves book details including title, price, stock status, and product description.
- Categorizes books into their respective categories in the Excel file.
- Downloads and saves book images in a local directory.

## Prerequisites

- Python 3.6+
- pip
- Virtual environment (recommended)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RobertAnuta/python_projects/tree/2fe7768f817da5e4f56c29864a49a1f44969eac4/price_monitoring
   cd price_monitoring
   ```

2. **Create a Virtual Environment**

    - On Windows
    ```bash
    python -m venv venv
    ```

    - On macOS/Linux
    ```bash
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**
    
    - On Windows
    ```bash
    .\venv\Scripts\activate
    ```

    - On macOS/Linux
    ```bash
    source venv/bin/activate
    ```

4. **Install Required Packages**
   
     ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from the command line.

   - On Windows
    ```bash
    python main.py
    ```

    - On macOS/Linux
    ```bash
    python3 main.py
    ```

## Modifying the Script

To customize the range of books processed or change settings:

- Edit the main.py script's following section before running:
    ```python
    if __name__ == "__main__":
        books_urls()
        generate_excel(all_books_urls[0:2])  # Modify the slice as needed
    ```