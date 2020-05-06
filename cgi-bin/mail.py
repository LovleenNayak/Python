#!C:\Users\91876\Anaconda3\python.exe

import pymysql
from Conn_DB import MySQLConnection
import cgi, cgitb
cgitb.enable()
import random
from random import randint
import string
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class forgetpassword:
    def datavalidation(self,conn):
        print("Content-type:text/html\r\n\r\n")
        form = cgi.FieldStorage()
        cust_id = form.getvalue('custid')
        mail = form.getvalue('email')
        sql = 'SELECT * FROM customer WHERE CustID = %s AND email = %s'
        val = (cust_id,mail)
        my_cursor = conn.cursor()
        my_cursor.execute(sql,val)
        record = my_cursor.fetchone()
        my_cursor.close()
        conn.close()
        return record
    def randomString(self,stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(stringLength))
    def sendMail(self,record,pwd):
        mail_content = '''Hello,
        This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
        Generated Password is : '''+pwd+'''
        Thank You
        '''
        #The mail addresses and password
        sender_address = 'bankingpython@gmail.com'
        sender_pass = 'lovlin@88'
        receiver_address = record[7]
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        url = "http://localhost/htdocs/home.html"
        print('<html>')
        print('<body>')
        print('<center><h5 style="color:red">Mail has been sent to registred email.id</h5></center>')
        print("Please"'<a href ="{}">click here</a>'"to login".format(url))
        print('</body>')
        print('</html>')
    def updatetable(self,conn,pwd,record):
        conn.ping(reconnect = True)
        sql = 'UPDATE CUSTOMER SET pwd = %s WHERE CustID = %s'
        val = (pwd,record[0])
        my_cursor2 = conn.cursor()
        my_cursor2.execute(sql,val)
        conn.commit()
        my_cursor2.close()
my_conn = MySQLConnection()
conn = my_conn.connection()
fpwd = forgetpassword()
record = fpwd.datavalidation(conn)
if record is None:
    redirectURL = "http://localhost/htdocs/mail.html"
    r = requests.post(url = redirectURL)
    print(r.text)
    print('<html>')
    print('<body>')
    print('<center><h5 style="color:red">Invalid Customer ID or Mail !!!</h5></center>')
    print('</body>')
    print('</html>')
else:
    temp_pwd = fpwd.randomString(8)
    fpwd.updatetable(conn,temp_pwd,record)
    fpwd.sendMail(record,temp_pwd)
    
