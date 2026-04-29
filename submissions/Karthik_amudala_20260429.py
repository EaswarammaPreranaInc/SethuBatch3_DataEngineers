
Write  a  program  to  print  first  'n'  rows  of  emp  table
 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
How many rows ? : 2
   empno            ename            sal
    111          Rama Rao        10000.0
    222             Sita         20000.0
Number of tuples fetched : 2
Cursor can not be closed
How many rows ? : 5
   empno            ename            sal
    111          Rama Rao        10000.0
    222             Sita         20000.0
    333            Rajesh        15000.0
Number of tuples fetched : 3
How many rows ? : 0
Number of tuples fetched : 0
How many rows ? : -1
Number of tuples fetched : 0


import mysql.connector as mc
try:
    con = mc.connect(database='emp1', user='root')
    cur = con.cursor()
    n = int(input('How many rows ? : '))
    if n <= 0:
        rows = []
    else:
        cur.execute('select * from emp')
        rows = cur.fetchmany(n)
    if len(rows) > 0:
        for x in cur.description:
            print('{:^10}'.format(x[0]), end='\t')
        print()
        for tpl in rows:
            for x in tpl:
                print('{:^10}'.format(str(x)), end='\t')
            print()
    print('Number of tuples fetched :', len(rows))
    try:
        cur.close()
    except:
        print('Cursor can not be closed')
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) table name')
except mc.errors.InterfaceError:
    print('Please start mysql')


Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time
1) How  to  call  execute()  method ?  --->	cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")
2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string
3) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  inputs  empno , ename  and  sal
4) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table
5) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError
6) Can  a  tuple  be  inserted  into  MySqlCursor  object ?  --->  No  becoz  it  is  immutable
Enter empno : 444
Enter emp name : AAA
Enter salary : 40000
1 row is inserted
Insert another row ? (y / n) : y
Enter empno : 555
Enter emp name : BBB
Enter salary : 50000
1 row is inserted
Insert another row ? (y / n) : n
Enter empno : 222
Enter emp name : KKK
Enter salary : 20000
Duplicate empno and hence row can not be inserted
Insert another row ? (y / n) : y
Enter empno : 666
Enter emp name : CCC
Enter salary : 60000
1 row is inserted
Insert another row ? (y / n) : n



