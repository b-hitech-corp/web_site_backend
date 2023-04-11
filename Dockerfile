# tuto: https://www.geeksforgeeks.org/how-to-dockerize-django-application-for-production-deployement-with-gunicorn-and-nginx/
# Fetching official base image for python
FROM python:3.11-alpine as web

LABEL maintainer="Amadou Barry"

# Setting up the work directory
WORKDIR /home/app/

# Preventing python from writing
# pyc to docker container
ENV PYTHONDONTWRITEBYTECODE 1

# Flushing out python buffer
ENV PYTHONUNBUFFERED 1

# Updating the os
RUN apk update

# Installing mysqlclient dependencies
RUN apk add gcc musl-dev mariadb-connector-c-dev && rm -f /var/cache/apk/*

# Installing python3
RUN apk add python3-dev

# Copying requirement file
COPY ./requirements.txt ./

# Upgrading pip version
RUN pip install --upgrade pip

# Installing dependencies
RUN pip install gunicorn

# Installing dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

# Copying all the files in our project
COPY . .


# tuto: https://blog.devgenius.io/dockerizing-django-application-gunicorn-and-nginx-5a74b250198f
#FROM ubuntu:22.04
#ADD . /app
#WORKDIR /app
#
#RUN apt-get update -y
#RUN apt-get install software-properties-common -y
#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN apt-get install python3.10 -y
#RUN apt-get install python3-pip -y
#RUN python3.10 -m pip install --upgrade setuptools
#RUN apt-get install sudo ufw build-essential libpq-dev libmysqlclient-dev python3.10-dev default-libmysqlclient-dev libpython3.10-dev -y
#RUN python3.10 -m pip install -r requirements.txt
#RUN python3.10 -m pip install psycopg2-binary
#RUN sudo ufw allow 8000
#
#EXPOSE 8000

#Run at the project’s root (same level of manage.py):
#    docker build -t <docker-username>/<project-name>:<tag|latest> .
#    and
#    docker push <docker-username>/<project-name>:<tag|latest>
#
#Run inside the nginx directory created earlier:
#    docker build -t <docker-username>/<nginx-for-project-name>:<tag|latest> .
#    and
#    docker push <docker-username>/<nginx-for-project-name>:<tag|latest>
