# mod1.py  (Home  work)
import math
import time
import sys
from cal import add, mul, x
import sys.path
import sys
from cal import *
import cal
import importlib
import mod1  # error
import mod1
print('Hyd')
print('Sec')
print('Cyb')
# print('India')
# print('USA')

# Find  outputs  (Home  work)

# reload()  function  demo  program   (Home  work)
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')  # errror
reload(mod1)  # error

'''
Hyd
Sec
Cyd
Hyd
Sec
Cyd
Hyd
Sec
Cyd
'''

#  Find  outputs  (Home  work)
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

#  Find  outputs  (Home  work)
print(dir(cal))  # x,y, ...

#  Find  outputs  (Home  work)
x = 25


def disp():
    print('Hello')


class c1:
    def m1(self):
        pass


print(dir())  # ['x', 'disp()', 'c1']
print(type(dir()))  # 'class <list>'
print(type(dir))

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

# cal.py


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


class c1:
    def m1(self):
        pass


# End  of  the  class
x = 100
y = 200
if __name__ == '_main_':
    print('Hyd')
    print('Sec')
    print('Cyb')

['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())
print()
print()
print(dir())


#  Find  outputs
print(dir())  # []
print()
print()
print(dir())  # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())
print()
print()
print(dir())  # ['add',',mul', 'x']

# sys . path  demo   program
print('Original  sys.path')
for x in sys . path:
    print(x)
print(len(sys . path))  # 6

# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
# How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys . path))
# How  to  append  c:\sairam  folder  to  sys.path
sys.path.append('c:\\sairam ')
# How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys . path))
print(x)  # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
f1()  # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
c1().m1()  # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder
