import java.io.*;
import java.util.HashSet;
import java.util.Objects;

public class FileWorker {
    public  String rarestWord(String filename) {
        HashSet<StringCounter> hashSet = new HashSet<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename)) ) {
            String line;
            while ((line=reader.readLine())!=null) {
                String[] words =  line.split(" ");
                for (String word : words) {
                    hashSet.add(new StringCounter(word));
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Не удалось открыть файл");
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Произошла ошибка при работе с файлом.");
        }
        String rarestWord = null;
        int countTimes = 100;
        for (StringCounter stringCounter: hashSet) {
            //System.out.println(stringCounter.word+" "+stringCounter.occuring);
            if (stringCounter.occuring<countTimes) {
                countTimes = stringCounter.occuring;
                rarestWord = stringCounter.word;
            }
        }

        return rarestWord;
    }
    private class StringCounter {
        String word;
        int occuring = 1;

        public StringCounter(String word) {
            this.word = word;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            StringCounter that = (StringCounter) o;
            if (Objects.equals(word, that.word)) {
                that.occuring++;
                return true;
            }
            else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            return Objects.hash(word);
        }
    }

}
