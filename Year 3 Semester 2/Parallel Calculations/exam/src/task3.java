import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class task3 {

    final static int POOL_SIZE = 10;
    final static int INC_COUNT = 100;
    final static int DEC_COUNT = 10;
    final static int ITER_COUNT = 3;

    static AtomicInteger counter = new AtomicInteger(0);

    static class CounterThread extends Thread {
        private final int type;
        private final int iter_count;

        public CounterThread (int type, int iter_count) {
            this.type = type;
            this.iter_count = iter_count;
        }

        @Override
        public void run() {
            for (int i = 0; i < iter_count; i++) {
                try {
                    switch (type) {
                        case 1 -> inc();
                        case 2 -> sub(10);
                    }
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        private void inc() {
            final int val = counter.incrementAndGet();
            System.out.println("Current value of counter is " + val);
        }

        private void sub(int amount) {
            for (int i = 0; i < amount; i++) { counter.decrementAndGet(); }
        }
    }

    public static void main(String[] args) throws InterruptedException {
        final ExecutorService pool = Executors.newFixedThreadPool(POOL_SIZE);
//        create incrementer threads
        for (int i = 0; i < INC_COUNT; i++) {
            pool.execute(new CounterThread(1, ITER_COUNT));
        }
//        create substracter threads
        for (int i = 0; i < DEC_COUNT; i++) {
            pool.execute(new CounterThread(2, ITER_COUNT));
        }
        pool.shutdown();
        pool.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    }
}
