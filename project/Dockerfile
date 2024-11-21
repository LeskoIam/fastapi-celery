# pull official base image
FROM python:3.13-slim-bookworm

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copy project
COPY . .
COPY ./requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -U -r requirements.txt
