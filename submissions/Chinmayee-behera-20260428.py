'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector
con = mysql.connector.connect(
    database='sssdc',
    user='root',
    password='',
    host='localhost'
)
cur = con.cursor()
cur.execute('select * from emp')
print(F'{'empno':<10}{'ename':<12}{'sal':<12}')
while True:
    tpl = cur.fetchone()
    if tpl is None:
        break
    print(F'{tpl[0]:<10}{tpl[1]:<12}{tpl[2]:<12}')
print('Number of tuples :', cur.rowcount)
cur.close()
con.close()



'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()
'''
import mysql.connector
con = mysql.connector.connect(
    database='sssdc',
    user='root',
    password='',
    host='localhost'
)
cond = input("Enter any condition: ")
cur = con.cursor()
cur.execute(f"select * from emp where {cond}")
print(f'{"empno":<10}{"ename":<12}{"sal":<12}')
count = 0
while True:
    tpl = cur.fetchone()
    if tpl is None:
        break
    count += 1 
    print(f'{tpl[0]:<10}{tpl[1]:<12}{tpl[2]:<12}')
if count == 0:
    count = -1
print("Number of tuples :", count)
cur.close()
con.close()

'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector
con = mysql.connector.connect(
    database='sssdc',
    user='root',
    password='',
    host='localhost'
)
colname = input("Enter any column name: ")
cur = con.cursor()
cur.execute(f"select * from emp order by {colname}")
print(f'{"empno":<10}{"ename":<12}{"sal":<12}')
count = 0
while True:
    tpl = cur.fetchone()
    if tpl is None:
        break
    count += 1 
    print(f'{tpl[0]:<10}{tpl[1]:<12}{tpl[2]:<12}')
if count == 0:
    count = -1
print("Number of tuples :", count)
cur.close()
con.close()

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
    database='sssdc',
    user='root',
    password='',
    host='localhost'
)
try:
    table = input("Enter table name: ")
    cur = con.cursor()
    cur.execute(f"select * from {table}")
    print(f'{"empno":<10}{"ename":<12}{"sal":<12}')
    count = 0
    try:
        while True:
            tpl = next(cur)   
            print(f'{tpl[0]:<10}{tpl[1]:<12}{tpl[2]:<12}')
            count += 1
    except StopIteration:
        pass
    if count == 0:
        print("No records found")
    else:
        print("Number of tuples :", count)
except  mysql.connector.errors.ProgrammingError:
	print('Invalid  database  (or)  user  (or)  password  (or)  tablename')
except  mysql.connector.errors.DatabaseError:
	print('Start  mysql')
cur.close()
con.close()

'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector

con = mysql.connector.connect(
    database='sssdc',
    user='root',
    password='',
    host='localhost'
)
cur = con.cursor()
cur.execute(f"select * from emp")
print(f'{"empno":<10}{"ename":<12}{"sal":<12}')
rows = cur.fetchall()
count = 0
for x in rows:
    print(f'{x[0]:<10}{x[1]:<12}{x[2]:<12}')
    count += 1
if count == 0:
    print("No records found")
else:
    print("Number of tuples :", count)
cur.close()
con.close()

''' Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)'''
import  random
for  x  in  range(10):   #  Ten  otp's
	print(random . randint(000000 , 999999))