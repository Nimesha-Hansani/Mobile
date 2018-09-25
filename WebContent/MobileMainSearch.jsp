<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Animated Search box [Pure CSS]</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Antic'>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div align="center">
  <div class="text">Mobile</div>
  <br>
  <form  action="MobileServlet" method="GET">
  <input class="button" type="text" name="searchtext"  placeholder="Search..." onkeypress="submitOnEnter(this, event);"/>
  </form>
  <br>
  <% 
     String name=(String)request.getAttribute("resultset");
     out.println(name);
     
   %>
  
  <script src='https://use.edgefonts.net/amaranth.js'>
   
  </script>
  </div>

</body>
</html>