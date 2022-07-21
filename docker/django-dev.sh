#!/usr/bin/env bash
set -e

python manage.py makemigrations authentication
python manage.py migrate authentication
python manage.py migrate

mkdir -p /data/public

python manage.py runserver --settings=inside.settings 0.0.0.0:8000
