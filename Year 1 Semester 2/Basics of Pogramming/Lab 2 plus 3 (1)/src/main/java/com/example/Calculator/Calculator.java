package com.example.Calculator;

public class Calculator {

    public double calculate(String a, String b, String c, String d, String formula) throws IllegalStateException {
        double newA = Double.parseDouble(a);
        double newB = Double.parseDouble(b);
        double newC = Double.parseDouble(c);
        double newD = Double.parseDouble(d);

        double result = 0;
        switch (formula) {
            case ("1"):
                result = Math.sqrt(Math.abs(Math.sin(newA) - 4 * Math.log(newB) / Math.pow(newC, newD)));
                break;
            case ("2"):
                result = (Math.pow(Math.E, newA) + 3 * Math.log(newC)) / Math.pow(newB, newC / 2) * Math.abs(Math.atan(newD));
                break;
            case ("3"):
                result = Math.pow(2 * Math.sin(newA) + Math.cos(Math.abs(newB * Math.sqrt(newC))), newD);
                break;
            default:
                throw new IllegalStateException("Equation type has not been chosen");
        }
        return result;
    }
}
