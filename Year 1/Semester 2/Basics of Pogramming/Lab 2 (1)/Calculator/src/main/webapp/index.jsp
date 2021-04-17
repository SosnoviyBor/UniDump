<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>OP. Lab 2</title>
</head>
<body>
<h1><%= "Hello World!" %>
</h1>
<br/>
<form method="post" action="CalculatorServlet">
    <input type="radio" id="formula_1" name="formula" value="1">
    <label for="formula_1"> <img src="formula1.png"> </label><br><br>

    <label>a: </label> <input type="text" id="a" name="a_field"> <br><br>
    <label>b: </label> <input type="text" id="b" name="b_field"> <br><br>
    <label>c: </label> <input type="text" id="c" name="c_field"> <br><br>
    <label>d: </label> <input type="text" id="d" name="d_field"> <br><br>
    <input type="submit" value="Calculate">
</form>
<a href="hello-servlet">Hello Servlet</a>
</body>
</html>