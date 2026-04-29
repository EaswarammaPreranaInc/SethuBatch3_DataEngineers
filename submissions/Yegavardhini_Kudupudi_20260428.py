'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector
con = mysql.connector.connect(database='sssdc',user='root',password='',host='localhost')
cur = con.cursor()
cur.execute('select * from emp')
while tpl:=cur.fetchone():
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
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
con = mysql.connector.connect(database='sssdc',user='root',password='',host='localhost')
cur = con.cursor()
cond = input('Enter any condition : ')
cur.execute(f'select * from emp where {cond}')
while tpl:=cur.fetchone():
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
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
con = mysql.connector.connect(database='sssdc',user='root',password='',host='localhost')
cur = con.cursor()
col = input('Enter column name : ')
cur.execute(f'select * from emp order by {col}')
print('empno\tename\tsal')
while tpl:=cur.fetchone():
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
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
con = mysql.connector.connect(database='sssdc',user='root',password='',host='localhost')
cur = con.cursor()
table_name = input('Enter table name : ')
cur.execute(f'select * from {table_name}')
print('empno\tename\tsal')
while True:
    try:
        print(*next(cur),sep='\t')
    except StopIteration:
        break
print('Number of tuples :  ',cur.rowcount)
cur.close()
con.close()


'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''

import mysql.connector
con = mysql.connector.connect(database='sssdc',user='root',password='',host='localhost')
cur = con.cursor()
cur.execute('select * from emp')
list = cur.fetchall()
print('empno\tename\tsal')
for tpl in list:
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
cur.close()
con.close()


#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

from random import *
for i in range(10):
    print(randint(000000,999999))
