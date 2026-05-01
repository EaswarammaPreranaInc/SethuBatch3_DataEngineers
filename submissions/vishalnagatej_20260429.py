import mysql.connector

mydb = mysql.connector.connect(
        host = 'root@localhost',
        username = 'root',
        password = ''
)

print(mydb)