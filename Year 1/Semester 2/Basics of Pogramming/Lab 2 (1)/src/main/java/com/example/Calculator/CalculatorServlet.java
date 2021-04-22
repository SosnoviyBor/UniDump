package com.example.Calculator;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "CalculatorServlet", value = "/CalculatorServlet")
public class CalculatorServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        PrintWriter writer = response.getWriter();
        Calculator calculator = Calculator.getInstance();
        Util utils = Util.getInstance();
        int defaultCookieAge = 2*24*60*60;

        String a = utils.unnulifier(request.getParameter("a_field"));
        String b = utils.unnulifier(request.getParameter("b_field"));
        String c = utils.unnulifier(request.getParameter("c_field"));
        String d = utils.unnulifier(request.getParameter("d_field"));
        String formula = utils.unnulifier(request.getParameter("formula"));
        String result;

        try {
            double calculationResult = calculator.calculate(a,b,c,d,formula);
            result = "Result: "+calculationResult;
        } catch (Throwable e) {
            result = "Something went wrong... " + e.getMessage();
        }

        response.addCookie(utils.newCookieGen("a_val", a, defaultCookieAge));
        response.addCookie(utils.newCookieGen("b_val", b, defaultCookieAge));
        response.addCookie(utils.newCookieGen("c_val", c, defaultCookieAge));
        response.addCookie(utils.newCookieGen("d_val", d, defaultCookieAge));

        writer.printf(utils.htmlCode, a, b, c, d, result);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
