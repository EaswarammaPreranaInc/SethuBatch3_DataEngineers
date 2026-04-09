# # mod1 . py
# print('Hyd')
# print('Sec')
# print('Cyb')
# x = 25
# def  f1():
# 	print('Function')
# class   c1:
# 	def   m1(self):
# 			print('Method')

#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import mod1 #How  to  import  mod1
print(mod1.x) #How  to   print   variable  'x'   of  mod1
mod1.f1() #How  to  call  function  f1()  of  mod1
mod1.c1().m1() #How  to  call  method  m1()  of  class  c1  in  mod1
print('Bye')
import  mod4
#print(x) Error
#f1()# Error

#  Find  outputs  (Home  work)
print('Before')
run_module('mod1') #How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy . run_module(mod1)

# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import * #How  to  import  all  the  members  of  cal  module
print(x)
print(y)
print(cal . x)# Error
print(add(10,7))
print(sub(10,7))
print(mul(10,7))
print(div(10,7))
print(cal . add(x , y))# Error
c1().m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()# Error

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
__all__=['x','add','mul','c1'] #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
from cal import *
print(x)
print(y)# Error
print(cal . x)#Error
print(add(10,7))
print(sub(10 , 7))# Error
print(mul(10,7))
print(div(10 , 7))# Error
c1().m1()

# Module  alias
print('Begin')
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)
print(c.y)
print(c.add(10,7)) #How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10,7)) #How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10,7)) #How  to  call  div()  function  of  cal  module  with  10  and  7)
c.c1().m1() #How  to  call  m1()  method  of  c1  class  in  cal  module
#print(cal . x)# Error
#from  math  as   m  import  * # Error

# Member  alias
__all__=['x' as var,'add' as a,'mul' as m,'c1' as c] #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(var)
print(x)# Error
print(a(10,7))
print(m(10,7))
c().m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))# Error
b = c1() # Error

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
print(x) # no clarity
disp() # no clarity
a = c1()# no clarity
a . m1()# no clarity

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)# no clarity
disp()# no clarity
a = c1()# no clarity
a . m1()# no clarity

# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1, mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)
mod1.disp()
mod1.c1().m1()
print()
print(mod2.x)
mod2.disp()
mod2.c1().m1()
print()
print(x)
disp()
c1().m1()

# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as c1_mod1
from mod2 import x as x2, disp as disp2, c1 as c1_mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)
disp1() #How  to  call  disp()  function  of  mod1
c1_mod1().m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x2) #How  to  print  variable  'x'  of  mod2)
disp2() #How  to  call  disp()  function  of  mod2
c1_mod2().m1() #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)
disp() #How  to  call  disp()  function  of current  module
c1().m1() #How  to  call  method  m1()  of  class   c1  in  current  module

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
import   mod1 # One Two Three Seven Eight Nine 
print('End  of  mod2') # End  of  mod2

#  Find  outputs
import  cal
print(cal . x)# 10
print(cal . y)# 20
print(cal . add(10 , 7))# 17
print(cal . sub(10 , 7))# 3
print(cal . mul(10 , 7))# 70
print(cal . div(10 , 7))# 1.42
a = cal . c1()
a . m1()# m1 method 

#  Find  outputs
from  cal  import   y , sub , mul
print(x)# Error
print(y)#20
print(add(10 , 7))# Error
print(sub(10 , 7))# 3
print(mul(10 , 7))# 70
print(div(10 , 7))# Error
a = c1()

# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()# obj a is created and constructor is called automatically  nr=22, dr=7
b = Rat(9)# nr=9, dr=7
c = Rat(5,  8) # nr=5, dr=8
d = Rat(dr1 = 9)# Error
e = Rat(dr1 = 3 , nr1 = 2)# Error
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
#f = Rat(x , y) #Error
print('a  :  ' , a)# 22/7
print('b  :  ' , b)#9/7
print('c  :  ' , c)#5/8
print('d  :  ' , d)#Error
print('e  :  ' , e)#Error
#print('f  :  ' , f)#Error
c . __init__()#Error
print('c  :  ' , c)#Error
a . __init__(3.8  , 4.6)#Error
print('a  :  ' , a)
# g = Rat(nr1 = 9 , 5) Error bcz no PA after KA 
h = Rat(nr = 9 , dr = 5)

# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)
print('b  :  ' , b . __dict__)
print('c  :  ' , c . __dict__)
#d = Date() Error
#e = Date(dd = 30 , mm = 4 , yy = 2022) Error
#f = Date(dd1 = 26 , mm1 = 8 , 2023)# Error bcz PA after KA 


# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
#a = c1()# c1 class constructor  and Error due to non -None
b = c2()# c2 class constructor and NOne is ignored
print(b)# ___str__ () is executed
print(b . __init__())# c2 class constructor and None
c = c3()# c3 class constructor
print(c . __init__())# c3 class constructor and None

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()# Constructor in finite 

#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()# obj created and calls constructor , prints msg constructor
print(a . __dict__)# {'x':10, 'y':20}
b = c2()# obj created
print(b . __dict__)# {}
b . init()# Method 
print(b . __dict__)#{'x': 30,'y': 40}

# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()# a=10
print(x . __dict__)# {'a':10}
x . m1()# b=20
print(x . __dict__)# {'a':10,'b':20}
f1()# x=30
print(x . __dict__)# {'a':10,'b':20,'c':30}
x . d = 40
print(x . __dict__)# {'a':10,'b':20,'c':30,'d':40}
y = c2()
y . m3()#e=50
print(x . __dict__)## {'a':10,'b':20,'c':30,'d':40,'e':50}
z = c1()
print(z . __dict__)## {'a':10}


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)# {'x':10,'y':20,'z':30}
print(b . __dict__)# {'x':10,'y':20,'z':30}
del  a . x
del  b . y
print(a . __dict__)#{'y':20,'z':30}}
print(b . __dict__)#{'x':10,'z':30}}
#print(a . x)# Error
#print(b . y)# Error

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()# #rd constructor

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)# Two argument constructor : 10 20 
#b = c1(30)
#c = c1()

#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)# Two  argument  constructor : 10 20
b = c1(30)# Two  argument  constructor : 30 200
c = c1()# Two  argument  constructor : 100 200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
# End  of  the  class
a = f1()# constructor
print(a)# Address 

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()# Function 
print(a)# None

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()#Error
b = c1(25)# function 25
print(b)# None


# prog9a module
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # c1  class  of  prog9b


#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()# c1 class of prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c1_a #How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
c1() #How  to  create  c1  class  object  of  current  module
c1_a()

#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)

import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
c1() #How  to  create  c1  class  object  of  current  module
prog9a.c1() #How  to  create  c1  class  object  of  prog9a

