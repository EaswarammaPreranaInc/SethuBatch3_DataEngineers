#Repeat  prog8b(fetchmany)  but  validate  input
#i.e. Print  a  msg  when  input > number  of  tuples
#Hint:  Use  fetchmany()  method
import mysql.connector as ms
con=ms.connect(database='sssdc', user='root')
cur=con.cursor()
n=int(input("Enter how many rows : "))
try:
    cur.execute(f'select * from emp;')
    list=cur.fetchmany(n)
    if n<=0 or n>len(list):
        print("Invalid input")
    else:
        for c in cur.description():
            print(f"{c[0]:^10}, end='\t'")
        for tpl in list:
            for x in tpl:
                print(f"{x:^10}, end='\t'")
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid  database  (or)  user  (or)  password  (or)  tablename')
except mc.errors.InterfaceError:
    print("Database is not connected")

## Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql.connector as mc
try:
    con=mc.connect(database='sssdc',user='root')
    cur=con.cursor()
    n=int(input("How many rows ? : "))
    list=[]
    for i in range(n):
        tpl=()
        empno=int(input("Enter rno : "))
        ename=input("Enter name : ")
        sal=float(input("Enter salary : "))
        tpl=(empno,ename,sal)
    list.append(tpl)
    cur.executemany("insert into emp values(%s,%s,%s)", list)
    print(f"{cur.rowcount()} rows are inserted")
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print("Table name or user name doenot exist")
except mc.errors.InterfaceError:
    print("Database not connected")

