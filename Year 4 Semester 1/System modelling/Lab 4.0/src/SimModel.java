import utils.Consts;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Random;

public class SimModel {
    public static void main(String[] args) {
        final int TASK = 2;
        final boolean DO_OUTPUT = true;

        System.out.println("---------- Task #" + TASK + " ----------");

        for (int n = 100; n < 101; n += 100) {
            Element.refreshNextId();
            Create c = new Create(10, 1);
            c.setName("Create");
            c.setDistribution(Consts.DistributionType.exponential);

            ArrayList<Element> list = new ArrayList<>();
            list.add(c);

            switch (TASK) {
                case 1 -> {
                    Element previousElement = c;
                    for (int i = 0; i < n; i++) {
                        Process p = new Process(10, 1, Integer.MAX_VALUE);
                        p.setName("Processor #" + i);
                        p.setDistribution(Consts.DistributionType.exponential);
                        previousElement.setNextElement(p);
                        list.add(p);
                        previousElement = p;
                    }
                }
                case 2 -> {
                    for (int i = 0; i < n; i++) {
                        Process p = new Process(10, 1, Integer.MAX_VALUE);
                        p.setName("Processor #" + i);
                        p.setDistribution(Consts.DistributionType.exponential);

                        Element randomElement = list.get(new Random().nextInt(list.size()));
                        if (randomElement.getNextElementQueue() == null)
                            randomElement.setNextElementQueue(new PriorityQueue<>());
                        randomElement.getNextElementQueue().add(new QueueElement(p, 0));

                        list.add(p);
                    }
                }
            }

//            for (int i = 1; i < list.size(); i++) {
//                list.get(i).inAct();
//            }

            double TIME = 10_000.0;
            Model model = new Model(list, DO_OUTPUT);
            System.out.println(">>>    Loop #" + n / 100 + "     <<<");
            long startTime = System.currentTimeMillis();
            model.simulate(TIME);
            long endTime = System.currentTimeMillis();
            System.out.println("Time spent simulating: " + (endTime - startTime) / 1_000.0 + "s\n");
        }
    }
}
