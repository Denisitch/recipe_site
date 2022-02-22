FROM python:3.8
MAINTAINER Denis Osyushkin

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src