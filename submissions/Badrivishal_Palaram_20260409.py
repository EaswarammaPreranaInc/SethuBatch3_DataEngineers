
#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
How  to  import  mod1#---------------------------------------import  mod1
print(How  to  print   variable  'x'   of  mod1)#------------print(mod1.x)
How  to  call  function  f1()  of  mod1#---------------------mod1.f1()
How  to  call  method  m1()  of  class  c1  in  mod1#--------a = mod1.c1()
a.m1()
print('Bye')
import  mod4
print(x)#
f1()#


#  Find  outputs  (Home  work)
print('Before')
How  to  run  mod1------#import mod1
print(mod1 . x)---------#25
mod1 . f1()-------------#Function
a = mod1 . c1()
print('After')----------#After

run_module('mod1')------#Mod1
runpy . run_module(mod1)#Mod1



#HomeWork
How  to  use  members  of  cal  module  with  from  statement ?#from  cal  import  *
print('Begin')------------------------------------------------#Begin
How  to  import  all  the  members  of  cal  module-----------#from  cal  import  *
print(How  to  print  variable  'x'  of  cal   module)---------#print(x)
print(How  to  print  variable  'y'  of  cal   module)---------#print(y)
print(cal . x)-------------------------------------------------#100
print(How  to  call  add()  function  of  cal  module  with  10  and  7)#print(add(10 , 7))
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)#print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)#print(mul(10 , 7))
print(How  to  call  div()  function  of  cal  module  with  10  and  7)#print(div(10 , 7))
print(cal . add(x , y))#300


H
How  to  call  m1()  method  of  class  c1  in  cal  module----#from  cal  import  c1
b = cal . c1()
# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')----------#Begin
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle-------#import  cal
print(How  to  print  variable  'x'  of  cal   module)#print(cal . x)
print(y)--------------------------------------------------------#NameError: name 'y' is not defined
print(cal . x)---------------------------------------------------------------#NameError: name 'cal' is not defined
print(How  to  call  add()  function  of  cal  module  with  10  and  7)------#print(cal . add(10 , 7))
print(cal . sub(10 , 7))------------------------------------------------------#NameError: name 'cal' is not defined
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)--------#print(cal . mul(10 , 7))
print(cal . div(10 , 7))--------------------------------------------#NameError: name 'cal' is not defined




How  to  call  m1()  method  of  class  c1  in  cal  module------# cal . c1().m1()
# Module  alias
print('Begin')#Begin
How  to  import  cal  module  with   another  name  using  import  statement-------#import  cal  as   c
print(How  to  print  variable  'x'  of  cal   module)-----------------------#print(cal . x)
print(How  to  print  variable  'y'  of  cal   module)------------------#print(cal . y)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)#print(cal . add(10 , 7))
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)#print(cal . sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)#print(cal . mul(10 , 7))
print(How  to  call  div()  function  of  cal  module  with  10  and  7)#print(cal . div(10 , 7))
How  to  call  m1()  method  of  c1  class  in  cal  module-------------#cal . c1().m1()
print(cal . x)--------------------------------------------------------------#100
from  math  as   m  import  *-----------------------------------------#import  all  functions  and  variables  of  math  module


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
		print('c3  class  constructor')
# End  of  class
a = c1()
b = c2()
print(b)#  type and address of  b
print(b . _init_())#  c2  class  constructor
c = c3()
print(c . _init_())#  c3  class  constructor



# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
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
print(a . _dict_)#  {'x': 10, 'y': 20}
b = c2()
print(b . _dict_)#  {}
b . init()
print(b . _dict_)#  {'x': 30, 'y': 40}



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
print(x . _dict_)#  {'a': 10}
x . m1()
print(x . _dict_)#  {'a': 10, 'b': 20}
f1()
print(x . _dict_)#  {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . _dict_)#  {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . _dict_)#  {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . _dict_)#  {'a': 10}



'''
object  'x'  --->#  {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

object  'z'  --->#  {'a': 10}

object  'y'  --->#  {}
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
print(a . _dict_)#  {'x': 10, 'y': 20, 'z': 30}
print(b . _dict_)#  {'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . _dict_)#  {'y': 20, 'z': 30}#  {'x': 10, 'z': 30}
print(b . _dict_)#  {'x': 10, 'z': 30}#  {'y': 20, 'z': 30}
print(a . x)#  AttributeError: 'c1' object has no attribute 'x'
print(b . y)#  AttributeError: 'c1' object has no attribute 'y'


'''
Object  'a'   --->  #  {'y': 20, 'z': 30}

Object  'b'   --->  #  {'x': 10, 'z': 30}
'''



  #  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()# 3rd  constructor



#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#  Two  argument  constructor :  10 20
b = c1(30)#  TypeError:  c1()  takes  no  arguments  but  one  was  given
c = c1()#  TypeError:  c1()  takes  no  arguments  but  zero  were  given



#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#  Two  argument  constructor :  10 20
b = c1(30)#  Two  argument  constructor :  30 200
c = c1()#  Two  argument  constructor :  100 200




# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1()# Constructor
print(a)#type and address




# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()# Function
print(a)# None




 # Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()# TypeError:  c1()  missing  1  required  positional  argument:  'x'
b = c1(25)# Function :  25
print(b)# None




#prog9a.py
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')




#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()# c1  class  of  prog9b



#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()# c1  class  of  prog9a



 #  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a #from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
How  to  create  c1  class  object  of  current  module # a = c1()# c1  class  of  prog9d
How  to  create  c1  class  object  of  prog9a# a = c1()# c1  class  of  prog9a



'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a # import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module # a = c1()# c1  class  of  prog9e
How  to  create  c1  class  object  of  prog9a# a = prog9a.c1()# c1  class  of  prog9a

