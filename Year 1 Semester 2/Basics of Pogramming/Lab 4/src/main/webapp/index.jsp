<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>JSP - Hello World</title>
</head>
<body>
<form action="InstituteServlet">
    <button name="institutes" value="all">Показать все институты</button>
</form>
<form action="FacultyServlet">
        <button name="institutes" value="all">Показать все факультеты</button>
    </form>
<form action="StudentServlet">
    <button name="faculties" value="all">Показать всех студентов</button>
</form>
<br>
<br>
<form action="FindStudentServlet">
    <input type="text" name="markBookIndex" value="">
    <button type="submit"> Поиск сдудента за номером студенческого</button>
    <c:if test="${!empty requestScope.FoundedStudent }">
        <c:if test="${ requestScope.FoundedStudent!=null }">
            <br>
            По запросу найден студент,${requestScope.FoundedStudent.name},который учиться на ${requestScope.FoundedStudent.faculty.name}
            <br>
        </c:if>
    </c:if>
</form>
</body>
</html>