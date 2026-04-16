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

'''
1) What  are  the  members  of  mod1 ?  --->  Object  'x' ,  function  f1()  and  class  c1

2) py  mod1.py
    What  are  the  outputs ?  --->  Hyd  <next line>  Sec  <next  line>  Cyb  <next  line>

3) Why  are  function  f1()  and  method  m1()  not  executed ?  --->  Since  they  are  not  called
'''



#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
How  to  import  mod1
print(How  to  print   variable  'x'   of  mod1)
How  to  call  function  f1()  of  mod1
How  to  call  method  m1()  of  class  c1  in  mod1
print('Bye')
import  mod4
print(x)
f1()


print('Hello')
import mod1 
print(mod1.x)
mod.f1()
print('Bye')
obj = mod1.c1()
obj.m1()
print('Bye')


#  Find  outputs  (Home  work)
print('Before') # Before
How  to  run  mod1 
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy . run_module(mod1)

import mod1
import runpy
print('Before')
print(mod1.x)
mod1.f1(_
a = mod1.c1()
print('After')
runpy . run_module(mod1) 



# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') # Begin
How  to  import  all  the  members  of  cal  module 
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y))
How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()

print('Begin')
from cal import *
print(x)
print(y)
print(add(10,7))
print(sub(10,7))
print(mul(10,7))
print(div(10,7))
print(add(x,y))
b = c1()
b.m1()
print('end')



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7))
How  to  call  m1()  method  of  class  c1  in  cal  module

print('Begin')
from import x,add,mul,c1 *
print(x)
print(add(10,7))
print(mul(10,7))
b.m1()
b=c1()
print('end')


# Module  alias
print('Begin')
How  to  import  cal  module  with   another  name  using  import  statement
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)

print('Begin')
import cal as c
print(c.x)
print(c.y)
print(c.add(10,7))
print(c.sub(10,7))
print(c.mul(10,7))
print(c.div(10,7))
a=c.c1()
a.m1()
print(c.x)


# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(How  to  print  variable  'x'  of  cal   module)
print(x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()

from cal import x, add, mul, c1

Print module variable x
print(x)

Call module functions
print(add(10, 7))
print(mul(10, 7))

Create instance of class c1 and call method m1
a = c1()
a.m1()

Another instance example (optional)
b = c1()



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



'''
1) What  is  the  module  name ?  --->  cal

2) What  are  the  members  of  cal  module ?  --->  Two  objects  x  and  y ,
																			      Four  functions  add() , sub() , mul()  and  div()  and
																				  class  c1

3) Is  m1()  a  member  of  cal  module ?  --->  No  becoz  it  is  a  method  of  class

4) How  many  statements  are  in  cal  module ?  --->  Two
																				     i.e.  x =  100   and  y = 200

5) py  cal . py
    What  are  the  outputs ?  --->  Nothing  becoz  there  are  no  print  statements  in  cal  module
'''


# Module  alias
print('Begin')
How  to  import  cal  module  with   another  name  using  import  statement
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)
from  math  as   m  import  *

print("Begin")

 Import cal module as 'c'
import cal as c

# Print variables
print(c.x)
print(c.y)

# Call functions
print(c.add(10, 7))
print(c.sub(10, 7))
print(c.mul(10, 7))
print(c.div(10, 7))

# Call class method
obj = c.c1()
obj.m1()   # prints "m1 method"





# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(How  to  print  variable  'x'  of  cal   module)
print(x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()


# Member alias example
print("Begin")

# Import specific members with aliases
from cal import x as var_x, add as addition, mul as multiplication, c1 as MyClass

# Print variable x
print("How to print variable 'x' of cal module:")
print(var_x)

# Call add() and mul() functions
print("How to call add() function of cal module with 10 and 7:")
print(addition(10, 7))

print("How to call mul() function of cal module with 10 and 7:")
print(multiplication(10, 7))

# Call m1() method of class c1
print("How to call m1() method of class c1 in cal module:")
b = MyClass()
b.m1()




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



'''
1) What  is  the  module  name ?  --->  cal

2) What  are  the  members  of  cal  module ?  --->  Two  objects  x  and  y ,
																			      Four  functions  add() , sub() , mul()  and  div()  and
																				  class  c1

3) Is  m1()  a  member  of  cal  module ?  --->  No  becoz  it  is  a  method  of  class

4) How  many  statements  are  in  cal  module ?  --->  Two
																				     i.e.  x =  100   and  y = 200

5) py  cal . py
    What  are  the  outputs ?  --->  Nothing  becoz  there  are  no  print  statements  in  cal  module
'''



# mod1.py
x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')


'''
What  are  the  members  of  mod1 ?   ---> Object  'x' , function  disp()  and  class  c1
'''

# main.py
import mod1

# Access variable
print(mod1.x)  

# Call function
mod1.disp()  

# Create instance of class and call method
obj = mod1.c1()
obj.m1()





# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One') # one
print('Two') # two
print('Three') # three
print('Four') # Four
print('Five') # five
print('Six') # six
print('Seven')# seven
print('Eight')# eight
print('Nine') # nine


# Find  outputs (Home  work)
print('Begining  of  mod2') # beginning of mod2
import   mod1
print('End  of  mod2') # error


#  Find  outputs
import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.42
a = cal . c1() 
a . m1()



#  Find  outputs
from  cal  import   y , sub , mul
print(x)
print(y)
print(add(10 , 7)) # 17
print(sub(10 , 7)) # 3
print(mul(10 , 7)) #70
print(div(10 , 7)) 
a = c1()
