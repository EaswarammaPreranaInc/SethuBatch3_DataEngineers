'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
# Code :
import mysql.connector as mc
con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
cur = con.cursor()
c = con.cursor()
c.execute('select * from emp')
l = c.fetchall()
n = int(input("How many rows ? :  "))
try:
    if n<=0 or n>len(l):
        print('Invalid input')
    else:
        try:
            cur.execute('select * from emp')
            list = cur.fetchmany(n)
            for x in cur.description:
                print(f'{x[0]:^10}',end='\t')
            print()
            for row in list:
                for val in row:
                    print(f'{val:^10}',end='\t')
                print()
            print('Number of tuples fetched :  ',cur.rowcount)
            cur.close() 
            con.close()
        except mc.errors.InternalError:
            print('Cursor can not be closed')
except mc.errors.InterfaceError:
    print('Please connect to the database')
except mc.errors.ProgrammingError:
    print('The database or user or password is incorrect')

'''Output:
How many rows ? :  5
Invalid input

How many rows ? :  0
Invalid input

How many rows ? :  3
  rollno          sname           marks   
   111           Rama Rao        10000.0  
   222             Sita          20000.0  
   333            Rajesh         15000.0  
Number of tuples fetched :   3

How many rows ? :  2
  rollno          sname           marks   
   111           Rama Rao        10000.0  
   222             Sita          20000.0  
Number of tuples fetched :   2
Cursor can not be closed
'''
# Write  a  program  to  insert  multiple  rows  into  emp  table
# Code :
import mysql.connector as mc
con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
cur = con.cursor()
n = int(input("How many rows would you like to insert ?  :  "))
try:
    list = []
    for i in range(n):
        print('Employee : ',i+1)
        emp_no = int(input('Enter employee number : '))
        emp_name = input('Enter employee name :  ')
        emp_sal = int(input('Enter salary : '))
        temp = (emp_no,emp_name,emp_sal)
        list.append(temp)
    cur.executemany('insert into emp values (%s,%s,%s)',list)
    print(f'{cur.rowcount} rows are inserted')
    cur.close() 
    con.close()
except mc.errors.IntegrityError as msg:
    print('Duplicate emp no  : ',msg)
except mc.errors.InterfaceError:
    print('Please connect to the database')
except mc.errors.ProgrammingError:
    print('The database or user or password is incorrect')

''' Output:
How many rows would you like to insert ?  :  3
Employee :  1
Enter employee number : 777
Enter employee name :  PPP
Enter salary : 70000 
Employee :  2
Enter employee number : 888
Enter employee name :  QQQ
Enter salary : 80000
Employee :  3
Enter employee number : 999
Enter employee name :  RRR
Enter salary : 90000
3 rows are inserted

How many rows would you like to insert ?  :  3
Employee :  1
Enter employee number : 100
Enter employee name :  A
Enter salary : 10000
Employee :  2
Enter employee number : 100
Enter employee name :  B
Enter salary : 20000
Employee :  3
Enter employee number : 200
Enter employee name :  C 
Enter salary : 30000
Duplicate emp no  :  1062 (23000): Duplicate entry '100' for key 'emp.PRIMARY'
'''
import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@localhost/empdb")
df = pd.read_sql("select  *  from   emp", engine)
for  x   in  df . columns:
	print(x , end = '\t')
print()	
for x  in  df . itertuples(index=False):
	print(x[0] , x[1] , x[2] , sep = '\t')

''' Output:
rollno          sname           marks   
111           Rama Rao        10000.0  
222             Sita          20000.0  
333            Rajesh         15000.0  
'''