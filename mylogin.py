#!/usr/bin/env python3

# Import modules for CGI handling 
import cgi, cgitb 
import secret
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')


if username != None and password != None and username == secret.username and password == secret.password:
    print("Set-Cookie:UserID=ivan\r\n")
    print("Set-Cookie:Password=123\r\n")
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')

    print("""
    <h1> Hi, {username}! </h1>
    <p> <small> your password is:
        <span class="spoilers"> {password}</span>.
        </small>
    </p>
    """.format(username=username,
            password=password))
    print('</head>')
    print("<body>")
    print("<p> This is a body </p>")
    print("</body>")
    print('</html>')
else:
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print("<h1> Your password or username is wrong </h1>")

    print('</head>')
    print('</html>')