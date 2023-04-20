import models.Matrix;

public class Main {
    public static void main(String[] args) {
//        var matrix1 = new Matrix(new int[][]{
//                {1, 5, 1},
//                {2, 5, 1},
//                {1, 5, 1}
//        });
//        var matrix2 = new Matrix(new int[][]{
//                {1, 2, 3},
//                {5, 5, 8},
//                {5, 5, 8}
//        });
//        Calculator.sequential(matrix1, matrix2).getMatrix().print();
//        Calculator.fox(matrix1, matrix2, 16).getMatrix().print();

        var dims = new int[]{ 250,500,1000,2000,3000 };
        var threads = new int[] { 2, 8, 16, 32, 64 };

        for (int dim : dims) {
            System.out.println("----+---------------------------------------------------");
            Calculator.sequential(
                    new Matrix(dim,dim,-10000,10000),
                    new Matrix(dim,dim,-10000,10000))
                    .printResults();
            System.out.println("----+---------------------------------------------------");
            for (int thread_count : threads) {
                Calculator.fox(
                        new Matrix(dim, dim, -10000, 10000),
                        new Matrix(dim, dim, -10000, 10000), thread_count)
                        .printResults();
            }
        }
        System.out.println("----+---------------------------------------------------");
    }

}