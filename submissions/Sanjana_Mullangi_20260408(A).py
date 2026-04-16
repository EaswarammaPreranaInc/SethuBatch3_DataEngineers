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
'''
Hyd 
Sec
Cyb'''



'''
1) What  are  the  members  of  mod1 ?  --->  Object  'x' ,  function  f1()  and  class  c1

2) py  mod1.py
    What  are  the  outputs ?  --->  Hyd  <next line>  Sec  <next  line>  Cyb  <next  line>

3) Why  are  function  f1()  and  method  m1()  not  executed ?  --->  Since  they  are  not  called
'''


#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import mod1#How  to  import  mod1
print(mod1.x)#How  to  print   variable  'x'   of  mod1
a=mod1.c1()#How  to  call  function  f1()  of  mod1
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1
print('Bye')
import  mod4
print(x)#error
f1()#error


#  Find  outputs  (Home  work)
print('Before')
import mod1
import runpy#How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy . run_module(mod1)#error-mod1 is not in string
'''
Before
25
After
'''

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
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7))
How  to  call  m1()  method  of  class  c1  in  cal  module


# Module  alias
print('Begin')
import cal as c#How  to  import  cal  module  with   another  name  using  import  statement
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)
from  math  as   m  import  *


# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(How  to  print  variable  'x'  of  cal   module)
print(x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  class  c1  in  cal  module
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
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)
disp()
a = c1()
a . m1()
'''
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''


# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)
disp()
a = c1()
a . m1()
'''
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''


# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(How  to  print  variable  'x'  of  mod2
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module


# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module


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