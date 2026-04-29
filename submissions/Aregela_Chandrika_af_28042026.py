'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="database"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM emp")
row = cursor.fetchone()

while row is not None:
    print(row)   
    row = cursor.fetchone()
cursor.close()
conn.close()



'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''


import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="database"
)
cur = conn.cursor()
cond = input("Enter condition (e.g., salary > 50000): ")
query = f"SELECT * FROM emp WHERE {cond}"
cur.execute(query)
row = cur.fetchone()
if row is None:
    print("No records found")
else:
    while row is not None:
        print(row)
        row = cur.fetchone()
cur.close()
conn.close()



'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''



'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Raises StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''



'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="database"
)
cur = conn.cursor()
cur.execute("SELECT * FROM emp")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()