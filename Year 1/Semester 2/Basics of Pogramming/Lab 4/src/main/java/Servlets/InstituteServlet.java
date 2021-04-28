package Servlets;

import Logic.AdditionalFunc;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;

@WebServlet(name = "InstituteServlet", value = "/InstituteServlet")
public class InstituteServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            request.setAttribute("institutes", AdditionalFunc.institutes);
            request.getRequestDispatcher("WEB-INF/jsp/Institues.jsp").forward(request,response);
    }
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
