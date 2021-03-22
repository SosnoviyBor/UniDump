public class SparseTable{
	private int[][] compactTable;
	private int size = 0;
	private int distance = 0;
	
	// n is initTable length
	// k is compactTable length

	public SparseTable(int[] initTable){
		// Time difficulty = O(n)
		// Space difficulty = O(k)
		for (int i = 0; i < initTable.length-1; i++) {
			if (initTable[i] != 0 || i == initTable.length-1) {
				size++;
			}
		}
		compactTable = new int[2][size];
		int k = 0;
		for (int i = 0; i < initTable.length-1; i++, distance++) {
			if (initTable[i] != 0) {
				compactTable[0][k] = initTable[i];	// Value
				compactTable[1][k] = distance;		// Distance
				distance = 0;
				k++;
			} else if (i == initTable.length-1) {
				compactTable[0][i] = 0;
				compactTable[1][i] = distance;
			}
		}
	}

	public int get(int index) throws IndexOutOfBoundsException {
		// Time difficulty = O(k)
		// Space difficulty = O(1)
		int currentIndex = 0;
		for (int i = 0; i < compactTable[0].length-1; i++) {
			currentIndex += compactTable[1][i];
			if (currentIndex == index) {
				return compactTable[0][i];
			} else if (currentIndex > index) {
				return 0;
			}
		}
		throw new IndexOutOfBoundsException("Index can't be larger than array's length");
	}

	public void set(int value, int distance) {
		// Time difficulty = O(k)
		// Space difficulty = O(k)
		int length = 0;
		for (int i = 0; i < compactTable[0].length; i++) {
			length += compactTable[1][i];
		}
		if (distance > length) {
			int[][] tmpTable = new int[2][compactTable[0].length+1];
			System.arraycopy(compactTable[0], 0, tmpTable[0], 0, compactTable[0].length-1);
			System.arraycopy(compactTable[1], 0, tmpTable[1], 0, compactTable[0].length-1);
			tmpTable[1][compactTable[0].length-1] += distance-length;
			tmpTable[0][compactTable[0].length] = value;
			tmpTable[1][compactTable[0].length] = 0;
			compactTable = tmpTable;
		} else {
			insert(value, distance);
		}
	}

	public void insert(int value, int distance) throws IndexOutOfBoundsException {
		// Time difficulty = O(k^2)
		// Space difficulty = O(k)
		int length = 0;
		for (int i = 0; i < compactTable[0].length; i++) {
			length += compactTable[1][i];
		}
		if (distance == 0){
			int[][] tmpTable = new int[2][compactTable[0].length];
			System.arraycopy(compactTable[0], 0, tmpTable[0], 1, compactTable[0].length-1);
			System.arraycopy(compactTable[1], 0, tmpTable[1], 1, compactTable[0].length-1);
			tmpTable[1][compactTable[0].length-1] += distance-length;
			tmpTable[0][0] = value;
			tmpTable[1][0] = 0;
			compactTable = tmpTable;
			return;
		} else {
			int currentValueIndex = 0;
			int distanceToPrevValue;
			for (int i = 0; i < compactTable[0].length; i++) {
				currentValueIndex += compactTable[1][i];
				distanceToPrevValue = 0;
				for (int j = 0; j < currentValueIndex; j++, distanceToPrevValue++) {
					if (j == distance) {
						int[][] tmpTable = new int[2][compactTable[0].length];
						System.arraycopy(compactTable[0], 0, tmpTable[0], 0, i-1);
						System.arraycopy(compactTable[0], i+1, tmpTable[0], i+1, compactTable[0].length-i);
						System.arraycopy(compactTable[1], 0, tmpTable[1], 0, i-1);
						System.arraycopy(compactTable[1], i+1, tmpTable[1], i+1, compactTable[0].length-i);
						tmpTable[0][i] = value;
						tmpTable[1][i] = distanceToPrevValue;
						tmpTable[1][i+1] -= distanceToPrevValue;
						compactTable = tmpTable;
						return;
					}
				}
			}
		}
		throw new IndexOutOfBoundsException("You cannot insert value out of bounds of array");
	}

	public void sort () {
		// Bubble sort lets goooo
		// Time difficulty = O(n^2)
		// Space difficulty = O(1)
		int n = compactTable.length;
		for (int i = 0; i < n-1; i++) {
			for (int j = 0; j < n-i-1; j++) {
				if (compactTable[0][j] > compactTable[0][j+1]) {
					int temp = compactTable[0][j];
					compactTable[0][j] = compactTable[0][j+1];
					compactTable[0][j+1] = temp;
				}
			}
		}
	}
}