import json

from kafka import KafkaConsumer

import utils.consts as consts

consumer = KafkaConsumer(consts.topics.B3, auto_offset_reset="latest")

for i, msg in enumerate(consumer, start=1):
    print(f"{i} | {json.loads(msg.value)}")
