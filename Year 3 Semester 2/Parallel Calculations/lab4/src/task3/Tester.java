package task3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.concurrent.ForkJoinPool;

class Tester {
    public static void main(String[] args) {
        File[] filePaths = new File("./src/data/task3").listFiles();
        assert filePaths != null;
        ForkJoinPool forkJoinPool = new ForkJoinPool();

        CommonWordsFinder commonWordsFinder = new CommonWordsFinder(filePaths, 0, filePaths.length - 1);
        Set<String> commonWords = forkJoinPool.invoke(commonWordsFinder);

        System.out.println(
                "Files reviewed: " + Arrays.toString(filePaths) + "\n" +
                "Common words: " + commonWords);
    }
}