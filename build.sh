#!/usr/bin/env bash

set -o errexit  # exit on error

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py collectstatic --no-input --clear
python manage.py migrate
