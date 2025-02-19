package org.labs.intro;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(name = "memberServlet", value = "/members/*")
public class MemberServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        String path;
        ServletContext servletContext = getServletContext();

        String pathInfo = request.getPathInfo();
        String[] urlParts = pathInfo.split("/");
        int id = Integer.parseInt(urlParts[urlParts.length - 1]);

        if (id == 1) {
            path = "/member-1.html";
        } else if (id == 2) {
            path = "/member-2.html";
        } else {
            path = "/member-3.html";
        }

        RequestDispatcher requestDispatcher = servletContext.getRequestDispatcher(path);
        requestDispatcher.forward(request, response);
    }
}
