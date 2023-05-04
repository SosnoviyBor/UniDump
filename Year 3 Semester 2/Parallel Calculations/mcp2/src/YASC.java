import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class YASC extends RecursiveTask<Double> {
    // Yet Another Sum Calculator
    private static final int THRESHOLD = 1000;
    private final double[] numbers;
    private final int start;
    private final int end;

    public YASC(double[] numbers, int start, int end) {
        this.numbers = numbers;
        this.start = start;
        this.end = end;
    }

    @Override
    protected Double compute() {
        int length = end - start;
        if (length <= THRESHOLD) {
            return computeSequentially();
        }
        YASC leftTask = new YASC(numbers, start, start + length/2);
        YASC rightTask = new YASC(numbers, start + length/2, end);
        leftTask.fork();
        double rightResult = rightTask.compute();
        double leftResult = leftTask.join();
        return leftResult + rightResult;
    }

    private double computeSequentially() {
        double sum = 0;
        for (int i = start; i < end; i++) {
            sum += numbers[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        final int NUM_AMOUNT = 10000;

        ForkJoinPool forkJoinPool = new ForkJoinPool(10);
        double[] numbers = new double[NUM_AMOUNT];
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = i;
        }

        double sum = forkJoinPool.invoke(new YASC(numbers, 0, numbers.length));
        System.out.println("Sum: " + sum);
        System.out.println("(kinda a lot)");
    }
}
