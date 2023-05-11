package task2.models;

import java.util.Arrays;

public class Matrix {
    private final int[][] matrix;

    //    gens matrix from given array
    public Matrix(int[][] matrix) {
        this.matrix = matrix;
    }

    //    gens empty matrix of a given size
    public Matrix(int rowsSize, int columnsSize) {
        matrix = new int[rowsSize][columnsSize];
    }

    //    gens matrix with random ints in certain range
    public Matrix(int rowsSize, int columnsSize, int from, int to) {
        matrix = new int[rowsSize][columnsSize];
        for (int i = 0; i < getWidth(); i++) {
            for (int j = 0; j < getHeight(); j++) {
                set(i, j, randInt(from, to));
            }
        }
    }

    public void addBlock(Matrix matrix, int i, int j) {
        final int blockHeight = matrix.getHeight();
        final int blockWidth = matrix.getWidth();
        final int[][] blockTable = matrix.getMatrix();
        for (int k = 0; k < blockHeight; k++) {
            for (int l = 0; l < blockWidth; l++) {
                this.matrix[i * blockHeight + k][j * blockWidth + l] += blockTable[k][l];
            }
        }
    }

    public Block[][] split(int blockHeight, int blockWidth) {
        final int blockCountX = getWidth() / blockWidth;
        final int blockCountY = getHeight() / blockHeight;
        final Block[][] blocks = new Block[blockCountY][blockCountX];

        for (int i = 0; i < blockCountY; i++) {
            for (int j = 0; j < blockCountX; j++) {
                blocks[i][j] = new Block(this, i * blockHeight, j * blockWidth, blockHeight, blockWidth);
            }
        }
        return blocks;
    }

    public Block toBlock() {
        return new Block(
                this,0, 0, getHeight(), getWidth()
        );
    }

    public static Matrix concatVertically(Matrix m1, Matrix m2) {
        final int m1Height = m1.getHeight();
        final int m2Height = m2.getHeight();
        final int resultHeight = m1Height + m2Height;
        final int resultWidth = m1.getWidth();
        if (resultWidth != m2.getWidth()) {
            throw new IllegalArgumentException("Can't concatenate");
        }

        final Matrix matrix = new Matrix(resultHeight, resultWidth);
        final int[][] m1Table = m1.getMatrix();
        final int[][] m2Table = m2.getMatrix();
        final int[][] matrixTable = matrix.getMatrix();
        for (int i = 0; i < m1Height; i++) {
            System.arraycopy(m1Table[i], 0, matrixTable[i], 0, resultWidth);
        }
        for (int i = 0; i < m2Height; i++) {
            System.arraycopy(m2Table[i], 0, matrixTable[m1Height + i], 0, resultWidth);
        }
        return matrix;
    }

    public static Matrix concatHorizontally(Matrix m1, Matrix m2) {
        final int m1Width = m1.getWidth();
        final int m2Width = m2.getWidth();
        final int resultWidth = m1Width + m2Width;
        final int resultHeight = m1.getHeight();
        if (resultHeight != m2.getHeight()) {
            throw new IllegalArgumentException("Can't concatenate");
        }

        final Matrix matrix = new Matrix(resultHeight, resultWidth);
        final int[][] m1Table = m1.getMatrix();
        final int[][] m2Table = m2.getMatrix();
        final int[][] matrixTable = matrix.getMatrix();
        for (int i = 0; i < m1Width; i++) {
            for (int j = 0; j < resultHeight; j++) {
                matrixTable[j][i] = m1Table[j][i];
            }
        }
        for (int i = 0; i < m2Width; i++) {
            for (int j = 0; j < resultHeight; j++) {
                matrixTable[j][m1Width + i] = m2Table[j][i];
            }
        }
        return matrix;
    }

    public void print()
    {
        Arrays.stream(matrix).map(Arrays::toString).forEach(System.out::println);
    }

    public int[][] getMatrix() {
        return matrix;
    }

    public int getHeight() {
        return matrix.length;
    }

    public int getWidth() {
        return matrix[0].length;
    }

    public int get(int i, int j) {
        return matrix[i][j];
    }

    public void set(int i, int j, int value) {
        matrix[i][j] = value;
    }


    private int randInt(int min, int max) {
        return min + (int)(Math.random() * ((max - min) + 1));
    }
}