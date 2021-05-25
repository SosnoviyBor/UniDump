FROM python:3

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY . /usr/src/app/


RUN pip install pika

EXPOSE 8080


CMD ["python", "Sender.py"]