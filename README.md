Enter your database name (YOUR_DB_NAME) and password (YOUR_PASSWORD).

Backend Setup (Django)
1. Create Virtual Environment

```bash
python -m venv post-env

2. Activate Virtual Environment

Windows:

post-env\Scripts\activate

Mac/Linux:

source post-env/bin/activate

3. Install Dependencies
pip install django djangorestframework psycopg2-binary django-cors-headers

4. Create Project
django-admin startproject backend
cd backend

5. Create App
python manage.py startapp backend

Add the app in backend/settings.py:

INSTALLED_APPS = [
    ...
    'backend',
    'rest_framework',
]

6. Database Configuration (PostgreSQL)

Update backend/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR_DB_NAME',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

7. Run Migrations
python manage.py makemigrations
python manage.py migrate

8. Create Superuser
python manage.py createsuperuser

9. Run Backend Server
python manage.py runserver

Backend will run at:

http://127.0.0.1:8000/

-------------------------------------------------------------------------------------------------

## Frontend Setup

1. Install dependencies:
   npm install

2. Start the development server:
   npm run dev

Reference:
https://www.youtube.com/watch?v=-MvulwTbI4E&list=PL7BQ4lqtgECQ5HWarFCgH2RsgGkpQkTeQ&index=5
