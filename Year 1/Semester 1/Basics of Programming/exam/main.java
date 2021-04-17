class lab5 {
	public static void main (String[] argv) {
		int[][] scoreboard = {
		{0,2,0,1,1},
		{0,0,2,2,2},
		{0,0,0,2,0},
		{0,0,2,0,1},
		{1,0,2,2,0}
		};

		boolean matrixCheck = guard(scoreboard);
		if (matrixCheck == false) {
			System.out.println("Похоже, вы ввели неправильную таблицу");
			return;
		}

		boolean hasWon = isUnbalanced(scoreboard);
		if (hasWon) {
			System.out.println("Да, хотя бы одна команда и впрямь выиграла больше половины матчей");
		}	else {System.out.println("Ко всеобщему удивлению ни одна команда не выиграла больше половины матчей");}
	}

	static boolean guard (int[][] scoreboard) {
		if (scoreboard.length != scoreboard[0].length) {
			return false;
		}
		for (int i = 0; i < scoreboard.length; i++) {
			if (scoreboard[i][i] != 0) {
				return false;
			}
		}
		return true;
	}
	
	static boolean isUnbalanced (int[][] results) {
		int wins;
		for (int i = 0; i < results.length; i++) {
			wins = 0;
			for (int j = 0; j < results[i].length; j++) {
				if (results[i][j] == 2) {
					wins++;
				}
			}
			if (wins > (results.length-1)/2) {
				return true;
			}
		}
		return false;
	}
}