import java.util.concurrent.ArrayBlockingQueue;

public class ABC {
    public static void main(String[] args) {
        ArrayBlockingQueue<Object> buffer = new ArrayBlockingQueue<>(10); // буфер обмеженої довжини

        Thread producer = new Thread(() -> { // Потік А
            try {
                for (int i = 0; i < 20; i++) { // створення та додавання об'єктів
                    Object obj = new Object();
                    buffer.put(obj);
                    System.out.println("Producer added: " + obj);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread consumer1 = new Thread(() -> { // Потік С
            try {
                while (true) { // вилучення об'єктів
                    Object obj = buffer.take();
                    System.out.println("Consumer 1 removed: " + obj);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread consumer2 = new Thread(() -> { // Потік В
            try {
                while (true) { // вилучення об'єктів
                    Object obj = buffer.take();
                    System.out.println("Consumer 2 removed: " + obj);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        producer.start(); // запуск потоку А
        consumer1.start(); // запуск потоку С
        consumer2.start(); // запуск потоку В
    }
}
