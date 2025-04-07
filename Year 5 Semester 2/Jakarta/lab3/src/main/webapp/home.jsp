<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <title>Електронна черга</title>
</head>
<body>
<div id="wrapper">
    <%--@elvariable id="queueList" type="java.util.ArrayList"--%>
    <c:if test="${queueList.size() > 0}">
        <div id="queue-list">
            <h2>Відкриті черги</h2>
            <c:forEach var="queue" items="${queueList}">
                <h3>
                    <a href="queue/${queue['id']}">
                        <c:out value="${queue['name']}"/>
                    </a>
                    (<c:out value="${queue['size']}"/> 👨)
                </h3>
            </c:forEach>
        </div>
        <hr>
    </c:if>
    <div>
        <h2>Створення нової черги</h2>
        <input type="text" id="new-queue-name" placeholder="Назва черги">
        <input type="password" id="new-queue-password" placeholder="Пароль адміністратора">
        <button id="new-queue-button">Створити</button>
    </div>
</div>
<script type="text/javascript" src="<%= request.getContextPath() %>/js/home.js"></script>
</body>
</html>
