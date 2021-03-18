package op.laba15.Oplaba15;

import java.io.*;
import java.util.Enumeration;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

@WebServlet(name = "helloServlet", value = "/hello-servlet")
public class HelloServlet extends HttpServlet {
    private String message;

    public void init() {
        message = "Hello World!";
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");

        // Hello
        PrintWriter out = response.getWriter();
        out.println("Header:<br/>");
        for (Enumeration<String> names = request.getHeaderNames();
             names.hasMoreElements(); ) {
            String name = names.nextElement();
            out.print(name + ": ");

            for (Enumeration<String> values = request.getHeaders(name);
                 values.hasMoreElements(); ) {
                String value = values.nextElement();
                out.print(value + ";");
            }
            out.println("<br/>");
        }
        out.println("DataSegment:" + request.getSession().getAttribute("StoredData") + "<br>");
        out.printf("a:%s  b:%s  c:%s  d:%s", request.getSession().getAttribute("A"), request.getSession().getAttribute("B"),
                request.getSession().getAttribute("C"), request.getSession().getAttribute("D"));
    }

    public void destroy() {
    }
}