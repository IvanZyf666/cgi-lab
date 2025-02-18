# #!/usr/bin/env python3
# import cgi
# import cgitb

# import os

# # print all environment variables
# print("Content-type: text/html\r\n\r\n");
# print("<font size=+1>Environment</font><\br>");
# for param in os.environ.keys():
#    print("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))

# cgitb.enable()
# print()
# print()
# print("<p> QUERY_STRING: {}</p>".format(os.environ["QUERY_STRING"]))

#!/usr/bin/env python3
import os, json
import cgi
import cgitb


def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(r"""
    <h1> Welcome! </h1>
    <form method="POST" action="afterLogin.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>
        <button type="submit"> Login! </button>
    </form>
    """)


def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return ("""
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }
            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }
            label {
                display: flex;
                flex-direction: row;
            }
            label > span {
                flex: 0;
            }
            label> input {
                flex: 1;
            }
            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """ + page + """
    </body>
    </html>
    """)


print("Content-type:text/html\r\n\r\n")
print("<title>Lab3 CGI</title>")
cgitb.enable()
json_object = json.dumps(dict(os.environ), indent=4)

for param in os.environ.keys():
    if (param == "QUERY_STRING"):
        print("<br><b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if (param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
#
print(login_page())