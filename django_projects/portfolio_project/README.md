# Portfolio - Django Web Application

This is a personal portfolio web application built with Django. It displays a homepage with a brief introduction and profile picture, followed by a list of job entries, each with an image and description. Clicking on a job card redirects to a detail page with more information about that specific job.

The project also includes an admin interface where new job entries can be created, edited, or deleted.

---

## Features

- Homepage with brief introduction and profile image
- List of job entries with thumbnail and short description
- Individual job detail pages
- Django admin interface for managing jobs
- Custom CSS and static images
- PostgreSQL database integration

---

## Built With

- [Python 3.12](https://www.python.org/)
- [Django 5.1](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [python-decouple](https://pypi.org/project/python-decouple/) – for managing environment variables

---

## Project Structure

portfolio/ 
├── jobs/ # Main app containing models, views, templates, static files 
├── portfolio/ # Project settings and routing 
├── templates/ # Base HTML template 
├── static/ # Global static files 
└── manage.py

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio

---

2. **Install dependencies**
```bash
pip install -r requirements.txt

---

3. **Create .env file**
```bash
DJANGO_SECRET_KEY=your-secret-key

---

4. **Set up the database**
### Make sure PostgreSQL is running, then:
```bash
python manage.py makemigrations
python manage.py migrate

---

5. **Run the server**
```bash
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to see the app.

---

## Admin Panel

To access the Django admin interface:

1. **Create a superuser:**
```bash
python manage.py createsuperuser

---

2. **Log in at:**
http://127.0.0.1:8000/admin/

---

## Screens and Content

**Homepage: Displays your photo and a short description.**

**Jobs: Each job is shown with an image and text summary.**

**Job Detail: Clicking a job shows the full image and description.**

**Admin: You can add/edit/delete jobs via Django Admin.**

---

## Environment Variables

**This project uses python-decouple for secure config handling. You'll need:**

- DJANGO_SECRET_KEY – your Django secret key

- PostgreSQL credentials set in settings.py (for development)

---

## License

**This project is for educational purposes and personal portfolio use. No license is currently attached.**