<%@ page contentType="text/html; charset=UTF-8" import="Logic.Calculator" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>JSP</title>
</head>
<body>
<div> <img src="images/1.png" alt="formula"> </div>
<%!
    int fromA = 0, fromB = 0, fromC = 0, fromD = 0;
    int toA = 0, toB = 0, toC = 0, toD = 0;
    int stepA = 0, stepB = 0, stepC = 0, stepD = 0;
%>
<%
    fromA = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("fromA"));
    fromB = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("fromB"));
    fromC = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("fromC"));
    fromD = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("fromD"));
    toA = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("toA"));
    toB = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("toB"));
    toC = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("toC"));
    toD = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("toD"));
    stepA = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("stepA"));
    stepB = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("stepB"));
    stepC = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("stepC"));
    stepD = request.getParameter("fromA")==null?0:Integer.parseInt(request.getParameter("stepD"));

%>

<form action="index.jsp">
    a: from:<input type="text" name ="fromA" value="<%= fromA %>">
    to:<input type="text" name ="toA" value="<%= toA %>">
    step: <input type="text" name ="stepA" value="<%= stepA %>"> <br>

    b: from:<input type="text" name ="fromB" value="<%= fromB %>">
    to:<input type="text" name ="toB" value="<%= toB %>">
    step: <input type="text" name ="stepB" value="<%= stepB %>"> <br>

    c: from:<input type="text" name ="fromC" value="<%= fromC %>">
    to:<input type="text" name ="toC" value="<%= toC %>">
    step: <input type="text" name ="stepC" value="<%= stepC %>"> <br>

    d: from:<input type="text" name ="fromD" value="<%= stepD %>">
    to:<input type="text" name ="toD" value="<%= toD %>">
    step: <input type="text" name ="stepD" value="<%= stepD %>"> <br>
    <input type="submit" value="Calculate">
</form>
<%

//    int fromA = this.fromA;
//    int fromB = this.fromB;
//    int fromC = this.fromC;
//    int fromD = this.fromD;
//    int toA = this.toA;
//    int toB = this.toB;
//    int toC = this.toC;
//    int toD = this.toD;
    int stepA = this.stepA;
    int stepB = this.stepB;
    int stepC = this.stepC;
    int stepD = this.stepD;

    if (stepD!=0 || stepA!=0 || stepB!=0 ||stepC!=0) {
        out.write("" +
                "<table>\n" +
                "    <tr>\n" +
                "        <th>a</th>\n" +
                "        <th>b</th>\n" +
                "        <th>c</th>\n" +
                "        <th>d</th>\n" +
                "        <th>y</th>\n" +
                "    </tr>");

        if (stepA==0)
            stepA=Integer.MAX_VALUE;
        if (stepD==0)
            stepD=Integer.MAX_VALUE;
        if (stepB==0)
            stepB=Integer.MAX_VALUE;
        if (stepC==0)
            stepC=Integer.MAX_VALUE;

        for ( int i = fromA;i<=toA; i+=stepA) {
            if (stepA != Integer.MAX_VALUE) {
                out.write("<tr>" +
                        "<td>" + i + "</td>" +
                        "<td>" + fromB + "</td>" +
                        "<td>" + fromC + "</td>" +
                        "<td>" + fromD + "</td>" +
                        "<td>" + Calculator.calculate(i, fromB, fromC, fromD) + "</td>" +
                        "</tr>");
        }
            for (int k = fromB  ;k<=toB; k+=stepB) {
                if (stepB != Integer.MAX_VALUE) {
                    out.write("<tr>" +
                            "<td>" + i + "</td>" +
                            "<td>" + k + "</td>" +
                            "<td>" + fromC + "</td>" +
                            "<td>" + fromD + "</td>" +
                            "<td>" + Calculator.calculate(i, k, fromC, fromD) + "</td>" +
                            "</tr>");
            }
                for ( int l = fromC ;l<=toC; l+=stepC) {
                    if (stepC != Integer.MAX_VALUE) {
                        out.write("<tr>" +
                                "<td>" + i + "</td>" +
                                "<td>" + k + "</td>" +
                                "<td>" + l + "</td>" +
                                "<td>" + fromD + "</td>" +
                                "<td>" + Calculator.calculate(i, k, l, fromD) + "</td>" +
                                "</tr>");
                }
                    for (int o = fromD ;o<=toD; o+=stepD) {
                        if (stepD!=Integer.MAX_VALUE) {
                            out.write("<tr>" +
                                    "<td>" + i + "</td>" +
                                    "<td>" + k + "</td>" +
                                    "<td>" + l + "</td>" +
                                    "<td>" + o + "</td>" +
                                    "<td>" + Calculator.calculate(i, k, l, o) + "</td>" +
                                    "</tr>");
                        }
                    }
                }
            }
        }
    } else {

    }
%>
    </table>
<br/>
</body>
</html>
