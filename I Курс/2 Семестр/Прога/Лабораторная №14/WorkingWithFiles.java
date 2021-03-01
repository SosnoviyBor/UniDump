import java.io.*;
import java.sql.SQLOutput;

public class WorkingWithFiles {
    public String firstLongestString(String filename) {
        File file = new File(filename);
        String longestWord = "";
        try (BufferedReader reader = new BufferedReader(new FileReader(file),200)){
            StringBuilder currentWord = new StringBuilder();
            int c;
            while ( (c = reader.read() ) != -1 ) {
                if ( (char) c == ' ' ) {
                  if (currentWord.length() > longestWord.length()) {
                      longestWord = currentWord.toString();
                  }
                  currentWord.delete(0,currentWord.length());
                }
                else {
                    currentWord.append( (char) c );
                }
            }
            // Проверка самого последнего слова, так как после него может и не стоять пробел
            if (currentWord.length() > longestWord.length()) {
                longestWord = currentWord.toString();
            }
        } catch (FileNotFoundException e) {
            System.out.println("Не удалось открыть файл");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return longestWord;
    }
    public byte checkSum(String filename){
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filename))){
            byte answer = (byte) bufferedReader.read();
            byte nextByte;
            while ( ( nextByte = (byte) bufferedReader.read() )!=-1 ) {
                answer = (byte) (answer ^ nextByte);
            }
            return answer;
        } catch (FileNotFoundException e) {
            System.out.println("Файл не найден.");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return -1;
    }


}
