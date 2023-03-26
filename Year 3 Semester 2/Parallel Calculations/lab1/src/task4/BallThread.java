package task4;

public class BallThread extends Thread {
    private Ball b;

    public BallThread(Ball ball) {
        b = ball;
    }

    @Override
    public void run() {
        try {
            int max_iterations = 1000;
            for (int i = 1; i < max_iterations; i++) {
                if (b.isStopped()) {
                    while (b.isStopped()) {
                        Thread.sleep(0);
                    }
                }
                b.move();
                System.out.println("Thread name = "
                        + Thread.currentThread().getName());
                Thread.sleep(5);

            }
        } catch (InterruptedException ex) {
        }
    }

}
