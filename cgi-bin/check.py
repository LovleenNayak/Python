#!C:\Users\91876\Anaconda3\python.exe

import cgi, cgitb
#cgitb.enable()
import smtplib
from email.mime.text import MIMEText
import socket



print("Content-type:text/html\r\n\r\n")
socket.getaddrinfo('localhost', 8080)
msg = MIMEText("Got from script")
me = "bankingpython@gmail.com"
you = "lovleennayak92@gmail.com"
msg['Subject'] = "Password Chnage"
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()

print('<html>')
print('<body>')
print('<center><h5 style="color:red">Mail Sent</h5></center>')
print('</body>')
print('</html>')