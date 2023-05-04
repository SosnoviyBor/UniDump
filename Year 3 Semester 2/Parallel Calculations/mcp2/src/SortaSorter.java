import mpi.*;

import java.util.Arrays;

public class SortaSorter {
    public static void main(String[] args) {
        MPI.Init(args);

        final int rank = MPI.COMM_WORLD.Rank();
        final int size = MPI.COMM_WORLD.Size();

        String[] A = {"apple", "banana", "cherry", "date", "elderberry", "fig"};
        final int n = A.length / size;
        final int m = A.length % size;

        if (rank == 0) {
            // Головний процес
            for (int i = 1; i < size; i++) {
                String[] buf = new String[(i <= m) ? (n + 1) : n];
                System.arraycopy(A, i * n + Math.min(i, m), buf, 0, buf.length);
                MPI.COMM_WORLD.Send(buf, 0, buf.length, MPI.OBJECT, i, 0);
            }

            String[] result = new String[1];

            for (int i = 1; i < size; i++) {
                MPI.COMM_WORLD.Recv(result, 0, result.length, MPI.OBJECT, i, 0);
                System.out.println("Process #" + i + " returned word '" + result[0] + "'");
            }
        } else {
            // Процес-працівник
            String[] buf = new String[(rank <= A.length % size) ? (A.length / size + 1) : (A.length / size)];
            MPI.COMM_WORLD.Recv(buf, 0, buf.length, MPI.OBJECT, 0, 0);

            Arrays.sort(buf);
            String[] result = {buf[0]};

            MPI.COMM_WORLD.Send(result, 0, result.length, MPI.OBJECT, 0, 0);
        }

        MPI.Finalize();
    }
}
