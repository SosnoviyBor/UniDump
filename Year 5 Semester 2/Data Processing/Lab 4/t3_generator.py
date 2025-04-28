import random
import json
import time

from kafka import KafkaProducer

import utils.consts as consts
from utils.random_date import random_date
from utils.progress_bar import print_progress_bar


producer = KafkaProducer(
    bootstrap_servers=consts.BOOTSTRAP_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    key_serializer=lambda k: bytes(k)
)


entries = 100

print_progress_bar(0, entries)
for i in range(entries):
    producer.send(
        topic=consts.topics.B1,
        key=i,
        value={
            "id": i,
            "date": random_date(
                "2009-02-23", "2021-06-01", "%Y-%m-%d", random.random()
            ),
        },
    )
    producer.send(
        topic=consts.topics.B2,
        key=i,
        value={
            "id": i,
            "solar_mwh": random.uniform(323.579662605013, 12.1098796796944),
        },
    )
    # producer.send(
    #     topic=consts.topics.B3,
    #     value={
    #         "id": i,
    #         "solar_capacity": round(random.uniform(500, 3.6), 1),
    #     },
    # )
    producer.flush(3)
    print_progress_bar(i + 1, entries)
    time.sleep(0.001)

producer.flush()
producer.close()
