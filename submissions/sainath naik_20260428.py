1.
'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector

#step 1 : connecting mysql database
con = mysql.connector.Connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'testdb'
)

#step 2 : create cursor object
cursor = con.cursor()

#step 3 : execute query

cursor.execute('select * from emp')

#step 4 : fetchone() method

row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

#step 5 : close the connection
cursor.close()
con.close()



2.
'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector

# 1) Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

# 2) Create cursor object
cur = con.cursor()

# 3) Read condition from user (pre-requisite)
cond = input("Enter condition for WHERE clause (e.g., deptno=20): ")

# 4) Call execute() with user condition
query = f"SELECT * FROM emp WHERE {cond}"
cur.execute(query)

# 5) Fetch and print one row at a time
row = cur.fetchone()
while row is not None:
    print(row)      # tuple → monitor
    row = cur.fetchone()

# 6) Close connection
cur.close()
con.close()




3.
'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''

import mysql.connector

# 1) Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

# 2) Create cursor
cur = con.cursor()

# 3) Pre-requisite: read column name from user
colname = input("Enter column name to sort by (e.g., sal, deptno, ename): ")

# Optional: read order
order = input("Enter order (ASC/DESC): ").strip().upper()
if order not in ("ASC", "DESC"):
    order = "ASC"

# 4) Call execute() with ORDER BY
query = f"SELECT * FROM emp ORDER BY {colname} {order}"
cur.execute(query)

# 5) Fetch and print one row at a time
row = cur.fetchone()
while row is not None:
    print(row)     # tuple → monitor
    row = cur.fetchone()

# 6) Close resources
cur.close()
con.close()



4.
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

# 1) Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

# 2) Create cursor
cur = con.cursor()

# 3) Pre-requisite: read table name from user
table = input("Enter table name to display: ")

# 4) Call execute()
query = f"SELECT * FROM {table}"
cur.execute(query)

# 5) Use next() to fetch tuples one by one
try:
    while True:
        row = next(cur)   # yields next tuple
        print(row)        # tuple → monitor
except StopIteration:
    # End of cursor rows
    pass

# 6) Close resources
cur.close()
con.close()



5.
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''

import mysql.connector

# 1) Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

# 2) Create cursor object
cur = con.cursor()

# 3) Execute query on emp table
cur.execute("SELECT * FROM emp")

# 4) Fetch all rows at once (list of tuples)
rows = cur.fetchall()

# 5) Iterate list and print each tuple
for row in rows:
    print(row)     # tuple → monitor

# 6) Close resources
cur.close()
con.close()


6.
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


7.
#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)



import random

for _ in range(10):
    otp = random.randint(0, 999999)
    print(f"{otp:06d}")