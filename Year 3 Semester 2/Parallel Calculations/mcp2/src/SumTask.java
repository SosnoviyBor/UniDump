import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class SumTask extends RecursiveTask<Long> {
    private static final int THRESHOLD = 10000; // мінімальний розмір підзадачі для паралельної обробки
    private final int[] array;
    private final int low;
    private final int high;

    public SumTask(int[] array, int low, int high) {
        this.array = array;
        this.low = low;
        this.high = high;
    }

    @Override
    protected Long compute() {
        if (high - low <= THRESHOLD) { // якщо розмір підзадачі менший або дорівнює THRESHOLD, обчислюємо суму послідовно
            long sum = 0;
            for (int i = low; i < high; ++i) {
                sum += array[i];
            }
            return sum;
        } else { // якщо розмір підзадачі більший THRESHOLD, розділяємо задачу на дві частини і запускаємо їх паралельно
            int mid = low + (high - low) / 2;
            SumTask left = new SumTask(array, low, mid);
            SumTask right = new SumTask(array, mid, high);
            left.fork();
            long rightResult = right.compute();
            long leftResult = left.join();
            return leftResult + rightResult;
        }
    }

    public static void main(String[] args) {
        int[] array = new int[1000000]; // ініціалізуємо масив довільними значеннями
        for (int i = 0; i < array.length; ++i) {
            array[i] = i + 1;
        }
        ForkJoinPool pool = new ForkJoinPool();
        SumTask task = new SumTask(array, 0, array.length);
        long result = pool.invoke(task); // запускаємо обчислення суми
        System.out.println("Sum: " + result);
    }
}
