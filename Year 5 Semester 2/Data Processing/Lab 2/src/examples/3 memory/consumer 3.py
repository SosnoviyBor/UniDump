from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'lab-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: x.decode('utf-8'),
    key_deserializer=lambda x: x.decode('utf-8'),
    max_poll_records=1000,  # fetch up to 1000 records in each poll
    fetch_max_bytes=52428800,  # 50 MB per fetch
    fetch_min_bytes=10000  # minimum 10 KB of data to fetch
)

for message in consumer:
    print(f"Consumed message: {message.value}")