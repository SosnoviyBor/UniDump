<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: Heheh
  Date: 3/30/2021
  Time: 9:05 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Information</title>
</head>
<body>
<a href="./index.jsp"> Return to Main</a> <br>
<c:forEach var="faculty" items="${requestScope.faculties}">
    Faculty: ${ faculty.name } <br>
    Кол-во студентов: ${faculty.countStudents()} <br>
    <form action="StudentServlet"><button value="${faculty.name}" name="faculties">Просмотреть студентов этого факультета</button></form>
    <hr>
</c:forEach>
</body>
</html>
