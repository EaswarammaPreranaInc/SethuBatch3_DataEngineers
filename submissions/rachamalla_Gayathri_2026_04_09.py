 # cal . py
 # Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ') #disp function of same module
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) #30
disp()
a = c1()
a . m1() #m1 method of class c1 is same module
# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) #30
disp()disp  function  of  same  module
a = c1()
a . m1()m1  method of  class  c1  in  same  module
 # How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
How  to  import  mod1  and  mod2
import *from mod1
import *from mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
print(x)
How  to  call  disp()  function  of  mod1
disp()
How  to  call  method  m1()  of  class   c1  in  mod1
a=c1()
a.m1()

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
"if__name__==__main__":
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
print(cal . x)
print(cal . y)
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.2
a = cal . c1()
a . m1()
 #  Find  outputs
from  cal  import   y , sub , mul
print(x)
print(y)
print(add(10 , 7))#not imported
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#error
a = c1()
# Find  outputs (Home  work)
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_)
print('b  :  ' , b . _dict_)
print('c  :  ' , c . _dict_)
d = Date()
e = Date(dd = 30 , mm = 4 , yy = 2022)
f = Date(dd1 = 26 , mm1 = 8 , 2023)

a :  {'dd': 15, 'mm': 8, 'yy': 1947}
b :  {'dd': 26, 'mm': 1, 'yy': 1950}
c :  {'dd': 19, 'mm': 7, 'yy': 1985}


'''
Object  'a'   --->  

Object  'b'   --->  

Object  'c'   --->  
'''
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  _init_(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  _init_(self):
		print('c3  class  constructor')#c3  class  constructor
None
# End  of  class
a = c1()
b = c2()
print(b)#c2 class constructor
print(b . _init_())
c = c3()
print(c . _init_())

c2  class  constructor
None
c3  class  constructor
None
 # Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')#constructor
		b = c1()
# End  of  class
a = c1()
 #  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  _init_(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()
print(a . _dict_)
b = c2()
print(b . _dict_)
b . init()
print(b . _dict_)

{}
{}
Method
{'x': 30, 'y': 40}

'''
Object  'a'  --->  

Object  'b'  ---> 
'''
# Find  outputs (Home  work)
class   c1:
        def   _init_(self):
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
x = c1()
print(x . _dict_)
x . m1()
print(x . _dict_)
f1()
print(x . _dict_)
x . d = 40
print(x . _dict_)
y = c2()
y . m3()
print(x . _dict_)
z = c1()
print(z . _dict_)


'''
object  'x'  --->

object  'z'  --->

object  'y'  --->
'''
# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_)
print(b . _dict_)
del  a . x
del  b . y
print(a . _dict_)
print(b . _dict_)
print(a . x)
print(b . y)


'''
Object  'a'   --->  

Object  'b'   --->  
'''
[1:15 pm, 09/04/2026] SRINIVAS Sir Maths: #  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #no output
#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y) #Two  argument  constructor : ' , 10,20
# End  of  the  class
a = c1(10 , 20)
b = c1(30)#error
c = c1()
#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#error
b = c1(30)#error
c = c1()
 # What  happens  when  function  and  class  have  same  name ? #class is executed
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor') #constructor
# End  of  the  class
a = f1()
print(a)#address
# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)
# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()
b = c1(25)
print(b)
#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')
: #  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()#'c1  class  of  prog9b
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import
 #  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()
#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
How  to  create  c1  class  object  of  current  module
a=cl()
How  to  create  c1  class  object  of  prog9a
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a