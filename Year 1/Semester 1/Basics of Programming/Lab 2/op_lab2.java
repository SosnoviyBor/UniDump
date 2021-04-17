import static java.lang.Math.*;

class Lab2 {
    public static void main(String[] args) {
        Variant9 var9 = new Variant9();
        System.out.println("Variant #9, result = " + var9.solve());
        Variant19 var19 = new Variant19();
        System.out.println("Variant #19, result = " + var19.solve());
        Variant29 var29 = new Variant29();
        System.out.println("Variant #99, result = " + var29.solve());
    }
}

class Variant9 {
    private double a = -2.98;
    private double b = 5.55;
    private double c = 0.045;
    private double d = 0.129;
    public double solve() {
        double y = (sin(abs(a))+cos(sqrt(b))) / (2*tan(c)+exp(d));
        return y;
    }
}

class Variant19 {
    private double a = 1.234;
    private double b = -3.12;
    private double c = 5.45;
    private double d = 2.0;
    public double solve() {
        double y = (pow(tan(a), c) / (1+cosh(log(d+c))));
        return y;
    }
}

class Variant29 {
    private double a = -2.86;
    private double b = 1.62;
    private double c = 10.874;
    private double d = 2.19;
    public double solve() {
        double y = pow(2*cos(sqrt(a/b)+4*log(d+sqrt(pow(a, 2)+1))), c);
        return y;
    }
}