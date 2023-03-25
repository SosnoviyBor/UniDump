public class States {
    private static Object lock = new Object();
    private static String state = "s";

    public static void main(String[] args) {
        Thread threadA = new Thread(() -> {
            while (true) {
                synchronized (lock) {
                    if (state.equals("s")) {
                        state = "z";
                    } else {
                        state = "s";
                    }
                    lock.notifyAll();
                }
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        Thread threadB = new Thread(() -> {
            while (true) {
                synchronized (lock) {
                    while (!state.equals("s")) {
                        try {
                            long countdown = 100;
                            while (countdown > 0) {
                                System.out.println("Countdown: " + countdown);
                                countdown--;
                                Thread.sleep(1);
                            }
                            lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                    System.out.println("State switched to 's', resuming Thread B.");
                }
            }
        });

        threadA.start();
        threadB.start();
    }
}
