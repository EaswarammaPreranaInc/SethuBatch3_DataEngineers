'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
# Code :

import mysql.connector as mc
try:
    con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
    cur = con.cursor()
    cur.execute('select * from emp')
    n = int(input('How many rows ? : '))
    if n<=0:
        print('Number of rows fetched : 0 ')
    else :
        list=cur.fetchmany(n)
        temp = cur.description
        for x in temp:
            print(f'{x[0]: ^10}',end='\t')
        print()
        for row in list:
            for val in row:
                print(f'{val: ^10}',end='\t')
            print()
        print('Number of tuples fetched :  ',cur.rowcount)
        cur.close()
        con.close()
except mc.errors.InterfaceError :
    print('Please connect to the database first')
except mc.errors.ProgrammingError :
    print('The database or user or password is incorrect')
except mc.errors.InternalError:
    print('Cursor can not be closed')

''' Output:
How many rows ? : 2
  empno           ename            sal    
   111           Rama Rao        10000.0  
   222             Sita          20000.0  
Number of tuples fetched :   2
Cursor can not be closed

How many rows ? : 5
  empno           ename            sal    
   111           Rama Rao        10000.0  
   222             Sita          20000.0  
   333            Rajesh         15000.0  
Number of tuples fetched :   3

How many rows ? : 0
Number of rows fetched : 0

How many rows ? : -1
Number of rows fetched : 0
'''
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
# Code :

import mysql.connector as mc
try:
    con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
    cur = con.cursor()
    while True:
        empno = int(input('Enter empno : '))
        ename = input('Enter emp name : ')
        sal = int(input('Enter salary : '))
        cur.execute(f"insert into emp values({empno},'{ename}',{sal})")
        print('1 row inserted')
        ans = input('Insert another row ? (y/n) : ')
        if ans == 'n' or ans == 'N':
            break
    con.commit()
    cur.close()
    con.close()
except mc.errors.IntegrityError:
    print('Duplicate empno and hence the row can not be inserted')
except mc.errors.InterfaceError :
    print('Please connect to the database first')
except mc.errors.ProgrammingError :
    print('The database or user or password is incorrect')
except mc.errors.InternalError:
    print('Cursor can not be closed')

''' Output:
Enter empno : 444
Enter emp name : AAA
Enter salary : 40000
1 row inserted
Insert another row ? (y/n) : y
Enter empno : 555
Enter emp name : BBB
Enter salary : 50000
1 row inserted
Insert another row ? (y/n) : n

Enter empno : 222
Enter emp name : KKK
Enter salary : 20000
Duplicate empno and hence the row can not be inserted
'''

'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
# Code :

import mysql.connector as mc
try:
    con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
    cur = con.cursor()
    cond = input('Enter condition (Enter to delete all the rows) : ' )
    if cond =='':
        cur.execute('delete from emp')
        print(cur.rowcount,'rows deleted')
    else:
        cur.execute(f'delete from emp where {cond}')
        print(cur.rowcount,'rows deleted')
    con.commit()
    cur.close()
    con.close()
except mc.errors.InterfaceError :
    print('Please connect to the database first')
except mc.errors.ProgrammingError :
    print('The database or user or password is incorrect')

''' Output:
Enter condition (Enter to delete all the rows) : sal > 30000
2 rows deleted

Enter condition (Enter to delete all the rows) : 
3 rows deleted
'''
'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
'''
# Code : 

import mysql.connector as mc
try:
    con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
    cur = con.cursor()
    cond = input('Enter condition (Enter key to modify all the rows ) : ' )
    expr = input('Enter expression : ')
    if cond =='':
        cur.execute(f'update emp set {expr}')
        print(cur.rowcount,'rows are updated')
    else:
        cur.execute(f'update emp set {expr} where {cond}')
        print(cur.rowcount,'rows are updated')
    con.commit()
    cur.close()
    con.close()
except mc.errors.InterfaceError :
    print('Please connect to the database first')
except mc.errors.ProgrammingError :
    print('The database or user or password is incorrect')


''' Output:
Enter condition (Enter key to modify all the rows ) : sal>18000
Enter expression : sal=sal+1000
1 rows are updated
'''
'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->									
	cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->																
			Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
# Code :
import mysql.connector as mc
try:
    con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
    cur = con.cursor()
    tbl = input('Enter table name : ')
    cur.execute(f'create  table  {tbl}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
    print(f'{tbl} table is created')
    cur.close()
    con.close()
except:
    print(f'Existing {tbl} table is deleted')
    cur.execute(f'drop table {tbl}')
    cur.execute(f'create  table  {tbl}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
    print(f'New {tbl} table is created')

''' Output:
Enter table name : stud
stud table is created

