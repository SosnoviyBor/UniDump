import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        String filePath = "Test.txt";
        WorkingWithFiles wwf = new WorkingWithFiles();
        System.out.println( wwf.firstLongestString(filePath));
        System.out.println(      wwf.checkSum(filePath));
    }
}
