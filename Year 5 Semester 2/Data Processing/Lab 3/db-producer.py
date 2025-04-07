import sqlite3
import json

from kafka import KafkaProducer

import consts

con = sqlite3.connect("lab2.db")
cur = con.cursor()
producer = KafkaProducer(
    bootstrap_servers=consts.BOOTSTRAP_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

for row in cur.execute("SELECT * FROM solar"):
    data = {
        "date": row[0],
        "solar_mwh": row[1],
        "solar_capacity": row[2]
    }
    producer.send(consts.TOPICS["total"], data)
    print(data)

producer.flush()
producer.close()
