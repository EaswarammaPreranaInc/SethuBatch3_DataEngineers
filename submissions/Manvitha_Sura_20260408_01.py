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

#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import mod1
print(mod1.x)
mod1.f1()
a=mod1.c1()
a.m1()
print('Bye')
import  mod4
print(x)
f1()

#  Find  outputs  (Home  work)
print('Before')
import runpy
print(mod1 . x)  #error-mod1 is not imported
mod1 . f1()  #error-mod1 is not imported
a = mod1 . c1()  #error-mod1 is not imported
print('After')
run_module('mod1') #error-no run module fun in current module
runpy . run_module(mod1)

'''
Before
After
Hyd
Sec
Cyb
'''

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')  #Begin
from cal import *
print(x)  #100
print(y)  #200
print(cal . x)  #error
print(add(10,7))  #17
print(sub(10,7))  #3
print(mul(10,7))  #70
print(div(10,7))  #1.42
print(cal . add(x , y))  #error
a=c1()  #c1 class object is created
a.m1()  #m1 method
b = cal . c1()  #error


# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')  #Begin
from cal import *  #imports only those members in __all__ list
print(x)  #100
print(y)  #error--not imported as it is not part of __all_
print(cal . x)  #error
print(add(10,7))  #17
print(sub(10 , 7))  #error-not imported as it is not part of __all__
print(mul(10,7))  #70
print(div(10 , 7))    #error-not imported as it is not part of __all__
c=c1()
c.m1()  #m1 method

# Module  alias
print('Begin')  #Begin
import cal as c
print(c.x)  #100
print(c.y)  #200
print(c.add(10,7))  #17
print(c.sub(10,7))  #3
print(c.mul(10,7))  #70
print(c.div(10,7))  #1.42
a=c.c1()  #error
a.m1()  #if a=c1() then prints ->m1 method
print(cal . x)  #error -cal is imported as c not cal
from  math  as   m  import  * #error-no module alias in from statement

# Member  alias
from cal import x as b , add as a, mul as m,c1 as c 
print(b)  #100
print(x)  #error-no x in current module and x is notimported
print(a(10,7))  #17
print(m(10,7))  #70
q=c() 
q.m1()  #m1 method
print(add(10 , 7))  #error-no add method in current module or imported module
b = c1()  #error-no c1 class in current module or imported module

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
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
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
b=mod2.c1()
b.m1()
print()
print(x)
disp()
c=c1()
c.m1()



# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as a,disp as b,c1 as c
from mod2 import x as d,disp as e,c1 as f
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(a)
b()
q=c()
q.m1()
print()
print()
print(d)
e()
w=f()
w.m1()
print()
print()
print(x)
disp()
r=c1()
r.m1()



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
End of mod2

'''


#  Find  outputs
import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))
print(cal . sub(10 , 7))
print(cal . mul(10 , 7))
print(cal . div(10 , 7))
a = cal . c1()
a . m1()
'''
100
200
17
3
70
1.42
m1 method
'''



#  Find  outputs
from  cal  import   y , sub , mul
print(x)  #error-not imported
print(y)  #200
print(add(10 , 7))  #error-not imported and current program doesnt have add()
print(sub(10 , 7))  #3
print(mul(10 , 7))  #70
print(div(10 , 7))  #error-not imported and current program doesnt have div()
a = c1()  #there is no class c1 in current program
