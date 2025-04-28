package org.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.JoinWindows;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.StreamJoined;

import java.time.Duration;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "lab4-task3");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        final StreamsBuilder builder = new StreamsBuilder();
        final ObjectMapper mapper = new ObjectMapper();
        final CountDownLatch latch = new CountDownLatch(1);

        final KStream<String, String> b1Stream = builder.stream("lab4-b1");
        final KStream<String, String> b2Stream = builder.stream("lab4-b2");

        final KStream<String, String> b3Stream = b1Stream.join(
                b2Stream,
                (b1, b2) -> {
                    try {
                        ObjectNode b1Json = (ObjectNode) mapper.readTree(b1);
                        ObjectNode b2Json = (ObjectNode) mapper.readTree(b2);
                        b1Json.setAll(b2Json);
                        return mapper.writeValueAsString(b1Json);
                    } catch (Exception e) {
                        //noinspection CallToPrintStackTrace
                        e.printStackTrace();
                        return null;
                    }
                },
                JoinWindows.ofTimeDifferenceWithNoGrace(Duration.ofSeconds(5)),
                StreamJoined.with(Serdes.String(), Serdes.String(), Serdes.String())
        );
        b3Stream.to("lab4-b3");

        try(KafkaStreams streams = new KafkaStreams(builder.build(), props)) {
            streams.start();
            latch.await();
        }


    }
}