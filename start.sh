#!/usr/bin/env bash
set -o errexit

gunicorn wapproject.wsgi:application --chdir wapproject
