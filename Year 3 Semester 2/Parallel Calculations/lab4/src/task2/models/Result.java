package task2.models;

public class Result {
    private final Matrix matrix;
    private final long time;
    private final String type;

    public Result(Matrix matrix, long time, String type) {
        this.matrix = matrix;
        this.time = time;
        this.type = type;
    }

    public Matrix getMatrix() {
        return matrix;
    }

    public void printResults() {
        System.out.println(String.format(
                "%s | %d*%d took %dms to complete",
                type, matrix.getHeight(), matrix.getHeight(), time));
    }

    public long getTime() { return time; }
}
