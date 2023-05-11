package task2;

import task2.models.Matrix;
import task2.models.Result;

public class MultiplySequential {

    public static Result multiply(Matrix matrixA, Matrix matrixB) {
        is_multiplyable(matrixA, matrixB);

        final Matrix resultMatrix = new Matrix(matrixA.getHeight(), matrixB.getWidth());

        final long startTime = System.nanoTime();
        for (int i = 0; i < matrixA.getWidth(); i++) {
            for (int j = 0; j < matrixB.getHeight(); j++) {
                for (int k = 0; k < matrixA.getWidth(); k++) {
                    final var val = resultMatrix.get(i, j) + matrixA.get(i, k) * matrixB.get(k, j);
                    resultMatrix.set(i, j, val);
                }
            }
        }
        //        nanoseconds to milliseconds
        final long resultTime = (System.nanoTime() - startTime) / 1000000;

        return new Result(resultMatrix, resultTime, "Sequential");
    }

    private static void is_multiplyable(Matrix matrixA, Matrix matrixB) {
        if (matrixA.getWidth() != matrixB.getHeight() ||
                matrixA.getWidth() != matrixA.getHeight() ||
                matrixB.getWidth() != matrixB.getHeight()) {
            throw new IllegalArgumentException();
        }
    }
}
