import java.lang.Math;

class Main {
	public static void main (String args[]) {
		Rectangle r1 = new Rectangle(3,4);
		System.out.println(r1);
		System.out.println(r1.expandToSquare().toString());
		//Rectangle r2 = new Rectangle(4,4);
		//System.out.println(r2.toString());
		//System.out.println(r1.equals(r2));
	}
}

abstract class Shape {
	private String name;

	Shape (String name) {
		this.name = name;
	}

	String getName () {
		return name;
	}

	double getSquare () {
		return 0;
	}

	double getPerimeter () {
		return 0;
	}
}

class Rectangle extends Shape {
	private double length;
	private double width;

	Rectangle (double length, double width) {
		super("Rectangle");
		this.length = length;
		this.width = width;
	}
	Rectangle () {
		super("Rectangle");
		this.length = 0;
		this.width = 0;
	}

	@Override
	public String toString() {
		return "Shape{"+
		"name="+super.getName()+
		", length="+length+
		", width="+width+
		", square="+getSquare()+
		", perimeter="+getPerimeter()+"}";
	}

	double getSquare () {
		return length*width;
	}

	double getPerimeter () {
		return 2*(length+width);
	}

	double getLength () {
		return length;
	}

	double getWidth () {
		return width;
	}

	public boolean equals(Rectangle o) {
		if (o == this)
			return true;		
		if (!(o instanceof Rectangle))
			return false;
		
		Rectangle other = (Rectangle) o;
		
		if (this.width == other.getWidth() && this.length == other.getLength())
			return true;
		else
			return false;
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

class Circle extends Shape {
	private double radius;

	Circle (double radius) {
		super("Circle");
		this.radius = radius;
	}
	Circle () {
		super("Circle");
		this.radius = 0;
	}

	@Override
	public String toString() {
		return "Shape{"+
		"name="+super.getName()+
		", radius="+radius+
		", square="+getSquare()+
		", perimeter="+getPerimeter()+"}";
	}
	
	double getSquare () {
		return Math.PI*radius*radius;
	}

	double getPerimeter () {
		return 2*Math.PI*radius;
	}

	double getRadius () {
		return radius;
	}

	public boolean equals(Object o) {
		if (o == this)
			return true;		
		if (!(o instanceof Circle))
			return false;
		
		Circle other = (Circle) o;
		
		if (this.radius == other.getRadius())
			return true;
		else
			return false;
	}

	Circle createOneMore (double newRadius) {
		Circle res = new Circle (newRadius);
		return res;
	}
}