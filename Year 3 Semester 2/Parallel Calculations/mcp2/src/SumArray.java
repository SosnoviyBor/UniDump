import mpi.*;

public class SumArray{
    public static void main(String[] args) {
        MPI.Init(args);
        int rank = MPI.COMM_WORLD.Rank();

        int[] globalSum = new int[1];
        int[] sum = new int[1];

        int[] arr = {1,2,3,4,5};
        int localSum = 0;

        for (int value : arr) {
            localSum += value;
        }
        MPI.COMM_WORLD.Reduce(new int[]{localSum}, 0, globalSum, 0, 1, MPI.INT, MPI.SUM, 0);
        MPI.COMM_WORLD.Bcast(globalSum, 0, 1, MPI.INT, 0);
        sum[0] = globalSum[0];

        System.out.println("Process " + rank + " resulted sum=" + sum[0]);
        MPI.Finalize();
    }
}