import static java.lang.Math.*;

class number1 {
	public static void main(String[] args) {
		Variant1 var1 = new Variant1();

		double[] debugTable = {1, 2, 0, -1, -2, Double.MAX_VALUE, Double.NaN};
		
		int i = 0;
		double m;
		while (i<debugTable.length) {
			m = debugTable[i];
			i = i + 1;
			System.out.println("m: "+m+" result: ");
			try {
				System.out.println(var1.solve(m));
			} catch (IllegalArgumentException e) {
				System.out.println("EXCEPTION!" + e.getMessage());
			}
		}
	}
}

class Variant1 {
	private double i = 1;
	private double k = 30;
	private double result;
	
	public double solve(double m) {
		double finalResult = 0;
		while (i <= k) {
			result = sqrt(m/i)*sin(m*i);
			finalResult = finalResult + result;
			i += 1;
		}
		i = 1;
		return finalResult;
	};
}