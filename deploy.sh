#!/bin/bash

# Set environment variables for superuser creation
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=adminpassword

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser without interactive input
python manage.py createsuperuser --noinput

# Start the Django development server
python manage.py runserver 0.0.0.0:80
