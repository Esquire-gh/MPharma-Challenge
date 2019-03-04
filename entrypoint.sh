#!/bin/bash

#run migrations
python manage.py makemigrations
python manage.py migrate

#run application
python manage.py runserver 0.0.0.0:8000