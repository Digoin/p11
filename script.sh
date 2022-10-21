#!/bin/bash

source env/bin/activate
pip install -r requirements.txt
python pur_beurre/manage.py migrate
python pur_beurre/manage.py collectstatic --noinput
deactivate
sudo systemctl restart gunicorn