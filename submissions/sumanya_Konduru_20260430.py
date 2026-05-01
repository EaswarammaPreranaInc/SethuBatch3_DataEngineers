'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''



'''import mysql.connector as ms
try:
    con = ms.connect(
        host="localhost",
        user="root",
        password="chandrika@123",
        database="empdb"
    )
    cur = con.cursor()
    cur.execute("select count(*) from emp")
    total = cur.fetchone()[0]
    n = int(input("How many rows ? : "))
    if n <= 0 or n > total:
        print("Invalid input")
    else:
        cur.execute("select * from emp")
        rows = cur.fetchmany(n)

        print("empno\tename\tsal")
        for i in rows:
            print(i[0], "\t", i[1], "\t", i[2])

        print("Number of rows :", len(rows))

    cur.close()
    con.close()
except  ms . errors . ProgrammingError:
	print('Invalid  database  (or)  user  (or)  password  (or)  tablename')
except  ms . errors . InterfaceError:
	print('Pls  start  mysql')
 '''
 
 # Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql.connector as mc
try:
    con = mc.connect(
        host="localhost",
        user="root",
        password="chndrika@123",
        database="empdb"
    )
    cur = con.cursor()
    emp_list = []
    n = int(input("How many rows would you like to insert ? "))
    for i in range(1, n+1):
        print("Employee :", i)
        eno = int(input("Enter employee number : "))
        name = input("Enter employee name : ")
        sal = float(input("Enter salary : "))
        t = (eno, name, sal)   
        emp_list.append(t)     
    for x in emp_list:
        cur.execute("insert into emp values(%s,%s,%s)", x)
    con.commit()
    print(n, "rows are inserted")
    cur.execute("select * from emp")
    print("empno\t ename\t sal")
    for row in cur.fetchall():
        print(row[0], "\t", row[1], "\t", row[2])
    cur.close()
    con.close()
except  mc . errors . ProgrammingError:
	print('Invalid  database  (or)  user  (or)  password  (or)  tablename')
except  mc . errors . InterfaceError:
	print('Pls  start  mysql')