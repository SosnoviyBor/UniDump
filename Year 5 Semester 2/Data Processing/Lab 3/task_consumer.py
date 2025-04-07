import json

from kafka import KafkaConsumer

import consts

topics = [
    # consts.TOPICS["by year"],
    consts.TOPICS["capacity <10"],
    # consts.TOPICS["capacity 10-100"],
    # consts.TOPICS["capacity >100"],
]
consumer = KafkaConsumer(*topics)


print("Consuming from topics:")
for topic in topics:
    print(f"> {topic}")


i = 1
for msg in consumer:
    print(f"{i} | {json.loads(msg.value)}")
    i += 1
