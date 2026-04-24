# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

# output :
 Hyd
Sec
Cyb


#-------------------

# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

# output : 

Hyd
Sec
Cyb

#-----------------------

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)

# output : 
Hyd
Sec
Cyb

Hyd
Sec
Cyb

Hyd
Sec
Cyb

#----------------------------

# #  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

# output :: 
['__doc__', '__name__', 'asctime', 'ctime', 'sleep',
 'localtime', 'time', 'strftime', ...]

['__doc__', '__name__', 'ceil', 'floor', 'sqrt',
 'factorial', 'pi', 'e', 'sin', 'cos', 'tan', ...]

#-------------------------------------

#  Find  outputs  (Home  work)
import  cal
print(dir(cal))

#output : 
['__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__',
 'add', 'x']

#----------------------------------

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

# output : 

['__builtins__', '__name__', 'c1', 'disp', 'x']
<class 'list'>
<class 'builtin_function_or_method'>

#------------------------------------------

Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables

# output ; 
import cal

a = []

for name in dir(cal):
    if not (name.startswith('__') and name.endswith('__')):
        a.append(name)

print(a)

#-----------------------------------
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

# output : 

['add', 'sub', 'mul', 'div', 'c1', 'x', 'y']

#-------------------------------------

#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())

# output : 

['__builtins__', '__name__']


['__builtins__', '__name__', 'cal']


#--------------------------------------

#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())

# output : 

['__builtins__', '__name__']

['__builtins__', '__name__', 'add', 'sub', 'mul', 'div', 'c1', 'x', 'y']

#--------------------------------------

#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())

# output : 

['__builtins__', '__name__']

['__builtins__', '__name__', 'add', 'mul', 'x']

# ------------------------------------

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal

# output : 

Original sys.path

#-----------------------------------

# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

# output : 

import sys

#  Print number of directories in sys.path
print("Before append:", len(sys.path))

#Append c:\sairam to sys.path
sys.path.append(r"c:\sairam")

# Print number of directories again
print("After append:", len(sys.path))

# Import sample module
import sample

# Print object x
print("x =", sample.x)

#  Call function f1()
sample.f1()

#  Call method m1() of class c1
obj = sample.c1()
obj.m1()