#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
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
print(hasattr(a , 'nr'))# True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False



# Object  'a'  --->


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
#Meow Meow Meow ....
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
setattr(a , varname , value)
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))#10 20
	except:
		print(F'Invalid  variable   name   :  {varname}')# Invalid  variable   name   : z
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
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop
class  Emp:
        pass
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e =Emp()
for x,y in dict.items():
        setattr(e,x,y)
for k in dict:
        print(k,getattr(e,k))


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
#Hyd Sec Cyb




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
a = mod1.c1()
a.m1()
print('Bye')
import  mod4#module error
print(x)#valuennotfound error
f1()#function error
#Hello
Hyd
Sec
Cyb
25
Function
Method
Bye


#  Find  outputs  (Home  work)
print('Before')
How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy . run_module(mod1)


# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import *
print(x)#How  to  print  variable  'x'  of  cal   module
print(y)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y))
How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()
# Outputs:
print('Begin')
from cal import *
print(x)
print(y)
# print(cal . x)
print(add(10,7))
print(sub(10,7))
print(mul(10,7))
print(div(10,7))
b = c1()
b.m1()


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
#Outputs
print('Begin')
from cal import x,add,mul,c1
print(x)
# print(y)
# print(cal.x)
print(add(10,7))
# print(sub(10,7))
print(mul(10,7))
b = c1()
b.m1()


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
#Outputs:
import  cal as c
print('Begin')
print(c.x)
print(c.y)
print(c.add(10,7))
print(c.sub(10,7))
print(c.mul(10,7))
print(c.div(10,7))
b = c.c1()
b.m1()
# print(cal . x)error


# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(How  to  print  variable  'x'  of  cal   module)
print(x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()
#outputs
from cal import x ,add as a, mul as m , c1 as c
print(x)
print(a)
print(m)
b = c()
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
print(x)10
disp()#disp  function  of  mod1
a = c1()
a . m1()#'m1  method  of  class  c1  in  mod1




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
import  mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1,x)
mod1.disp()
b=mod1.c1
b.m1()
print()
print(mod2.x)
mod2.disp()
b=mod2.c1()
b.m1()
print()
print(x)
disp()
a= c1()
a.m1()


 # How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import *
from mod2 import *
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1,x)
mod1.disp()
b=mod1.c1
b.m1()
print()
print(mod2.x)
mod2.disp()
b=mod2.c1()
b.m1()
print()
print(x)
disp()
a= c1()
a.m1()


# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
if __name__='__main__':
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


#  Find  outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.
a = cal . c1()
a . m1()#m1 method



#  Find  outputs
from  cal  import   y , sub , mul
print(x)#error
print(y)#200
print(add(10 , 7))#error
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#error
a = c1()#error