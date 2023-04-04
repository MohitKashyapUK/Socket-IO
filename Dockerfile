# Dockerfile for Flask application
FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3-pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-w", "1", "--threads", "100", "main:app"]

# Dockerfile for Telegram bot API
FROM aiogram/telegram-bot-api:latest

ENV TELEGRAM_API_ID="27269597"
ENV TELEGRAM_API_HASH="ef91ab7dfb77baea3d5f87e5d6cd5744"

VOLUME /var/lib/telegram-bot-api

EXPOSE 8081

CMD ["telegram-bot-api"]
