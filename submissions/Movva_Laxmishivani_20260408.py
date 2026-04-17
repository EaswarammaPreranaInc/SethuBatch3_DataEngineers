'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way
1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)
2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

5a
import math
class triangle:
    def get(self):
        self.a = float(input('Enter first side : '))
        self.b = float(input('Enter second side : '))
        self.c = float(input('Enter third side : '))
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print('Not a triangle')
            return False
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
t = triangle()
t.get()
if t.test():
    print('Area :', t.area())
    print('Perimeter :', t.peri())
'''
from prog5a import triangle
t = triangle()
triangle.get(t)
if triangle.test(t):
    print('Area :', triangle.area(t))
    print('Perimeter :', triangle.peri(t))
'''
# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
class Student:
    def get(self):
        self.roll = int(input('Enter roll number : '))
        self.name = input('Enter student name : ')
        self.gender = input('Enter gender (m/f) : ')
        self.m1 = float(input('Enter marks of subject 1 : '))
        self.m2 = float(input('Enter marks of subject 2 : '))
        self.m3 = float(input('Enter marks of subject 3 : '))
    def compute(self):
        self.total = self.m1 + self.m2 + self.m3
        self.avg = self.total / 3
        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
            self.grade = 'Fail'
        elif self.avg >= 70:
            self.grade = 'Distinction'
        elif self.avg >= 60:
            self.grade = 'First class'
        elif self.avg >= 50:
            self.grade = 'Second class'
        else:
            self.grade = 'Third class'
    def disp(self):
        print('Roll Number  : ', self.roll)
        print('Student Name : ', self.name)
        print('Gender       : ', self.gender)
        print('Total Marks  : ', self.total)
        print('Average      : ', round(self.avg, 2))
        print('Grade        : ', self.grade)
    def __str__(self):
        return f'{self.roll}   {self.name}   {self.gender}   {self.total}   {round(self.avg,2)}   {self.grade}'
s = Student()
s.get()
s.compute()
s.disp()
print(s)
---------------------------------------------------------
from  prog9a  import  student
s = student()
print(s . __dict__) # {}
s . get()
'''
{
 'roll': 1,
 'name': 'Rama rao',
 'gender': 'm',
 'm1': 80.0,
 'm2': 70.0,
 'm3': 60.0
}
'''
print(s . __dict__)
s . compute()
print(s . __dict__)
'''
{
 'roll': 1,
 'name': 'Rama Rao',
 'gender': 'm',
 'm1': 80.0,
 'm2': 70.0,
 'm3': 60.0,
 'total': 210.0,
 'avg': 70.0,
 'grade': 'Distinction'
}
'''
'''

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite
2) Use  list  of  objects
from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list

Sample output:
How many students ? : 4

Student 1
Enter roll number : 111
Enter student name : AAA
Enter gender (m/f) : m
Enter marks of subject 1 : 52
Enter marks of subject 2 : 48
Enter marks of subject 3 : 55

Student 2
Enter roll number : 222
Enter student name : BBB
Enter gender (m/f) : f
Enter marks of subject 1 : 100
Enter marks of subject 2 : 100
Enter marks of subject 3 : 0

Student 3
Enter roll number : 333
Enter student name : CCC
Enter gender (m/f) : m
Enter marks of subject 1 : 67
Enter marks of subject 2 : 78
Enter marks of subject 3 : 89

Student 4
Enter roll number : 444
Enter student name : DDD
Enter gender (m/f) : f
Enter marks of subject 1 : 78
Enter marks of subject 2 : 89
Enter marks of subject 3 : 45

111   AAA   m   155   51.67   Second class
222   BBB   f   200   66.67   Fail
333   CCC   m   234   78.00   Distinction
444   DDD   f   212   70.67   Distinction
'''
from prog9a import student
n = int(input('How many students ? : '))
a = []
for i in range(n):
    print('Student', i + 1)    
    s = student()      
    s.get()            
    s.compute()            
    a.append(s)        
print()
for s in a:
    print(s)        

'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero

import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  
		How  to  read  denominator 
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    _str_(self):
			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object  
	
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	
	def   sub(self , a , b):
		How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		How  to  simplify  object  
	
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	
	def   mul(self , a , b):
		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	
	def    div(self , a , b):
		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	
	def   simplify(self):
			How  to  find  gcd  of  numerator  and   denominator
			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
# End  of the class
How  to  create  6  objects  a , b , c , d , e , f
How  to  read  rational  number  into  object  'a'
How to  read  rational  number  into  object  'b'
How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')
  
Sample output:
Enter numerator : 2
Enter denominator : 3
Enter numerator : 5
Enter denominator : 9

Sum : 11 / 9
Difference : 1 / 9
Product : 10 / 27
Division : 6 / 5

Enter numerator : 2
Enter denominator : 3
Enter numerator : 0
Enter denominator : 9

Sum : 2 / 3
Difference : 2 / 3
Product : 0 / 27
Division is not permitted
'''
import math
class Rat:
    def get(self):
        self.num = int(input('Enter numerator : '))
        self.den = int(input('Enter denominator : '))
        self.test()
    def test(self):
        while self.den == 0:
            print('Denominator cannot be zero, re-enter')
            self.den = int(input('Enter denominator : '))
    def __str__(self):
        return f'{self.num} / {self.den}'
    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g
    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()
    def div(self, a, b):
        if b.num == 0:
            self.num = 0
            self.den = 1
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a.get()
b.get()
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
if b.num != 0:
    f.div(a, b)
print('Sum :', c)
print('Difference :', d)
print('Product :', e)

if b.num != 0:
    print('Division :', f)
else:
    print('Division is not permitted')

#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test', '__str__']
print()
print()
print(dir(a)) # ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test', '__str__', 'nr', 'dr']

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False

# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()
'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''	
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''
{'x': 10, 'y': 20}
10
10
20
Invalid  variable   name   :  z
'''

