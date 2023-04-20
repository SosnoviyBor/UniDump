package models;

public class Result {
    private final Matrix matrix;
    private final long time;
    private int threads = 0;

    public Result(Matrix matrix, long time) {
        this.matrix = matrix;
        this.time = time;
    }

    public Result(Matrix matrix, long time, int threads) {
        this.matrix = matrix;
        this.time = time;
        this.threads = threads;
    }

    public Matrix getMatrix() {
        return matrix;
    }

    public void printResults() {
        if (threads == 0) {
            System.out.println(String.format("Syn | %d*%d took %dms to complete",
                    matrix.getHeight(), matrix.getHeight(), time));
        } else {
            System.out.println(String.format("Fox | Using %d threads %d*%d took %dms to complete",
                    threads, matrix.getHeight(), matrix.getHeight(), time));
        }
    }
}
