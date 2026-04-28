'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                fetchone()             print()
Sample output:
empno            ename            sal
111           Rama  Rao         10000.0
222               Sita          20000.0
333             Rajesh          15000.0

Number of tuples : 3
'''

import mysql.connector
try:
    con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',   
    database='emp_dept'
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
except mysql.connector.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mysql.connector.errors.DatabaseError:
    print('Start mysql')

'''
Write  a  program  to  print  emp  table  based  on  user  condition
1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')
2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user
3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                execute()                      fetchone()              print()
Enter any condition : sal > 12000
empno            ename            sal
222               Sita          20000.0
333             Rajesh          15000.0
Number of tuples : 2

Enter any condition : ename like 's%'
empno            ename            sal
222               Sita          20000.0
Number of tuples : 1

Enter any condition : sal between 25000 and 30000
empno            ename            sal
Number of tuples : 0
'''
import mysql.connector
try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='emp_dept'
    )
    cur = con.cursor()
    cond = input('Enter any condition : ')
    cur.execute(f'SELECT * FROM emp WHERE {cond}')
    print('{:<10}{:<15}{:<10}'.format('empno','ename','sal'))
    while True:
        tpl = cur.fetchone()
        if tpl is None:
            break
        print('{:<10}{:<15}{:<10}'.format(tpl[0], tpl[1], tpl[2]))
    print('Number of tuples :', cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mysql.connector.errors.DatabaseError:
    print('Start mysql')

'''
Write  a  program  to  print  emp  table  in  sorted  order
1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')
2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname
3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
Enter column name: sal
empno            ename            sal
111           Rama  Rao         10000.0
333             Rajesh          15000.0
222               Sita          20000.0
Number of tuples : 3 

Enter column name: ename desc
empno            ename            sal
222               Sita          20000.0
111           Rama  Rao         10000.0
333             Rajesh          15000.0
Number of tuples : 3
'''
import mysql.connector
try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='emp_dept'
    )
    cur = con.cursor()
    colname = input('Enter column name : ')
    cur.execute(f'SELECT * FROM emp ORDER BY {colname}')
    print('{:<10}{:<15}{:<10}'.format('empno','ename','sal'))
    while True:
        tpl = cur.fetchone()
        if tpl is None:
            break
        print('{:<10}{:<15}{:<10}'.format(tpl[0], tpl[1], tpl[2]))

    print('Number of tuples :', cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mysql.connector.errors.DatabaseError:
    print('Start mysql')

'''
Write  a  program  to  print  user  input  table  with  next()  function
1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')
2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name
3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object
4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Raises StopIteration  error
5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
Enter table name : emp
empno            ename            sal
111           Rama  Rao         10000.0
222               Sita          20000.0
333             Rajesh          15000.0
Number of tuples : 3
'''
import mysql.connector
try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='emp_dept'
    )
    cur = con.cursor()
    table = input('Enter table name : ')
    cur.execute(f'SELECT * FROM {table}')
    print('{:<10}{:<15}{:<10}'.format('empno','ename','sal'))
    while True:
        try:
            tpl = next(cur)   
            print('{:<10}{:<15}{:<10}'.format(tpl[0], tpl[1], tpl[2]))
        except StopIteration:
            break
    print('Number of tuples :', cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mysql.connector.errors.DatabaseError:
    print('Start mysql')

'''
Write  a  program  to  print  cursor  with  fetchall()  method
 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()

empno            ename            sal
111           Rama  Rao         10000.0
222               Sita          20000.0
333             Rajesh          15000.0
Number of tuples : 3
'''
import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='emp_dept'
    )
    cur = con.cursor()
    cur.execute('select * from emp')
    lst = cur.fetchall()      
    print('{:<10}{:<15}{:<10}'.format('empno','ename','sal'))
    for tpl in lst:
        print('{:<10}{:<15}{:<10}'.format(tpl[0], tpl[1], tpl[2]))
    print('Number of tuples :', len(lst))
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mysql.connector.errors.DatabaseError:
    print('Start mysql')
'''
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import  random
for  x  in  range(10):   #  Ten  otp's
	print(random . randint(100000 , 999999))   #  Random  number  between  100000  and   999999
'''

#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
for x in range(10):
    otp = random.randint(0,999999)
    print('%06d' % otp)

