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
1) What  are  the  members  of  mod1 ?  --->  Object  'x' ,  function  f1()  and  class  c1
2) py  mod1.py
What  are  the  outputs ?  --->  Hyd  <next line>  Sec  <next  line>  Cyb  <next  line>
3) Why  are  function  f1()  and  method  m1()  not  executed ?  --->  Since  they  are  not  called
'''
#  How  to  reuse  mod1  ?:-by importing the module mod1 to this module  (Home  work)
print('Hello')
import mod1#How  to  import  mod1
print(mod1.x)#How  to  print   variable  'x'   of  mod1)
mod1.f1()#How  to  call  function  f1()  of  mod1
mod1.c1.m1()#error we not created the obj for the class in mod1 and not created in this  current module so error if obj=c1()so error ###How  to  call  method  m1()  of  class  c1  in  mod1
print('Bye')
#import  mod4#error module not found error 
print(x)#error x is  not defined in current module and it not imported from mod1 also so error 
f1()#error f1 functions is not defined in current module and it not imported from mod1 also so error 

 #Find  outputs  (Home  work)
import mod1
#import runpy ###here this is  missimg so we cannot use without import runpy module the run_module() function 
print('Before')#Before
runpy.run_module("mod1")#How  to  run  mod1###here error without importing runpy module how can i use the runpy module function 
print(mod1 . x)#25
mod1 . f1()#function
a = mod1 . c1()#c1 class obj is created with class name a 
print('After')#After
runpy.run_module('mod1')#runs the mod1 module 
runpy . run_module(mod1)#error  agument mod1 should be enclosed in string ("mod1") 

from cal import *   # How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * #How  to  import  all  the  members  of  cal  module
print(x)#How  to  print  variable  'x'  of  cal   module
print(y)#How  to  print  variable  'y'  of  cal   module
print(cal . x)#error we are imported the members of the cal module but not the cal modeule itself so error
print(add(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7
print(sub(10,7))#How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10,7))#How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y))#error we are imported the members of the cal module but not the cal modeule itself so error
a=c1()
a.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()#error we are imported the members of the cal module but not the cal modeule itself so error ,andalso there was no obj b in cal class so error 

from cal import x,add,mul,c1# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')#Begin
from cal import x,add,mul,c1#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)#How  to  print  variable  'x'  of  cal   module)
print(y)#error we can access the y of cal module as we not imported it 
print(cal . x)##error we are imported the members of the cal module but not the cal modeule itself so error
print(a.add(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7##here there was no object created for class c1() so we cannot call it without creating the object so error 
print(sub(10 , 7))#error we not imported the sub method sub method from cal and current module also not have the sub function so error 
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7))#error we not imported the mul method sub method from cal and current module also not have the mul function so error 
a=c1()
a.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module


# Module  alias
print('Begin')#Begin
import cal as calsi  #How  to  import  cal  module  with   another  name  using  import  statement
print(calsi.x)#How  to  print  variable  'x'  of  cal   module)
print(calsi.y)#How  to  print  variable  'y'  of  cal   module)
print(calsi.add(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(calsi.sub(10,7))#How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(calsi.mul(10,7))#How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(calsi.div(10,7))#How  to  call  div()  function  of  cal  module  with  10  and  7)
a=calsi.c1()
a.m1()#How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)#error as due to cal computer asks for wht is cal object 
from  math  as   m  import  *#error from statement only supports the member alias  but not the module alias


# Member  alias
from cal import x as i ,add as ADD,mul as MUL, c1 as C1#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(i) # How  to  print  variable  'x'  of  cal   module
print(x)#error x is not defined ie.error as due to in current module x is not defined .it is odd name of i as computer only recognizes new name only 
print(ADD(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(MUL(10,7))#How  to  call  mul()  function  of  cal  module  with  10  and  7)
a=C1()
a.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))#error computer searches in the current module and in current module the add method is not present 
b = c1()#error there is no c1 class in the current module .


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
print(x)#10
disp()#disp  function  of  mod1
a = c1()
a . m1()#m1  method  of  class  c1  in  mod1

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)#20
disp()#disp  function  of  mod2
a = c1()
a . m1()#m1  method  of  class  c1  in  mod2

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1 ,mod2  #  How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1
mod1.disp()#How  to  call  disp()  function  of  mod1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print()#nothing is printed 
print(mod2.x)#How  to  print  variable  'x'  of  mod2
mod2.disp()#How  to  call  disp()  function  of  mod2
a=mod2.c1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()#nothing is printed 
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
a=c1()
a.m1()#How  to  call  method  m1()  of  class   c1  in  current  module

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import *   #How  to  import  members  of  mod1
from mod2 import *    #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1)
mod1.disp()#How  to  call  disp()  function  of  mod1
a=mod1.c1()
mod1.c1(a)#How  to  call  method  m1()  of  class   c1  in  mod1
print()#nothing 
print()#nothing
print(mod2.x)#How  to  print  variable  'x'  of  mod2)
mod2.disp()#How  to  call  disp()  function  of  mod2
a=mod2.c1()#
mod2.c1(a)#How  to  call  method  m1()  of  class   c1  in  mod2
print()#nothing 
print()#nothing
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
a=c1()
a.m1()#How  to  call  method  m1()  of  class   c1  in  current  module


# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__=='__main__:
    print('Four')
    print('Five')
    print('Six')
print('Seven')
print('Eight')
print('Nine')


# Find  outputs (Home  work)
print('Begining  of  mod2')#Begining  of  mod2
import   mod1
#####outputs of mod1 stmts execution :--###One<nxt>Two<nxt>Three<nxt>Seven<nxt>Eight<nxt>Nine
print('End  of  mod2')#End  of  mod2



#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.42
a = cal . c1()
a . m1()#m1  method


#  Find  outputs
from  cal  import   y , sub , mul
print(x)#error because the x is not defined in  the current module 
print(y)#100
print(add(10 , 7))#errro because the add()function  is not defined in  the current module 
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#errro because the adiv()function  is not defined in  the current module 
a = c1()#error c1 class it is the member of the module we cannot imported the module we imported the module itself so error if it was 