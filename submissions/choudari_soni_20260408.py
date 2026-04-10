# mod1 . py
print('Hyd')#Hyd
print('Sec')#Sec
print('Cyb')#Cyb
x = 25
def  f1():
	print('Function')#Function
class   c1:
	def   m1(self):
			print('Method')#Method

'''
1) What  are  the  members  of  mod1 ?  --->  Object  'x' ,  function  f1()  and  class  c1
2) py  mod1.py
    What  are  the  outputs ?  --->  Hyd  <next line>  Sec  <next  line>  Cyb  <next  line>

3) Why  are  function  f1()  and  method  m1()  not  executed ?  --->  Since  they  are  not  called
'''

#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import  mod1
print(mod1.x)
mod1.f1()
obj=mod1.c1()
obj.m1()
print('Bye')


import  mod4
print(x)
f1()

#Find  outputs  (Home  work)
import runpy
print('Before')#Before
import mod1
print(mod1 . x)#error
mod1 . f1()
a = mod1 . c1()
print('After')#After
runpy . run_module(mod1)

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
import cal
print(cal.x)
print(cal.y)
print(cal.add(10, 7))
print(cal.sub(10, 7))
print(cal.mul(10, 7))
print(cal.div(10, 7))

print(cal.add(cal.x, cal.y))

# Correct way to call m1
obj = cal.c1()
obj.m1()
print('End')

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
from cal import x,add,mul,c1
print(x)
print(add(10,7))
print(mul(10,7))
obj=c1()
obj.m1()

# Module  alias
print('Begin')
import cal as c
print(c.x)
print(c.y)
print(c.add(10,7))
print(c.sub(10,7))
print(c.mul(10,7))
print(c.div(10,7))
obj=c.c1
print(c . x)

from  math  as   m  import  *#error

# Member  alias
from cal import x as a, add,mul,c1
print(a)
print(add(10,7))
print(mul(10,7))
obj=c1
print(add(10 , 7))
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

# mod2.py
x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')


'''
What  are  the  members  of  mod2 ? --->  Object  'x' ,  function  disp()  and  class  c1
'''

# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')#disp function of same module
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')#m1 method of class c1 in same module
from  mod2  import   *
from  mod1  import   *
print(x)#30
disp()
a = c1()
a . m1()

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')#disp function of same module
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')#m1 method of class c1 in same module
print(x)#30
disp()
a = c1()
a . m1()

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
mod1.m1()
print()
print(mod2.x)
mod2.disp()
mod2.m1()
print()
print(mod2.x)
disp()  
disp.m1()

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
import mod1
import mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1.x)
mod1.disp()
mod1.m1()
print()
print()
print(mod2.x)
mod2.x
mod2.m1()
print()
print()
print(x)
disp()
disp.m1()

# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if	__name__=='__main__':
	print('Four')
	print('Five')
	print('Six')
print('Seven')
print('Eight')
print('Nine')

# Find  outputs (Home  work)
print('Begining  of  mod2')#Begining of mod2
import   mod1
print('End  of  mod2')#End of mod2

#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.285
a = cal . c1()
a . m1()

#  Find  outputs
from  cal  import   y , sub , mul
print(x)#100
print(y)#200
print(add(10 , 7))#17
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#1.285
a = c1()