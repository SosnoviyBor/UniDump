<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%--@elvariable id="queueName" type="java.lang.String"--%>
    <title><c:out value="${queueName}"/></title>
</head>
<body>
<div id="wrapper">
    <a href="<c:url value="/home"/>">Назад</a>
    <%--@elvariable id="queueId" type="int"--%>
    <h2 id="queue-name">
        <c:out value="${queueName}"/>
    </h2>
    Користувачі в черзі:
    <ol id="userList">
        <%--@elvariable id="users" type="java.util.ArrayList"--%>
        <c:forEach var="user" items="${users}">
            <li id="<c:out value="${user['id']}"/>">
                <c:out value="${user['name']}"/>
            </li>
        </c:forEach>
    </ol>
    <p>Статус: <a id="status"></a></p>
    <hr>
    <%--@elvariable id="isQueueOpen" type="java.lang.Boolean"--%>
    <div id="new-user-form">
        <h3>Додати користувача до черги</h3>
        <input id="new-user-name" type="text" placeholder="Ваше ім'я">
        <button id="new-user-submit">Додати</button>
    </div>
    <div id="login-form">
        <h3>Зайти як хазяїн черги</h3>
        <input id="login-password" type="password" placeholder="Пароль">
        <button id="login-submit">Зайти</button>
    </div>
</div>
<div id="data"
     data-queue-id="<c:out value="${queueId}"/>"
     data-is-open="<c:out value="${isQueueOpen}"/>">
</div>
<script type="module" src="<%= request.getContextPath() %>/js/queue.js"></script>
</body>
</html>
