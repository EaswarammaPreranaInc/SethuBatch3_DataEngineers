'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = con.cursor()

cur.execute("SELECT empno, ename, sal FROM emp")

n = int(input("How many rows ?: "))

rows = cur.fetchmany(n)

print("{:<10} {:<15} {:<10}".format("empno", "ename", "sal"))

for row in rows:
    print("{:<10} {:<15} {:<10}".format(row[0], row[1], row[2]))

print("Number of tuples fetched :", len(rows))

cur.close()
con.close()
#=====================================================================================
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

con = mc.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = con.cursor()

while True:
    try:
        empno = int(input("Enter empno : "))
        ename = input("Enter emp name : ")
        sal = float(input("Enter salary : "))

        cur.execute(f"insert into emp values ({empno}, '{ename}', {sal})")
        con.commit()

        print(cur.rowcount, "row is inserted")

    except mc.errors.IntegrityError:
        print("Duplicate empno and hence row can not be inserted")

    ch = input("Insert another row ? (y / n) : ")
    if ch.lower() != 'y':
        break

cur.close()
con.close()
#====================================================================================
'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
import mysql.connector as mc

con = mc.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = con.cursor()

cond = input("Enter condition (Enter to delete all the rows): ")

if cond.strip() == "":
    cur.execute("delete from emp")
else:
    cur.execute(f"delete from emp where {cond}")

con.commit()

print(cur.rowcount, "rows are deleted")

cur.close()
con.close()
#==============================================================================
'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
'''
import mysql.connector as mc

con = mc.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = con.cursor()

cond = input("Enter condition (Enter key to modify all the rows) : ")
expr = input("Enter expression : ")

if cond.strip() == "":
    cur.execute(f"update emp set {expr}")
else:
    cur.execute(f"update emp set {expr} where {cond}")

con.commit()

print(cur.rowcount, "rows are updated")

cur.close()
con.close()
#=============================================================================================
'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->									
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->																
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
import mysql.connector as mc

con = mc.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = con.cursor()

tablename = input("Enter table name : ")

try:
    cur.execute(f"create table {tablename}(rollno int primary key, sname char(20), marks float)")
    print(tablename, "table is created")
except mc.errors.ProgrammingError:
    cur.execute(f"drop table {tablename}")
    print("Existing", tablename, "table is deleted")
    cur.execute(f"create table {tablename}(rollno int primary key, sname char(20), marks float)")
    print("New", tablename, "table is created")

cur.close()
con.close()
#=====================================================================================================
# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super().m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()  
		m1()  
		print('child  Method')
# End  of  the  class
child.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()  
self . m1()
#=============================================================================================
# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()   
		self . m1()  
		m1()  
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class
#================================================================================================================
# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super(child, child).m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() 
		super(child) . m1() 
		self . m1()  
		cls . m1()  
		print('child  method')
#end of the class
child.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()
#==================================================================================
# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child, child).m1()#How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()  
		self . m1()  
		cls . m1()   
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class
#===================================================================================================================
# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'
		print(parent.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)  
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x)#How  to  print  variable  'x'
		print(parent.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x)#How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y)#How  to  print  variable  'y'
		print(child.y)#How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) 
		print(y)  
# End  of child  class
p = parent()
p.m1()#How  to  call   m1()  method  of  parent  class
c = child()
c.m2()    #How  to  call   m2()  method  of  child  class
#=======================================================================================================
# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(super().x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x)#How  to  print  variable  'x'  of  child  class
		print(child.x)#How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c = child()
c.m1()#How  to  call  m1()  method  of  child  class
#=======================================================================================================
#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a = int(input())
        self.b = int(input())#How  to   read  inputs  into   variables  a  and  b  of  object		
	def    disp(self):
		print(self.a, self.b, sep="\t", end="\t")#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def  get(self):
		#How  to   read  inputs  into   variables  a  and  b  of  object
		#How  to   read  inputs  into   variables  c  and  d  of  object
         self.a = int(input())
         self.b = int(input())
         self.c = int(input())
         self.d = int(input())		
	def   disp(self):
		#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		#How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
		print(self.a, self.b, sep="\t", end="\t")
        print(self.c, self.d, sep="\t", end="\t")
	def  total(self):
		#return   sum  of  values  in  object 
		return self.a + self.b + self.c + self.d 
# End of child class
print('parent  object')
#How  to  read  inputs  into  parent  class  object  'p'
p = parent()
p.get()

print('child  object')
#How  to  read  inputs  into  child  class  object  'c'
c = child()
c.get()

print('parent  object  :  ' , end = '\t')
#How  to  print  object  'p'
p.disp()
print()

print('child  object  :  ' , end = '\t')
#How  to  print  object  'c'
c.disp()
print()
print('Sum of  the  values  in  child  object :  ' , c.total())# How  to  obtain  sum of  values  of  object  'c')
#=======================================================================================================================
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
	    self.r = float(input("Enter Radius of the circle : "))#How  to  read  radius  into  object
	def   area(self):
		return 3.14159 * self.r ** 2      #return  area  of  circle
	def   cir(self):
		return 2 * 3.14159 * self.r      #return  circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r = float(input("Enter Radius of the circle : "))        #How  to  read  radius  into  the  object  
		self.h = float(input("Enter height of the cylinder : "))       #How  to  read  height  into  the  object 
	def  area(self):
		return 2 * 3.14159 * self.r ** 2 + 2 * 3.14159 * self.r * self.h          #return  area  of  cylinder
	def  volume(self):
		return 3.14159 * self.r ** 2 * self.h                     #return   volume  of  cylinder
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
		case 1:
            c = circle()
            c.get()
            print("Area : ", round(c.area(), 2))
            print("Circumference : ", round(c.cir(), 2))

        case 2:
            cy = cylinder()
            cy.get()
            print("Area : ", round(cy.area(), 2))
            print("Volume : ", round(cy.volume(), 2))

        case 3:
            break
#=================================================================================================================
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
		self.a = float(input("Enter a Side : "))      #How  to  read  side  of  square
	def   area(self):
		return self.a ** 2          #return  area  of  square
	def   peri(self):
		return 4 * self.a      #return   perimeter  of  square
class   rectangle(square):
	def   get(self):
		self.a = float(input("Enter a Side : ")) #How  to  read  length  of  rectangle
		self.b = float(input("Enter Breadth : "))  #How  to  read  breadth  of  rectangle
	def   area(self):
		return self.a * self.b    #return  area  of  rectangle
	def   peri(self):
		return 2 * (self.a + self.b)#return   perimeter  of   rectangle
class   cube(square):
	def   get(self):
		self.a = float(input("Enter a Side : "))#How  to  read  side  of  cube
	def   area(self):
		return 6 * self.a ** 2 #return  area  of  cube
	def   volume(self):
		return self.a ** 3   #return  volume  of  cube
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
			s = square()#How  to  read  side  into   square  object  's'
			s.get()
			print('Area   :  ' , round(s.area(), 2))
			print('Perimeter  :  ' , round(s.peri(), 2))
		case   2:
			r = rectangle()#How  to  read  length  and  breadth  into   rectangle  object  'r'
			r.get()
			print('Area  :  ' ,  round(r.area(), 2))
			print('Perimeter  :  ' ,  round(r.peri(), 2))
		case   3:
			c = cube()#How  to  read  side  into  cube  object  'c'
			c.get()
			print('Area  :   ' ,  round(c.area(), 2))
			print('Volume  :  ' ,  round(c.volume(), 2))

		case  4:
			break#How  to  stop  execution
#=============================================================================================================
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
		c3.m1()How  to  call  m1()  method  of  class  c3
		c4.m1()#How  to  call  m1()  method  of  class  c4
		c2().m1()#How  to  call  m1()  method  of  class  c2
		c1().m1()#How  to  call  m1()  method  of  class  c1
		self.m1()#How  to  call  m1()  method  of  class  c5
		m1()#How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
#How  to  call  m2()  method  of  class  c5	
obj = c5()
obj.m2()
#========================================================================================================
'''
Write  a  program  to  delete  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
import os

