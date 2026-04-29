'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root", 
    database="emp_dept"
)

cur = con.cursor()
cur.execute('select * from emp ')
while tp:= cur.fetchone():
    print(tp)


'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root", 
    database="emp_dept"
)

cur = con.cursor()
cond=input('Enter condition')
cur.execute(f'select * from emp where {cond} ')
while tp:= cur.fetchone():
    print(tp)

'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root", 
    database="emp_dept"
)

cur = con.cursor()
colname=input('Enter col name')

cur . execute(F'select  *  from  emp  order  by  {colname}')
while tp:= cur.fetchone():
    print(tp)


'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Raises StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root", 
    database="emp_dept"
)

cur = con.cursor()
table=input('Enter table name')

cur . execute(F'select  *  from  {table}')
while True:
    try:
        print(next(cur))
    except StopIteration:
        break
