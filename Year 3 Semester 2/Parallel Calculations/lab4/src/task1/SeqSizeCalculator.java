package task1;

import java.util.HashMap;
import java.util.Map;

public class SeqSizeCalculator {

    public Map<Integer, Integer> extractWordSizes(String text) {
        text = text.trim().replaceAll("\\s+", " ");
        final RecursiveSizeExtractor sizeCalculator = new RecursiveSizeExtractor(
                text, 0, text.length());

        return sizeCalculator.compute();
    }

    private static class RecursiveSizeExtractor {
        private static final String WORD_DELIMITER = " ";

        private final String subtext;
        private final int beginText;
        private final int endText;

        public RecursiveSizeExtractor(String subtext, int beginText, int endText) {
            this.subtext = subtext;
            this.beginText = beginText;
            this.endText = endText;
        }

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
            final Map<Integer, Integer> frequencyMapLeft = new RecursiveSizeExtractor(
                    subtext.substring(0, index),
                    beginText,
                    beginText + index
            ).compute();
            final Map<Integer, Integer> frequencyMapRight = new RecursiveSizeExtractor(
                    subtext.substring(index + WORD_DELIMITER.length()),
                    beginText + index + WORD_DELIMITER.length(),
                    endText
            ).compute();
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