path = input("Enter directory name (or) path : ")

if not os.path.exists(path):
    print("Directory", path, "does not exist")

elif not os.path.isdir(path):
    print(path, "is not a directory")

else:
    try:
        os.rmdir(path)
        print("Directory", path, "is removed")
    except OSError:
        print("Directory", path, "is non-empty")

#======================================================================================================
'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
import os
import shutil

path = input("Enter path of directory : ")

if not os.path.exists(path):
    print("Directory", path, "does not exist")

else:
    shutil.rmtree(path)
    print("Directory (or) directories are removed")

#========================================================================================================
#  Write  a  program  to  rename  a  file
import os

f1 = input("Enter 1st filename : ")
f2 = input("Enter 2nd filename : ")

if not os.path.exists(f1):
    print("File", f1, "does not exist")

elif os.path.exists(f2):
    print("File", f2, "exists")

else:
    os.rename(f1, f2)
    print("File", f1, "is renamed to", f2)

#=======================================================================================
# Write  a  program  to  rename  a  directory
import os

d1 = input("Enter 1st directory name : ")
d2 = input("Enter 2nd directory name : ")

if not os.path.exists(d1):
    print("Directory", d1, "does not exist")

elif os.path.exists(d2):
    print("Directory", d2, "exists")

else:
    os.rename(d1, d2)
    print("Directory", d1, "is renamed to", d2)

#========================================================================================================
'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import os

path = input("Enter directory name (or) path : ")

if not os.path.exists(path):
    print("Directory", path, "does not exist")

else:
    files = []
    dirs = []

    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
        elif os.path.isdir(os.path.join(path, item)):
            dirs.append(item)

    print("Files of directory", path, ":", files)
    print()
    print("Directories of directory", path, ":", dirs)

#======================================================================================================================
# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import os

for path, dirs, files in os.walk("sairam"):
    print("Directory Path :", path)
    print("Sub Directories :", dirs)
    print("Files :", files)
    print()                                	
		
	
    
    
    
    
    
    
    
    
    