<%-- 
    Document   : MenuUser
    Created on : 4/07/2017, 02:28:47 AM
    Author     : alejandro
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/style.css"/>
        <title>USAC Drive</title>
    </head>
    <body>
        <center><p><h1>Bienvenido <%= session.getAttribute("user") %></h1></p></center>
        <table border="0" width="1000" align="center">
             <tr bgcolor="skyblue">
                <th><a href="MenuUser.jsp">USAC Drive</a></th>
                <th><a href="index.jsp">Cerrar Sesíon</a></th> 
            </tr> 
        </table>
<%-- 
        <center>
        <p><h2>USAC Drive</h2></p><br>
        </center>
--%>
    
    </body>
</html>