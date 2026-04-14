# mod1.py  (Home  work)
print('Hyd') #hyd
print('Sec')#sec
print('Cyb')#cyb
#print('India')#india
#print('USA')#usa
# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
 # reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print() 
#hyd
sec
cyb
importlib . reload(mod1)
print()
#hyd
sec
cyb
importlib . reload(mod1)
#hyd
sec
cyb
importlib . reload('mod1')#not allowd
reload(mod1)#error
 #  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()#['__name__','__argv__',....]
print()
print(dir(time))
print()#['time','sleep']
print(dir(math))#['sqrt','pi','sin']
 #  Find  outputs  (Home  work)
import  cal
print(dir(cal))#['add','c1','div','mul','sub','x','y']
#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#['c1','disp','x','__builtins__','__name__',...]
print(type(dir()))#<class'list'>
print(type(dir))#<class >

Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
 import cal
a=[ ]
for x in dir(cal):
      if not x.startswith('_'):
           a.append(x)
print(a)


1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
# cal.py
def  add(a , b):
	return  a + b #17
def  sub(a , b):
	return  a - b#3
def  mul(a , b):
	return  a * b#70
def  div(a , b):
	return  a / b#1.42
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
print()#['__name__','__builtins__',...]
import  cal
print() #['cal','__name__',....]
print(dir())
#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())#['add','sub','mul','div','c1','x','y']
#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())#['add','mul','x']
# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal
 # Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
How  to  print  number  of  directories  (or)  folders  in  sys.path
print("before append:)
print("number of folders=",len(sys.path))
How  to  append  c:\sairam  folder  to  sys.path
sys.path.append('c:\\sairam')
print("\n after append:")
print("number of folders=",len(sys.path))

import sample
print(\n value of x=",sample.x)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder