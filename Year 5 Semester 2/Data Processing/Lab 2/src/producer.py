import random
import json
import time

import kafka

import utils.consts as consts
from utils.random_date import random_date
from utils.progress_bar import print_progress_bar

producer = kafka.KafkaProducer(
    bootstrap_servers=consts.BOOTSTRAP_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

data = [
    {
        "date": random_date("2009-02-23", "2021-06-01", "%Y-%m-%d", random.random()),
        "solar_mwh": random.uniform(323.579662605013, 12.1098796796944),
        "solar_capacity": round(random.uniform(500, 3.6), 1),
    }
    for _ in range(20)
]

print_progress_bar(0, len(data))
for i in range(len(data)):
    producer.send(consts.TOPIC, data[i])
    print_progress_bar(i + 1, len(data))
    time.sleep(3)
