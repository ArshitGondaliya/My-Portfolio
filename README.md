# Arshit Gondaliya Portfolio

A database-driven personal portfolio built with Django, SQLite, HTML, CSS, and vanilla JavaScript.

## Windows setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the portfolio and `http://127.0.0.1:8000/admin/` for content management.

## Admin content

The first migration seeds the resume-backed profile, skills, internships, projects, education, and social links. Update these records from Django admin without editing templates. Upload replacements for the three profile image fields in **Portfolio profile**. Project images can be uploaded from **Projects**.

Contact form submissions are saved as `ContactMessage` records and can be marked read/unread in admin.

## Configuration

Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` as environment variables for deployment. Run `python manage.py collectstatic` and configure a production WSGI/ASGI host. SQLite is suitable for local use; move to a managed database when deploying at scale.