'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop
'''
class Emp:
    pass

d = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()

for key in d:
    setattr(e, key, d[key])

for key in d:
    print(key, "=", getattr(e, key))

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# mod1 . py
print('Hyd')
print('Sec')
print('Cyb')
x = 25
def  f1():
	print('Function')
class   c1:
	def   m1(self):
			print('Method')

#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
How  to  import  mod1
print(mod1.x) #How  to  print   variable  'x'   of  mod1)
mod1.f1() #How  to  call  function  f1()  of  mod1
obj = mod1.c1() # How  to  call  method  m1()  of  class  c1  in  mod1
obj.m1()
print('Bye')
import  mod4
print(x)
f1()

#  Find  outputs  (Home  work)
print('Before')
import mod1
import runpy # How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy.run_module('mod1')
runpy . run_module(mod1) #Error

# cal . py
x = 100
y = 200
def  add(a , b):
	return  a + b
def	 sub(a , b):
	return  a - b
def	 mul(a , b):
	return  a * b
def	 div(a , b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * # How  to  import  all  the  members  of  cal  module
print(x) # How  to  print  variable  'x'  of  cal   module)
print(y) # How  to  print  variable  'y'  of  cal   module)
print(cal . x) # Error because cal is not imported
print(add(10, 7))#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10, 7))#How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(mul(10, 7)) #How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10, 7)) #How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y)) # Error because cal is not imported
b = c1()
b.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1() # Error because cal is not imported

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x, add, mul, c1  #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #How  to  print  variable  'x'  of  cal   module)
print(y) # Error y is not imported
print(cal . x) # Error because cal is not imported
print(add(10, 7)) # How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10 , 7)) # Error sub not imported
print(mul(10, 7)) # How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7)) # Error div not imported
b = c1()
b.m1() # How  to  call  m1()  method  of  class  c1  in  cal  module


# Module  alias
print('Begin')
import cal as c # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) # How  to  print  variable  'x'  of  cal   module)
print(c.y) # How  to  print  variable  'y'  of  cal   module)
print(c.add(10, 7)) # How  to  call  add()  function  of  cal  module  with  10  and  7)
print(c.sub(10, 7)) # How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(c.mul(10, 7)) # How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(c.div(10, 7)) # How  to  call  div()  function  of  cal  module  with  10  and  7)
b = c.c1()
b.m1() # How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x) # Error because module imported with alias 'c'
from  math  as   m  import  * # Error first import then execute

# Member  alias
from cal import x as a, add as ad, mul as mu, c1 as C # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a) # How  to  print  variable  'x'  of  cal   module
print(x) # Error x is imported as a so x is not valid to use
print(ad(10, 7)) # How  to  call  add()  function  of  cal  module  with  10  and  7)
print(mu(10, 7)) # How  to  call  mul()  function  of  cal  module  with  10  and  7)
b = C()
b.m1() # How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7)) # Error add is imported as ad so add is not valid to use
b = c1() # Error c1 is renamed to 'C'

# mod1.py
x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')

# mod2.py
x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')

# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) # 10 
disp() # disp  function  of  mod1
a = c1()
a . m1() # m1  method  of  class  c1  in  mod1

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # 30
disp() # disp  function  of  same  module
a = c1()
a . m1() # m1  method of  class  c1  in  same  module

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1, mod2 # How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) # How  to  print  variable  'x'  of  mod1
mod1.disp() # How  to  call  disp()  function  of  mod1
a = mod1.c1()
a.m1() 3 How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) # How  to  print  variable  'x'  of  mod2
mod2.disp() # How  to  call  disp()  function  of  mod2
b = mod2.c1()
b.m1() # How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
c = c1()
c.m1() # How  to  call  method  m1()  of  class   c1  in  current  module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as d1, c1 as C1 # How  to  import  members  of  mod1
from mod2 import x as x2, disp as d2, c1 as C2 #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1) # How  to  print  variable  'x'  of  mod1)
d1() # How  to  call  disp()  function  of  mod1
a = C1()
a.m1() # How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x2) # How  to  print  variable  'x'  of  mod2)
d2() # How  to  call  disp()  function  of  mod2
b = C2()
b.m1() # How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
c = c1()
c.m1() # How  to  call  method  m1()  of  class   c1  in  current  module

# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__ == "__main__":
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')

# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')
'''
Begining  of  mod2
One
Two
Three
Seven
Eight
Nine
End  of  mod2
'''

#  Find  outputs
import  cal
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7))  # 70
print(cal . div(10 , 7)) # 1.42
a = cal . c1()
a . m1() # m1 method

#  Find  outputs
from  cal  import   y , sub , mul
print(x) # Error because x is not imported
print(y) # 200
print(add(10 , 7)) # Error because add is not imported
print(sub(10 , 7)) # 3
print(mul(10 , 7)) # 70
print(div(10 , 7)) # Error because div is not imported
a = c1() # Error because c1 is not imported