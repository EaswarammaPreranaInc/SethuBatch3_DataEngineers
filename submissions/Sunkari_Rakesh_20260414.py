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

from prog10a import rat

a = rat()
b = rat()
c = rat()

a.get()
b.get()

c = rat()
c.add(a, b)
print('c  =  a  +  b  :  ' , c)

c = rat()
c.sub(a, b)
print('c  =  a  -  b  :  ' , c)

c = rat()
c.mul(a, b)
print('c  =  a  *  b  :  ' , c)

c = rat()
if b.nr != 0:
	c.div(a, b)
	print('c  =  a  /  b  :  ' , c)
else:
	print('Division  is  not  possible  (b  is  0)')








Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
#program

 




# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

#output

Hyd
Sec
Cyb
Hyd
Sec
Cyb


 # Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

#output
Hyd
Sec
Cyb


 # reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1') # error bec the arguement is string
reload(mod1) # error bec it searches in current module

# output
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
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

# output
methods, classes and objects of sys module & also envirnment variables

Methods, classes and objects of time module & also envirnment variables

Methods< classes and abjects of math module & also envirnment variables




 #  Find  outputs  (Home  work)
import  cal
print(dir(cal))

# methods, classes and objects of cal class



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

# output
methods of current module




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

# output
Hyd
Sec
Cyb

 ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']






 #  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())

# output
 methods, classes and objects of current module
 
 
 methods, classes and objects of cal module



 #  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())

# output
 
 methods, classes and objects of current module


  methods, classes and objects of cal module i.e  ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
 
 

 #  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())

# output
 
methods, classes and objects of current module
 
['add','mul','x']





 # sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal

# output

 Original  sys.path

Hyd
sec
Cyb

 # Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys.path

print(dir(sys.path))  #How  to  print  number  of  directories  (or)  folders  in  sys.path # 
How  to  append  c:\sairam  folder  to  sys.path # sys.path.append("c.\\sairam")
How  to  print  number  of  directories  (or)  folders  in  sys.path # dir(sys.path)
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder # c:\sairam.x

import sample
sample.f1()  # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder # c:\sairam.f1()
object=class:
object.method1()  # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder # 

