package cabbage;

public class SelectionSort implements SortChooser {
	public void sort(float[] table) {
		int n = table.length;
		for (int i = 0; i < n-1; i++) {
			int min_idx = i;
			for (int j = i+1; j < n; j++) {
				if (table[j] < table[min_idx]) {
					min_idx = j;
				}
			}
			float temp = table[min_idx]; 
			table[min_idx] = table[i]; 
			table[i] = temp; 
		}
	}
}
