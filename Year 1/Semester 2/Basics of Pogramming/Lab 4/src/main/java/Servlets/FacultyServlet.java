package Servlets;

import Logic.AdditionalFunc;
import Logic.Faculty;
import Logic.Institute;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "FacultyServlet", value = "/FacultyServlet")
public class FacultyServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String institute = request.getParameter("institutes");
        if ("all".equals(institute)) {
            request.setAttribute("faculties", AdditionalFunc.allFaculties());
        }
       else {
            for (Institute inst: AdditionalFunc.institutes)
             if (inst.getName().equals(institute)) {
                 request.setAttribute("faculties",inst.getFaculties());
             }
        }
        request.getRequestDispatcher("WEB-INF/jsp/Faculties.jsp").forward(request,response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
