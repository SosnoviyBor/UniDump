import static java.lang.Math.*;

class lab3 {
	public static void main(String[] args) {
		Variant4 var4 = new Variant4();

		double[][] debugTable = {
			{1, 1},
			{2, 2},
			{0, 0},
			{0, 10},
			{10, 0},
			{10, 10},
			{0, -10},
			{-10, 0},
			{-10, -10},
			{0, Double.MAX_VALUE},
			{10, Double.MAX_VALUE},
			{10, Double.NaN}
		};
		
		int i = 0;
		double a;
		double b;
		while (i<debugTable.length) {
			a = debugTable[i][0];
			b = debugTable[i][1];
			i = i + 1;
			System.out.println("a: "+a+" b: "+b+" result: ");
			try {
				System.out.println(var4.solve(a, b));
			} catch (IllegalArgumentException e) {
				System.out.println("EXCEPTION!" + e.getMessage());
			}
		}
	}
}

class Variant4 {
	private double i = 1;
	private double k = 30;
	private double result;
	
	public double solve(double a, double b) {
		double finalResult = 0;
		while (i <= k) {
			result = sqrt(a*i*sqrt(b/i));
			finalResult = finalResult + result;
			i += 1;
		}
		i = 1;
		return finalResult;
	};
}