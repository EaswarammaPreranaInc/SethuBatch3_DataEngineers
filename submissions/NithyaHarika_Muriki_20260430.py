
# Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql.connector as mc
con = mc.connect(database = 'emp',host = 'localhost',root = 'Nithya@1234')
cur = con.cursor()
cur.execute("Select * from emp_demo")
n = int(input("How many rows would you like to insert? "))
for i in range(1,n+1):
    print("Employee :" ,i)
    empno= int(input("Enter employee number: "))
    ename = input("Enter emp name: ")
    sal=  float(input("Enter salary: "))
print(i,"rows inserted")
