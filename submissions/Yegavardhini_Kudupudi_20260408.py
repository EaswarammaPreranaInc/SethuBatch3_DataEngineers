'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''

import prog5a
t=prog5a.triangle()   #How  to  create  triangle  object
prog5a.triangle.get(t)  #How  to  call  get()  method  in  another  way
prog5a.triangle.test(t) #How  to  call  test()  method  in  another  way
print('Area : ', prog5a.triangle.area(t))
print('Perimeter: ', prog5a.triangle.peri(t))




# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog5a  import  Student
s = Student()
print(s . __dict__) # {}
s . get() 
print(s . __dict__) # {'roll_num': 22, 'name': 'rama', 'gender': 'm', 'm1': 23, 'm2': 43, 'm3': 51}
s . compute()
print(s . __dict__)# {'roll_num': 22, 'name': 'rama', 'gender': 'm', 'm1': 23, 'm2': 43, 'm3': 51, 'total_marks': 117, 'avg_marks': 39.0, 'grade': 'Fail'}




'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects

from prog9a import Student
n=int(input('How many students? '))
l=[]
for i in range(n):
    print(F'Student {i+1}')
    s=Student()
    s.get()
    l.append(s)
for x in l:
    s.compute()
for x in l:
    s.disp()
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
'''
import  math
class  Rat:
	def  get(self):
		self.num=int(input('Enter Numrator: '))  
		self.dem=int(input('Enter Denominator: '))  
		self.test()
	def  test(self):
		if self.dem==0:
			self.dem=int(input('Enter Denominator: '))
	def __str__(self):
			 return f"{self.num} / {self.dem}"
	def add(self , a , b):
		self.num=a.num*b.dem+b.num*a.dem
		self.dem=a.dem+b.dem
		if self.num != 0:
			self.simplify()
  

	def sub(self , a , b):
		self.num=a.num*b.dem-b.num*a.dem
		self.dem=a.dem+b.dem
		if self.num != 0:
			self.simplify()  
	
	def mul(self , a , b):
		self.num=a.num*b.num
		self.dem=a.dem*b.dem
		if self.num != 0:
			self.simplify() 

	def div(self , a , b):
		self.num=a.num/b.num
		self.dem=a.dem/b.dem 
		if self.num != 0:
			self.simplify()

	def simplify(self):
		self.num = int(self.num)
		self.dem = int(self.dem)
		g = math.gcd(self.num, self.dem)
		self.num //= g
		self.dem //= g

# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
a.get()    #How  to  read  rational  number  into  object  'a'
b.get()    #How to  read  rational  number  into  object  'b'
c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b) #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b) #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b) #How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
c.simplify()
d.simplify()
e.simplify()
if  f.dem>0:
	f.simplify()
else:
	print('Division  is  not  permitted')
	



#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # ['num','dem','add','sub','mul','div']
print()
print()
print(dir(a)) 



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

Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....



#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) # a.y=20
print(a . __dict__) # {x:10,y:20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) # 10 20
	except:
		print(F'Invalid  variable   name   :  {varname}') # Invalid  variable   name   : z
		break




'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
a=Emp()
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
for x in dict:  
    setattr(a , x , dict[x])

for x in dict:
    print(x,'=',getattr(a , x))



# mod1 . py
print('Hyd') # Hyd
print('Sec') # Sec
print('Cyb') # Cyb
x = 25
def  f1():
	print('Function')
class   c1:
	def   m1(self):
			print('Method')



#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import  mod1
print(mod1.x)
mod1.f1()
mod1.c1() 
print('Bye')
import  mod4
print(x) # error
f1() # error


#  Find  outputs  (Home  work)
print('Before')
runpy.run_module('mod1')
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy . run_module(mod1)



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
from cal import *
print(x)
print(y)
print(cal . x) # error
print(add(10,7))
print(sub(10,7))
print(mul(10,7))
print(div(10,7))
print(cal . add(x , y)) # error
a=c1()
a.m1()
b = cal . c1() # error



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x , add , mul
print(x)
print(y) # error
print(cal . x) # error
print(add(10,7))
print(sub(10 , 7)) # error
print(mul(10,7))
print(div(10 , 7)) # error
a=c1()
a.m1()



# Module  alias
print('Begin')
import  cal as c
print(c.x)
print(c.y)
print(c.add(10,7))
print(c.sub(10,7))
print(c.mul(10,7))
print(c.div(10,7))
How  to  call  m1()  method  of  c1  class  in  cal  module
a=c.c1()
a.m1()
print(cal . x) # error
from  math  as   m  import  * # error



# Member  alias
from cal import x as v, add as s , mul  as m,c1 as c
print(v)
print(x) # error
print(s(10,7))
print(m.(10,7))
a=c()
a.m1()
print(add(10 , 7)) # error
b = c1() # error



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
disp() 
a = c1() # disp  function  of  same  module
a . m1() # m1  method of  class  c1  in  same  module



# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)
mod1.disp()
a=mod1.c1()
a.m1()
print()
print(mod2.x)
mod2.disp()
a=mod2.c1()
a.m1()
print()
print(x)
disp()
b=c1()
b.m1()



# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1,disp as d1,c1 as mc1
from mod2 import x as x2,disp as d2, c1 as mc2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)
d1()
a=mc1()
a.m1()
print()
print()
print(x2)
d2()
b=mc2()
b.m1()
print()
print()
print(x)
disp()
c=c1()
c.m1()



# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__=='__main__':
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')



# Find  outputs (Home  work)
print('Begining  of  mod2') # Begining  of  mod2
import   mod1 # One <nextLine> Two <nextLine> Three <nextLine> Seven <nextLine> Eight <nextLine> Nine
print('End  of  mod2') # End  of  mod2



#  Find  outputs
import  cal
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.42
a = cal . c1()
a . m1() # m1  method



#  Find  outputs
from  cal  import   y , sub , mul
print(x) # error
print(y) # 200
print(add(10 , 7)) # error
print(sub(10 , 7)) # 3
print(mul(10 , 7)) # 70
print(div(10 , 7)) # error
a = c1() # error

