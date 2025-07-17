FROM python:3.11.4-slim-buster

ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_PASSWORD

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
RUN DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME} DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} DJANGO_SUPERUSER_EMAIL= python manage.py createsuperuser --noinput
