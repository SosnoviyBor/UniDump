package op.laba15.Oplaba15;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

@WebServlet(name = "CalculatorServlet", value = "/CalculatorServlet")
public class CalculatorServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        // Hello
        String aParam = request.getParameter("a");
        String bParam = request.getParameter("b");
        String cParam = request.getParameter("c");
        String dParam = request.getParameter("d");
        String typeOfEquation = request.getParameter("equation");


        PrintWriter out = response.getWriter();
        out.println("<html><head><title>Cool calculator</title></head><body>");
        try {
            double result = CalculatorLab16.calculateEquation(aParam, bParam, cParam, dParam, typeOfEquation);
            request.getSession().setMaxInactiveInterval(60 * 60 * 24 * 2); //Это в секундах
            String currentData = String.format("-a:%s|b:%s|c:%s|d:%s|%s|result:%s", aParam, bParam, cParam, dParam, typeOfEquation, result);
            String prevData = (String) request.getSession().getAttribute("StoredData");
            String newData = prevData == null ? currentData : prevData + currentData;
            request.getSession().setAttribute("StoredData", newData);

            request.getSession().setAttribute("A", aParam);
            request.getSession().setAttribute("B", bParam);
            request.getSession().setAttribute("C", cParam);
            request.getSession().setAttribute("D", dParam);


            out.printf("<h2>The result is: %f</h2>", result);
            if (newData != null) {
                out.println("<b>Calculator History:</b>");
                for (String paramsForDifferentEquation : newData.split("-")) {
                    out.println("<p>");
                    int dumpCounter = 0;
                    for (String params : paramsForDifferentEquation.split("\\|")) {
                        if (dumpCounter == 4) {
                            out.printf("<img src=\"%s.png\">", params);
                        } else {
                            out.println(params + " ");
                        }
                        dumpCounter++;
                    }
                    out.println("</p>");
                }
            }
        } catch (Throwable e) {
            out.printf("<h2>%s</h2>", "Something went wrong");
        }
        out.println("</body></html>");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

}
