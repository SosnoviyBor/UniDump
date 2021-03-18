import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        String filePath = "Test.txt";
        WorkingWithFiles wwf = new WorkingWithFiles();
		try {
        	System.out.println( wwf.firstLongestString(filePath));
        	System.out.println( wwf.checkSum(filePath));
		} catch (IllegalArgumentException e) {
			System.out.println(e.getMessage());
		}
    }
}
