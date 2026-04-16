# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
# End of class
a = Rat()
b = Rat(9)
c = Rat(5,  8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  # Input: 11
y = eval(input('Enter Denominator  :  '))    # Input: 15
f = Rat(x , y)
print('a  :  ' , a)  # a  :  22 / 7
print('b  :  ' , b)  # b  :  9 / 7
print('c  :  ' , c)  # c  :  5 / 8
print('d  :  ' , d)  # d  :  22 / 9
print('e  :  ' , e)  # e  :  2 / 3
print('f  :  ' , f)  # f  :  11 / 15
c . __init__()
print('c  :  ' , c)  # c  :  22 / 7
a . __init__(3.8  , 4.6)  
print('a  :  ' , a)  # a  :  3.8 / 4.6
# g = Rat(nr1 = 9 , 5)  # Error because positional argument follows keyword argument
# h = Rat(nr = 9 , dr = 5)  # Error because unexpected keyword arguments 'nr' and 'dr' (args are nr1, dr1)

# -----------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)  # a  :  {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . __dict__)  # b  :  {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . __dict__)  # c  :  {'dd': 19, 'mm': 7, 'yy': 1985}
# d = Date()  # Error because missing 3 required positional arguments
# e = Date(dd = 30 , mm = 4 , yy = 2022)  # Error because unexpected keyword arguments (args are dd1, mm1, yy1)
# f = Date(dd1 = 26 , mm1 = 8 , 2023)  # Error because positional argument follows keyword argument

# -----------------------------------------------------------------------------------------------------

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
# a = c1()  # Error because __init__() should return None, not 'int'
b = c2() # c2 class constructor
print(b) # <__main__.c2 object at 0x...>
print(b . __init__())  # c2 class constructor / None
c = c3()  # c3 class constructor
print(c . __init__())  # c3 class constructor / None

# -----------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		# b = c1() # This line would cause a RecursionError
# a = c1()  # Constructor / Error because of infinite recursion

# -----------------------------------------------------------------------------------------------------

# Difference  between  init()  and  __init__()  (Home  work)
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
a = c1()  # Constructor
print(a . __dict__)  # {'x': 10, 'y': 20}
b = c2()
print(b . __dict__)  # {}
b . init()  # Method
print(b . __dict__)  # {'x': 30, 'y': 40}

# -----------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
class   c2:
        def  m3(self):
                x . e = 50
def   f1():
        x . c = 30

x = c1()
print(x . __dict__)  # {'a': 10}
x . m1() 
print(x . __dict__)  # {'a': 10, 'b': 20}
f1()
print(x . __dict__)  # {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . __dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . __dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . __dict__)  # {'a': 10}

# -----------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
a = c1(); b = c1()
print(a . __dict__)  # {'x': 10, 'y': 20, 'z': 30}
print(b . __dict__)  # {'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . __dict__)  # {'y': 20, 'z': 30}
print(b . __dict__)  # {'x': 10, 'z': 30}
# print(a . x)  # Error because attribute 'x' was deleted
# print(b . y)  # Error because attribute 'y' was deleted

# -----------------------------------------------------------------------------------------------------

# Find  outputs (Home  work) - Method Overloading (Last definition wins)
class   c1:
	def  __init__(self): print('1st  constructor')
	def  __init__(self): print('2nd  constructor')
	def  __init__(self): print('3rd  constructor')
a = c1()  # 3rd  constructor

# -----------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
class   c1:
	def  __init__(self): print('No argument constructor')
	def  __init__(self , x): print('single argument constructor : ' , x)
	def  __init__(self , x , y): print('Two argument constructor : ' , x , y)
a = c1(10 , 20)  # Two argument constructor : 10 20
# b = c1(30)  # Error because missing 1 argument (needs x and y)
# c = c1()  # Error because missing 2 arguments (needs x and y)

# -----------------------------------------------------------------------------------------------------

# Find outputs
class   c1:
	def  __init__(self , x = 100 , y = 200):
		print('Two argument constructor : ' , x , y)
a = c1(10 , 20)  # Two argument constructor : 10 20
b = c1(30)  # Two argument constructor : 30 200
c = c1()  # Two argument constructor : 100 200

# -----------------------------------------------------------------------------------------------------

# What happens when function and class have same name?
def   f1():
	print('Function'); return 25
class   f1:
	def  __init__(self): print('Constructor')
a = f1()  # Constructor
print(a)  # <__main__.f1 object at 0x...>

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home  work)
class    c1:
	def   __init__(self): print('Constructor')
def  c1():
	print('Function')
a = c1()  # Function
print(a)  # None

# -----------------------------------------------------------------------------------------------------

# Save in prog9a.py
class   c1:
	def  __init__(self): print('c1  class  of  prog9a')

# Find  outputs (Home  work) - From prog9b.py
from  prog9a  import  c1
class   c1:
	def  __init__(self): print('c1  class  of  prog9b')
a = c1()  # c1  class  of  prog9b

# Find  outputs (Home  work) - From prog9c.py
class   c1:
	def  __init__(self): print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()  # c1  class  of  prog9a

# How to use both - From prog9d.py
from  prog9a import  c1 as c
class   c1:
	def  __init__(self): print('c1  class  of  prog9d')
a = c1() # c1 class of prog9d
b = c()  # c1 class of prog9a

# How to use both - From prog9e.py
import prog9a
class   c1:
	def  __init__(self): print('c1  class  of  prog9e')
a = c1()        # c1 class of prog9e
b = prog9a.c1() # c1 class of prog9a