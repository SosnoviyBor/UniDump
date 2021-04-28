<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Information</title>
</head>
<body>
<a href="./index.jsp"> Return to Main</a>
<h1>institutes</h1>
 <c:forEach var="institute" items="${requestScope.institutes}">
     Институт: ${ institute.name } <br>
     Кол-во студентов: ${institute.countStudents()} <br>
     Кол-во Факультетов ${institute.faculties.size()} <br>
     <form action="FacultyServlet"><button value="${institute.name}" name="institutes">Просмотреть все факультеты</button></form>
     <hr>
 </c:forEach>

</body>
</html>
