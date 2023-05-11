package task2;

import task2.models.Matrix;
import task2.models.Result;

class Tester {
    public static void main(String[] args) {

        final boolean accuracyMode = false;

        if (accuracyMode) {
            /* accuracy test */
            final Matrix m1 = new Matrix(new int[][] {
                    {1, 2, 3, 4},
                    {5, 6, 7, 8},
                    {9, 10, 11, 12},
                    {13, 14, 15, 16}
            });
            final Matrix m2 = new Matrix(new int[][] {
                    {16, 15, 14, 13},
                    {12, 11, 10, 9},
                    {8, 7, 6, 5},
                    {4, 3, 2, 1}
            });
            System.out.println("    Sequential algorithm");
            MultiplySequential.multiply(m1, m2).getMatrix().print();

            System.out.println("\n    Fox algorithm");
            MultiplyFox.multiply(m1, m2, 16).getMatrix().print();

            System.out.println("\n    ForkJoin algorithm");
            MultiplyForkJoin.multiply(m1, m2, 50).getMatrix().print();
        } else {
            /* speed test */
            final int[] sizes = {500, 1000, 1500};
            for (int n : sizes) {
                final Matrix m1 = new Matrix(n, n, -10000, 10000);
                final Matrix m2 = new Matrix(n, n, -10000, 10000);

                final Result seq = MultiplySequential.multiply(m1, m2);
                final Result fox = MultiplyFox.multiply(m1, m2, 16);
                final Result fj = MultiplyForkJoin.multiply(m1, m2, 100);

                System.out.println("-------------------------------------------------");
                seq.printResults();
                fox.printResults();
                fj.printResults();
                System.out.println(String.format(
                        "-------------------------------------------------\n" +
                        "Sequential vs ForkJoin | x%f \n" +
                        "Fox vs ForkJoin:       | x%f",
                        (double) seq.getTime() / fj.getTime(),
                        (double) fox.getTime() / fj.getTime()));
            }
            System.out.println("-------------------------------------------------");
        }
    }
}