# Create a Virtual Environment

## On Windows
python -m venv venv

## On macOS/Linux
python3 -m venv venv


# Activate the Virtual Environment

## On Windows
.\venv\Scripts\activate

## On macOS/Linux
source venv/bin/activate


# Install Required Packages
pip install -r requirements.txt


# Run the Script while the virtual environment is activated:

## On Windows
python main.py

## On macOS/Linux
python3 main.py

<!-- FOR TEST -->
# Replace the following code from the end of the main.py file:

if __name__ == "__main__":
    books_urls()
    generate_excel(all_books_urls[0:2])