import json

from kafka import KafkaConsumer

import utils.consts as consts

consumer = KafkaConsumer(consts.TOPIC)

i = 1
for msg in consumer:
    print(f"{i} | {json.loads(msg.value)}")
    i += 1
