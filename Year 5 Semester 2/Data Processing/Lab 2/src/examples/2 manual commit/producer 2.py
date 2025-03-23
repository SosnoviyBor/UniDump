from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,
    value_serializer=str.encode,
    acks='all',  # wait for acknowledgment from all brokers
    retries=3,   # retry up to 3 times
    compression_type='gzip',  # use GZIP compression for messages
    linger_ms=10  # wait 10ms to accumulate messages for batching
)

producer.send('separate-topic', key='key2', value='value2')

producer.flush()
producer.close()