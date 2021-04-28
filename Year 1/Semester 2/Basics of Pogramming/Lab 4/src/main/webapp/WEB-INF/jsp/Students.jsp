<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: Heheh
  Date: 3/30/2021
  Time: 8:46 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Students</title>
</head>
<body>
<a href="./index.jsp"> Return to Main</a>
    <h1>hello from students</h1>
    <c:forEach var="student" items="${requestScope.students}">
        Институт: ${ student.name } <br>
        номер залікової книжки: ${student.markBookIndex} <br>
        середній бал ${student.GPA} <br>
        <hr>
    </c:forEach>
</body>
</html>
