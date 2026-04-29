'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector
con=mysql.connector.connect(database='joinsdb',user='root')
cur=con.cursor()
cur.execute('select * from employees_demo')
print('eid\tename\tdeptno')
while tpl:=cur.fetchone():
	print(f'{tpl[0]}\t{tpl[1]}\t{tpl[2]}')
print('Number of rows: ',cur.rowcount)




'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector
con=mysql.connector.connect(database='joinsdb',user='root')
cur=con.cursor()
cond=input('Enter condition: ')
cur.execute(f'select * from employees_demo where {cond}')
print('eid\tename\tdeptno')
while tpl:=cur.fetchone():
	print(f'{tpl[0]}\t{tpl[1]}\t{tpl[2]}')









'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector
con=mysql.connector.connect(database='joinsdb',user='root')
cur=con.cursor()
cond=input('Enter condition: ')
cur.execute(f'select * from employees_demo where {cond}')
print('eid\tename\tdeptno')
while tpl:=cur.fetchone():
	print(f'{tpl[0]}\t{tpl[1]}\t{tpl[2]}')
if cur.rowcount!=-1:
	print('Number of rows: ',cur.rowcount)
else:
	print('Number of rows: ',cur.rowcount+1)







'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''


import mysql.connector
con=mysql.connector.connect(database='joinsdb',user='root')
cur=con.cursor()
colname=input('Enter column name to sort: ')
cur.execute(f'select * from employees_demo order by {colname}')
print('eid\tename\tdeptno')
while tpl:=cur.fetchone():
	print(f'{tpl[0]}\t{tpl[1]}\t{tpl[2]}')
if cur.rowcount!=-1:
	print('Number of rows: ',cur.rowcount)
else:
	print('Number of rows: ',cur.rowcount+1)






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
con=mysql.connector.connect(database='joinsdb',user='root')
cur=con.cursor()
tablename=input('Enter table name: ')
cur.execute(f'select * from {tablename}')
print('eid\tename\tdeptno')
while True:
	try:
		print(next(cur))
	except StopIteration:
		break

if cur.rowcount!=-1:
	print('Number of rows: ',cur.rowcount)
else:
	print('Number of rows: ',cur.rowcount+1)






'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector
con=mysql.connector.connect(database='joinsdb',user='root')
cur=con.cursor()
cur.execute(f'select * from employees_demo')
print('eid\tename\tdeptno')
x=cur.fetchall()
for i in x:
	print(f'{i[0]}\t{i[1]}\t{i[2]}')
if cur.rowcount!=-1:
	print('Number of rows: ',cur.rowcount)
else:
	print('Number of rows: ',cur.rowcount+1)




for  i  in   range(4):  #  i = 0
	for   i   in  range(2): #  i = 1
			pass
	print(i)
'''
1
1
1
1
'''

#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

from random import choice
b=[0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    print(f'{choice(b)}{choice(b)}{choice(b)}{choice(b)}{choice(b)}{choice(b)}')