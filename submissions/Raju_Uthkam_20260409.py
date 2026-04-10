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
g = Rat(nr1 = 9 , 5) #Error
h = Rat(nr = 9 , dr = 5) #Error


'''
Enter numerator  :  11
Enter Denominator  :  15
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   11  /  15
c  :   22  /  7
a  :   3.8  /  4.6
'''

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
print('a  :  ' , a . _dict_) #{'dd1':15,'mm1':8,"yy1":1947}
print('b  :  ' , b . _dict_) #{'dd1':26,'mm1':1,"yy1":1950}
print('c  :  ' , c . _dict_){'dd1':19,'mm1':7,"yy1":1985}
d = Date()
e = Date(dd = 30 , mm = 4 , yy = 2022) #Error
f = Date(dd1 = 26 , mm1 = 8 , 2023) #Error


'''
Object  'a'   --->   dd1=15   mm1=8   yy1= 1947

Object  'b'   --->  dd1=26   mm1=1   yy1= 1950

Object  'c'   --->  dd1=19   mm1=7   yy1= 1985
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
a = c1() #Error
b = c2() #c2 class constructor
print(b) #class '__main__.c1'
print(b . _init_()) # c2 class constructor  None
c = c3() #c3 class constructor
print(c . _init_()) #c3 class constructor none


# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class 
a = c1() #Constructor  /n Consturcotr....


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
a = c1() #Constructor
print(a . _dict_) #{x:10,y:20}
b = c2()
print(b . _dict_) #{}
b . init() #Method
print(b . _dict_) #{x:30,y:40}


'''
Object  'a'  --->  x=10   y=20

Object  'b'  --->  x=30 y=40
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
print(x . _dict_) #{'a':10}
x . m1()
print(x . _dict_) #{a:10,b:20}
f1()
print(x . _dict_) #{a:10,b:20,c:30}
x . d = 40
print(x . _dict_) #{a:10,b:20,c:30,d:40}
y = c2()
y . m3()
print(x . _dict_) ##{a:10,b:20,c:30,d:40,e:50}
z = c1()
print(z . _dict_) #{a:10}


'''
object  'x'  ---> a=10  b=20  c=30  d=40  e=50

object  'z'  ---> a=10

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
print(a .__dict__) #{x:10,y:20,z:30}
print(b .__dict__) #{x:10,y:20,z:30}
del  a . x
del  b . y
print(a.__dict__) #{y:20,z:30}
print(b .__dict__) #{x:10,z:30}
print(a . x) #Error
print(b . y) #Error


'''
Object  'a'   --->  y=20  z=30

Object  'b'   --->  x=10  z=30
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
a = c1() #3rd constructor


#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10   20
b = c1(30) #Error
c = c1() #Error

#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor :  10 20
b = c1(30) #Two  argument  constructor : 30  200
c = c1()  #Two  argument  constructor : 100 200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1() #Constructor
print(a) #'__main__.f1' at address

# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1() #Function
print(a) #None


# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1() #Error
b = c1(25) #Function :25
print(b) #None

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
a = c1() #c1  class  of  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a=c1()
from prog9a import c1
b=c1()


'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1()
b=prog9a.c1()