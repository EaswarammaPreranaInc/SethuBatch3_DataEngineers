#1
'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  --->  True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal

print(dir(cal))

a = []

for x in dir(cal):
    if x.startswith('__') and x.endswith('__'):
        continue
    else:
        a.append(x)

print(a)


# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')


# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
'''
modules can be imported only ones
module mod1 and statements of the module both are imported
'''


# reload()  function  demo  program   (Home  work)
import importlib
import mod1 # Hyd <> Sec <> Cyb
print()
importlib . reload(mod1) # Hyd <> Sec <> Cyb
print()
importlib . reload(mod1) # Hyd <> Sec <> Cyb
importlib . reload('mod1') # error , argument of the reload function id module, not string module
reload(mod1) # error , reload function is searched in the current program


#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # members of sys module and environment variables are given in the form of list of strings
print()
print()
print(dir(time)) # members of time module and environment variables are given in the form of list of strings
print()
print(dir(math)) # members of math module and environment variables are given in the form of list of strings


#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) # members of cal module and environment variables are given in the form of list of strings


#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) # members of current module and environment variables are given in the form of list of strings
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>


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
if  __name__   ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')


# Find  outputs
print(dir()) # environment variables
print()
import  cal
print()
print(dir()) # environment variables and cal module


#  Find  outputs
print(dir()) # environment variables
print()
from  cal  import  *
print()
print(dir()) # environment variables and members of cal module


#  Find  outputs
print(dir()) # environment variables
print()
from  cal  import  add , mul , x
print()
print(dir()) # environment variables and members add , mul and x of cal module


# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x) # all the directories in sys . path are printed one by one
print(len(sys . path)) # 6
import  cal


# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') # How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x) # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample . f1() # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = sample.c1() 
a.m1() # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder