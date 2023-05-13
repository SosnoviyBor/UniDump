package task4;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

class Tester {
    public static void main(String[] args) throws IOException {
        File[] files = new File("./src/data").listFiles();
        assert files != null;
        final String[] keywords = {"internet", "devices", "applications"};

        for (File file : files) {
            final String text = Files.readString(file.toPath());
            if (KeywordMatcher.matchesKeywords(keywords, text)) {
                System.out.println("Found matches in file: " + file.getPath());
            }
        }
    }
}