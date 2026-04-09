
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

'''
output
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   11  /  15
c  :   22  /  7
a  :   3.8  /  4.6
SyntaxError
TypeError
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

output
c1 class constructor
TypeError: __init__() should return None, not 'int'




# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()

output
Constructor
Constructor
Constructor
Constructor
...
RecursionError: maximum recursion depth exceeded


Creating object inside __init__() of same class = infinite recursion




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

output
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}

'''
Object 'a' ---> {'x': 10, 'y': 20}
Object 'b' ---> {'x': 30, 'y': 40}
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


output
{'a': 10}
{'a': 10, 'b': 20}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
{'a': 10}

'''
object 'x' ---> {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

object 'z' ---> {'a': 10}

object 'y' ---> {}
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

output
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}
AttributeError: 'c1' object has no attribute 'x'


'''
Object 'a' ---> {'y': 20, 'z': 30}

Object 'b' ---> {'x': 10, 'z': 30}'''




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

output
3rd constructor


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

output
Two argument constructor :  10 20
TypeError: __init__() missing 1 required positional argument: 'y'
NOT EXECUTED





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

output
Two argument constructor :  10 20
Two argument constructor :  30 200
Two argument constructor :  100 200


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

output
Constructor
<__main__.f1 object at 0x...>



# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)

output
Function
None




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

output
TypeError: c1() missing 1 required positional argument: 'x'



#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()

output
Local class c1 is overridden by imported c1.
So constructor of prog9a.c1 is executed.



#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')


output
Imported class overrides local class.
So constructor of prog9a.c1 is executed.





#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()


output
c1 class of prog9a



'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a = c1()  #How  to  create  c1  class  object  of  current  module
b = p.c1()  #How  to  create  c1  class  object  of  prog9a












