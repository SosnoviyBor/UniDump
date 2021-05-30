import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("Rabin Karp Algorithm Test!");
        String fileName = "text.txt";

        BufferedReader fileReader = new BufferedReader(new FileReader(fileName));
        StringBuilder stringBuilder = new StringBuilder();
        String line = null;
        String ls = System.getProperty("line.separator");
        while ((line = fileReader.readLine()) != null) {
            stringBuilder.append(line);
            stringBuilder.append(ls);
        }
        fileReader.close();
        stringBuilder.deleteCharAt(stringBuilder.length() - 1);
        String text = stringBuilder.toString();

        BufferedReader inputReader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("\nEnter Pattern");
        String pattern = inputReader.readLine();
        inputReader.close();

        long time = System.currentTimeMillis();
        new RabinKarp(text, pattern);
        time = System.currentTimeMillis() - time;
        System.out.println("This operation took " + time + "ms");
    }
}
