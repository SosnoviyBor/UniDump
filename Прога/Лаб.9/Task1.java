class Task1 {
	public static void main (String args[]){
		int inp = 51966;
		String word = intToHexString(inp);
		System.out.println("Input: "+inp+"\nResult: "+word);
	}

	static String intToHexString(int i) {
		return Integer.toHexString(i).toUpperCase();
	}
}