#!/usr/bin/env python3
import os
import templates
import cgi
import secret
import json
json_obj = json.dumps(dict(os.environ), indent=4)
#print(json_obj)

print(templates.login_page())

storage = cgi.FieldStorage()
if len(storage)  > 0:
    print(storage['username'])
    print(storage['password'])
    
    if storage['password'].value == secret.password and storage['username'].value == secret.password:
        print('Set-Cookie:UserID = %s;\r\n'%(secret.username))
        print('Set-Cookie:Password = %s;\r\n'%(secret.password))
        print('SET-Cookie:Expires = Tuesday, 31-Dec-2100 23:12:40')
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>Test CGI</title>")
        print("</head>")
        print(templates.secret_page(secret.password, secret.password))
        print("</html>")
        print(templates.secret_page(secret.password, secret.password))
