from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "lab-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",  # start from the latest message
    enable_auto_commit=True,  # auto commit the offsets
    value_deserializer=lambda x: x.decode("utf-8"),  # convert bytes to string
    key_deserializer=lambda x: x.decode("utf-8"),  # convert bytes to string
)

for message in consumer:
    print(f"Consumed message: {message.value}")
