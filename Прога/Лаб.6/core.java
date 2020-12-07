import java.util.Random;

class lab6 {
	public static void main (String[] argv) {
		float[] table = new float[10];
		System.out.println("##### Initial array #####");
		for(int i = 0; i < table.length; i++) {
			table[i] = generator();
			System.out.println(table[i]);
		}

		float[] bubbleSorted = bubbleSort(table.clone());
		float[] selectionSorted = selectionSort(table.clone());

		System.out.println("\n##### Bubble Sort #####");
		for (float i : bubbleSorted) {
			System.out.println(i);
		}
		System.out.println("\n##### Selection Sort #####");
		for (float i : selectionSorted) {
			System.out.println(i);
		}
	}

	static float generator() {
		float min = -20;
		float max = 20;
		Random randomFloat = new Random();
		return randomFloat.nextFloat() * (max - min) + min;
	}

	static float[] bubbleSort(float table[]) {
		int n = table.length; 
		
		for (int i = 0; i < n-1; i++) {
			for (int j = 0; j < n-i-1; j++) {
				if (table[j] > table[j+1]) {
					float temp = table[j]; 
					table[j] = table[j+1]; 
					table[j+1] = temp; 
				}
			}
		}

		return table;
	}

	static float[] selectionSort(float[] table) {
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

		return table;
	}
}