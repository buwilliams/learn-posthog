# Django

## Start here

If, like me, you haven't worked with Django before, the best place to start with is 
[Writing your first Django app](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) 
from the official Django website. This gives you a quick understanding of the major 
parts of Django without needing to read an entire book to get it.

## Useful Django commands

- `django-admin startproject mysite` - creates Django project
- `python manage.py runserver` - starts Django web server (optionally add a port at the end `8080`)
- `python manage.py startapp polls` - creates Django app in project
- `python manage.py makemigrations polls` - creates migration scripts in migrations folder
- `python manage.py sqlmigrate polls 0001` - shows SQL that will run for this migration but doesn't perform it
- `python manage.py migrate` - performs all migrations
- `python manage.py shell` - puts you in a Django ORM shell to play with the models on the command-line
- `python manage.py createsuperuser` - creates super user for django admin app which comes by default with all Django projects, url `/admin`
- `python manage.py test polls` - run tests for polls app

## Reading Django code