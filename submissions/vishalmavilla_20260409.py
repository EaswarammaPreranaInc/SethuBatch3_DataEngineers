# Find  outputs
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()
b = Rat(9)
c = Rat(5,  8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a) # a  :  22  /  7
print('b  :  ' , b) # b  :  9   /  7
print('c  :  ' , c) # c  :  5   /  8
print('d  :  ' , d) # d  :  22  /  9
print('e  :  ' , e) # e  :  2   /  3
print('f  :  ' , f) # f  :  11  /  15
c . _init_()
print('c  :  ' , c) # c  :  22  /  7
a . _init_(3.8  , 4.6)
print('a  :  ' , a) # a  :  3.8  /  4.6
g = Rat(nr1 = 9 , 5) # Error because the positional arguments cannot be followed after keyword arguments
h = Rat(nr = 9 , dr = 5) # Error because the variables nr and dr are not defined


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
print('a  :  ' , a . _dict_) # a  :  {'dd' : 15 , 'mm' : 8 , 'yy' : 1947} 
print('b  :  ' , b . _dict_) # b  :  {'dd' : 26 , 'mm' : 1 , 'yy' : 1950} 
print('c  :  ' , c . _dict_) # c  :  {'dd' : 19 , 'mm' : 7 , 'yy' : 1985} 
d = Date() # Error because there are no arguments are passed while creating the object
e = Date(dd = 30 , mm = 4 , yy = 2022) # Error because variables dd,mm and yy are defined
f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error because the positional arguments cannot be followed by keyword arguments


'''
Object  'a'   --->  dd = 15 , mm = 8 , yy = 1947

Object  'b'   --->  dd = 26 , mm = 1 , yy = 1950

Object  'c'   --->  dd = 19 , mm = 7 , yy = 1985
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
		print('c3  class  constructor')
# End  of  class
# a = c1() # Error because the constructor cannot return a value
b = c2() # c2  class  constructor
print(b) # <class '__main__.c2'> and address of object b
print(b . _init_()) # c2  class  constructor <nextline> None
c = c3() # c3  class  constructor
print(c . _init_()) # c3  class  constructor <nextline> None

# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() # Infinite times Constructor is printed

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
print(a . _dict_) # {'x' : 10 , 'y' : 20}
b = c2() 
print(b . _dict_) # {}
b . init() # Method
print(b . _dict_) # {'x' : 30 , 'y' : 40}


'''
Object  'a'  --->  x = 10 , y = 20

Object  'b'  --->  x = 30 , y = 40
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
print(x . _dict_) # {'a' : 10}
x . m1()
print(x . _dict_) # {'a' : 10 , 'b' : 20}
f1()
print(x . _dict_) # {'a' : 10 , 'b' : 20 , 'c' : 30}
x . d = 40
print(x . _dict_) # {'a' : 10 , 'b' : 20 , 'c' : 30 , 'd' : 40}
y = c2() 
y . m3()
print(x . _dict_) # {'a' : 10 , 'b' : 20 , 'c' : 30 ,  'd' : 40 , 'e' : 50}
z = c1()
print(z . _dict_) # {'a' : 10}


'''
object  'x'  ---> a = 10 , b = 20 , c = 30 , d = 40 , e = 50

object  'z'  ---> a = 10

object  'y'  ---> empty
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
print(a . _dict_) # { 'x' : 10 , 'y' : 20 , 'z' : 30}
print(b . _dict_) # { 'x' : 10 , 'y' : 20 , 'z' : 30}
del  a . x
del  b . y
print(a . _dict_) # { 'y' : 20 , 'z' : 30}
print(b . _dict_) # { 'x' : 10 , 'z' : 30}
print(a . x) # Error instance variable x is not there in the object a
print(b . y) # Error instance variable y is not there in the object b


'''
Object  'a'   --->  y = 20 , z = 30

Object  'b'   --->  x = 10 , z = 30
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
a = c1() # 3rd  constructor

#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
b = c1(30) # Error only one argument is passed while creating object but requires two arguments
c = c1() # Error no argument is passed while creating object but requires two arguments

#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
b = c1(30) # Two  argument  constructor : 30 200
c = c1() # Two  argument  constructor : 100 200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1() # Constructor
print(a) # <class '__main__.f1'> and address of object a

# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1() # Function
print(a) # None

# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1() # Error the function c1() requires one argument
b = c1(25) # Function : 25
print(b) # None

#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1() # c1  class  of  prog9b

#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() # c1  class  of  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a = c1() # c1  class  of  prog9d
from prog9a import c1
b = prog9a.c1() # c1  class  of  prog9a

'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a = c1() # c1  class  of  prog9e
b = prog9a.c1() # c1  class  of  prog9a