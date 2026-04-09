# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self.nr}/{self.dr}'
#end  of  the  class
a = Rat() # object a is created of class Rat
b = Rat(9) # object b is created of class Rat with 9 as numerator and default denoinator i.e 7
c = Rat(5,  8) # object c is created of class Rat with 5 as numerator and 8 as denominator
d = Rat(dr1 = 9) # object d is created of class Rat with 9 as denominator and default numerator 22
e = Rat(dr1 = 3 , nr1 = 2) # object e is created of class Rat with 2 as numerator and 3 as denominator
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # object f is created of class Rat with 11 as numerator and 15 as denominator
print('a  :  ' , a) # a : 22 / 7
print('b  :  ' , b) # b : 9 / 7
print('c  :  ' , c) # c : 5 / 8
print('d  :  ' , d) # d : 22 / 9
print('e  :  ' , e) # e : 2 / 3
print('f  :  ' , f) # f : 11 / 15
c . __init__()
print('c  :  ' , c) # c : 22 / 7
a . __init__(3.8  , 4.6)
print('a  :  ' , a) # a : 3.8 / 4.6
# g = Rat(nr1 = 9 , 5) # error because 5 is not a keyword argument
# h = Rat(nr = 9 , dr = 5) # error because nr and dr are not keyword arguments

# Find  outputs 
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) # objecta is created of class Date 
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26) # objectb is created of class Date
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) # objectc is created of class Date
print('a  :  ' , a . __dict__) # a : {'dd':15, 'mm':8, 'yy':1947}
print('b  :  ' , b . __dict__) # b : {'dd':26, 'mm':1, 'yy':1950}
print('c  :  ' , c . __dict__) # c : {'dd':19, 'mm':7, 'yy':1985}
d = Date() # Date.__init__() missing 3 required positional arguments: 'dd1', 'mm1', and 'yy1'
e = Date(dd1 = 30 , mm1 = 4 , yy = 2022) # Date.__init__()got an unexpected keyword argument 'dd'
f = Date(dd1 = 26 , mm1 = 8 , 2023) # error positional argument follows keyword argument


'''
Object  'a'   --->  # a : {'dd':15, 'mm':8, 'yy':1947}

Object  'b'   --->  # b : {'dd':26, 'mm':1, 'yy':1950}

Object  'c'   --->  # c : {'dd':19, 'mm':7, 'yy':1985}
'''

# Find  outputs 
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
# a = c1() # error __init__() should return None, not 'int' 
b = c2() # <__main__.c2 object at 0x0000025639E479E0>
print(b) # None
print(b . __init__()) # c2  class  constructor None
c = c3() # c3  class  constructor
print(c . __init__()) # c3  class  constructor

# Find  outputs 
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() # Constructor , Constructor......... "Error: maximum recursion depth exceeded while calling a Python object"

#  Difference  between  init()    and  __init__()   methods (Home  work)
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
a = c1() # Constructor
print(a . __dict__) # {'x': 10, 'y': 20}
b = c2() # object b is created of class c2
print(b . __dict__) # {} because  init()  is  not  called
b . init() # Method
print(b . __dict__) # {'x': 30, 'y': 40}


'''
Object  'a'  --->  {'x': 10, 'y': 20}

Object  'b'  ---> {'x': 30, 'y': 40}
'''

# Find  outputs 
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
x = c1() # object  'x'  of  class  c1
print(x . __dict__) # {'a': 10}
x . m1() 
print(x . __dict__) # {'a': 10, 'b': 20}
f1() # f1() is  called
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . __dict__) # {'a': 10}


'''
object  'x'  ---> # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

object  'z'  ---> # {'a': 10}

object  'y'  ---> # {}
'''

#  Find  outputs 
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() # 3rd constructor

#  Find  outputs  
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :  10 20
b = c1(30) # error missing 1 required positional argument: 'y'
c = c1() # x and y are missing

def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
# End  of  the  class
a = f1()
print(a) # Constructor <__main__.f1 object at 0x000002B016D176B0>

class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
# a = c1() # error missing 1 required positional argument: 'x'
b = c1(25) # Function :  25
print(b) # None

#  Find  outputs 
from  Ajay_Sougani_20260408  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # c1  class  of  prog9b

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  Ajay_Sougani_20260408  import  c1
a = c1() # 'c1  class  of  prog9c' 'c1  class  of  prog9c'

from Ajay_Sougani_20260408  import  c1 as prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
# How  to  create  c1  class  object  of  current  module
a=c1()
# How  to  create  c1  class  object  of  prog9a
b=prog9a()

'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
# How  to  import  prog9a
from Ajay_Sougani_20260408 import c1 as c1_prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
# How  to  create  c1  class  object  of  current  module
a=c1()
# How  to  create  c1  class  object  of  prog9a
b = c1_prog9a()