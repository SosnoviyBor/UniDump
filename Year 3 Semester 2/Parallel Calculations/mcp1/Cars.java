import java.util.concurrent.Semaphore;

class TrafficLight implements Runnable {
    private final Semaphore semaphore;
    private final int greenDuration = 60; // in milliseconds
    private final int yellowDuration = 10; // in milliseconds
    private final int redDuration = 40; // in milliseconds

    public TrafficLight(Semaphore semaphore) {
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        while (true) {
            try {
                semaphore.acquire();
                System.out.println("Green light is on!");
                Thread.sleep(greenDuration);

                System.out.println("Yellow light is on!");
                Thread.sleep(yellowDuration);

                System.out.println("Red light is on!");
                Thread.sleep(redDuration);

                System.out.println("Yellow light is on!");
                Thread.sleep(yellowDuration);

                semaphore.release();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class Car implements Runnable {
    private final int carNumber;
    private final Semaphore semaphore;

    public Car(int carNumber, Semaphore semaphore) {
        this.carNumber = carNumber;
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        while (true) {
            try {
                semaphore.acquire();
                System.out.println("Car " + carNumber + " is crossing the intersection.");
                Thread.sleep(2);
                semaphore.release();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class Cars {
    public static void main(String[] args) {
        final int numCars = 100;
        final int numIterations = 1000;
        final Semaphore semaphore = new Semaphore(1);
        final Thread trafficLightThread = new Thread(new TrafficLight(semaphore));
        final Thread[] carThreads = new Thread[numCars];

        trafficLightThread.start();
        for (int i = 0; i < numCars; i++) {
            carThreads[i] = new Thread(new Car(i, semaphore));
            carThreads[i].start();
        }

        try {
            for (int i = 0; i < numIterations; i++) {
                Thread.sleep(400);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            trafficLightThread.interrupt();
            for (int i = 0; i < numCars; i++) {
                carThreads[i].interrupt();
            }
        }
    }
}
