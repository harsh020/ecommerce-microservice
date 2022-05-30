FROM python:3.8

COPY requirements.txt /app/
COPY requirements/* /app/requirements/

RUN pip install -r /app/requirements.txt
#COPY . /app

WORKDIR /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
