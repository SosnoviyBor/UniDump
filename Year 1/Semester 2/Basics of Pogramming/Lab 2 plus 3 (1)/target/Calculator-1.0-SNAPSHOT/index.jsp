<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="com.example.Calculator.Util" %>
<!DOCTYPE html>
<html>
<head>
    <title>OP. Lab 2</title>
</head>
<body>
<%!Util utils = new Util(); %>
<h1 style="text-decoration: underline">Welcome to second lab work!</h1><br/>
<form method="post" action="CalculatorServlet">
    <input type="radio" id="formula_1" name="formula" value="1"> <img src="formula1.png" style="vertical-align:middle"><br><br>
    <input type="radio" id="formula_2" name="formula" value="2"> <img src="formula2.png" style="vertical-align:middle"><br><br>
    <input type="radio" id="formula_3" name="formula" value="3"> <img src="formula3.png" style="vertical-align:middle"><br><br>

    <%Cookie[] cookies = request.getCookies();%>

    <label>a: </label> <input type="text" id="a" name="a_field" value="<%=utils.initCookieValGet(cookies,"a_val")%>"> <br><br>
    <label>b: </label> <input type="text" id="b" name="b_field" value="<%=utils.initCookieValGet(cookies,"b_val")%>"> <br><br>
    <label>c: </label> <input type="text" id="c" name="c_field" value="<%=utils.initCookieValGet(cookies,"c_val")%>"> <br><br>
    <label>d: </label> <input type="text" id="d" name="d_field" value="<%=utils.initCookieValGet(cookies,"d_val")%>"> <br><br>
    <input type="submit" value="Calculate">

    <p>${result}</p>
</form>
</body>
</html>