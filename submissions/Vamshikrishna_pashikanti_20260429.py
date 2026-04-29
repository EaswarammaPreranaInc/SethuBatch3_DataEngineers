'''

Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method



emp  table ----------------> cursor  object -----------------> tpl ---------> monitor

                     execute()                                 fetchone()             print()

'''

import   mysql . connector   #  Executes  __init__  module  of  mysql . connector  package

try:

	con = mysql . connector . connect(host = 'localhost' , database = 'emp' , user = 'root' , password = 'Teji@1836')   #  Connects  to  database  and   returns  MySqlConnection  object

	cur =  con . cursor() 

	cur . execute('select  *  from  employee')

        count=0   

	row=cur . fetchone()  

	while row is not None:

		print(row)

                count+=1

		row=cur.fetchone()

	cur . close()  

	con . close()  

except  mysql.connector.errors.ProgrammingError:

	print('Invalid  database  (or)  user  (or)  password  (or)  tablename')

except  mysql.connector.errors.DatabaseError:

	print('Start  mysql')

print("Number of tuples:", count)

--------------------------------------------------------------------------------------------------

'''

Write  a  program  to  print  emp  table  based  on  user  condition



1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')



2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user



3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor

                         execute()                                 fetchone()              print()



'''

import mysql.connector

try:

    con = mysql.connector.connect(

        host='localhost',

        database='emp',

        user='root',

        password='Teji@1836'

    )

    cur = con.cursor()

    cond = input("Enter condition (e.g., salary > 50000): ")

    query = f"SELECT * FROM employee WHERE {cond}"

    cur.execute(query)

    row = cur.fetchone()

    if row is None:

        print("No records found")

    else:

        while row is not None:

            print(row)

            row = cur.fetchone()

    cur.close()

    con.close()

except Exception as e:

    print("Error:", e)
