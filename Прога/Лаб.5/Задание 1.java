import static java.lang.Math.*;

class lab5 {
	public static void main(String argv[]) {
		int[][] matrix = {
			{1, 2, 3, 4, 5, 1},
			{-1, -2, -3, -4, -5, 1},
			{0, 1, 0, 1, 0, 1}
		};
		
		boolean matrixCheck = guard(matrix);
		if (matrixCheck == false) {
			System.out.println("Looks like what you entered is not a matrix");
			return;
		}
		
		int result = minElementInLargestColumn(matrix);
		System.out.println(result);
	}

	static boolean guard (int[][] matrix) {
		int basicLength = matrix[0].length;
		for (int i = 1; i < matrix.length; i++) {
			if (basicLength != matrix[i].length) {
				return false;
			}
		}
		return true;
	}

	static int minElementInLargestColumn(int[][] matrix) {
		int[] sumOfModules = new int [matrix[0].length];
		int absVal = 0;
		for (int i = 0; i < matrix[0].length; i++, absVal = 0) {
			for (int j = 0; j < matrix.length; j++) {
				absVal += abs(matrix[j][i]);
			}
			sumOfModules[i] = absVal;
		}

		int biggestVal = sumOfModules[0];
		for (int currentVal : sumOfModules) {
			if (currentVal > biggestVal) {
				biggestVal = currentVal;
			}
		}

		int[] goodIndexes = new int[sumOfModules.length];
		int counter = 0;
		for (int i = 0; i < sumOfModules.length; i++) {
			if (sumOfModules[i] == biggestVal) {
				goodIndexes[counter++] = i;
			}
		}

		int minVal = matrix[0][goodIndexes[0]];
		for (int i = 0; i < counter; i++) {
			for ( int j = 0; j < matrix.length; j++) {
				if (matrix[j][goodIndexes[i]] < minVal) {
					minVal = matrix[j][goodIndexes[i]];
				}
			}
		}

		return minVal;
	}
}