#!/bin/sh

python manage.py makemigrations
python manage.py migrate

gunicorn --bind 0.0.0.0:8000 app.wsgi:application