import mysql.connector as mc
try:
    con = mc.connect(database='emp1', user='root')
    cur = con.cursor()
    while True:
        empno = int(input('Enter empno : '))
        ename = input('Enter emp name : ')
        sal = float(input('Enter salary : '))
        try:
            cur.execute(f"insert into emp values({empno},'{ename}',{sal})")
            con.commit()
            print(cur.rowcount,'row is inserted')
        except mc.errors.IntegrityError:
            print('Duplicate empno and hence row can not be inserted')
        ch = input('\nInsert another row ? (y / n) : ')
        if ch.lower() == 'n':
            break
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) table name')
except mc.errors.InterfaceError:
    print('Please start mysql')


Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition
1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')
2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
Enter condition (Enter to delete all the rows): sal > 30000
3 rows are deleted
Enter condition (Enter to delete all the rows):
3 rows are deleted
'''
import mysql.connector as mc
try:
    con = mc.connect(database='emp1', user='root')
    cur = con.cursor()
    cond = input('Enter condition (Press Enter key to delete all the rows): ')
    if cond == '':
        cur.execute('delete from emp')
    else:
        cur.execute(f'delete from emp where {cond}')
    con.commit()
    print(cur.rowcount,'rows are deleted')
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) table name')
except mc.errors.InterfaceError:
    print('Please start mysql')


Write  a  program to  modify  data  of  emp  table
1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')
2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
Enter condition (Enter key to modify all the rows): sal < 18000
Enter expression : sal = sal + 1000
2 rows are updated

import mysql.connector as mc
try:
    con = mc.connect(database='emp1', user='root')
    cur = con.cursor()
    cond = input('Enter condition (Press Enter key to modify all the rows): ')
    expr = input('Enter expression : ')
    if cond == '':
        cur.execute(f'update emp set {expr}')
    else:
        cur.execute(f'update emp set {expr} where {cond}')
    con.commit()
    print(cur.rowcount,'rows are updated')
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) table name')
except mc.errors.InterfaceError:
    print('Please start mysql')



Write  a  program  to  create  student  table
1) How  to  call  execute()  method ?  --->	cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')														
2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name
3) What  action  to  be  made  when  table  already  exists ?  --->	Delete  the  existing  table  and  create  a  new  table  with  same  name																													
Enter table name : stud
stud table is created
Enter table name : emp
Existing emp table is deleted
New emp table is created



import mysql.connector as mc
try:
    con = mc.connect(database='emp1',user='root')
    cur = con.cursor()
    tablename = input('Enter table name : ')
    try:
        cur.execute(f'create table {tablename}(rollno int primary key, sname char(20), marks float)')
        print(tablename,'table is created')
    except mc.errors.ProgrammingError:
        cur.execute(f'drop table {tablename}')
        print('Existing',tablename,'table is deleted')
        cur.execute(f'create table {tablename}(rollno int primary key, sname char(20), marks float)')
        print('New',tablename,'table is created')
    con.commit()
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) table name')
except mc.errors.InterfaceError:
    print('Please start mysql')


# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()  # Error because self can't be used in class method
		m1()  # Error because m1() can't be called directly
		print('child  Method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child . m1() # Another way to call m1()
super() . m1() # Error because super() can't be used outside class methods
self . m1() # Error because self can't be used outside class

parent Method
parent Method
parent Method
parent Method
parent Method
child Method
parent Method


# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1() # ERROR because m1() calling itself
		self . m1() # ERROR because self can't be used in class method
		m1()  # ERROR because m1() can't be called directly
		print('child  Method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class



parent Method
parent Method
parent Method
parent Method
parent Method
child Method
parent Method
	

# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		m1 = parent.m1
        m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
	    super() . m1() # ERROR because super() can't be used in static method
		super(child) . m1() # EROOR because no arguments for super() in static method
		self . m1() # ERROR because self can't be used in static method 
		cls . m1()  # ERROR because cls can't be used in static method
		print('child  method')
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child . m1() # Another way to call m1()



parent method
parent method
parent method
parent method
child method
parent method







# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m = parent.m1
        m() # How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
	    super() . m1() # ERROR because super() can't be used in static method
		self . m1()  # ERROR because self can't be used in static method
		cls . m1()   # ERROR because cls can't be used in static method
		print('child  method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class



parent method
parent method
parent method
child method





# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x) # How  to  print  variable  'x'
		print(parent.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x) # Error because x can't be directly used
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x) # How  to  print  variable  'x'
		print(parent.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child.x) # How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x) # How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y) # How  to  print  variable  'y'
		print(child.y) # How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) # # Error because parent class has no variable y
		print(y) # Error because y can't be directly used
# End  of child  class
p = parent()
p.m1() # How  to  call   m1()  method  of  parent  class
c = child()
c.m2() # How  to  call   m2()  method  of  child  class




10
10
10
10
10
10
20
20






# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x) # How  to  print  variable  'x'  of  parent  class
		print(parent.x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(super().x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x) # How  to  print  variable  'x'  of  child  class
		print(child.x) # How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent()
p.m1() # How  to  call  m1()  method  of  parent  class
c = child()
c.m1() # How  to  call  m1()  method  of  child  class




10
10
10
10
20
20





#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a = int(input('Enter a : '))
		self.b = int(input('Enter b : ')) # How  to   read  inputs  into   variables  a  and  b  of  object		
	def    disp(self):
		print(self.a, self.b, sep='\t') # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super().get() # How  to   read  inputs  into   variables  a  and  b  of  object
		# How  to   read  inputs  into   variables  c  and  d  of  object		
		self.c = int(input('Enter c : '))
		self.d = int(input('Enter d : '))
	def   disp(self):
		print(self.a, self.b, end='\t') # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c, self.d, sep='\t') # How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self.a+self.b+self.c+self.d  
# End of child class
print('parent  object')
p = parent() # How  to  read  inputs  into  parent  class  object  'p'
p.get() 
print('child  object')
c = child() # How  to  read  inputs  into  child  class  object  'c'
c.get()
print('parent  object  :  ' , end = '\t')
p.disp()  # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp()  # How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,c.total())



parent object
child object
parent object :   10    20
child object :    30    40    50    60
Sum of the values in child object : 180






Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder
1) What  is  the  area  of  circle ?  ---> 3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r
2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h
3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
1. Circle
2. Cylinder
3. Exit
Enter choice : 2
Enter Radius of the circle : 3.5
Enter height of the cylinder : 4.8
Area : 182.53
Volume : 184.73
1. Circle
2. Cylinder
3. Exit
Enter choice : 1
Enter Radius of the circle : 2.9
Area : 26.42
Circumference : 18.22
1. Circle
2. Cylinder
3. Exit
Enter choice : 3



import math

class circle:
    def get(self):
        self.r = float(input('Enter Radius of the circle : '))
    def area(self):
        return math.pi * self.r ** 2
    def cir(self):
        return 2 * math.pi * self.r

class cylinder(circle):
    def get(self):
        super().get()
        self.h = float(input('Enter height of the cylinder : '))
    def area(self):
        return 2*math.pi*self.r**2 + 2*math.pi*self.r*self.h
    def volume(self):
        return math.pi*self.r**2*self.h

def menu():
    print('1. Circle')
    print('2. Cylinder')
    print('3. Exit')

while True:
    menu()
    ch = eval(input('Enter choice : '))
    match ch:
        case 1:
            c = circle()
            c.get()
            print('Area : ',round(c.area(),2))
            print('Circumference : ',round(c.cir(),2))

        case 2:
            cy = cylinder()
            cy.get()
            print('Area : ',round(cy.area(),2))
            print('Volume : ',round(cy.volume(),2))

        case 3:
            break




Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube
1) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a
2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  ---> 2 * (a + b)
3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  --->  a ^ 3
4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 2
Enter a Side : 4
Enter Breadth : 5
Area : 20.0
Perimeter : 18.0
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 3
Enter a Side : 5
Area : 150.0
Volume : 125.0
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 1
Enter a Side : 4
Area : 16.0
Perimeter : 16.0
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 4




class square:
    def get(self):
        self.a = float(input('Enter a Side : '))

    def area(self):
        return self.a * self.a

    def peri(self):
        return 4 * self.a


class rectangle(square):
    def get(self):
        self.a = float(input('Enter length : '))
        self.b = float(input('Enter Breadth : '))
    def area(self):
        return self.a * self.b
    def peri(self):
        return 2 * (self.a + self.b)


class cube(square):
    def get(self):
        super().get()
    def area(self):
        return 6 * self.a * self.a
    def volume(self):
        return self.a * self.a * self.a

def menu():
    print('1. Square')
    print('2. Rectangle')
    print('3. Cube')
    print('4. Exit')
while True:
    menu()
    ch = int(input('Enter choice : '))
    match ch:
        case 1:
            s = square()
            s.get()
            print('Area : ', s.area())
            print('Perimeter : ', s.peri())
        case 2:
            r = rectangle()
            r.get()
            print('Area : ', r.area())
            print('Perimeter : ', r.peri())
        case 3:
            c = cube()
            c.get()
            print('Area : ', c.area())
            print('Volume : ', c.volume())
        case 4:
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
		c3.m1() # How  to  call  m1()  method  of  class  c3
		c4.m1() # How  to  call  m1()  method  of  class  c4
		c2().m1() # How  to  call  m1()  method  of  class  c2
		super().m1() # How  to  call  m1()  method  of  class  c1
		self.m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
# How  to  call  m2()  method  of  class  c5
x = c5()
x.m2()

m1 method of class c3
m1 method of class c4
m1 method of class c2
m1 method of class c1
m1 method of class c5
m1 function


Write  a  program  to  delete  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
Enter directory name (or) path : d:\Hyd
Directory d:\Hyd is removed
Enter directory name (or) path : d:\Hyd
Directory d:\Hyd does not exist
Enter directory name (or) path : d:\A
Directory d:\A is non-empty
Enter directory name (or) path : d:\A\B
Directory d:\A\B is removed



import os
dirname = input('Enter directory name (or) path : ')
try:
    os.rmdir(dirname)
    print('Directory',dirname,'is removed')
except FileNotFoundError:
    print('Directory',dirname,'does not exist')
except OSError:
    print('Directory',dirname,'is non-empty')


Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
Enter path of directory : d:\A\B\C
Directory (or) directories are removed

import os
path = input('Enter path of directory : ')
try:
    os.removedirs(path)
    print('Directory (or) directories are removed')
except FileNotFoundError:
    print('Directory does not exist')
except OSError:
    print('Directories can not be removed')


#  Write  a  program  to  rename  a  file
Enter 1st filename : test.py
Enter 2nd filename : sample.py
File test.py is renamed to sample.py
Enter 1st filename : test.py
Enter 2nd filename : abc.py
File test.py does not exist
Enter 1st filename : prog9a(walk()).txt
Enter 2nd filename : sample.py
File sample.py exists



import os
f1 = input('Enter first filename : ')
f2 = input('Enter second filename : ')
try:
    os.rename(f1,f2)
    print('File',f1,'is renamed to',f2)
except FileNotFoundError:
    print('File',f1,'does not exist')
except FileExistsError:
    print('File',f2,'exists')


# Write  a  program  to  rename  a  directory
Enter 1st directory name : a
Enter 2nd directory name : b
Directory a is renamed to b
Enter 1st directory name : a
Enter 2nd directory name : c
Directory a does not exist
Enter 1st directory name : b
Enter 2nd directory name : x
Directory x exists

import os
d1 = input('Enter first directory name : ')
d2 = input('Enter second directory name : ')
try:
    os.rename(d1,d2)
    print('Directory',d1,'is renamed to',d2)
except FileNotFoundError:
    print('Directory',d1,'does not exist')
except FileExistsError:
    print('Directory',d2,'exists')


Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
Enter directory name (or) path : c:\sairam
Files of directory c:\sairam : ['file1.txt', 'file2.txt', 'file3.txt']
Directories of directory c:\sairam : ['Hyd', 'Sec']
Enter directory name (or) path : c:\pak
Directory c:\pak does not exist


import os
dirname = input('Enter directory name (or) path : ')
try:
    lst = os.listdir(dirname)
    files = []
    dirs = []
    for x in lst:
        if '.' in x:
            files.append(x)
        else:
            dirs.append(x)
    print('Files of directory',dirname,':',files)
    print('Directories of directory',dirname,':',dirs)
except FileNotFoundError:
    print('Directory',dirname,'does not exist')


# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
Directory Path : sairam
Sub Directories : ['Karnataka', 'Telangana']
Files : ['File1.txt', 'File2.txt', 'File3.txt']
Directory Path : sairam\Karnataka
Sub Directories : ['Banglore']
Files : ['File1.txt']
Directory Path : sairam\Karnataka\Banglore
Sub Directories : []
Files : []
Directory Path : sairam\Telangana
Sub Directories : ['Hyd', 'Warangal']
Files : ['File1.txt', 'File2.txt']
Directory Path : sairam\Telangana\Hyd
Sub Directories : ['Banajara-Hills']
Files : ['File1.txt']
Directory Path : sairam\Telangana\Hyd\Banajara-Hills
Sub Directories : []
Files : []
Directory Path : sairam\Telangana\Warangal
Sub Directories : []
Files : []


import os

for path,dirs,files in os.walk('sairam'):
    print('Directory Path :',path)
    print('Sub Directories :',dirs)
    print('Files :',files)
    print()