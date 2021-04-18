#!C:\Users\arhan\AppData\Local\Microsoft\WindowsApps\python.exe -u
import cgi
import cgitb; cgitb.enable() 

print ("Content-type: text/html")

print ("""
<html>
<head><title>Sample CGI Script</title></head>
<body>
<script language = "javascript" type = "text/javascript">
         <!--
            document.write("Java script:This is for the sum of two numbers")
         //-->
</script>    

<h3> Sample CGI Script </h3>
""")

form = cgi.FieldStorage()

if "num_1" in form and "num_2" in form:
    message = form.getvalue("num_1" )
    message1 = form.getvalue("num_2" )

    print ("""<p> Sum : """) 
    print(int(message) + int(message1))
    

print("""</p>
 
<p>form
 
<form method="post" action="hello2.py">
<p>number1: <input type="number" name="num_1"/></p>
<p>number2: <input type="number" name="num_2"/></p>
<input type = "submit" value = "Submit" />
</form>
</body>
</html>
""") 



