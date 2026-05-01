'''
1) Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples
Hint:  Use  fetchmany()  method
'''
import sqlite3
con = sqlite3.connect("sample.db")
cur = con.cursor()
cur.execute("select * from emp")
n = int(input("How many rows ? : "))
if n <= 0:
    print("Invalid input")
else:
    rows = cur.fetchmany(n)
    if len(rows) == 0:
        print("Invalid input")
    else:
        print("empno   ename   sal")
        i = 0
        while i < len(rows):
            print(rows[i][0], "   ", rows[i][1], "   ", rows[i][2])
            i = i + 1
        if n > len(rows):
            print("Requested rows exceed available data")
        print("Number of rows :", len(rows))
cur.close()
con.close()
'''
2) # Write  a  program  to  insert  multiple  rows  into  emp  table
'''
import sqlite3
con = sqlite3.connect("sample.db")
cur = con.cursor()
n = int(input("How many rows would you like to insert ? : "))
if n <= 0:
    print("Invalid input")
else:
    i = 1
    while i <= n:
        print("Employee :", i)
        empno = int(input("Enter employee number : "))
        ename = input("Enter employee name : ")
        sal = float(input("Enter salary : "))
        cur.execute("insert into emp values(?,?,?)", (empno, ename, sal))
        i = i + 1
    con.commit()
    print(n, "rows are inserted")
cur.close()
con.close()