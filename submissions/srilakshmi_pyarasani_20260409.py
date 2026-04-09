1) outputs 
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_)#a : {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . _dict_)#b : {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . _dict_)#c : {'dd': 19, 'mm': 7, 'yy': 1985}
d = Date()
e = Date(dd = 30 , mm = 4 , yy = 2022)
f = Date(dd1 = 26 , mm1 = 8 , 2023)#Errro bcz of 2023

2) outputs
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
print(b)#Type and address of object b
print(b . _init_())#c2 class constructor <nextline> None
c = c3()
print(c . _init_())#c3 class constructor <nextline> None

3) outputs 
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()

4) Difference  between  init()    and  _init_()   methods 
class c1:
    def  _init_(self):
        print('Constructor')#Constructor
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')#Method
        self . x = 30
        self . y = 40
a = c1()
print(a . _dict_)#{'x': 10, 'y': 20}
b = c2()
print(b . _dict_)#{}
b . init()
print(b . _dict_)#{'x': 30, 'y': 40}


'''
Object  'a'  --->   x = 10 y= 20

Object  'b'  --->   x = 30 y = 40
'''
5) outputs 
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
print(x . _dict_)#{'a': 10}
x . m1()
print(x . _dict_)#{'a': 10, 'b': 20}
f1()
print(x . _dict_)#{'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . _dict_)#{'a': 10, 'b': 20, 'c': 30, 'd':40}
y = c2()
y . m3()
print(x . _dict_)#{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . _dict_)#{'a': 10}


'''
object  'x'  ---> a =10 b=20 c=30 d=40 
object  'z'  ---> a = 10

object  'y'  --->a=10 b=20 c= 30
'''

6) outputs  
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_)#{'x': 10, 'y': 20, 'z': 30}
print(b . _dict_)#{'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . _dict_)#{'y': 20, 'z': 30}
print(b . _dict_)#{'x': 10, 'z': 30}
print(a . x)#Error because it is not valid
print(b . y)#Error because it is not valid


'''
Object  'a'   --->  y = 20 z = 30

Object  'b'   --->  x=10 z = 30
'''
8) outputs 
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()#Not executed until unless it is called

9) outputs  
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#Error because it is not valid
b = c1(30)#Error because it is not valid
c = c1()#Error because it is not valid

10) outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#Error because it is not valid
b = c1(30)#Error because it is not valid
c = c1()

11) What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1()
print(a)#Type and address of object a

12) outputs 
class    c1:
	def   _init_(self):
		print('Constructor')#Discarded
def  c1():
	print('Function')#Function
#end of the  class
a = c1()
print(a)#None

13) outputs  
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)#Function : 25
# End  of  class  c1
a = c1()
b = c1(25)
print(b)

14) Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')#c1  class  of  prog9a

15) outputs 
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')#c1  class  of  prog9b
a = c1()

16) outputs 
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')#c1  class  of  prog9c
from  prog9a  import  c1
a = c1()

17) How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
import prog9a #How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a = c1() #How  to  create  c1  class  object  of  current  module
b = prog9a.c1() #How  to  create  c1  class  object  of  prog9a

18) How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a #How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a = c1() #How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a