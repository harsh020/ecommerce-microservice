#!/bin/bash

# Wait for Postgres to start its services
#until psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -U ${POSTGRES_USER} -c 'select 1;' > /dev/null 2>&1; do
#  echo 'Waiting for Postgres to start...'
#  sleep 2
#done

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000