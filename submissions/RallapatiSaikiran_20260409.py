
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
a = c1() # error
b = c2() # c2 class constructor
print(b) # class c2 and address
print(b . _init_()) # c2 class constructor none
c = c3() # c3  class  constructor 
print(c . _init_()) # c3  class  constructor None

# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() #Constructor
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
a = c1() # Constructor
print(a . _dict_) #{'x':10,'y':20}
b = c2() # 
print(b . _dict_) #{}
b . init()  # method
print(b . _dict_) # {'x':30,'y':40}


'''
Object  'a'  --->  x=10,y=20

Object  'b'  --->  x=30,y=40
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
print(x . _dict_) # {a=10}
x . m1()
print(x . _dict_) # {"a":10,"b":20}
f1()
print(x . _dict_)# {"a":10,"b":20,"c":30}
x . d = 40
print(x . _dict_)# {"a":10,"b":20,"c":30,"d":40}
y = c2()
y . m3()
print(x . _dict_)# {"a":10,"b":20,"c":30,"d":40,"e":50}
z = c1()
print(z . _dict_)# {"a":10}


'''
object  'x'  ---> a=10,b=20,c=30,d=40,e=50

object  'z'  ---> a=10

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
b = c1() #{'x':10,'y':20,z:30}
print(a . _dict_)#{'x':10,'y':20,'z':30}
print(b . _dict_)#{'x':10,'y':20,'z':30}
del  a . x
del  b . y
print(a . _dict_)#{'y':20,'z':30}
print(b . _dict_) #{'x':10,'z':30}
print(a . x)# error
print(b . y) # error


'''
Object  'a'   ---> 'y'=20,'z'=30 

Object  'b'   --->  'x'=10,'z'=30
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
a = c1(10 , 20) #Two  argument  constructor : 10 20
b = c1(30) #error
c = c1() #error

 #  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10 20
b = c1(30) #Two  argument  constructor : 30 200
c = c1() #Two  argument  constructor : 100 200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1() # COnstructor
print(a) # class f1 and id

# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1() # Function
print(a) # class Nonetype

# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1() # error
b = c1(25) # Function 25
print(b) # None

#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1() #c1  class  of  prog9b

 #  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a=c1() #How  to  create  c1  class  object  of  current  module
#not possible ,it is over ridden  #How  to  create  c1  class  object  of  prog9a

'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1() #How  to  create  c1  class  object  of  current  module
b=prog9a.c1() #How  to  create  c1  class  object  of  prog9a
