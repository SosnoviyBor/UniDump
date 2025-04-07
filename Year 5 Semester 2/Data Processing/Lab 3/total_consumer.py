import json

from kafka import KafkaConsumer

import consts

consumer = KafkaConsumer(topics=consts.TOPICS["total"], auto_offset_reset="earliest")

i = 1
for msg in consumer:
    print(f"{i} | {json.loads(msg.value)}")
    i += 1
