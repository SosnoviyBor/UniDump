import static java.lang.Math.*;

class number6 {
	public static void main(String[] args) {
		Variant6 var6 = new Variant6();

		double[] debugTable = {1, 2, 0, -1, -2, Double.MAX_VALUE, Double.NaN};
		
		int j = 0;
		double t;
		while (j<debugTable.length) {
			t = debugTable[j];
			j = j + 1;
			System.out.println("t: "+t+" i: 1 result: ");
			try {
				System.out.println(var6.solve(t, 1));
			} catch (IllegalArgumentException e) {
				System.out.println("EXCEPTION!" + e.getMessage());
			}
			System.out.println("t: "+t+" i: 2 result: ");
			try {
				System.out.println(var6.solve(t, 2));
			} catch (IllegalArgumentException e) {
				System.out.println("EXCEPTION!" + e.getMessage());
			}
			System.out.println("t: "+t+" i: 10 result: ");
			try {
				System.out.println(var6.solve(t, 10));
			} catch (IllegalArgumentException e) {
				System.out.println("EXCEPTION!" + e.getMessage());
			}
		}
	}
}

class Variant6 {
	private double k = 1;
	private double result;
	
	public double solve(double t, int i) {
		double finalResult = 0;
		if (i == 1) {
			finalResult = sqrt(t);
		}	else if (i == 2) {
			finalResult = 1/sqrt(t);
		} else while (k <= i) {
			result = k*t;
			finalResult = finalResult + result;
			k += 1;
		}
		k = 1;
		return finalResult;
	};
}