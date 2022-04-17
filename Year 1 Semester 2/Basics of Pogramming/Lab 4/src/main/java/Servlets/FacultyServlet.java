package Servlets;

import Model.AdditionalFunc;
import Model.Institute;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;

@WebServlet(name = "FacultyServlet", value = "/FacultyServlet")
public class FacultyServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String institute = request.getParameter("institutes");
        AdditionalFunc additionalFunc = AdditionalFunc.getInstance();
        if ("all".equals(institute)) {
            request.setAttribute("faculties", additionalFunc.allFaculties());
        }
       else {
            for (Institute inst: additionalFunc.getInstitutes())
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
