from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,   # convert keys to byte format
    value_serializer=str.encode  # convert values to byte format
)

producer.send('lab-topic', key='key1', value='value1')

producer.flush()
producer.close()