Enter table name : emp
Existing emp table is deleted
New emp table is created
'''
# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1() # parent  Method
		super().m1() # parent  Method
		cls.m1() # parent  Method
		child().m1() # parent  Method
		# self . m1() # Error m1() is a classmethod not a instance method	
		# m1() # Error cannot call m1() method directly
		print('child  Method')
# End  of  the  class
parent.m1() # parent Method
c = child()
c.m2() # child Method
child . m1() # parent Method
super() . m1()  # Error super() method cannot be called outside the function
self . m1() # Error variable self is not defined

# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
                parent().m1() # parent  Method
		super().m1() # parent  Method
		# cls . m1()  # Infinite recursion
		# self . m1() # Error variable self is not defined
		# m1() # Error m1() function is not defined
		print('child  Method')
# End  of  the  class
parent.m1() # parent  Method
child.m1() # child  Method

# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1() # parent method
		parent().m1() # parent method
		child().m1() # parent method
		#super() . m1() # Error super() function needs two arguments
		#super(child) . m1()  # Error super() function needs two arguments
		#self . m1()  # Error variable self is not defined
		#cls . m1()  # Error variable cls is not defined
		print('child  method')
#end of the class
parent.m1() # parent method
child().m2() # child method
child . m1() # parent method

# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() # parent method
		super(child,child).m1()  # parent method
		# super() . m1() # Error super() function requires two arguments but not no arguments
		# self . m1() # Error variable self is not defined
		# cls . m1() # Error variable cls is not defined
		print('child  method')
# End  of  the  class
parent.m1()  # parent method
child.m1()  # child method

# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) # 10
		print(parent().x) # 10
		print(self.x) # 10
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x) # 10
		print(child.x) # 10
		print(super().x) # 10
		print(parent.x) # 10
		print(child().y) # 20
		print(child.y) # 20
		# print(super() . y) # Error because there is no variable y in parent class
		# print(y) # Error variable y is not defined  
# End  of child  class
parent().m1()
child().m2()

# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x) # 10
		print(parent.x) # 10
class   child(parent):
	x = 20
	def  m1(self):
		print(parent().x) # 10
		print(super().x) # 10
		print(child.x) # 20
		print(self.x) # 20
# End  of  the  class
parent().m1() 
child().m1()

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class parent:
    def get(self):
        self.a = int(input())
        self.b = int(input())

    def disp(self):
        print(self.a, self.b, sep='\t',end='\t')

class child(parent):
    def get(self):
        super().get()
        self.c = int(input())
        self.d = int(input())

    def disp(self):
        super().disp()
        print(self.c, self.d, sep='\t')

    def total(self):
        return self.a + self.b + self.c + self.d

print('parent object')
p = parent()
p.get()
print('child object')
c = child()
c.get()
print('parent object  :  ', end='\t')
p.disp()
print()
print('child object  :  ', end='\t')
c.disp()
print('Sum of the values in child object :  ', c.total())

''' Output:
parent object
10
20
child object
30
40
50
60
parent object  :        10      20
child object  :         30      40      50      60
Sum of the values in child object :   180
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
	    self.r = float(input('Enter Radius of the circle : '))
	def   area(self):
		return  round(math.pi * self.r * self.r,2)
	def   cir(self):
		return  round(2 * math.pi * self.r,2)
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super().get() 
		self.h = float(input('Enter height of the cylinder : '))
	def  area(self):
		return  round(2 * super().area()+ super().cir() * self.h ,2)
	def  volume(self):
		return  round(super().area()* self.h,2)
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
				c = circle()
				c.get()
				print('Area  :  ' ,  c.area())
				print('Circumference :  ' ,  c.cir())
		case  2:
				cy = cylinder()
				cy.get()
				print('Area : ' ,  cy.area())
				print('Volume :  ' ,  cy.volume())
		case  3:
				break;
	# End  of  match

