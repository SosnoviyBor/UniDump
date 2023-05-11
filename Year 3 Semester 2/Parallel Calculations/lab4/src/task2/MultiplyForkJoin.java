package task2;

import task2.models.Block;
import task2.models.Matrix;
import task2.models.Result;

import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.RecursiveTask;
import java.util.stream.IntStream;

public class MultiplyForkJoin {
    private static int blockThreshold;

    public static Result multiply(Matrix m1, Matrix m2, int blockThreshold) {
        MultiplyForkJoin.blockThreshold = blockThreshold;

        final ForkJoinPool pool = ForkJoinPool.commonPool();
        final CountBlock task = new CountBlock(m1.toBlock(), m2.toBlock());

        final long startTime = System.nanoTime();
        final Matrix resultMatrix = pool.invoke(task);
        final long resultTime = (System.nanoTime() - startTime) / 1000000;

        return new Result(resultMatrix, resultTime, "ForkJoin  ");
    }

    private static class CountBlock extends RecursiveTask<Matrix> {
        private final Block m1Block;
        private final Block m2Block;

        public CountBlock(Block m1Block, Block m2Block) {
            this.m1Block = m1Block;
            this.m2Block = m2Block;
        }

        @Override
        protected Matrix compute() {
            final int n = m1Block.getSizeI();
            final int m = m1Block.getSizeJ();
            final int p = m2Block.getSizeJ();

            final int max = IntStream
                    .of(n, m, p)
                    .max()
                    .getAsInt();

            if (max <= blockThreshold) { return this.countResult(); }

            if (max == n) {
                final int topBlockSizeI = m1Block.getSizeI() / 2;
                final Block topBlock = new Block(m1Block,
                        m1Block.getOffsetI(),
                        m1Block.getOffsetJ(),
                        topBlockSizeI,
                        m1Block.getSizeJ());
                final Block botBlock = new Block(m1Block,
                        m1Block.getOffsetI() + topBlockSizeI,
                        m1Block.getOffsetJ(),
                        m1Block.getSizeI() - topBlockSizeI,
                        m1Block.getSizeJ());
                final CountBlock topMatrixBlock = new CountBlock(topBlock, m2Block);
                final CountBlock botMatrixBlock = new CountBlock(botBlock, m2Block);
                ForkJoinTask.invokeAll(topMatrixBlock, botMatrixBlock);

                final Matrix resultTopBlock = topMatrixBlock.join();
                final Matrix resultBotBlock = botMatrixBlock.join();
                return Matrix.concatVertically(resultTopBlock, resultBotBlock);

            } else if (max == p) {
                final int leftBlockSizeJ = m2Block.getSizeJ() / 2;
                final Block leftBlock = new Block(m2Block,
                        m2Block.getOffsetI(),
                        m2Block.getOffsetJ(),
                        m2Block.getSizeI(),
                        leftBlockSizeJ);
                final Block rightBlock = new Block(m2Block,
                        m2Block.getOffsetI(),
                        m2Block.getOffsetJ() + leftBlockSizeJ,
                        m2Block.getSizeI(),
                        m2Block.getSizeJ() - leftBlockSizeJ);
                final CountBlock leftMatrixBlock = new CountBlock(m1Block, leftBlock);
                final CountBlock rightMatrixBlock = new CountBlock(m1Block, rightBlock);
                ForkJoinTask.invokeAll(leftMatrixBlock, rightMatrixBlock);

                final Matrix resultLeftBlock = leftMatrixBlock.join();
                final Matrix resultRightBlock = rightMatrixBlock.join();
                return Matrix.concatHorizontally(resultLeftBlock, resultRightBlock);

            } else {
                final int leftBlockSizeJ = m1Block.getSizeJ() / 2;
                final Block leftBlock = new Block(m1Block,
                        m1Block.getOffsetI(),
                        m1Block.getOffsetJ(),
                        m1Block.getSizeI(),
                        leftBlockSizeJ);
                final Block rightBlock = new Block(m1Block,
                        m1Block.getOffsetI(),
                        m1Block.getOffsetJ() + leftBlockSizeJ,
                        m1Block.getSizeI(),
                        m1Block.getSizeJ() - leftBlockSizeJ);

                final int topBlockSizeI = m2Block.getSizeI() / 2;
                final Block topBlock = new Block(m2Block,
                        m2Block.getOffsetI(),
                        m2Block.getOffsetJ(),
                        topBlockSizeI,
                        m2Block.getSizeJ());
                final Block botBlock = new Block(m2Block,
                        m2Block.getOffsetI() + topBlockSizeI,
                        m2Block.getOffsetJ(),
                        m2Block.getSizeI() - topBlockSizeI,
                        m2Block.getSizeJ());

                final CountBlock split1MatrixBlock = new CountBlock(leftBlock, topBlock);
                final CountBlock split2MatrixBlock = new CountBlock(rightBlock, botBlock);
                ForkJoinTask.invokeAll(split1MatrixBlock, split2MatrixBlock);

                final Matrix res1 = split1MatrixBlock.join();
                final Matrix res2 = split2MatrixBlock.join();
                res1.addBlock(res2, 0, 0);
                return res1;
            }
        }

        private Matrix countResult() {
            final int resultHeight = m1Block.getSizeI();
            final int resultWidth = m2Block.getSizeJ();
            final int m1BlockOffsetI = m1Block.getOffsetI();
            final int m1BlockOffsetJ = m1Block.getOffsetJ();
            final int m2BlockOffsetI = m2Block.getOffsetI();
            final int m2BlockOffsetJ = m2Block.getOffsetJ();
            final int[][] blockTable1 = m1Block.getMatrix();
            final int[][] blockTable2 = m2Block.getMatrix();

            final Matrix result = new Matrix(resultHeight, resultWidth);
            final int[][] resultTable = result.getMatrix();
            for (int i = 0; i < resultHeight; i++) {
                for (int j = 0; j < resultWidth; j++) {
                    double value = 0;
                    for (int k = 0; k < resultHeight; k++) {
                        value += blockTable1[m1BlockOffsetI + i][m1BlockOffsetJ + k]
                                * blockTable2[m2BlockOffsetI + k][m2BlockOffsetJ + j];
                    }
                    resultTable[i][j] += value;
                }
            }

            return result;
        }
    }
}
