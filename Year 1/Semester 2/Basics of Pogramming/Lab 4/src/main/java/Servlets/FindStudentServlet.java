package Servlets;

import Model.AdditionalFunc;
import Model.Student;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.util.ArrayList;

@WebServlet(name = "FindStudentServlet", value = "/FindStudentServlet")
public class FindStudentServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        AdditionalFunc additionalFunc = AdditionalFunc.getInstance();
       String markBookInd = request.getParameter("markBookIndex");
       for (Student student: additionalFunc.allStudents()) {
           if (student.getMarkBookIndex().equals(markBookInd)){
               request.setAttribute("FoundedStudent",student);
               break;
           }
       }
       request.getRequestDispatcher("./index.jsp").forward(request,response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
