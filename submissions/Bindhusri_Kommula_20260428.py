'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
cur.execute("SELECT * FROM emp")
while (tpl := cur.fetchone()):
    print(tpl[0],tpl[1],tpl[2],sep="\t")
print('Number of tuples:',cur.rowcount)

'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
cond=input('Enter any condition: ')
cur.execute(f"SELECT * FROM emp where {cond}")
while (tpl := cur.fetchone()):
    print(tpl[0],tpl[1],tpl[2],sep="\t")
print('Number of tuples:',cur.rowcount)



'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
col=input('Enter column name: ')
cur.execute(f"SELECT * FROM emp order by {col}")
while (tpl := cur.fetchone()):
    print(tpl[0],tpl[1],tpl[2],sep="\t")
print('Number of tuples:',cur.rowcount)



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
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
table=input('Enter table name: ')
cur.execute(f"SELECT * FROM {table}")
try:
    while True:
        tpl=next(cur)
        print(tpl[0],tpl[1],tpl[2],sep='\t')
except StopIteration:
   print('Number of tuples:',cur.rowcount)


'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
cur.execute(f"SELECT * FROM emp")
tpl=cur.fetchall()
for x in tpl:
    print(x[0],x[1],x[2],sep='\t')
print('Number of tuples:',cur.rowcount)

for  i  in   range(4):  #  i = 0
	for   i   in  range(2): #  i = 1
			pass
	print(i) # 1 1 1 1



#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)