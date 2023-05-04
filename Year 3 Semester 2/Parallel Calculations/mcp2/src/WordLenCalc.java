import java.util.ArrayList;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class WordLenCalc extends RecursiveTask<Double> {
    private final ArrayList<String> list;
    final int THRESHOLD = 1000;

    public WordLenCalc(ArrayList<String> list) {
        this.list = list;
    }

    @Override
    protected Double compute() {
        if (list.size() <= THRESHOLD) {
            return calculateAverageLength();
        } else {
            int mid = list.size() / 2;
            WordLenCalc left = new WordLenCalc(new ArrayList<>(list.subList(0, mid)));
            WordLenCalc right = new WordLenCalc(new ArrayList<>(list.subList(mid, list.size())));

            left.fork();
            double rightResult = right.compute();
            double leftResult = left.join();

            return (leftResult + rightResult) / 2;
        }
    }

    private double calculateAverageLength() {
        double totalLength = 0;
        for (String word : list) {
            totalLength += word.length();
        }
        return totalLength / list.size();
    }

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("please");
        list.add("give");
        list.add("me");
        list.add("a");
        list.add("good");
        list.add("mark");
        list.add("on");
        list.add("this");
        list.add("test");
        list.add(":)");

        ForkJoinPool forkJoinPool = new ForkJoinPool();
        WordLenCalc calculator = new WordLenCalc(list);

        double result = forkJoinPool.invoke(calculator);
        System.out.println("Average word length: " + result);
    }
}
