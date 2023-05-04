import mpi.*;
import java.util.concurrent.ThreadLocalRandom;

public class TemperatureThingy {
    public static void main(String[] args) throws MPIException {
        MPI.Init(args);
        final int rank = MPI.COMM_WORLD.Rank();
        final int size = MPI.COMM_WORLD.Size();

        if (size < 4) {
            System.out.println("This program requires at least 4 processes");
            MPI.Finalize();
            return;
        }

        if (rank == 3) {
            // process #3 - sender
            double[] sentTempData = new double[30];
            for (int i = 0; i < sentTempData.length; i++) {
                sentTempData[i] = ThreadLocalRandom.current().nextDouble(-20, 30);
            }

            for (int i = 0; i < size; i++) {
                // send data to everyone except process #3
                if (i != 3) {
                    MPI.COMM_WORLD.Send(sentTempData, 0, sentTempData.length, MPI.DOUBLE, i, 0);
                }
            }
        } else {
            // processes except #3 - receivers
            double[] recvTempData = new double[30];
            MPI.COMM_WORLD.Recv(recvTempData, 0, recvTempData.length, MPI.DOUBLE, 3, 0);

            // print is not working as good as i wanted, but whatever
            System.out.println("Process " + rank + " received next temperature data from process 3: ");
            for (double temp : recvTempData) {
                System.out.printf("%.2f; ", temp);
            }
            System.out.println();

            MPI.Finalize();
        }
    }
}
