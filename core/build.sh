#!/usr/bin/env bash
set -o errexit

python manage.py makemigrations
python manage.py migrate