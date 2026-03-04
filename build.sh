#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python wapproject/manage.py collectstatic --noinput
python wapproject/manage.py migrate
