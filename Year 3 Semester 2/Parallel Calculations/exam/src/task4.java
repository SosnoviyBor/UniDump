import mpi.MPI;

import java.util.Arrays;
import java.util.Random;

public class task4 {

    final static int MASTER = 0;
    final static int WORKER_COUNT = 15;
    final static int ARR_SIZE = 100;

    public static void main(String[] args) {

        MPI.Init(args);

        final int rank = MPI.COMM_WORLD.Rank();
        final int size = MPI.COMM_WORLD.Size();

        final int chunk_size = ARR_SIZE / 10;
//        master
        if (rank == MASTER) {
            int offset = 0;

            int[] inp_arr = new int[ARR_SIZE];
            int[] out_arr = new int[chunk_size];
            Random random = new Random();
            for (int i = 0; i < ARR_SIZE; i++) {
                inp_arr[i] = random.nextInt(100);
            }
            System.out.println("Input array: " + Arrays.toString(inp_arr));

            for (int i = 1; i < WORKER_COUNT + 1; i++) {
                MPI.COMM_WORLD.Send(inp_arr, offset, chunk_size, MPI.OBJECT, i, 0);
                offset += chunk_size;
            }
            for (int i = 1; i < WORKER_COUNT + 1; i++) {
                MPI.COMM_WORLD.Recv(out_arr, 0, 1, MPI.INT, i, 0);
            }
            System.out.println("Result: " + Arrays.toString(out_arr));

//        worker
        } else {
            int[] inp_arr = new int[chunk_size];
            int temp = 0;

            MPI.COMM_WORLD.Recv(inp_arr, 0, chunk_size, MPI.OBJECT, MASTER, 0);

//            bubble sort
            for (int i = 0; i < inp_arr.length; i++){
                for (int j = 1; j < (inp_arr.length - i); j++){
                    if (inp_arr[j - 1] > inp_arr[j]){
                        temp = inp_arr[j - 1];
                        inp_arr[j - 1] = inp_arr[j];
                        inp_arr[j] = temp;
                    }
                }
            }

            int[] largest = {inp_arr[0]};
            MPI.COMM_WORLD.Send(largest, 0, 1, MPI.INT, MASTER, 0);
        }

//        СКАЗАТИ ПРО ЦЕ
        MPI.Finalize();
    }
}
