from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'separate-topic',
    bootstrap_servers='localhost:9092',
    group_id="separate-group",
    auto_offset_reset='earliest',  # start consuming from the earliest message
    enable_auto_commit=False,  # disable auto commit
    value_deserializer=lambda x: x.decode('utf-8'),
    key_deserializer=lambda x: x.decode('utf-8')
)

for message in consumer:
    print(f"Consumed message: {message.value}")
    
    # manually commit offsets
    consumer.commit()