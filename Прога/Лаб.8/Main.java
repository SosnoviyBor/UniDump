class Main {
	public static void main (String args[]) {

	}
}

class Shape {
	boolean isRound;
	double square() {
		return 0;
	}
}

class Rectangle extends Shape {
	private double length;
	private double width;

	Rectangle (double length, double width) {
		this.length = length;
		this.width = width;
	}
	Rectangle () {
		this.length = 0;
		this.width = 0;
	}
	Rectangle (Rectangle a) {
		this.length = a.length;
		this.width = a.width;
	}

	@Override
	double square () {
		return length*width;
	}

	Rectangle cutToSquare () {
		double side;
		if (width < length) {side = width;}
		else {side = length;}
		Rectangle res = new Rectangle(side, side);
		return res;
	}
	Rectangle expandToSquare () {
		double side;
		if (width < length) {side = length;}
		else {side = width;}
		Rectangle res = new Rectangle(side, side);
		return res;
	}
}