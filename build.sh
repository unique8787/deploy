#!/usr/bin/env bash
set .o errrexit

pip install -r requirements.txt
cd bms

python manage.py migrate
