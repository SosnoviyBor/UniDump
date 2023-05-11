package task1;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.RecursiveTask;

public class FJSizeCalculator {

    public Map<Integer, Integer> extractWordSizes(String text) {
        text = text.trim().replaceAll("\\s+", " ");
        final RecursiveSizeExtractor sizeExtractor = new RecursiveSizeExtractor(
                text, 0, text.length());

        RecursiveTask.invokeAll(sizeExtractor);
        return sizeExtractor.join();
    }

    private static class RecursiveSizeExtractor extends RecursiveTask<Map<Integer, Integer>> {
        private static final String WORD_DELIMITER = " ";

        private final String subtext;
        private final int beginText;
        private final int endText;

        public RecursiveSizeExtractor(String subtext, int beginText, int endText) {
            this.subtext = subtext;
            this.beginText = beginText;
            this.endText = endText;
        }

        @Override
        protected Map<Integer, Integer> compute() {
            final int center = subtext.length() / 2;
            final int indexRight = subtext.indexOf(WORD_DELIMITER, center);
            final int indexLeft = subtext.lastIndexOf(WORD_DELIMITER, center);

            if (indexRight != -1 || indexLeft != -1) {
//                split sentence in half by spaces
                if (center - indexLeft > Math.abs(indexRight - center)) {
                    return this.splitJoin(indexRight);
                } else {
                    return this.splitJoin(indexLeft);
                }
            } else {
//                if the current text does not contain any spaces
                return this.countWord();
            }
        }

        private Map<Integer, Integer> splitJoin(int index) {
            final RecursiveSizeExtractor splitLeft = new RecursiveSizeExtractor(
                    subtext.substring(0, index),
                    beginText,
                    beginText + index
            );
            final RecursiveSizeExtractor splitRight = new RecursiveSizeExtractor(
                    subtext.substring(index + WORD_DELIMITER.length()),
                    beginText + index + WORD_DELIMITER.length(),
                    endText
            );
            ForkJoinTask.invokeAll(splitLeft, splitRight);
            final Map<Integer, Integer> frequencyMapLeft = splitLeft.join();
            final Map<Integer, Integer> frequencyMapRight = splitRight.join();

            frequencyMapRight.forEach((key, value) -> frequencyMapLeft.merge(key, value, Integer::sum));
            return frequencyMapLeft;
        }

        private Map<Integer, Integer> countWord() {
            final int wordSize = subtext.length();
            final Map<Integer, Integer> frequencyMap = new HashMap<>();
            frequencyMap.put(wordSize, 1);
            return frequencyMap;
        }
    }
}
