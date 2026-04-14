'''
Repeat  prog10a  with  3  objects
Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c
Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''
from prog10a import Rat   # Import the class

# Create only 3 objects
a = Rat()
b = Rat()
c = Rat()

# Input
print("Enter Rational Number A")
a.get()

print("\nEnter Rational Number B")
b.get()

# Addition
c.add(a, b)
print("\nSum =", c)

# Subtraction
c.sub(a, b)
print("Difference =", c)

# Multiplication
c.mul(a, b)
print("Product =", c)

# Division
if b.num != 0:
    c.div(a, b)
    print("Division =", c)
else:
    print("Division is not permitted")

'''
Repeat  prog10a  with  list  of  6  objects
Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from prog10a import Rat   # Import class

# Create list of 6 objects
a = [Rat() for i in range(6)]

# Input
print("Enter Rational Number A")
a[0].get()

print("\nEnter Rational Number B")
a[1].get()

# Operations
a[2].add(a[0], a[1])   # Sum
a[3].sub(a[0], a[1])   # Difference
a[4].mul(a[0], a[1])   # Product

# Output
print("\nSum =", a[2])
print("Difference =", a[3])
print("Product =", a[4])

# Division
if a[1].num != 0:
    a[5].div(a[0], a[1])
    print("Division =", a[5])
else:
    print("Division is not permitted")






# mod1.py  (Home  work)
print('Hyd')#Hyd
print('Sec')#Sec
print('Cyb')#Cyb
#print('India')
#print('USA')



# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1#imported mod1 only once



# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1 #mod1 executes for the first time
print()
importlib . reload(mod1)#mod1 executes again
print()
importlib . reload(mod1)#mod1 executes again
importlib . reload('mod1')#error reload args should be module 
reload(mod1)#error reload is not defined



#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))#prints all attrinutes present in sys directory
print()
print()
print(dir(time))#prints all attrinutes present in time directory
print()
print(dir(math))##prints all attrinutes present in math directory




#  Find  outputs  (Home  work)
import  cal
print(dir(cal))##prints all attrinutes present in cal directory



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())
print(type(dir()))
print(type(dir))
'''
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'traceback', 'x']
<class 'list'>
<class 'builtin_function_or_method'>
'''


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True
2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True
3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False
4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''



# cal.py
def  add(a , b):
	return  a + b
def  sub(a , b):
	return  a - b
def  mul(a , b):
	return  a * b
def  div(a , b):
	return  a / b
class    c1:
	def    m1(self):
		pass
#End  of  the  class
x = 100
y = 200
if  _name_   ==  '_main_':
	print('Hyd')
	print('Sec')
	print('Cyb')
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''
Hyd
Sec
Cyb
'''



#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__']
(after importing cal)
['__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'cal']
'''


#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())
'''
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
after importing 
['__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__',
 'cal', 'add', 'sub', 'mul', 'div', 'c1', 'x', 'y']



#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())
'''
(befor imporing)['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
(after importing)['__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'add', 'mul', 'x']




# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal
'''
Original sys.path
/path/to/current/directory
/usr/lib/python3.x
/usr/lib/python3.x/lib-dynload
/usr/local/lib/python3.x/site-packages
...





# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)

How  to  print  number  of  directories  (or)  folders  in  sys.path  #answer here
import sys
print(len(sys.path))

How  to  append  c:\sairam  folder  to  sys.path
sys.path.append(r'c:\sairam')

How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys.path))

How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
import sample
print(sample.x)

How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
sample.f1()

How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
obj = sample.c1()
obj.m1()