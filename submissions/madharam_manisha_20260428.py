'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
'''
Write a program to print emp table of the database with fetchone() method

emp table ----------------> cursor object -----------------> tpl ---------> monitor
                     execute()                               fetchone()        print()
'''

import mysql.connector   

try:
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=''
    )

    cur = con.cursor()
    cur.execute('select * from emp')

    print('Emp table data:\n')

    count = 0
    tpl = cur.fetchone()   

    while tpl is not None:
        print(tpl)         
        count += 1
        tpl = cur.fetchone()   

    
    print('\nNumber of tuples :', count)
    cur.close()
    con.close()

except mysql.connector.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) table name')

except mysql.connector.errors.DatabaseError:
    print('Start MySQL')
#=========================================================================================================
'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector

try:
    cond = input('Enter condition (e.g., sal > 10000): ')

    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=''
    )

    cur = con.cursor()

    cur.execute(f'select * from emp where {cond}')

    print('\nFiltered emp table data:\n')

    count = 0

    tpl = cur.fetchone()

    while tpl is not None:
        print(tpl)
        count += 1
        tpl = cur.fetchone()

    print('\nNumber of tuples :', count)

    cur.close()
    con.close()

except mysql.connector.errors.ProgrammingError:
    print('Invalid condition (or) database (or) table name')

except mysql.connector.errors.DatabaseError:
    print('Start MySQL')    
#=========================================================================================================
'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector

try:
    col = input('Enter column name to sort: ')

    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=''
    )

    cur = con.cursor()

    cur.execute(f'select * from emp order by {col}')

    print('\nSorted emp table data:\n')

    count = 0

    tpl = cur.fetchone()

    while tpl is not None:
        print(tpl)
        count += 1
        tpl = cur.fetchone()

    print('\nNumber of tuples :', count)

    cur.close()
    con.close()

except mysql.connector.errors.ProgrammingError:
    print('Invalid column name or table name')

except mysql.connector.errors.DatabaseError:
    print('Start MySQL')
#==========================================================================================
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

try:
    table = input('Enter table name: ')

    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=''
    )

    cur = con.cursor()

    cur.execute(f'select * from {table}')

    print('\nTable data:\n')

    count = 0

    while True:
        tpl = next(cur)
        print(tpl)
        count += 1

except StopIteration:
    print('\nNumber of tuples :', count)

    cur.close()
    con.close()

except mysql.connector.errors.ProgrammingError:
    print('Invalid table name or database')

except mysql.connector.errors.DatabaseError:
    print('Start MySQL')        
#==========================================================================================
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=''
    )

    cur = con.cursor()

    cur.execute('select * from emp')

    print('\nEmp table data:\n')

    count = 0

    lst = cur.fetchall()

    for tpl in lst:
        print(tpl)
        count += 1

    print('\nNumber of tuples :', count)

    cur.close()
    con.close()

except mysql.connector.errors.ProgrammingError:
    print('Invalid table name or database')

except mysql.connector.errors.DatabaseError:
    print('Start MySQL')

#===============================================================================================
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random

for i in range(10):
    otp = random.randint(0, 999999)
    print(f"{otp:06d}")        