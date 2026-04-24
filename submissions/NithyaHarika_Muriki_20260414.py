# mod1.py  (Home  work)
print('Hyd')#Hyd
print('Sec')#Sec
print('Cyb')#Cyb
#print('India')#India
#print('USA')#USA


# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
#Hyd
#Sec
#Cyb
#India
#USA


# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)
Hyd
Sec
Cyb

Hyd
Sec
Cyb

Hyd
Sec
Cyb

#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))#returns list of directories in the form of strings
print()
print()
print(dir(time))#all the members of the module
print()
print(dir(math))#returns list of directories in the form of strings



#  Find  outputs  (Home  work)
import  cal
print(dir(cal))


#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#prints all members objects and functions
print(type(dir))#function
print(type(dir()))#list


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

import cal
a = dir(cal)
b=[]

for x in a :
    if x.startswith("__") and x.endswith("__"):
        pass
    else:
        b.append(x)
print(b)

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



#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())

#  Find  outputs
print(dir())#prints modules
print()
from  cal  import  *
print()
print(dir())#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']


#  Find  outputs
print(dir())#prints modules
print()
from  cal  import  add , mul , x
print()
print(dir())

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)#list of all those directories present 
print(len(sys . path))
import  cal


# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)#list of all those directories present 
print(len(sys . path))

sys.path.append(r"c:/Sairam")

print(len(sys))

for  x  in   sys . path:
	print(x)

import sample

print(sample.x)
sample.f1()
a = sample.c1()
a.m1()