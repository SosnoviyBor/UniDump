package cabbage;

public class MergeSort implements SortChooser {
	void merge(float arr[], int l, int m, int r){
		int n1 = m - l + 1;
		int n2 = r - m;
		float L[] = new float[n1];
		float R[] = new float[n2];
		for (int i = 0; i < n1; ++i)
			L[i] = arr[l + i];
		for (int j = 0; j < n2; ++j)
			R[j] = arr[m + 1 + j];
		int i = 0, j = 0;
		int k = l;
		while (i < n1 && j < n2) {
			if (L[i] <= R[j]) {
				arr[k] = L[i];
				i++;
			}
			else {
				arr[k] = R[j];
				j++;
			}
			k++;
		}
		while (i < n1) {
			arr[k] = L[i];
			i++;
			k++;
		}
		while (j < n2) {
			arr[k] = R[j];
			j++;
			k++;
		}
	}
	void sorter(float arr[], int l, int r){
		if (l < r) {
			int m = (l + r) / 2;
			sorter(arr, l, m);
			sorter(arr, m + 1, r);
			merge(arr, l, m, r);
		}
	}
	public void sort (float[] arr) {
		sorter(arr, 0, arr.length-1);
	}
}