'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Umadevi@123",
    database="demo"
)
cur = con.cursor()
cur.execute("SELECT * FROM employees")
print(f"{'emp_no':^10} {'emp_name':^15} {'salary':^10}")
count=0
while tpl := cur.fetchone():
    print(f"{tpl[0]:^10} {tpl[1]:^15} {tpl[2]:^10}")
    count=count+1
print("Number of Tuple:",count)
cur.close()
con.close()
########################################################################################################
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
    password="Umadevi@123",
    database="demo"
)

cur = con.cursor()
condition=input("enter the condition:")#salary > 30000
cur.execute(f"SELECT * FROM employees where {condition}")

print(f"{'emp_no':^10} {'emp_name':^15} {'salary':^10}")
count=0
while tpl := cur.fetchone():
    print(f"{tpl[0]:^10} {tpl[1]:^15} {tpl[2]:^10}")
    count=count+1
print("Number of Tuple:",count)
cur.close()
con.close()
########################################################################################################

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
    password="Umadevi@123",
    database="demo"
)

cur = con.cursor()
colname=input("enter the column:")#emp_name or salary
cur.execute(f"SELECT * FROM employees order  by  {colname}")
print(f"{'emp_no':^10}{'emp_name':^15}{'salary':^10}")
#tpl=cur.fetchone()
count=0
while tpl:=cur.fetchone():
    print(f"{tpl[0]:^10} {tpl[1]:^15} {tpl[2]:^10}")
    count=count+1
print("Number of tuples:",count)
cur.close()
con.close()
########################################################################################################

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
import time
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Umadevi@123",
    database="demo"
)

cur = con.cursor()
tablename=input("enter the tablename:")#
cur.execute(f"SELECT * FROM  {tablename}")
print(f"{'emp_no':^10}{'emp_name':^15}{'salary':^10}")
count=0
try:
    while True:
        tpl=next(cur)
        print(f"{tpl[0]:^10} {tpl[1]:^15} {tpl[2]:^10}")
        time.sleep(1)
        count=count+1
except StopIteration:
    print("Number of tuples:",count)
cur.close()
con.close()
########################################################################################################
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''

import mysql.connector
import time
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Umadevi@123",
    database="demo"
)

cur = con.cursor()
tablename=input("enter the tablename:")#
cur.execute(f"SELECT * FROM  {tablename}")
print(f"{'emp_no':^10}{'emp_name':^15}{'salary':^10}")
list=cur.fetchall()
for i in list:
    print(f'{i[0]:^10}{i[1]:^15}{i[2]:^10}')
print("Number of Tuples:",len(list))
#print(list)
cur.close()
con.close()
########################################################################################################

#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

from random import *
import time
#print(a)
for i in range(10):
        otp=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
        print(otp)
        time.sleep(1)
########################################################################################################