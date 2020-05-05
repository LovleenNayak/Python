import pymysql

class MySQLConnection:
    def connection(self):
        conn = pymysql.connect("localhost","root","Abc@123","Banking")
        cursor = conn.cursor()
        #print("DataBase is connected")
        return conn
