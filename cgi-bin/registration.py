#!C:\Users\91876\Anaconda3\python.exe

#import and connect to Database

import pymysql
from Conn_DB import MySQLConnection
import random
from random import randint
import string
import cgi, cgitb
import time
from datetime import datetime
cgitb.enable()

class Password:
    def randomString(self,stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(stringLength))
class registration:
    def read_data(self,conn):
        print("Content-type:text/html\r\n\r\n")
        form = cgi.FieldStorage()
        fname = form.getvalue('fname')
        lname = form.getvalue('lname')
        dob = form.getvalue('dob')
        deposite = int(form.getvalue('amount'))
        mnum = int(form.getvalue('mnum'))
        email = form.getvalue('email')
        cust_id = randint(100000,999999)
        Pass = Password()
        pwd = Pass.randomString(8)
        Date_Of_Birth = datetime.strptime(dob,'%d-%m-%Y')
        sql = 'INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (cust_id,fname,lname,Date_Of_Birth,pwd,deposite,mnum,email)
        my_cursor = conn.cursor()
        my_cursor.execute(sql,val)
        conn.commit()
        my_cursor.close()
        conn.close()
        url = "http://localhost/htdocs/home.html"
        print('<html>')
        print('<body>')
        print('<center>')
        print("Customer ID : {}".format(cust_id))
        print('<br>')
        print("Password : {}".format(pwd))
        print('<br>')
        print("Please note Customer ID and Password")
        print('<br>')
        print("Please"'<a href ="{}">click here</a>'"to login".format(url))
        print('</center>')
        print('</body>')
        print('</html>')

my_conn = MySQLConnection()
conn = my_conn.connection()
reg = registration()
reg.read_data(conn)