import java.io.*;
import java.sql.SQLOutput;

public class WorkingWithFiles {
    public String firstLongestString(String filename) {
		// Проверка валидности входного аргумента
		filenameValidator(filename);
        File file = new File(filename);
        String longestLine = "";
        try (BufferedReader reader = new BufferedReader(new FileReader(file),200)){
            StringBuilder currentLine = new StringBuilder();
            int c;
            while ( (c = reader.read() ) != -1 ) {
                if ( (char) c == '\r' ) {
                  if (currentLine.length() > longestLine.length()) {
					longestLine = currentLine.toString();
                  }
                	currentLine.delete(0,currentLine.length());
					reader.read();	// Фиктивное дочитывание строки (символ 0А)
                }
                else {
                    currentLine.append( (char) c );
                }
            }
            // Проверка самой последней строки, так как после нее может и не стоять перевод строки (символ 0D)
            if (currentLine.length() > longestLine.length()) {
                longestLine = currentLine.toString();
            }
        } catch (FileNotFoundException e) {
            System.out.println("Не удалось открыть файл");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return longestLine;
    }
    public byte checkSum(String filename){
		filenameValidator(filename);
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
	private void filenameValidator(String filename) throws IllegalArgumentException {
		if (filename == null) { throw new NullPointerException("Filename can't be null"); }

		if (filename.charAt(0) == ' ') { throw new IllegalArgumentException("Filename can't start with space"); }

		String[] nameParts = filename.split("\\.");
		if (nameParts[nameParts.length-1].charAt(0) == ' ') { throw new IllegalArgumentException("File extention can't start with space"); }
		
		if (filename.contains("\\") || filename.contains("/") || filename.contains(":") ||
			filename.contains("*") || filename.contains("?") || filename.contains("\"") ||
			filename.contains("<") || filename.contains(">") || filename.contains("|") ) {
			throw new IllegalArgumentException("Filename can't have special characters");
		}
	}

}
