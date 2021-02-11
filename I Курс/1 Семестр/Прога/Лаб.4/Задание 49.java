import static java.lang.Math.*;

class lab4 {
	public static void main(String args[]) {
		int[] table = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		int bestIndex = 0;
		if (table.length == 0) {
			throw new IllegalArgumentException("Empty arrays are prohibited!");
		}
		for (int i = 3; i < table.length; i += 3) {
			int currentNumber = table [i];
			int previousNumber = table [i-3];
			boolean isBigger = filter(currentNumber, previousNumber, i);
			if (isBigger == true) {
				bestIndex = i;
			}
		}
		System.out.println("The biggest absolute value ("+table[bestIndex]+") on every 3rd index is located on position "+bestIndex);
	}

	static boolean filter (int currentNumber, int previousNumber, int index) {
		if (abs(previousNumber) < abs(currentNumber)) { 
			return true;
		} else return false;
	}
}