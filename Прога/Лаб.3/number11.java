import static java.lang.Math.*;

class number11 {
	public static void main(String[] args) {
		Variant11 var11 = new Variant11();

		double[] debugTable = {1, 1.5, 1.6, 1.64, 1.644};
		
		int i = 0;
		double e;
		while (i<debugTable.length) {
			e = debugTable[i];
			i = i + 1;
			if (e > 0) {
				System.out.println("e: "+e+" result: ");
				try {
					System.out.println(var11.solve(e));
				} catch (IllegalArgumentException error) {
					System.out.println("EXCEPTION!" + error.getMessage());
				}
			}
		}
	}
}

class Variant11 {
	public double solve(double e) {
		double i = 1;
		double finalResult = 0;
		while (abs(finalResult) < e) {
			double result = 1/pow(i, 2);
			finalResult = finalResult + result;
			i += 1;
		}
		return finalResult;
	};
}