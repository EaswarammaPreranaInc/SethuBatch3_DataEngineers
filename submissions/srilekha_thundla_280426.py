'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector   # Import MySQL connector

password = input("Enter password: ")

try:
    # Establish connection
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=password
    )

    cur = con.cursor()

    cur.execute('SELECT * FROM emp')

    print("Emp Table Records:\n")

    # Fetch one row at a time
    row = cur.fetchone()   # Get first row

    count = 0
    while row is not None:
        print(row)
        count += 1
        row = cur.fetchone()   # Get next row

    print("\nTotal rows fetched:", count)

    # Close resources
    cur.close()
    con.close()

except mysql.connector.errors.ProgrammingError:
    print('Invalid database/user/password/table name')

except mysql.connector.errors.DatabaseError:
    print('Start MySQL server')

'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector

# Read condition from user
cond = input("Enter condition  :")
password = input("Enter password: ")
try:
    # Connect to database
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=password
    )
    cur = con.cursor()
    query = f"SELECT * FROM emp WHERE {cond}"
    cur.execute(query)
    row = cur.fetchone()
    count = 0

    while True:
        print(row)
        count += 1
        row = cur.fetchone()
    if count == 0:
        print("No records found")
        print("\nTotal rows fetched:", count)

    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print('Invalid SQL condition or table name')
except mysql.connector.errors.DatabaseError:
    print('Start MySQL server')


'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector


colname = input("Enter column name to sort by (e.g., empno, ename, sal): ")
password = input("Enter password: ")
try:
    # Connect to database
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=password
    )
    cur = con.cursor()
    query = f"SELECT * FROM emp ORDER BY {colname}"
    cur.execute(query)
    print("\nEmp Table in Sorted Order:\n")
    row = cur.fetchone()
    count = 0
    while row is not None:
        print(row)
        count += 1
        row = cur.fetchone()
    if count == 0:
        print("No records found")
    print("\nTotal rows:", count)
    # Close resources
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print("Invalid column name")

except mysql.connector.errors.DatabaseError:
    print("Start MySQL server")




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
# Read table name from user
table = input("Enter table name: ")
password = input("Enter password: ")
try:
    # Connect to database
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=password
    )
    cur = con.cursor()
    query = f"SELECT * FROM {table}"
    cur.execute(query)
    print(f"\nRecords from table '{table}':\n")
    count = 0
    try:
        while True:
            row = next(cur)   
            print(row)
            count += 1
    except StopIteration:
        pass
    if count == 0:
        print("No records found")
    print("\nTotal rows:", count)
    # Close resources
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print("Invalid table name")

except mysql.connector.errors.DatabaseError:
    print("Start MySQL server")


'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''

import mysql.connector

password = input("Enter password: ")

try:
    # Connect to database
    con = mysql.connector.connect(
        host='localhost',
        database='empdb',
        user='root',
        password=password
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM emp")
    print("\nEmp Table Records:\n")
    data = cur.fetchall()   
    count = 0
    # Iterate through list
    for row in data:
        print(row)
        count += 1
    if count == 0:
        print("No records found")
    print("\nTotal rows:", count)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError:
    print("Invalid database/table/user/password")

except mysql.connector.errors.DatabaseError:
    print("Start MySQL server")

#find outputs
for  i  in   range(4):  #  i = 0
	for   i   in  range(2): #  i = 1
			pass
	print(i)#1<nxt>1<nxt>1<nxt>1
	























