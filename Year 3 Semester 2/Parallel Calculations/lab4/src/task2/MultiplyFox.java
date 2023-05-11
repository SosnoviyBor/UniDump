package task2;

import task2.models.Block;
import task2.models.Matrix;
import task2.models.Result;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class MultiplyFox {

    public static Result multiply(Matrix matrixA, Matrix matrixB, int thread_amount) {
        is_multiplyable(matrixA, matrixB);

        final Matrix result = new Matrix(matrixA.getWidth(), matrixB.getHeight());
        final int blockSize = findBlockSize(matrixA.getWidth());
        final int blockAmount = result.getWidth() / blockSize;
        final Block[][] blocksA = matrixA.split(blockSize, blockSize);
        final Block[][] blocksB = matrixB.split(blockSize, blockSize);

        final ExecutorService executorService = Executors.newFixedThreadPool(thread_amount);
        final List<Future<?>> tasks = new ArrayList<>();

        final long startTime = System.nanoTime();
        try {
            for (int i = 0; i < blockAmount; i++) {
                for (int j = 0; j < blockAmount; j++) {
                    final int taskI = i;
                    final int taskJ = j;

                    final Runnable countItem = () -> {
                        for (int stage = 0; stage < blockAmount; stage++) {
                            int k_bar = (taskI + stage) % blockAmount;
                            result.addBlock(
                                    multiplyBlock(blocksA[taskI][k_bar], blocksB[k_bar][taskJ]),
                                    taskI, taskJ);
                        }
                    };
                    final Future<?> task = executorService.submit(countItem);

                    tasks.add(task);
                }
            }

            for (Future<?> task : tasks) {
                task.get();
            }
        } catch (InterruptedException e) {
            throw new RuntimeException("Unexpected interruption!");
        } catch (ExecutionException e) {
            throw new RuntimeException("Computation error!");
        } finally {
            executorService.shutdown();
        }
    //        nanoseconds to milliseconds
        final long resultTime = (System.nanoTime() - startTime) / 1000000;

        return new Result(result, resultTime, "Fox, th="+thread_amount);
    }

    private static int findBlockSize(int matrixSize) {
        for (int i = Math.min(10, matrixSize - 1); i > 1; i--) {
            if (matrixSize % i == 0) {
                return i;
            }
        }
        return 1;
    }

    private static Matrix multiplyBlock(Block b1, Block b2) {
        if (b1.getWidth() != b2.getHeight()) {
            throw new IllegalArgumentException();
        }
        final Matrix result = new Matrix(b1.getSizeI(), b2.getSizeJ());

        final int resultHeight = result.getHeight();
        final int resultWidth = result.getWidth();
        final int[][] block1 = b1.getMatrix();
        final int[][] block2 = b2.getMatrix();
        final int[][] resultMatrix = result.getMatrix();

        for (int i = 0, items = resultWidth * resultHeight; i < items; i++) {
            final int resultI = i / resultWidth;
            final int resultJ = i % resultWidth;

            double value = 0;
            for (int j = 0; j < b1.getSizeJ(); j++) {
                value += block1[resultI + b1.getOffsetI()][j + b1.getOffsetJ()] *
                        block2[j + b2.getOffsetI()][resultJ + b2.getOffsetJ()];
            }
            resultMatrix[resultI][resultJ] = (int) value;
        }

        return result;
    }

    private static void is_multiplyable(Matrix matrixA, Matrix matrixB) {
        if (matrixA.getWidth() != matrixB.getHeight() ||
                matrixA.getWidth() != matrixA.getHeight() ||
                matrixB.getWidth() != matrixB.getHeight()) {
            throw new IllegalArgumentException();
        }
    }

}