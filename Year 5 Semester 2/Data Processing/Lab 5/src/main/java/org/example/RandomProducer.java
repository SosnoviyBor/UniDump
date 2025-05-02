package org.example;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;
import java.util.Random;

public class RandomProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        final Random random = new Random();

        try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {
            while (true) {
                String key = "key";
                String value = String.valueOf(random.nextInt());

                ProducerRecord<String, String> record = new ProducerRecord<>("lab5-data", key, value);

                producer.send(record, (RecordMetadata metadata, Exception exception) -> {
                    if (exception == null) {
                        System.out.printf("Sent record(key=%s value=%s)\n", key, value);
                    } else {
                        exception.printStackTrace();
                    }
                });

                producer.flush();

                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        }
    }
}