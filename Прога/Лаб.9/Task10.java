class Task10 {
	public static void main (String args[]){
		String in = "The user with the nickname koala757677 this month wrote 3 times more comments than the user with the nickname croco181dile920 4 months ago";
		String out = stringScreamer(in);
		System.out.println("#################\n    Input: \n"+in+"\n#################\n    Output: \n"+out+"\n#################");
	}

	static String stringScreamer(String s) {
		String result = "";
		for (int i = 0; i < s.length(); i++) {
			result += s.charAt(i);
		}
		return result.toUpperCase();
	}
}