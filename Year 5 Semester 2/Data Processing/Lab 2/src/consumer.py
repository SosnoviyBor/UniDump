import json

import kafka

import utils.consts as consts

consumer = kafka.KafkaConsumer(consts.TOPIC)

for msg in consumer:
    print(json.loads(msg.value))
