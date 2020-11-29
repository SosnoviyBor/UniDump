class lab4 {
	public static void main(String argv[]) {
		int[] table = {1,10,100,1000,10000};
		flipper(table);
		for (int i = 0; i < table.length; i++) {
			System.out.println(table[i]);
		}
	}

	static void flipper (int[] table) {
		int tmp;
		for (int i = 0; i < table.length/2; i++) {
			tmp = table[i];
			table[i] = table[table.length - i - 1];
			table[table.length - i - 1] = tmp;
		}
	}
}