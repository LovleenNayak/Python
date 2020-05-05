#!C:\Users\91876\Anaconda3\python.exe

#Import modules for CGI handling

import cgi, cgitb
cgitb.enable()

#create instance of FieldStorage

form = cgi.FieldStorage()

#Get data from fields

name = form.getvalue('uname')
password = form.getvalue('pwd')

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Wecolme</title>')
print('</head>')
print('<body>')
print('<center><h2>')
print('Welcome {}'.format(name))
print('</h2></center>')
print('</body>')
print('</html>')