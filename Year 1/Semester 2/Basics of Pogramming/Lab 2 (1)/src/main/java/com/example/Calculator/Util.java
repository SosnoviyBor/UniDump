package com.example.Calculator;

public class Util {
    private Util(){
    }

    private static Util instance;
    public static Util getInstance() {
        if (instance == null) {
            instance = new Util();
        }
        return instance;
    }

    public String unnulifier(String parameter) {
        if (parameter == null) {
            return "";
        } else {
            return parameter;
        }
    }

    public String htmlCode =           // For the love of God, don't watch code below. I've warned you >:(
        "<!DOCTYPE html>\n" +
        "<html>\n" +
        "<head>\n" +
        "    <title>OP. Lab 2</title>\n" +
        "</head>\n" +
        "<body>\n" +
        "<h1 style=\"text-decoration: underline\">Welcome to second lab work!</h1><br/>\n" +
        "<form method=\"get\" action=\"CalculatorServlet\">\n" +
        "    <input type=\"radio\" id=\"formula_1\" name=\"formula\" value=\"1\"> <img src=\"formula1.png\" style=\"vertical-align:middle\"><br><br>\n" +
        "    <input type=\"radio\" id=\"formula_2\" name=\"formula\" value=\"2\"> <img src=\"formula2.png\" style=\"vertical-align:middle\"><br><br>\n" +
        "    <input type=\"radio\" id=\"formula_3\" name=\"formula\" value=\"3\"> <img src=\"formula3.png\" style=\"vertical-align:middle\"><br><br>\n" +
        "\n" +
        "    <label>a: </label> <input type=\"text\" id=\"a\" name=\"a_field\" value=\"%s\"> <br><br>\n" +
        "    <label>b: </label> <input type=\"text\" id=\"b\" name=\"b_field\" value=\"%s\"> <br><br>\n" +
        "    <label>c: </label> <input type=\"text\" id=\"c\" name=\"c_field\" value=\"%s\"> <br><br>\n" +
        "    <label>d: </label> <input type=\"text\" id=\"d\" name=\"d_field\" value=\"%s\"> <br><br>\n" +
        "    <input type=\"submit\" value=\"Calculate\">\n" +
        "</form>\n" +
        "<p>%s</p>\n" +
        "</body>\n" +
        "</html>";
}
