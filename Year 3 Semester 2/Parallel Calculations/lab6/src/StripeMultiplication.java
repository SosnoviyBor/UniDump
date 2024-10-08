import mpi.MPI;

public class StripeMultiplication {

    private static final int MASTER = 0;
    private static final boolean DOPRINT = false;
    private static final int MATRIXSIZE = 2000;
    private static final int MAXVAL = 100;

    public static void main(String[] args) {

//        only for testing
//        int[] matrixSizes = {1000, 2000, 3000};
//        for (int MATRIXSIZE : matrixSizes) {

        int[][] matrixA = Utils.generateRandomMatrix(MATRIXSIZE, MAXVAL);
        int[][] matrixB = Utils.generateRandomMatrix(MATRIXSIZE, MAXVAL);
        int[][] matrixC = new int[MATRIXSIZE][MATRIXSIZE];

        MPI.Init(args);

        final int size = MPI.COMM_WORLD.Size();
        final int rank = MPI.COMM_WORLD.Rank();
        final int workerCount = size - 1;

        /* MASTER */
        if (rank == MASTER) {
            System.out.println("Started program with " + size + " processes!");
            if (DOPRINT) {
                System.out.println(String.format(
                        "------------------------------------------- \n" +
                        "   Matrix A \n" +
                        "%s \n" +
                        "------------------------------------------- \n" +
                        "   Matrix B \n" +
                        "%s",
                        Utils.matrixToString(matrixA),
                        Utils.matrixToString(matrixB)));
            }

            final long start = System.nanoTime();

            final int[] rows = new int[workerCount];
            final int[] offsets = new int[workerCount];
            final int averageRow = MATRIXSIZE / workerCount;
            int extra = MATRIXSIZE % workerCount;
            int offset = 0;

            for (int i = 1; i < workerCount + 1; i++) {
                final int rowsPerProcess = averageRow + (extra > 0 ? 1 : 0);

                rows[i - 1] = rowsPerProcess;
                offsets[i - 1] = offset;

                if (rowsPerProcess == 0)
                    break;

                MPI.COMM_WORLD.Send(new int[]{rowsPerProcess}, 0, 1, MPI.INT, i, Utils.FIRST_ROWS_NUM_TAG);
                MPI.COMM_WORLD.Send(matrixA, offset, rowsPerProcess, MPI.OBJECT, i, Utils.FIRST_MATRIX_TAG);
                MPI.COMM_WORLD.Send(matrixB, 0, MATRIXSIZE, MPI.OBJECT, i, Utils.SECOND_MATRIX_TAG);

                extra--;
                offset += rowsPerProcess;
            }
            for (int i = 1; i < workerCount + 1; i++) {
                MPI.COMM_WORLD.Recv(matrixC, offsets[i - 1], rows[i - 1], MPI.OBJECT, i, Utils.RES_TAG);
            }

            final long finish = System.nanoTime();

            if (DOPRINT) {
                System.out.println(
                        "------------------------------------------- \n" +
                        "   Result");
                for (int i = 0; i < MATRIXSIZE; i++) {
                    System.out.println();
                    for (int j = 0; j < MATRIXSIZE; j++) {
                        System.out.printf("%d ", matrixC[i][j]);
                    }
                }
                System.out.println();
            }

            System.out.println(String.format(
                    "------------------------------------------- \n" +
                    "Result matrix size: %dx%d \n" +
                    "Elapsed time: %.2fms",
                    MATRIXSIZE, MATRIXSIZE,
                    (finish - start) / 1_000_000D));

        /* WORKER */
        } else {
            int[] rowsPerProcess = new int[1];

            MPI.COMM_WORLD.Recv(rowsPerProcess, 0, 1, MPI.INT, MASTER, Utils.FIRST_ROWS_NUM_TAG);

            int[][] rowsA = new int[rowsPerProcess[0]][MATRIXSIZE];
            int[][] rowsB = new int[MATRIXSIZE][MATRIXSIZE];
            int[][] result = new int[rowsPerProcess[0]][MATRIXSIZE];

            MPI.COMM_WORLD.Recv(rowsA, 0, rowsPerProcess[0], MPI.OBJECT, MASTER, Utils.FIRST_MATRIX_TAG);
            MPI.COMM_WORLD.Recv(rowsB, 0, MATRIXSIZE, MPI.OBJECT, MASTER, Utils.SECOND_MATRIX_TAG);

            for (int i = 0; i < rowsA.length; i++) {
                for (int j = 0; j < rowsB[0].length; j++) {
                    int sum = 0;
                    for (int k = 0; k < rowsB.length; k++) {
                        sum += rowsA[i][k] * rowsB[k][j];
                    }
                    result[i][j] = sum;
                }
            }

            MPI.COMM_WORLD.Send(result, 0, result.length, MPI.OBJECT, MASTER, Utils.RES_TAG);
        }

        MPI.Finalize();
//    }
    }
}
