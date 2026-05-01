#1
'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con . cursor()
    cur . execute('select * from employees')

    n = int(input('How many rows to be fetched?:'))

    if n == 0:
        rows = cur . fetchmany(-1)
    else:
        rows = cur . fetchmany(n)

    for x in cur . description:
        print(f'{x[0]: ^10}' , end = '\t')

    for row in rows:
        for col in row:
            print(f'{str(col): ^10}' , end = '\t')

    print('\nNumber of tuples fetched:', cur . rowcount)

    cur.close()
    con.close()

except msc . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except msc . errors . InternalError:
    print('Cursor cannot be closed')


#2
'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  ---> cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  inputs  empno , ename  and  sal

4) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table

5) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError

6) Can  a  tuple  be  inserted  into  MySqlCursor  object ?  --->  No  becoz  it  is  immutable
'''
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con . cursor()

    while True:

        emp_id = int(input('Enter the Employee ID:'))
        name = input('Enter the Employee Name:')
        position = input('Enter the Employee Designation:')
        salary = float(input('Enter the Salary of the Employee:'))
        hire_date = input('Enter the date the Employee was hired on (YYYY-MM-DD):')

        cur . execute(f'insert into employees values ({emp_id} , "{name}" , "{position}" , {salary} , "{hire_date}")')
        con . commit()
        print(f'{cur . rowcount} row(s) inserted')

        c = input('Do you want to add another row? (Y/N):')

        if c . upper() == 'N':
            break

    cur.close()
    con.close()

except msc . errors . IntegrityError:
    print('Duplicate Employee ID cannot be inserted')
except msc . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except msc . errors . InternalError:
    print('Cursor cannot be closed')



#3
'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con . cursor()

    cond = input('Enter the condition (Press Enter Key without any condition if you want to delete all rows):')

    if cond:
        cur . execute(f'delete from employees where {cond}')
        con . commit()
        print(f'{cur . rowcount} row(s) deleted')
    else:
        cur . execute(f'delete from employees')
        con . commit()
        print('All rows deleted')
    

    cur.close()
    con.close()

except msc . errors . IntegrityError:
    print('Duplicate Employee ID cannot be inserted')
except msc . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except msc . errors . InternalError:
    print('Cursor cannot be closed')


#4
'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
'''
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con . cursor()

    cond = input('Enter the condition (Press Enter Key without any condition if you want to modify all rows):')

    exp = input('Enter the modification you want to perform:')

    if cond:
        cur . execute(f'update employees set {exp} where {cond}')
        con . commit()
        print(f'{cur . rowcount} row(s) modified / updated')
    else:
        cur . execute(f'update employees set {exp}')
        con . commit()
        print('All rows modified / updated')
    

    cur.close()
    con.close()

except msc . errors . IntegrityError:
    print('Duplicate Employee ID cannot be inserted')
except msc . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except msc . errors . InternalError:
    print('Cursor cannot be closed')


#5
'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  ---> cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  ---> Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con . cursor()

    tablename = input('Enter the name of the table you want to create:')


    cur . execute(f'create table {tablename}(sno int primary key , sname varchar(20) , marks float)')
    con . commit()
    print(f'{tablename} is created')
    
    cur.close()
    con.close()
    
except msc . errors . ProgrammingError:

    cur . execute(f'drop table {tablename}')
    print(f'Existing {tablename} is dropped')
    con . commit()
    cur . execute(f'create table {tablename} (sno int primary key , sname varchar(20) , marks float)')
    con . commit()
    print(f'New {tablename} is created')

except msc . errors . IntegrityError:
    print('Duplicate Employee ID cannot be inserted')
except msc . errors . InternalError:
    print('Cursor cannot be closed')


# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super() . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent . m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		c . m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		cls . m1() # How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1() # error , self is not an argument of classmethod
		m1() # error , m1() function is not defined
		print('child  Method')
# End  of  the  class
p = parent()
p . m1() # How  to  call  m1()  method  of  parent  class
c = child()
c . m2() # How  to  call  m2()  method  of  child  class
child . m1() # parent method
super() . m1() # error , super() cannot be used outside child class
self . m1() # error , self cannot be used outside method



# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super() . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent . m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1() # child class m1() method is excecuted (possible recursion?) 
		self . m1() # error , self is not an argument of classmethod
		m1() # error , m1() function is not defined
		print('child  Method')
# End  of  the  class
p = parent()
p . m1() # How  to  call  m1()  method  of  parent  class
c = child()
c . m1() # How  to  call  m1()  method  of  child  class



# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super(parent , child) . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent . m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		c . m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() # error , staticmethod cannot be called with super(no-args) function
		super(child) . m1() # error , super(1-arg) is invalid
		self . m1() # error , staticmethod has no argument self
		cls . m1() # error , staticmethod has no argument cls
		print('child  method')
#end of the class
p = parent()
p . m1() # How  to  call  m1()  method  of  parent  class
c = child()
c . m2() # How  to  call  m2()  method  of  child  class
child . m1() # parent method



# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		super(parent , child) . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent . m1() # How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1() # error , staticmethod cannot be called with super(no-args) function  
		self . m1() # error , staticmethod has no argument self
		cls . m1() # error , staticmethod has no argument cls
		print('child  method')
