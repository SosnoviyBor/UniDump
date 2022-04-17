from datetime import datetime

import time
import pika

time.sleep(40)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='broker'))
channel = connection.channel()

channel.queue_declare(queue='date')

while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    channel.basic_publish(exchange='', routing_key='date', body=dt_string)
    print(" Sent"+dt_string)
    time.sleep(3)
connection.close()