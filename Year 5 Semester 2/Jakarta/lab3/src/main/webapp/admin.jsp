<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Адмінка</title>
</head>
<body>
<div class="wrapper">
    <a href="/queue/<c:out value="${queueId}"/>/>">Назад</a>
    <h1>Адмінка</h1>
    <%--@elvariable id="queueId" type="int"--%>
    <%--@elvariable id="queueName" type="java.lang.String"--%>
    <%--@elvariable id="isQueueOpen" type="boolean"--%>
    <h3 id="queue-name">
        <c:out value="${queueName}"/>
    </h3>
    Користувачі в черзі:
    <ol id="userList">
        <%--@elvariable id="users" type="java.util.ArrayList"--%>
        <c:forEach var="user" items="${users}">
            <li class="user" id="<c:out value="${user['id']}"/>">
                <c:out value="${user['name']}"/>
                <input type="checkbox" class="confirmation">
                <button class="delete-user" id="<c:out value="${user['id']}"/>">❌</button>
            </li>
        </c:forEach>
    </ol>
    <p>Статус: <a id="status"></a></p>
    <hr>
    <button id="delete-first">Видалити першого в черзі</button>
    <button id="update-queue-status">Закрити/відкрити чергу</button>
</div>
<div id="data"
     data-queue-id="<c:out value="${queueId}"/>"
     data-is-open="<c:out value="${isQueueOpen}"/>">
</div>
<script type="text/javascript" src="<%= request.getContextPath() %>/js/admin.js"></script>
</body>
</html>
