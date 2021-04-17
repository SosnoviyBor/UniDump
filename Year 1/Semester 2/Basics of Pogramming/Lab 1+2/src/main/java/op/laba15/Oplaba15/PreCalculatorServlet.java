package op.laba15.Oplaba15;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "PreCalculatorServlet", value = "/PreCalculatorServlet")
public class PreCalculatorServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        PrintWriter out = response.getWriter();

        String a = request.getSession().getAttribute("A") == null ? "" : (String) request.getSession().getAttribute("A");
        String b = request.getSession().getAttribute("B") == null ? "" : (String) request.getSession().getAttribute("B");
        String c = request.getSession().getAttribute("C") == null ? "" : (String) request.getSession().getAttribute("C");
        String d = request.getSession().getAttribute("D") == null ? "" : (String) request.getSession().getAttribute("D");

        out.printf("<!DOCTYPE html>\n" +
                "<html lang=\"en\">\n" +
                "<head>\n" +
                "    <meta charset=\"UTF-8\">\n" +
                "    <title lang=\"ru\">Lab-16 Team-1</title>\n" +
                "</head>\n" +
                "<body>\n" +
                "    <form action=\"CalculatorServlet\">\n" +
                "        <label for=\"a\">A:</label> <input type=\"text\" id=\"a\" name=\"a\" value=\"%s\"><br>\n" +
                "        <label for=\"b\">B:</label> <input type=\"text\" id=\"b\" name=\"b\" value=\"%s\"><br>\n" +
                "        <label for=\"c\">C:</label> <input type=\"text\" id=\"c\" name=\"c\" value=\"%s\"><br>\n" +
                "        <label for=\"d\">D:</label> <input type=\"text\" id=\"d\" name=\"d\" value=\"%s\"><br>\n" +
                "\n" +
                "        <input type=\"radio\" id=\"equation1\" name=\"equation\" value=\"1\">\n" +
                "        <label for=\"equation1\"><img src=\"1.png\"></label><br>\n" +
                "\n" +
                "        <input type=\"radio\" id=\"equation2\" name=\"equation\" value=\"2\">\n" +
                "        <label for=\"equation2\"><img src=\"3.png\"></label><br>\n" +
                "\n" +
                "        <input type=\"radio\" id=\"equation3\" name=\"equation\" value=\"3\" >\n" +
                "        <label for=\"equation3\"><img src=\"2.png\"></label><br>\n" +
                "\n" +
                "        <input type=\"submit\" value=\"Calculate\">\n" +
                "\n" +
                "    </form>\n" +
                "</body>\n" +
                "</html>", a, b, c, d);

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
