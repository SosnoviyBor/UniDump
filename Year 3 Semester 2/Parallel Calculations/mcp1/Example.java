import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Example {

    private Lock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();
    private int count = 0;

    public void increment() {
        lock.lock();
        try {
            count++;
            condition.signalAll();
        } finally {
            lock.unlock();
        }
    }

    public void decrement() throws InterruptedException {
        lock.lock();
        try {
            while (count == 0) {
                condition.await();
            }
            count--;
        } finally {
            lock.unlock();
        }
    }
}
