'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples
Hint:  Use  fetchmany()  method
'''
import mysql.connector
try:
	con=mysql.connector.connect(host='localhost',username='root',password='UR_PWD',database='mysql_python')
	cur=con.cursor()
	cur.execute('select *from emp')
	n=int(input('Enter how many rows ?'))
	list = cur.fetchmany(n)
	if n>len(*list) or n<=0:
		print('Invalid Input')
	else:
		for i in cur.description:
			print(F'{i[0]:^10}',end='\t')
		print()
		for tpl in list:
			for i in tpl:
				print(F'{i:^10}',end='\t')
			print()
		print('Number of tuples fetched:  ',cur.rowcount)
	cur.close()
	con.close()
except mysql.connector.errors.InternalError:
	print('Cursor cannot be closed')
except   mysql.connector. errors . ProgrammingError:
	print('Invalid  database  (or)  user  (or)  password  (or)  tablename')
except   mysql.connector. errors . InterfaceError:
	print('Pls  start  mysql')
	
	
# Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql.connector
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Madhu$1234",
        database="mysql_python"
    )
cur = conn.cursor()
try:
    total_rows = int(input("How many rows would you like to insert? "))
    lt=[]
    for i in range(1, total_rows + 1):
        empno = int(input("Enter Employee Number (empno): ")) 
        ename = input("Enter Employee Name: ")
        sal = float(input("Enter Salary: "))
        emp_record=(empno,ename,sal)
        lt.append(emp_record)
    sql_query = "INSERT INTO emp (empno, ename, sal) VALUES (%s, %s, %s)"
    cur.executemany(sql_query,lt)
    print(F'{cur.rowcount} rows inserted')
    conn.commit()
    cur.close()
    conn.close()
except mysql.connector.errors.IntegrityError as error:
    print(F"Dulpicate empno : {error}'")
except   mysql.connector. errors . ProgrammingError:
	print('Invalid  database  (or)  user  (or)  password  (or)  tablename')
except   mysql.connector. errors . InterfaceError:
	print('Pls  start  mysql')
			
			
