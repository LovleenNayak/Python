#!C:\Users\91876\Anaconda3\python.exe

#import and connect to Database

import pymysql
from Conn_DB import MySQLConnection
import cgi, cgitb
cgitb.enable()
import requests

class LogIn:
    def validate(self,conn):
        print("Content-type:text/html\r\n\r\n")
        form = cgi.FieldStorage()
        name = form.getvalue('uname')
        pwd = form.getvalue('pwd')
        sql = 'SELECT * FROM customer WHERE CustID = %s AND Pwd = %s'
        val = (name,pwd)
        my_cursor = conn.cursor()
        my_cursor.execute(sql,val)
        record = my_cursor.fetchone()
        my_cursor.close()
        conn.close()
        if record is None:
            redirectURL = "http://192.168.1.103/htdocs/home.html"
            r = requests.post(url = redirectURL)
            print(r.text)
            print('<html>')
            print('<body>')
            print('<center><h5 style="color:red">Invalid username or Password !!!</h5></center>')
            print('</body>')
            print('</html>')
            
        else:
            print('<html>')
            print('<body>')
            print('<center><h2 style="color:blue">')
            cust_name = record[1]
            print("Welcome {}".format(cust_name))
            print('</h2></center>')
            print('</body>')
            print('</html>')
            redirectURL = "http://192.168.1.103/htdocs/user.html"
            r = requests.post(url = redirectURL)
            print(r.text)
            
            
my_conn = MySQLConnection()
conn = my_conn.connection()
login = LogIn()
login.validate(conn)