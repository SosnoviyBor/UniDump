import telebot
import datetime
import time
import pika, sys, os

time.sleep(40)
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='broker'))
    bot = telebot.TeleBot('1862144419:AAE75qwTYtnAsYqckKMkuTZ1gHRLx1XiFPw')
    channel = connection.channel()
    channel.queue_declare(queue='date')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        bot.send_message(448565207, body)


    channel.basic_consume(queue='date', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)