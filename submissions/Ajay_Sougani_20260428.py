'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector
con = mysql.connector.connect(database='emp',user='root',port=3306, password='12345', host='localhost')
cur = con.cursor()
cur.execute("SELECT * FROM emp")
row = cur.fetchone()
count = 0
while row is not None:
    print(row)
    count += 1
    row = cur.fetchone()
print('Number of tuples : ',count)
con.close()
cur.close



'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()
'''
import mysql.connector
cond = input("Enter condition (e.g., mobile > 50000): ")
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="emp"
)
cur = con.cursor()
query = f"SELECT * FROM emp WHERE {cond}"
cur.execute(query)
row = cur.fetchone()
count = 0
while row is not None:
    print(row)
    count += 1
    row = cur.fetchone()
print('Number of tuples : ',count)
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
colname = input("Enter column name to sort by: ")
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="emp"
)
cur = con.cursor()
query = f"SELECT * FROM emp ORDER BY {colname}"
cur.execute(query)
row = cur.fetchone()
count = 0
while row is not None:
    print(row)
    count += 1
    row = cur.fetchone()
print("Number of tuples: ",count)
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
table = input("Enter table name: ")
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="emp"
)
cur = con.cursor()
query = f"SELECT * FROM {table}"
cur.execute(query)
try:
    while True:
        row = next(cur)   # gets next tuple
        print(row)
except StopIteration:
    print("End of table")
cur.close()
con.close()



'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="emp"
)
cur = con.cursor()
cur.execute("SELECT * FROM emp")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
con.close()




for  i  in   range(4):  #  i = 0
	for   i   in  range(2): #  i = 1
			pass
	print(i)    #1  1   1   1



#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random
otp = random.randint(0, 999999)
otp = f"{otp:06}"
print("Your OTP is:", otp)