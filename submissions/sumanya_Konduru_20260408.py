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