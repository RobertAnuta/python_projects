# Django Project - My Site

## Description
my_site is a web application built with Django, designed as a blog with latest posts, individual post page and all posts together. This project demonstrates the use of Django's core features and follows best practices for web development. I upload the project as a practice and I'm working to improve the database using SQLite, user autentification, responsive design, Admin panel.

## Installation
### Prerequisites
- Python 3.x
- Git
- pip
- Virtual Environment (recommended)

### Clone the repository
```
git clone chttps://github.com/RobertAnuta/python_projects/tree/main/my_site
cd my_site
```

### Set up the virtual environment
```
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the root directory with the following structure:
```
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Apply Migrations
```
python manage.py migrate
```

### Run the Development Server
```
python manage.py runserver
```

## Usage
Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Contributing
Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Created by Robert Anuta - https://github.com/RobertAnuta
