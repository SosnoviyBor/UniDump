<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%--
  Created by IntelliJ IDEA.
  User: Heheh
  Date: 3/30/2021
  Time: 7:25 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Information</title>
</head>
<body>
<a href="./index.jsp"> Return to Main</a>
<h1>institutes</h1>
 <c:forEach var="institute" items="${requestScope.institutes}">
     Институт:  <c:out value="${ institute.name }"/> <br>
     Кол-во студентов: <c:out value="${institute.countStudents()}"/> <br>
     Кол-во Факультетов  <c:out value="${institute.faculties.size()}"/>  <br>
     <form action="FacultyServlet"><button value="${institute.name}" name="institutes">Просмотреть все факультеты</button></form>
     <hr>
 </c:forEach>

</body>
</html>
