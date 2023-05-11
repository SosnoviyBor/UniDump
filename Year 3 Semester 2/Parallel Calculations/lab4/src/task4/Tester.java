package task4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Tester {
    public static void main(String[] args) throws FileNotFoundException {
        final String filePath = "./src/data/";
        final String[] keywords = {"internet", "devices", "applications"};
        final String text = new Scanner(new File(filePath + "iot.txt")).useDelimiter("\\Z").next();

        assert KeywordMatcher.matchesKeywords(keywords, text);
        System.out.println("Success!");
    }
}