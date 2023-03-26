package task5;

public class Main {
    public static void main(String[] args) {
        // unordered
//        ThreadedPrint thread1 = new ThreadedPrint("-");
//        ThreadedPrint thread2 = new ThreadedPrint("|");
//        thread1.start();
//        thread2.start();

        // ordered
        TheCoolerThreadedPrint order_thread1 = new TheCoolerThreadedPrint("-");
        TheCoolerThreadedPrint order_thread2 = new TheCoolerThreadedPrint("|");
        order_thread1.start();
        order_thread2.start();

    }
}