''' Output:
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 2
Enter Radius of the circle : 3.5
Enter height of the cylinder : 4.8
Area :  182.51
Volume :   184.7
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 1
Enter Radius of the circle : 2.9
Area  :   26.42
Circumference :   18.22
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 3
'''
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
class square:
    def get(self):
        self.side = float(input('Enter a side : '))
    def area(self):
        return self.side * self.side
    def peri(self):
        return 4 * self.side

class rectangle(square):
    def get(self):
        super().get()
        self.breadth = float(input('Enter breadth : '))
    def area(self):
        return self.side * self.breadth
    def peri(self):
        return 2 * (self.side + self.breadth)

class cube(square):
    def get(self):
        super().get()
    def area(self):
        return 6 * self.side * self.side
    def volume(self):
        return self.side * self.side * self.side

def menu():
    print('1 . Square')
    print('2 . Rectangle')
    print('3 . Cube')
    print('4 . Exit')
# End of the function
while True:
    menu()
    ch = int(input('Enter choice : '))
    match ch:
        case 1:
            s = square()
            s.get()
            print('Area   :  ', s.area())
            print('Perimeter  :  ', s.peri())
        case 2:
            r = rectangle()
            r.get()
            print('Area  :  ', r.area())
            print('Perimeter  :  ', r.peri())
        case 3:
            c = cube()
            c.get()
            print('Area  :   ', c.area())
            print('Volume  :  ', c.volume())
        case 4:
            break

''' Output:
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter choice : 2
Enter a side : 4
Enter breadth : 5
Area  :   20.0
Perimeter  :   18.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter choice : 3
Enter a side : 5
Area  :    150.0
Volume  :   125.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter choice : 1
Enter a side : 4
Area   :   16.0
Perimeter  :   16.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter choice : 4
'''

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
		c3.m1() # m1 method of  class c3
		c4.m1() # m1 method of  class c4
		c2().m1() # m1 method of class c2
		super().m1() # m1  method  of  class  c1
		self.m1() # m1 method of class c5
		m1() # m1 function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c5().m2()

'''
Write  a  program  to  delete  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
# Code :
import os
path = input('Enter directory name (or) path : ')
try :
    os.rmdir(path)
    print(f'Directory {path} is removed')
except FileNotFoundError:
    print(f'Directory {path} does not exist')
except OSError:
    print(f'Directory {path} is non-empty') 

''' Output:
Enter directory name (or) path : d:/a/b
Directory d:/a/b does not exist
'''
'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
# Code :
import os
path = input('Enter path of directory : ')
try :
    os.removedirs(path)
    print(f'Directory or directories are removed')
except FileNotFoundError:
    print(f'Directory {path} does not exist')
except OSError:
    print(f'Directory {path} is non-empty')

''' Output:
Enter path of directory : d:\A\B
Directory or directories are removed
'''
# Write  a  program  to  rename  a  directory
# Code :
import os
file1 = input('Enter 1st file name : ')
file2 = input('Enter 2nd file name : ')
try :
    os.rename(file1,file2)
    print(f'File {file1} is renamed to {file2}')
except FileNotFoundError:
    print(f'File {file1} does not exists')
except FileExistsError:
    print(f'File {file2} exists')

''' Output:
Enter 1st file name : emp.py
Enter 2nd file name : venus.py
File emp.py does not exists
'''
'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
# Code :
import os
def listdir(path):
    files = []
    dirs = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)      
        elif os.path.isdir(os.path.join(path, item)):
            dirs.append(item)                                       
    return files, dirs

path = input('Enter directory path : ')
files, dirs = listdir(path)
print('Files : ', files)
print('Directories : ', dirs)

''' Output:
Enter directory path : C:\Users\Dhanya\Desktop\SSSDC_Batch
Files :  ['DhanyaSri_Kokku_D-355.py', 'Github_uploading_guidelines.txt']
Directories :  ['.vscode', 'Home_Work', 'Sec', 'SQL_Assignments', 'Test']
'''

# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
# Code :

import os
path = input("Directory Path :")
items = os.listdir(path)
dirs = []
files = []
for item in items:
    if os.path.isdir(os.path.join(path, item)):
        dirs.append(item)
    else:
        files.append(item)

print("Sub Directories :", dirs)
print("Files :", files)