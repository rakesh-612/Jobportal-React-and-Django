Enter your database name (YOUR_DB_NAME) and password (YOUR_PASSWORD).

backend>backend>settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR_DB_NAME',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'localhost',
        'PORT': '5500'
    }
}

Reference video
https://www.youtube.com/watch?v=-MvulwTbI4E&list=PL7BQ4lqtgECQ5HWarFCgH2RsgGkpQkTeQ&index=5
