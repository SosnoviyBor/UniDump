from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,
    value_serializer=str.encode,
    batch_size=16384,  # 16 KB batch size
    linger_ms=5,  # wait up to 5ms to batch messages
    buffer_memory=33554432  # 32 MB memory buffer for storing messages
)

producer.send('lab-topic', key='key3', value='value3')

producer.flush()
producer.close()