'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
# Code :
import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='root123',database='emp')
cur = con.cursor()
cur.execute('select * from emp')
while tpl:=cur.fetchone():
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
cur.close()
con.close()

''' Output:
111     Rama Rao     10000.0
222     Sita         20000.0
333     Rajesh       15000.0
Number of tuples :   3
'''
'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

# Code

import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='root123',database='emp')
cur = con.cursor()
cond = input('Enter any condition : ')
cur.execute(f'select * from emp where {cond}')
while tpl:=cur.fetchone():
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
cur.close()
con.close()
''' Output:
Enter any condition : sal > 12000
222     Sita    20000.0
333     Rajesh  15000.0
Number of tuples :   2

Enter any condition : ename like 's%'
222     Sita    20000.0
Number of tuples :   1

Enter any condition : sal between 25000 and 30000
Number of tuples :   -1
'''
'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
# Code :
import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='root123',database='emp')
cur = con.cursor()
col = input('Enter column name : ')
cur.execute(f'select * from emp order by {col}')
print('empno\tename\tsal')
while tpl:=cur.fetchone():
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
cur.close()
con.close()

''' Output:
Enter column name : sal
empno   ename        sal
111     Rama Rao     10000.0
333     Rajesh       15000.0
222     Sita         20000.0
Number of tuples :   3

Enter column name : ename desc
empno   ename         sal
222     Sita          20000.0
111     Rama Rao      10000.0
333     Rajesh        15000.0
Number of tuples :   3

Enter column name : empno 
empno   ename         sal
111     Rama Rao      10000.0
222     Sita          20000.0
333     Rajesh        15000.0
Number of tuples :   3
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
# Code :

import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='root123',database='emp')
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

'''Output:
Enter table name : emp
empno   ename       sal
111     Rama Rao    10000.0
222     Sita        20000.0
333     Rajesh      15000.0
Number of tuples :   3
'''
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
# Code :
import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='root123',database='emp')
cur = con.cursor()
cur.execute('select * from emp')
list = cur.fetchall()
print('empno\tename\tsal')
for tpl in list:
    print(*tpl,sep='\t')
print('Number of tuples :  ',cur.rowcount)
cur.close()
con.close()

''' Output:
empno   ename        sal
111     Rama Rao     10000.0
222     Sita         20000.0
333     Rajesh       15000.0
Number of tuples :   3
'''

#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

# Code :
from random import *
for i in range(10):
    print(randint(000000,999999))

''' Output:
692609
566638
955060
770684
649147
350671
762591
277296
625776
894049
'''