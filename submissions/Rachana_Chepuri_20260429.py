#Write  a  program  to  print  first  'n'  rows  of  emp  table
import mysql.connector as mc
con=mc.connect(database='sssdc',user='root')
cur=con.cursor()
cur.execute('select * from emp')
n=int(input("Enter how many rows? : "))
if n<=0:
    print("Fetched zero rows")
else:
    list=cur.fetchmany(n)
    print(list)
    print(cur.rowcount())
try:
    cur.close()
    con.close()
except:
    print("Conn cannot be closed")

#Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time
import mysql.connector as mc
con=mc.connect(database='sssdc',user='root')
cur=con.cursor()
while True:
    empno=int(input("Enter empno : "))
    ename=input("Enter table name : ")
    marks=int(input("Enter marks : "))
    cur.execute(f"insert into emp values({empno}, '{ename}', {marks})")
    con.commit()
    print("1 row is inserted")
    choice=input(" Want to insert new record(y/n): ")
    if choice.lower()!='y':
        break
cur.close()
con.close()

#Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition
import mysql.connector as mc
con=mc.connect(databse='sssdc',user='root')
cur=con.cursor()
cond=input("Enter condition : ")
if cond=='':
    cur.execute(f"delete from emp")
    print("Deleted rows")
else:
    cur.execute(f"delete from emp where {cond}")
    print("Deleted rows from emp")
con.commit()
cur.close()
con.close()

# Write  a  program to  modify  data  of  emp  table
import mysql.connector as mc
con=mc.connect(database='sssdc'. user='root')
cur=con.cursor()
exp=input("Enter exp : ")
cond=input("Enter cond : ")
cur.execute(f"update emp set {exp} where {cond}")
con.commit()
cur.close()
con.close()

# Write  a  program  to  create  student  table
import mysql.connector as mc
con=mc.connect(database='sssdc', user='root')
cur=con.cursor()
table_name=input("Enter table name : ")
rno=int(input("Enter roll num : "))
sname=input("Enter s name : ")
marks=int(input("Enter marks : "))
try:
    cur.execute(f"create table {table_name}({rno} int, '{sname}' varchar(50), {marks} int)")
    print("Table {table_name} is created")
except:
    cur.execute(f"drop table {table_name}")
    cur.execute(f"create table {table_name}({rno} int, '{sname}' varchar(50), {marks} int)")
    print("Table {table_name} is created")
    
con.commit()
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
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1() # Error 
		#m1()  # error, bcz no func
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()
#super() . m1()  # Error , bcz we cant use super() outside class
#self . m1() # error, self is not dfined 

# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()  # child method 
		#self . m1() # error 
		#m1() Error 
		print('child  Method')
# End  of  the  class
parent.m1()
child.m1()#How  to  call  m1()  method  of  child  class

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
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		#super() . m1() # Error
		#super(child) . m1() # error
		#self . m1()  #error
		#cls . m1()  # error 
		print('child  method')
#end of the class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()

# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		#super() . m1()  # error
		#self . m1()  
		#cls . m1()   
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class

# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x) #How  to  print  variable  'x'
		print(parent.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x)  # error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(super().x) #How  to  print  variable  'x'
		print(parent.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(p.x) #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(self.x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y) #How  to  print  variable  'y'
		print(child.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		#print(super() . y) # error
		#print(y)  #error
# End  of child  class
p=parent()
p.m1() #How  to  call   m1()  method  of  parent  class
c=child()
c.m2() #How  to  call   m2()  method  of  child  class


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
		print(p.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x) #How  to  print  variable  'x'  of  child  class
		print(self.x) #How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p=parent()
p.m1() #How  to  call  m1()  method  of  parent  class
c=child()
c.m1() #How  to  call  m1()  method  of  child  class


#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=int(input("Enter a value : "))
		self.b=int(input("Enter b value : "))  #How  to   read  inputs  into   variables  a  and  b  of  object		
	def    disp(self):
		print(f'{self.a}\t {self.b}') #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a=int(input("Enter a value : "))
		self.b=int(input("Enter b value : ")) #How  to   read  inputs  into   variables  a  and  b  of  object
		self.c=int(input("Enter c value : "))
		self.d=int(input("Enter d value : ")) #How  to   read  inputs  into   variables  c  and  d  of  object		
	def   disp(self):
		print(f'{self.a}\t{self.b}') #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(f'{self.c}\t{self.d}') #How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return   self.a+self.b+self.c+self.d  
print('parent  object')
p=parent()
p.get() #How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()
c.get() #How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp() #How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp() #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c.total())


#Write  a  program  to  determine  area  and  circumference  of  circle.
#Also  find  area  and  volume  of  cylinder
import math
class circle:
	def get(self):
		self.r=float(input("Enter radius : ")) #How  to  read  radius  into  object
	def area(self):
		return  math.pi * (self.r ** 2)
	def cir(self):
		return  2 * math.pi * self.r
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r=float(input("Enter radius : "))#How  to  read  radius  into  the  object  
		self.h=float(input("Enter height : ")) #How  to  read  height  into  the  object 
	def  area(self):
		return  super().area() + 2 * math.pi * self.r * self.h #area  of  cylindersuper
	def  volume(self):
		return   math.pi * (self.r **2)* self.h
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
				c=circle()
				c.get() #How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  c.area())
				print('Circumference :  ' ,  c.cir())
		case  2:
				cy=cylinder() #How  to  read  raidus  and  height  into  cylinder  object
				cy.get()
				print('Area : ' ,  cy.area())
				print('Volume :  ' ,  cy.volume())
		case  3:
				exit()
	# End  of  match


#Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
#Also  find  surface  area  and  volume  of  cube

class   square:
	def   get(self):
		self.a=float(input("Enter side : "))#How  to  read  side  of  square
	def   area(self):
		return  self.a **2
	def   peri(self):
		return   4*self.a
class   rectangle(square):
	def   get(self):
		self.l=float(input("Enter length : "))#How  to  read  length  of  rectangle
		self.b=float(input("Enter breadth : ")) #How  to  read  breadth  of  rectangle
	def   area(self):
		return  self.l * self.b
	def   peri(self):
		return   2 * (self.l + self.b)
class   cube(square):
	def   get(self):
		self.a=float(input("Enter side : "))#How  to  read  side  of  cube
	def   area(self):
		return  6 *(self.a**2)
	def   volume(self):
		return  self.a**3
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
			s=square() #How  to  read  side  into   square  object  's'
			s.get()
			print('Area   :  ' ,  s.area())
			print('Perimeter  :  ' , s.peri())
		case   2:
			r=rectangle() #How  to  read  length  and  breadth  into   rectangle  object  'r'
			r.get() 
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' ,  r.peri())
		case   3:
			c=cube() #How  to  read  side  into  cube  object  'c'
			c.get()
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			exit()


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
		c3.m1() #How  to  call  m1()  method  of  class  c3
		c4.m1() #How  to  call  m1()  method  of  class  c4
		c=c2()
		c.m1() #How  to  call  m1()  method  of  class  c2
		super().m1() #How  to  call  m1()  method  of  class  c1
		self.m1()#How  to  call  m1()  method  of  class  c5
		m1() #How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
cc=c5() 
cc.m2() #How  to  call  m2()  method  of  class  c5


#Write  a  program  to  delete  a  directory.
#Input  is  either  directory  name  (or)  path  of  the  directory
import os
path=input("Enter path : ")
try:
    r=os.rmdir(path)
    print(f"{path} removed")
except FileNotFoundError:
    print(f"{path} doesnot exists")
except OSError:
    print(f"{path} is non empty")


#Write  a  program  to  delete  a  group  of  directories
#Input  is  directory  path
import os
path=input("Enter path : ")
try:
    r=os.removedirs(path)
    print(f"{path} removed")
except FileNotFoundError:
    print(f"{path} doesnot exists")
except OSError:
    print(f"{path} is non empty")

##  Write  a  program  to  rename  a  file
import os
old=input("Enter old file : ")
new=input("Enter new file : ")
try:
    rn=os.rename(old,new)
    print(f"{old} file name renamed to {new}")
except FileNotFoundError:
    print(f"{old} does not exists")
except FileExistsError:
    print(f"{new} file name already exists")

# for directories
import os
old=input("Enter old dir : ")
new=input("Enter new dir : ")
try:
    rn=os.rename(old,new)
    print(f"{old} dir  renamed to {new}")
except FileNotFoundError:
    print(f"{old} does not exists")
except FileExistsError:
    print(f"{new} dir already exists")

#Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
#Input :  Directory  (or)  path
#Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

import os
path=input("Enter path : ")
li=os.listdir(path)
l1=[]
l2=[]
for d in li:
    if d.endswith('.txt'):
        l1.append(d)
    else:
        l2.append(d)
print("All sub - directories :", l2)
print("All files :", l1)

import os
path=input("Enter path : ")
g=os.walk()
for x in g:
    l1=[]
    l2=[]
    for y in x:
        if y.endswith('.txt'):
            l1.append(y)
        else:
            l2.append(y)
    print("All sub - directories :", l2)
    print("All files :", l1) 
