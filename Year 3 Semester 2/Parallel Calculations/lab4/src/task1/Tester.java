package task1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;

public class Tester {
    public static void main(String[] args) throws FileNotFoundException {
        final FJSizeCalculator FJExtractor = new FJSizeCalculator();
        final SeqSizeCalculator seqExtractor = new SeqSizeCalculator();
        final Analyzer analyser = new Analyzer();

        final String filePath = "./src/data/";
        final String[] fileNames = {
                "iot.txt", "samurai.txt", "lorem.txt", "energy.txt", "don-quixote.html"
//                "don-quixote.html"
        };
        for (String fileName : fileNames) {
            final String path = filePath + fileName;
            final String text = new Scanner(new File(path)).useDelimiter("\\Z").next();
            System.out.println(String.format(
                    "------------------------------------------------\n" +
                    "   %s \n" +
                    "Text size: %d",
                    fileName, text.length()));

            final long SeqStartTime = System.nanoTime();
            final Map<Integer, Integer> SeqWordSizes = seqExtractor.extractWordSizes(text);
            SeqWordSizes.forEach((k, v) -> { assert v != 0; });
            final double SeqEstimatedTime = (System.nanoTime() - SeqStartTime) / 100_000_000D;
            System.out.println(String.format(
                    "Elapsed Sequential time: %f seconds",
                    SeqEstimatedTime));

            final long FJStartTime = System.nanoTime();
            final Map<Integer, Integer> FJWordSizes = FJExtractor.extractWordSizes(text);
            FJWordSizes.forEach((k, v) -> { assert v != 0; });
            final double FJEstimatedTime = (System.nanoTime() - FJStartTime) / 100_000_000D;
            System.out.println(String.format(
                    "Elapsed ForkJoin time:   %f seconds",
                    FJEstimatedTime));

            final double average = analyser.getAverage(FJWordSizes);
            assert average > 0;
            final double dispersion = analyser.getDispersion(FJWordSizes);
            assert dispersion > 0;
            final double std = analyser.getStd(FJWordSizes);
            assert std > 0;
            System.out.println(String.format(
                    "Average word size: %f \n" +
                    "Dispersion: %f \n" +
                    "Std: %f",
                    average, dispersion, std));
        }
        System.out.println("------------------------------------------------");
    }
}