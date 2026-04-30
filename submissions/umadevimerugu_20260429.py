'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
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
cur.execute("select * from employees")
n=int(input("enter the no of rows to print:"))
#list=cur.fetchmany(n)


try:
    if n>1:
        for x in cur.description:
            print(f'{x[0]:^10}',end='\t')
        print()
        list=cur.fetchmany(n)
        for i in list:
            for j in i:
                print(f'{j:^10}',end='\t')
            print()
        print("Number of records:",cur.rowcount)
    else:    #print(list)
        cur.close()
        con.close()
        
except:
    print("connection can't be closed")
#####################################################################
'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->															
															cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  inputs  empno , ename  and  sal

4) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table

5) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError

6) Can  a  tuple  be  inserted  into  MySqlCursor  object ?  --->  No  becoz  it  is  immutable
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

while True:
    try:
        emp_no=input("enter the emp_no:")
        emp_name=input("enter the emp_name:")
        sal=input("enter the salary:")
        cur.execute(f"INSERT INTO employees VALUES ({emp_no}, '{emp_name}', {sal})")
        con.commit()
        print("1 row inserted sucessfully")
    except mysql.connector.IntegrityError:
        print("Error: Duplicate empno not allowed!")

    except Exception as e:
        print("Error:", e)
    option=input("insert another row ?(y/n):")
    if option.upper()!='Y':
        break
        
            
cur.close()
con.close()
###########################################################
'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
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
condtion=input("enter the condition to delete rows:")
cur . execute(F'delete  from  employees  where  {condtion}')
con.commit()
print(cur.rowcount,"rows deleted")

            
cur.close()
con.close()
###########################################################################
import mysql.connector
import time
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Umadevi@123",
    database="demo"
)

cur = con.cursor()
cur . execute(F'select * from  employees ')
for x in cur.description:
    print(f'{x[0]:^5}',end='\t')
print()
for i in cur:
        print(i)
print(cur.rowcount)
cur.close()
con.close()
######################################################################
'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->									
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->																
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
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
tablename=input("enter the table name:")
cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
print("table created")
cur.close()
con.close()
############################################################################################
# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
            super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
            parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
            cls.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
            child.m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
            #self . m1()  #m1()  
            print('child  Method')
# End  of  the  class
p=parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c=child()
c.m1()#How  to  call  m2()  method  of  child  class
child . m2()
#super() . m1()  
#self . m1()
####################################################################################
class parent:
    @classmethod
    def m1(cls):
        print('parent Method')

class child(parent):
    @classmethod
    def m1(cls):
        super().m1()     # \
        parent.m1()      # 
        print('child Method')

# Calling parent method
parent.m1()

# Calling child method
child.m1()