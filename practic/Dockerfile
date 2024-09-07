FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
WORKDIR /practic
COPY requirements.txt /practic/
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .     


EXPOSE 7000

