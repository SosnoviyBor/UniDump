import mpi.*;

import java.util.Arrays;

public class MatrixThingy {
    public static void main(String[] args) {
        MPI.Init(args);

        final int rank = MPI.COMM_WORLD.Rank();
        final int size = MPI.COMM_WORLD.Size();

        final int rows = 4;
        int[][] A = {
                {1, 2, 3, 4},
                {1, 6, 7, 8},
                {1, 10, 11, 12},
                {1, 14, 15, 16}
        };
        int[][] B = {
                {16, 15, 14, 13},
                {12, 11, 10, 9},
                {8, 7, 6, 5},
                {4, 3, 2, 1}
        };
        int[] C = new int[rows];
        int[] globalC = new int[rows];

        final int rowsPerProcess = rows / size;
        final int n = rank * rowsPerProcess;
        final int m = n + rowsPerProcess;

        for (int i = n; i < m; i++) {
            int rowSumA = 0;
            int rowSumB = 0;
            for (int j = 0; j < rows; j++) {
                rowSumA += A[i][j];
                rowSumB += B[i][j];
            }
            C[i] = rowSumA + rowSumB;
        }

        MPI.COMM_WORLD.Allgather(C, n, rowsPerProcess, MPI.INT, globalC, n, rowsPerProcess, MPI.INT);

        if (rank == 0) {
            System.out.println(Arrays.toString(globalC));
        }

        MPI.Finalize();
    }
}
