# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
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
print('a  :  ' , a)
print('b  :  ' , b)
print('c  :  ' , c)
print('d  :  ' , d)
print('e  :  ' , e)
print('f  :  ' , f)
c . __init__()
print('c  :  ' , c)
a . __init__(3.8  , 4.6)
print('a  :  ' , a)
g = Rat(nr1 = 9 , 5)
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
d = Date()
e = Date(dd = 30 , mm = 4 , yy = 2022)
f = Date(dd1 = 26 , mm1 = 8 , 2023)


'''
Object  'a'   --->  

Object  'b'   --->  

Object  'c'   --->  
'''


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
a = c1()
b = c2()
print(b)
print(b . __init__())
c = c3()
print(c . __init__())


# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()


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
a = c1()
print(a . __dict__)
b = c2()
print(b . __dict__)
b . init()
print(b . __dict__)


'''
Object  'a'  --->  

Object  'b'  ---> 
'''


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
x = c1()
print(x . __dict__)
x . m1()
print(x . __dict__)
f1()
print(x . __dict__)
x . d = 40
print(x . __dict__)
y = c2()
y . m3()
print(x . __dict__)
z = c1()
print(z . __dict__)


'''
object  'x'  --->

object  'z'  --->

object  'y'  --->
'''


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)
print(b . __dict__)
del  a . x
del  b . y
print(a . __dict__)
print(b . __dict__)
print(a . x)
print(b . y)


'''
Object  'a'   --->  

Object  'b'   --->  
'''


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()


#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()


#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()


# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
# End  of  the  class
a = f1()
print(a)


# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)


# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()
b = c1(25)
print(b)


#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')
        
        
#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()  # c1  class  of  prog9b


#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()


#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a


'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a


