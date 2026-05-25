#!/bin/bash
echo "A aguardar MySQL..."
while ! nc -z db 3306; do sleep 1; done
python manage.py migrate
python manage.py loaddata social/fixtures/vulnerabilidades.json --ignore
python manage.py runserver 0.0.0.0:8000