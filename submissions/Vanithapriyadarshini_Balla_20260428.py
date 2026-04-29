#Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method
#emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
#   execute()                                 fetchone()             print()
import mysql.connector
con=mysql.connector.connect(database='sssdc',user='root',password='',host='localhost')
cur=con.cursor()
cur.execute('select * from emp;')
while True:
    tpl=cur.fetchone()
    if tpl is None:
        break
    print(tpl)

#Write  a  program  to  print  emp  table  based  on  user  condition
import mysql.connector
con=mysql.connector.connect(databse='sssdc', user='root', password='', host='localhost')
cur=con.cursor()
cond=input("Enter condition : ")
cur.execute(f'select * from emp where {cond};')
while True:
    tpl=cur.fetchone()
    if tpl is None:
        break
    print(tpl)

#Write  a  program  to  print  emp  table  in  sorted  order --

import mysql.connector
con=mysql.connector.connect(databse='sssdc', user='root', password='', host='localhost')
cur=con.cursor()
cond=input("Enter condition : ")
cur.execute(f'select * from emp where {cond};')
while True:
    tpl=cur.fetchone()
    if tpl is None:
        break
    print(tpl)

#Write  a  program  to  print  user  input  table  with  next()  function
import mysql.connector
con=mysql.connector.connect(databse='sssdc', user='root', password='', host='localhost')
cur=con.cursor()
table=input("Enter condition : ")
cur.execute(f'select * from {table};')
while True:
    try:
        tpl=next(cur)
        print(tpl)
    except:
        break

#Write  a  program  to  print  cursor  with  fetchall()  method
import mysql.connector
con=mysql.connector.connect(databse='sssdc', user='root', password='', host='localhost')
cur=con.cursor()
cur.execute(f'select * from emp;')
list=cur.fetchall()
for x in list:
    print(x)

#find outputs
for  i  in   range(4):  #  i = 2
	for   i   in  range(2): #  i = 1
			pass
	print(i)# i=1..... 1, 1, 1, 1







