#!C:\Users\91876\Anaconda3\python.exe

import pymysql
from Conn_DB import MySQLConnection
import cgi, cgitb
cgitb.enable()
import requests


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
        if record is None:
            redirectURL = "http://192.168.1.103/htdocs/mail.html"
            r = requests.post(url = redirectURL)
            print(r.text)
            print('<html>')
            print('<body>')
            print('<center><h5 style="color:red">Invalid Customer ID or Mail !!!</h5></center>')
            print('</body>')
            print('</html>')
        else:
            print('<html>')
            print('<body>')
            print('<center><h2 style="color:red">Mail sent</h2></center>')
            print('</body>')
            print('</html>')
            

my_conn = MySQLConnection()
conn = my_conn.connection()
fpwd = forgetpassword()
fpwd.datavalidation(conn)
