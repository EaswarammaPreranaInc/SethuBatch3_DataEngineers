'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
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
n=int(input('how many rows? '))
for x in cur.description:
    print(x[0],end="\t")
list=cur.fetchmany(n)
for x in list:
    print(x[0],x[1],x[2],sep='\t')
print('Number of tuples fetched:',cur.rowcount)
con.close()


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

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
while True:
    empno=int(input('Enter empno: '))
    ename=input('Enter ename: ')
    sal=float(input('Enter sal: '))
    try:
        cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")
        con.commit()
        print(cur.rowcount," row is inserted")
    except mysql.connector.IntegrityError:
        print('Duplicate empno and hence row can not inserted')

    ch=input('Insert other row?(y/n):')
    if ch=='n':
        break


cur.close()
con.close()



'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
cond=input('Enter condition: ')
cur . execute(F'delete  from  emp  where  {cond}')
con.commit()
    
print(cur.rowcount,'rows deleted')

cur.close()
con.close()


'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
'''

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
expr=input('Enter expression: ')
cond=input('Enter condition: ')
cur . execute(F'update  emp  set  {expr}   where  {cond}')
con.commit()
    
print(cur.rowcount,'rows updated')

cur.close()
con.close()


'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->									
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->															Delete  the  existing  table  and  create  a  new  table  with  same  name
'''

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bindhu@123",
    database="emp"
)

cur = con.cursor()
while True:
    tablename=input('Enter table name: ')
    try:
        cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
        print(f'{tablename} table is created')
    except mysql.connector.errors.InterfaceError:
        cur . execute(f'drop table {tablename}')
        print(f'Existing {tablename} table is deleted')
        cur . execute(F'create  table  {tablename}(empno int,ename varchar(20),sal decimal(10,1)')
        print(f'new {tablename} table is created')



cur.close()
con.close()


# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()  
		m1()  
		print('child  Method')
# End  of  the  class
child.m1() #How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()  
self . m1()



# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()   
		self . m1()  
		m1()  
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class



# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() 
		super(child) . m1() 
		self . m1()  
		cls . m1()  
		print('child  method')
#end of the class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1()



# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()  
		self . m1()  
		cls . m1()   
		print('child  method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class



# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'
		print(self.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)  
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x) #How  to  print  variable  'x'
		print(child.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(super().x) #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(self.x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y) #How  to  print  variable  'y'
		print(self.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) 
		print(y)  
# End  of child  class
parent.m1() #How  to  call   m1()  method  of  parent  class
child.m2() #How  to  call   m2()  method  of  child  class



# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'  of  parent  class
		print(self.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'  of  parent  class
		print(super().x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x) #How  to  print  variable  'x'  of  child  class
		print(self.x) #How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class



#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a = int(input())
                self.b = int(input())		
	def    disp(self):
		print(self.a, self.b, sep='\t')
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super().get()   
                self.c = int(input())
                self.d = int(input())		
	def   disp(self):
		super().disp()  
                print(self.c, self.d, sep='\t')
	def  total(self):
		return self.a + self.b + self.c + self.d  
# End of child class
print('parent  object')
p=parent() # How  to  read  inputs  into  parent  class  object  'p'
p.get()
print('child  object')
c=child() #How  to  read  inputs  into  child  class  object  'c'
c.get()
print('parent  object  :  ' , end = '\t')
p.disp() #How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp() #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c.total())



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
	    self.r = float(input("Enter radius: ")) #How  to  read  radius  into  object
	def   area(self):
		return  math.pi * self.r ** 2
	def   cir(self):
		return 2 * math.pi * self.r
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super().get()   
                self.h = float(input("Enter height: ")) 
	def  area(self):
		return 2 * math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h
	def  volume(self):
		return math.pi * self.r ** 2 * self.h
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
				c1 = circle()
                                c1.get()
				print('Area  :  ' ,  c1.area())
				print('Circumference :  ' ,  c1.cir())
		case  2:
				c2 = cylinder()
                                c2.get()
				print('Area : ' ,  c2.area())
				print('Volume :  ' ,  c2.volume())
		case  3:
				break
	# End  of  match



'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a

2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  ---> 2 * (a + b)

3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  --->  a ^ 3

4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
'''
class   square:
	def   get(self):
		self.a = float(input("Enter side: "))
	def   area(self):
		return self.a ** 2
	def   peri(self):
		return 4 * self.a
class   rectangle(square):
	def   get(self):
		 self.l = float(input("Enter length: "))
                 self.b = float(input("Enter breadth: "))
	def   area(self):
		 return self.l * self.b
	def   peri(self):
		return 2 * (self.l + self.b)
class   cube(square):
	def   get(self):
		 super().get()
	def   area(self):
		return 6 * self.a ** 2
	def   volume(self):
		return self.a ** 3
def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
while  True:
	menu()
	ch = int(input('Enter  choice : ')) 
	match   ch:
		case   1:
			s = square()
                        s.get()
			print('Area   :  ' ,  ???)
			print('Perimeter  :  ' , ???)
		case   2:
			r = rectangle()
                        r.get()
			print('Area  :  ' ,  ???)
			print('Perimeter  :  ' ,  ???)
		case   3:
			c = cube()
                        c.get()
			print('Area  :   ' ,  ???)
			print('Volume  :  ' ,  ???)
		case  4:
			break



# Find  outputs
class  c1:
	def  m1(self):
		print('m1  method  of  class  c1')
class  c2:
	def  m1(self):
		print('m1 method of class c2')
class  c3:
	@classmethod
	def  m1(cls):
		print('m1 method of  class c3')
class  c4:
	@staticmethod
	def  m1():
		print('m1 method of  class c4')
class  c5(c1):
	def  m1(self):
		print('m1 method of class c5')
	def  m2(self):
		c3.m1()
                c4.m1()
                c2().m1()
                super().m1()
                self.m1()
                m1()
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
How  to  call  m2()  method  of  class  c5



'''
Write  a  program  to  delete  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''

import os

path = input("Enter path of directory: ")

try:
    os.rmdir(path)
    print("Directory or directories removed")
except FileNotFoundError:
    print("Directory not found")
except OSError:
    print("Directory is not empty")


'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''

import os

path = input("Enter path of directory: ")

try:
    os.removedirs(path)
    print("Directory or directories removed")
except FileNotFoundError:
    print("Directory not found")
except OSError:
    print("Directory is not empty")


#  Write  a  program  to  rename  a  file

import os

old_name = input("Enter 1st file name: ")
new_name = input("Enter 2nd file name: ")

try:
    os.rename(old_name, new_name)
    print("File renamed successfully")
except FileNotFoundError:
    print("File not found")
except FileExistsError:
    print("New file name already exists")


# Write  a  program  to  rename  a  directory

import os

old_name = input("Enter old directory name: ")
new_name = input("Enter new directory name: ")

try:
    os.rename(old_name, new_name)
    print("Directory renamed successfully")
except FileNotFoundError:
    print("Directory not found")
except FileExistsError:
    print("New directory name already exists")


'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''


# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory




