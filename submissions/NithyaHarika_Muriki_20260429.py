'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import mysql.connector as mc

con = mc.connect(
    database="employee",
    host="localhost",
    password="Nithya@1234",
    user="root"
cur = con.cursor()
cur.execute("SELECT emp_id,emp_name,department,salary,age FROM employees_demo")
size = int(input("Enter size: "))
if size <0:
        print("Number of tuples fetched: ",0)
else:
    rows = cur.fetchmany(size)  
    for  x  in  cur . description:    #  Prints  all  the  column  names  of   emp  table
                print(F'{x[0] : ^10}' , end = '\t')
    print()
    for row in rows:
            for x in row:
                print(F'{x : ^10}' , end = '\t') 
            print()
    print("Number of tuples fetched: ",len(rows))


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

import mysql.connector as mc
con = mc.connect(database = "joinsdb",     
                host="localhost",
                password="Nithya@1234",
                user="root"
)

cur = con.cursor()
n = 'y'
while n == 'y':
    empno=eval(input("Enter eno: "))
    name=input("Enter emp name: ")
    salary=eval(input("Enter Salary: "))
    cur.execute(
        "INSERT INTO emp (emp_id, ename, sal) VALUES (%s, %s, %s)",
        (empno, name, salary)
    )

    con.commit()
    print("1 row inserted.")
    n = input("Inser another row? (y/n): ")


'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
import mysql.connector as mc
con = mc.connect(database = "joinsdb",     
                host="localhost",
                password="Nithya@1234",
                user="root"
)

con = mc.connect(database = "joinsdb",     
                host="localhost",
                password="Nithya@1234",
                user="root"
)

cur = con.cursor()
cond = input("Enter condition (Enter to delete all the rows: ")
cur.execute(f"delete from emp where {cond}")
print(f"{cur.rowcount} rows are detected.")



'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
'''
import mysql.connector as mc
con = mc.connect(database = "joinsdb",     
                host="localhost",
                password="Nithya@1234",
                user="root"
)
con = mc.connect(database = "joinsdb",     
                host="localhost",
                password="Nithya@1234",
                user="root"
)

cur = con.cursor()
expr = input("Enter expression : ")
cond = input("Enter condition (Enter key to modify all the rows: ")
cur . execute(F'update  emp  set  {expr}   where  {cond}')
print(f"{cur.rowcount} rows are updated.")


'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->									
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->																
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
'''






'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  ---> 3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import  math
class   circle:
	def   get(self):
	    self.rad=ch
	def   area(self):
		return  self.area()
	def   cir(self):
		return  self.cir()
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.rad # How  to  read  radius  into  the  object  
		self.height #How  to  read  height  into  the  object 
	def  area(self):
		return  area  of  cylinder
	def  volume(self):
		return   volume  of  cylinder
# End of cylinder class
def    menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
while  True:  
	menu()
	ch = eval(input('Enter choice : ')) 
	match  ch:
		case  1:
				How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  ???)
				print('Circumference :  ' ,  ???)
		case  2:
				How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  ???)
				print('Volume :  ' ,  ???)
		case  3:
				How  to  stop  execution
	# End  of  match