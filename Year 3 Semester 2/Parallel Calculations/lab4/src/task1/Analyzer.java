package task1;

import java.util.Map;

public class Analyzer {

    public double getAverage(Map<Integer, Integer> wordFrequency) {
        return this.getAverage(wordFrequency, this.getSum(wordFrequency));
    }

    private double getAverage(Map<Integer, Integer> wordFrequency, long total) {
        return (double) wordFrequency
                .entrySet()
                .stream()
                .mapToLong(entry -> (long) entry.getKey() * entry.getValue())
                .sum() / total;
    }

    private long getSum(Map<Integer, Integer> wordFrequency) {
        return wordFrequency
                .values()
                .stream()
                .mapToInt(value -> value)
                .sum();
    }

    public double getDispersion(Map<Integer, Integer> wordFrequency) {
        final long sum = this.getSum(wordFrequency);
        final double average = getAverage(wordFrequency, sum);

        return (double) wordFrequency
                .entrySet()
                .stream()
                .mapToLong(entry -> (long) entry.getKey() * entry.getKey() * entry.getValue())
                .sum() / sum - Math.pow(average, 2);
    }

    public double getStd(Map<Integer, Integer> wordFrequency) {
        return Math.sqrt(getDispersion(wordFrequency));
    }
}
