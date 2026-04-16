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
###############################################################################################
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
###############################################################################################
# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')
###############################################################################################
# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1#Hyd Sec Cyb
###############################################################################################
# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1#
print()
importlib . reload(mod1)#mod1 statements are executes
print()
importlib . reload(mod1)#mod1 statements are executes
importlib . reload('mod1')#error bcz argument should not be a string
reload(mod1)#error
###############################################################################################
#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))#prints list all the members of sys module in the form of strings 
print()
print()
print(dir(time))#prints list all the members of time module in the form of strings
print()
print(dir(math))#prints list all the members of math module in the form of strings
###############################################################################################
#  Find  outputs  (Home  work)
import  cal
print(dir(cal))#returns the list of all members of a cal module in the form of strings
###############################################################################################
#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir()))#<class 'list'>
print(type(dir))#returns the module name
###############################################################################################
'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  --->  True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a = []
for i in dir(cal):
    if not i.startswith('__'):
        a.append(i)

print(a)
###############################################################################################
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
###############################################################################################
#  Find  outputs
print(dir())#returns list of all the members of current  module in form of strings 
print()#newline
import  cal
print()
print(dir())#returns list of all the members of cal module in form of strings

###############################################################################################
#  Find  outputs
print(dir())#prints list of all members of current module 
print()
from  cal  import  *
print()
print(dir())#prints list of all members,functions,classes,objects of cal module 
###############################################################################################
print(dir())#prints list of all members of current module 
print()
from  cal  import  add , mul , x
print()
print(dir())#prints list of all members,functions,classes,objects of cal module 
###############################################################################################
# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal
###############################################################################################
'''# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder'''

import sys

# 1) Print number of directories in sys.path
print("Before appending:", len(sys.path))

# 2) Append c:\sairam to sys.path
sys.path.append("c:\\sairam")

# 3) Print number of directories again
print("After appending:", len(sys.path))

# 4) Import sample module
import sample

# 5) Print object 'x'
print("Value of x:", sample.x)

# 6) Call function f1()
sample.f1()

# 7) Call method m1() of class c1
obj = sample.c1()
obj.m1()