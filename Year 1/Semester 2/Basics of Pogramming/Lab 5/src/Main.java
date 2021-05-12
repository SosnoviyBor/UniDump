import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String fileName = "test.txt";
        FileWorker fileWorker = new FileWorker();
        System.out.println(fileWorker.rarestWord(fileName));
    }
}