# End  of  the  class
p = parent()
p . m1() # How  to  call  m1()  method  of  parent  class
c = child()
c . m1() # How  to  call  m1()  method  of  child  class



# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self . x) # How  to  print  variable  'x'
		print(parent . x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)  
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self . x) # How  to  print  variable  'x'
		print(super() . x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(parent . x) # How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(child . x) # How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self . y) # How  to  print  variable  'y'
		print(child .y) # How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) # error , parent class does not have object y
		print(y)  
# End  of child  class
p = parent()
p . m1() # How  to  call  m1()  method  of  parent  class
c = child()
c . m2() # How  to  call  m2()  method  of  child  class



# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self . x) # How  to  print  variable  'x'  of  parent  class
		print(parent . x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent . x) # How  to  print  variable  'x'  of  parent  class
		print(super() . x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self . x) # How  to  print  variable  'x'  of  child  class
		print(child . x) # How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent()
p . m1() # How  to  call  m1()  method  of  parent  class
c = child()
c . m1() # How  to  call  m1()  method  of  child  class



#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self . a = 10
		self . b = 20 # How  to   read  inputs  into   variables  a  and  b  of  object		
	def    disp(self):
		print(self . a , self . b , sep = '\t') # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self . a = 30
		self . b = 40 # How  to   read  inputs  into   variables  a  and  b  of  object
		self . c = 50
		self . d = 60 # How  to   read  inputs  into   variables  c  and  d  of  object		
	def   disp(self):
		print(self . a , self . b , sep = '\t') # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self . c , self . d , sep = '\t') # How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self . a + self . b + self . c + self . d # sum  of  values  in  object  
# End of child class
print('parent  object')
p = parent()
p . get() # How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c = child()
c . get() # How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p . disp() # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c . disp() # How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c . total())


#6
'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  ---> 3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import math

class circle:
    def get(self):
        self . r = float(input(f'Enter the radius of the Circle:')) # How  to  read  radius  into  object

    def area(self):
        return math . pi * self . r * self . r # area  of  circle

    def cir(self):
        return 2 * math . pi * self . r # circumference  of  circle
# End  of  circle  class


class cylinder(circle):
    def get(self):
        self . r = float(input(f'Enter the radius of the Cylinder:')) # How  to  read  radius  into  the  object  
        self . h = float(input(f'Enter the height of the Cylinder:')) # How  to  read  height  into  the  object 

    def area(self):
        return (2 * math . pi * self . r * self . r) + (2 * math . pi * self . r * self . h) # area  of  cylinder

    def volume(self):
        return math . pi * self . r * self . r * self . h # volume  of  cylinder
# End of cylinder class


def menu():
    print('1 . Circle')
    print('2 . Cylinder')
    print('3 . Exit')
#end of menu function


while True:
    menu()
    ch = eval(input('Enter choice : ')) 

    match ch:
        case 1:
            c = circle()
            c . get() # How  to  read  raidus  into  circle  object
            print('Area : ', c . area())
            print('Circumference : ', c . cir())

        case 2:
            cy = cylinder()
            cy . get() # How  to  read  raidus  and  height  into  cylinder  object
            print('Area : ', cy . area())
            print('Volume : ', cy . volume())

        case 3:
            break
# End  of  match



#7
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
        self . s = float(input('Enter the side:')) # How  to  read  side  of  square

    def area(self):
        return self . s ** 2 # area  of  square

    def peri(self):
        return 4 * self . s # perimeter  of  square


class rectangle(square):
    def get(self):
        self . l = float(input('Enter the length:')) # How  to  read  length  of  rectangle
        self . b = float(input('Enter the breadth:')) # How  to  read  breadth  of  rectangle

    def area(self):
        return self . l * self . b # area  of  rectangle

    def peri(self):
        return 2 * (self . l + self . b) # perimeter  of   rectangle


class cube(square):
    def get(self):
        self . s = float(input('Enter the side:')) # How  to  read  side  of  cube

    def area(self):
        return 6 * self . s ** 2 # area  of  cube

    def volume(self):
        return self . s ** 3 # volume  of  cube


def menu():
    print('1 . Square')
    print('2 . Rectangle')
    print('3 . Cube')
    print('4 . Exit')
# End  of  the  function


while True:
    menu()
    ch = int(input('Enter  choice : ')) 

    match ch:
        case 1:
            s = square()
            s . get() # How  to  read  side  into   square  object  's'
            print('Area   :  ' , s . area())
            print('Perimeter  :  ' , s . peri())

        case 2:
            r = rectangle()
            r . get() # How  to  read  length  and  breadth  into   rectangle  object  'r'
            print('Area  :  ' , r . area())
            print('Perimeter  :  ' , r . peri())

        case 3:
            c = cube()
            c . get() # How  to  read  side  into  cube  object  'c'
            print('Area  :   ' , c . area())
            print('Volume  :  ' , c . volume())

        case 4:
            break # How  to  stop  execution




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
		c3 . m1() # How  to  call  m1()  method  of  class  c3
		c4 . m1() # How  to  call  m1()  method  of  class  c4
		a = c2()
		a . m1() # How  to  call  m1()  method  of  class  c2
		super() . m1() # How  to  call  m1()  method  of  class  c1
		self . m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c = c5()
c . m2() # How  to  call  m2()  method  of  class  c5
