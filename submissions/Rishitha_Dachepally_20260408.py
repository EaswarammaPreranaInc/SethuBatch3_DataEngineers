'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from prog5a import triangle
t = triangle() # How  to  create  triangle  object
triangle.get(t) # How  to  call  get()  method  in  another  way
triangle.test(t) # How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(t)) # Area : 6.0
print('Perimeter: ', triangle.peri(t)) # Perimeter: 12.0

# -----------------------------------------------------------------------------------------------------

 # What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__) # {}
s . get() # Input: 25, Rama Rao, male, 52, 48, 55
print(s . __dict__) # {'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
s . compute()
print(s . __dict__) # {'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'tot': 155.0, 'avg': 51.67, 'grade': 'Second class'}

# -----------------------------------------------------------------------------------------------------

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
n = int(input('Enter number of students: ')) # How  to  read  number  of  students  into   variable  'n'
a = []
for i in range(n):
    a.append(student()) # How  to  store  'n'  student  class  objects   in  list  'a'

for x in a:
    x.get() # How  to   read  each  student  data  into   the  object  held  by  the  list
    x.compute() # How  to   store  results  in   each  object  held  by  the  list
    print(x) # How  to   print  each  object  held  by  the  list

# -----------------------------------------------------------------------------------------------------

 '''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers
'''
import  math
class  Rat:
	def  get(self):
		self.nr = int(input('Enter numerator: ')) # How  to  read  numerator  
		self.dr = int(input('Enter denominator: ')) # How  to  read  denominator 
		self.test() # How  to  call  test()  method
	def  test(self):
		while self.dr == 0:
			self.dr = int(input('Denominator is zero. Re-enter: ')) # Ask  user  to  reenter
	def    __str__(self):
			 return  F'{self.nr} / {self.dr}' # return values in '2 / 3' form
	def   add(self , a , b):
		self.nr = a.nr * b.dr + b.nr * a.dr # How  to  add  objects
		self.dr = a.dr * b.dr
		self.simplify() # How  to  simplify  object  
	def   sub(self , a , b):
		self.nr = a.nr * b.dr - b.nr * a.dr # How  to  subtract  objects
		self.dr = a.dr * b.dr
		self.simplify() # How  to  simplify  object  
	def   mul(self , a , b):
		self.nr = a.nr * b.nr # How  to  multiply  objects
		self.dr = a.dr * b.dr
		self.simplify() # How  to  simplify  object 
	def    div(self , a , b):
		self.nr = a.nr * b.dr # How  to  divide  objects
		self.dr = a.dr * b.nr
		self.simplify() # How  to  simplify  object 
	def   simplify(self):
		if self.nr != 0:
			common = math.gcd(self.nr, self.dr) # How  to  find  gcd
			self.nr //= common # How  to  simplify  rational  number
			self.dr //= common
# End  of the class

a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat() # How  to  create  6  objects
a.get(); b.get() # How  to  read  rational  numbers
c.add(a, b); d.sub(a, b); e.mul(a, b) # Perform operations
print('Sum: ', c) # How  to  print  object   'c'
print('Difference: ', d) # How  to  print  object   'd'
print('Product: ', e) # How  to  print  object   'e'
if b.nr != 0:
	f.div(a, b)
	print('Division: ', f) # How  to  print  object  'f
else:
	print('Division  is  not  permitted')

# -----------------------------------------------------------------------------------------------------

 #  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # List of attributes in Rat class
print(dir(a)) # List of attributes in object 'a' including nr, dr

# -----------------------------------------------------------------------------------------------------

 #  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # False
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False

# -----------------------------------------------------------------------------------------------------

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
		x . talk() # Meow Meow Meow .... / Mehar Mehar Mehar ....
	else:
		x . bark() # Bhow Bhow Bhow ....

# -----------------------------------------------------------------------------------------------------

 #  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume 'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume 20
setattr(a , varname , value)
print(a . __dict__) # {'x': 10, 'y': 20}
print(a . x) # 10
# Iteration 1: x -> 10, Iteration 2: y -> 20, Iteration 3: z -> Error
# print(getattr(a, 'z')) # Error because 'z' is not defined in object

# -----------------------------------------------------------------------------------------------------

# (Home  work)
# Write  a  program  to  convert  a  dictionary  to  Emp  class  object
class  Emp:
        pass
