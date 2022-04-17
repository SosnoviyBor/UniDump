package Servlets;

import Model.AdditionalFunc;
import Model.Faculty;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;

@WebServlet(name = "StudentServlet", value = "/StudentServlet")
public class StudentServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        AdditionalFunc additionalFunc = AdditionalFunc.getInstance();
        String faculty = request.getParameter("faculties");
        System.out.println(faculty);
        if ("all".equals(faculty)) {
            request.setAttribute("students", additionalFunc.allStudents());
        }
        else {
            for (Faculty faculty1: additionalFunc.allFaculties())
                if (faculty1.getName().equals(faculty)) {
                    request.setAttribute("students",faculty1.getStudents());
                }
        }
        request.getRequestDispatcher("WEB-INF/jsp/Students.jsp").forward(request,response);
    }
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
