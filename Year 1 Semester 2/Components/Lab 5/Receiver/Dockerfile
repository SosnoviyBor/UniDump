FROM python:3

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY . /usr/src/app/
RUN pip install pika
RUN pip install pyTelegramBotAPI

EXPOSE 8080


CMD ["python", "Receiver.py"]