#End  of  the  class
dict_emp = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
for k, v in dict_emp.items(): setattr(e, k, v) # How  to  convert  dictionary  to  object  'e'
for k in dict_emp.keys(): print(getattr(e, k)) # How  to  print  object  'e' (25, Rama Rao, 10000.0)

# -----------------------------------------------------------------------------------------------------

 #  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import mod1 # How  to  import  mod1
print(mod1 . x) # How  to  print   variable  'x' (25)
mod1 . f1() # How  to  call  function  f1()
obj = mod1 . c1(); obj . m1() # How  to  call  method  m1()
print('Bye')

# -----------------------------------------------------------------------------------------------------

 # Find  outputs  (Home  work)
print('Before')
import mod1 # How  to  run  mod1 (Hyd, Sec, Cyb)
print(mod1 . x) # 25
mod1 . f1() # Function
a = mod1 . c1(); a . m1() # Method
print('After')

# -----------------------------------------------------------------------------------------------------

 # How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * # How  to  import  all  the  members
print(x) # How  to  print  variable  'x' (100)
print(y) # How  to  print  variable  'y' (200)
print(add(10, 7)) # 17
print(sub(10, 7)) # 3
print(mul(10, 7)) # 70
print(div(10, 7)) # 1.428...
b = c1(); b.m1() # How  to  call  m1()

# -----------------------------------------------------------------------------------------------------

 # How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?
print('Begin')
from cal import x, add, mul, c1 # How  to  import  specific members
print(x) # 100
# print(y) # Error because name 'y' is not defined
print(add(10, 7)) # 17
# print(sub(10, 7)) # Error because name 'sub' is not defined
print(mul(10, 7)) # 70
# print(div(10, 7)) # Error because name 'div' is not defined
b = c1(); b.m1() # How  to  call  m1()

# -----------------------------------------------------------------------------------------------------

 # Module  alias
print('Begin')
import cal as cl # How  to  import  cal  module  with   another  name
print(cl.x) # 100
print(cl.y) # 200
print(cl.add(10, 7)) # 17
print(cl.sub(10, 7)) # 3
b = cl.c1(); b.m1() # How  to  call  m1()

# -----------------------------------------------------------------------------------------------------

 # Member  alias
from cal import x as val, add as plus, mul as product, c1 as classA # How  to  import  with  alias
print(val) # 100
# print(x) # Error because name 'x' is not defined
print(plus(10, 7)) # 17
print(product(10, 7)) # 70
b = classA(); b.m1() # How  to  call  m1()

# -----------------------------------------------------------------------------------------------------

 # Find  outputs  (Home  work) - Conflicting module names
from  mod2  import   *
from  mod1  import   *
print(x) # 10
disp() # disp  function  of  mod1
a = c1(); a . m1() # m1  method  of  class  c1  in  mod1

from  mod1  import  *
from  mod2  import  *
x = 30
print(x) # 30
disp() # disp  function  of  same  module (defined in script)
a = c1(); a . m1() # m1  method  of  class  c1  in  same  module

# -----------------------------------------------------------------------------------------------------

 # How  to  use  members  of  all  the  3  modules  with  import  statement ?
import mod1, mod2 # How  to  import  mod1  and  mod2
x = 30
def   disp(): print('disp  function  of  same  module')
class   c1:
	def   m1(self): print('m1  method of  same  module')
print(mod1.x) # 10
mod1.disp() # disp  function  of  mod1
obj1 = mod1.c1(); obj1.m1() # m1 method of mod1
print(mod2.x) # 20
mod2.disp() # disp  function  of  mod2
obj2 = mod2.c1(); obj2.m1() # m1 method of mod2
print(x) # 30
disp() # disp  function  of  same  module

# -----------------------------------------------------------------------------------------------------

 # mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported
if __name__ == "__main__":
    print('Four')
    print('Five')
    print('Six')

# -----------------------------------------------------------------------------------------------------

#  Find  outputs
from  cal  import   y , sub , mul
# print(x) # Error because name 'x' is not defined
print(y) # 200
# print(add(10, 7)) # Error because name 'add' is not defined
print(sub(10, 7)) # 3
print(mul(10, 7)) # 70
# print(div(10, 7)) # Error because name 'div' is not defined
# a = c1() # Error because name 'c1' is not defined

```