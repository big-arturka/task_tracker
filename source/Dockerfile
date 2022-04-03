FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
RUN pip install djangorestframework-simplejwt
COPY . /app/