import java.util.ArrayList;

public class Model {
    private final ArrayList<Element> list;
    private final boolean do_output;
    double tnext, tcurr;

    public Model(ArrayList<Element> elements, boolean do_output) {
        list = elements;
        tnext = 0.0;
        tcurr = tnext;
        this.do_output = do_output;
    }

    public void simulate(double time) {
//        starting message
        System.out.println("There are " + list.size() + " elements in simulation");

        while (tcurr < time) {
//            balance the process' queues
//            since it is written for specific realisation, i couldn't be bothered to make it less hardcoded
//            Process line1 = (Process) list.get(1);
//            Process line2 = (Process) list.get(2);
//            if (line1.getQueue() - line2.getQueue() > line1.swapThreshold) {
//                line1.setQueue(line1.getQueue()-1);
//                line2.setQueue(line2.getQueue()+1);
//                line1.swapCount++;
//                System.out.println("\n>>>     Moved a car from line 1 to line 2!     <<<");
//            } else if (line2.getQueue() - line1.getQueue() > line2.swapThreshold) {
//                line1.setQueue(line1.getQueue()+1);
//                line2.setQueue(line2.getQueue()-1);
//                line2.swapCount++;
//                System.out.println("\n>>>     Moved a car from line 2 to line 1!     <<<");
//            }

//            searching for nearest event
            tnext = Double.MAX_VALUE;
            int eventId = 0;
            for (Element e : list) {
                if (e.getTnext() < tnext) {
//                    current time
                    tnext = e.getTnext();
                    eventId = e.getId();
                }
            }

            if (do_output) System.out.println(String.format(
                "\n"+
                ">>>     Event in %s     <<<\n"+
                ">>>     time: %.4f     <<<",
                list.get(eventId).getName(), tnext));
            for (Element e : list) {
                e.doStatistics(tnext - tcurr);
            }
//            updating the current time
            tcurr = tnext;
            for (Element e : list) {
                e.setTcurr(tcurr);
            }
//            call the outAct()
            list.get(eventId).outAct();
            for (Element e : list) {
                if (e.getTnext() == tcurr) {
                    e.outAct();
                }
            }
            if (do_output) printInfo();
        }
        if (do_output) printResult();
//        System.out.println("The simulation has ended!\n");
    }

    public void printInfo() {
        for (Element e : list) {
            e.printInfo();
        }
    }

    public void printResult() {
        System.out.println("\n-------------RESULTS-------------");
        for (Element e : list) {
            e.printResult();
            if (e instanceof Process) {
                Process p = (Process) e;
                System.out.println(String.format(
                        "Mean length of queue = %.3f\n" +
                        "Failure probability = %.3f\n",
                        p.getMeanQueue() / tcurr,
                        p.getFailure() / (double) (p.getFailure() + p.getQuantity())));
            } else {
                System.out.println();
            }
        }
    }
}