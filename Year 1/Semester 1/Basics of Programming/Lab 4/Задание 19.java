class lab4 {
	public static void main (String args[] ) {
		int[] table = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5};
		int result = 0;
		for (int i : table) {
			int counterInt = counter(i);
			result += counterInt;
		}
		printResults(result);
	}

	static boolean filter (int i) {
		if (i >= 0) {
			return false;
		} else return true;
	}

	static int counter (int i) {
		if (filter(i) == false) {
			return 0;
		} else return 1;
	}

	static void printResults (int result) {
		try {
			System.out.println("Amount of negative numbers in the list is "+result);
		} catch (IllegalArgumentException e) {
			System.out.println("EXCEPTION! " + e.getMessage());
		}
	}
}