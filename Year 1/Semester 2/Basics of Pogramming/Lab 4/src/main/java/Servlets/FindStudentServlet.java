package Servlets;

import Logic.AdditionalFunc;
import Logic.Student;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;

@WebServlet(name = "FindStudentServlet", value = "/FindStudentServlet")
public class FindStudentServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
       String markBookInd = request.getParameter("markBookIndex");
       for (Student student: AdditionalFunc.allStudents()) {
           if (student.getMarkBookIndex().equals(markBookInd)){
               request.setAttribute("FoundedStudent",student);
           }
       }
       request.getRequestDispatcher("./index.jsp").forward(request,response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
