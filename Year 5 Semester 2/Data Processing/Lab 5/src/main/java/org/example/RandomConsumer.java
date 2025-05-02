package org.example;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.Metric;
import org.apache.kafka.common.MetricName;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.time.Duration;
import java.util.*;

public class RandomConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "lab5-consumer");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

        HashSet<String> relevantMetrics = new HashSet<>();
        relevantMetrics.add("records-lag");
        relevantMetrics.add("bytes-consumed-rate");
        relevantMetrics.add("records-consumed-rate");
        boolean consumerConnected = false;

        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
            consumer.subscribe(Collections.singleton("lab5-data"));
            Map<MetricName, ? extends Metric> metrics = consumer.metrics();

            while (true) {
                consumer.poll(Duration.ofSeconds(1));
                if (consumerConnected) {
                    System.out.println("\n========== Metrics ==========");
                }

                for (Map.Entry<MetricName, ? extends Metric> entry : metrics.entrySet()) {
//                    System.out.printf("Metric: %s = %s%n", entry.getKey().name(), entry.getValue().metricValue());}
                    MetricName name = entry.getKey();
                    String metricName = name.name();
                    String group = name.group();

                    if (
                            group.equals("consumer-fetch-manager-metrics")
                            && relevantMetrics.contains(metricName)
                            && name.tags().containsKey("topic")
                    ) {
                        System.out.printf("[%s] %s = %s%n", group, metricName, entry.getValue().metricValue());
                        consumerConnected = true;
                    }
                }
            }
        }
    }
}
