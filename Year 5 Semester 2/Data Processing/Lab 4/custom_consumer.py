import json

from kafka import KafkaConsumer

import utils.consts as consts

topics = [
    consts.TOPICS["b1"],
    # consts.TOPICS["b2"],
    # consts.TOPICS["b3"],
]
consumer = KafkaConsumer(*topics)


print("Consuming from topics:")
for topic in topics:
    print(f"> {topic}")


i = 1
for msg in consumer:
    print(f"{i} | key: {int.from_bytes(msg.key)}, value: {json.loads(msg.value)}")
    i += 1
