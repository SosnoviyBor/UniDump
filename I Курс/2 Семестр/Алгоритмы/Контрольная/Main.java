public class Main {
	public static void main(String[] args) {
		int[] sparseTable = {0,1,0,0,0,8,0,7,0,4,0,0,6,0};

		SparseTable test = new SparseTable(sparseTable);
		test.set(1, 20);
		System.out.println(test.get(20));
	}
}