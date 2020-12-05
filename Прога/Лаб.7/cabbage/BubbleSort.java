package cabbage;

public class BubbleSort implements SortChooser {
	public void sort(float table[]) {
		int n = table.length;
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < n - i - 1; j++) {
				if (table[j] > table[j + 1]) {
					float temp = table[j];
					table[j] = table[j + 1];
					table[j + 1] = temp;
				}
			}
		}
	}
}
