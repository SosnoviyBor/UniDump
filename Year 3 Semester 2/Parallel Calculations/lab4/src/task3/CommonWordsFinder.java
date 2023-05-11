package task3;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
import java.util.stream.Collectors;

public class CommonWordsFinder extends RecursiveTask<Set<String>> {
    private final File[] files;
    private final int start;
    private final int end;
    private static final int THRESHOLD = 2;

    public CommonWordsFinder(File[] files, int start, int end) {
        this.files = files;
        this.start = start;
        this.end = end;
    }

    @Override
    protected Set<String> compute() {
        if (end - start <= THRESHOLD) {
            try {
                return findCommonWords(files[start], files[end]);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        final int mid = (start + end) / 2;
        final CommonWordsFinder leftTask = new CommonWordsFinder(files, start, mid);
        final CommonWordsFinder rightTask = new CommonWordsFinder(files, mid + 1, end);
        leftTask.fork();
        final Set<String> rightResult = rightTask.compute();
        final Set<String> leftResult = leftTask.join();

        leftResult.retainAll(rightResult);
        return leftResult;
    }

    private Set<String> findCommonWords(File file1, File file2) throws IOException {
        final Set<String> words1 = Files.lines(file1.toPath())
                .flatMap(line -> Arrays.stream(line.split("\\W+")))
                .collect(Collectors.toSet());
        final Set<String> words2 = Files.lines(file2.toPath())
                .flatMap(line -> Arrays.stream(line.split("\\W+")))
                .collect(Collectors.toSet());
        words1.retainAll(words2);
        return words1;
    }
}

