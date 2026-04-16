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

from prog10a import Rat
a = Rat(1, 2)
b = Rat(3, 4)
c = Rat(5, 6)
d = a + b
print(d)
d = a - b
print(d)
d = a * b
print(d)
d = a / b
print(d)



'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from prog10a import rat
a = [rat() for i in range(6)]
print("Enter First Rational Number")
a[0].get()
print("Enter Second Rational Number")
a[1].get()
a[2].add(a[0], a[1])   # sum
a[3].sub(a[0], a[1])   # difference
a[4].mul(a[0], a[1])   # product
a[5].div(a[0], a[1])   # division
print("Sum:", a[2])
print("Difference:", a[3])
print("Product:", a[4])
if a[1].nr != 0:
    print("Division:", a[5])
else:
    print("Division is not permitted")


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
Hyd
Sec
Cyb'''



# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1 # Hyd <nextline> Sec <nextline> Cyb
print()
importlib . reload(mod1) #  # Hyd <nextline> Sec <nextline> Cyb
print()
importlib . reload(mod1)  # Hyd <nextline> Sec <nextline> Cyb
importlib . reload('mod1') # Error due to arg should be module but bot string module
reload(mod1)











#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # ['argv', 'exit', 'path',  ...]
print()
print()
print(dir(time)) # ['time', 'sleep',  ...]
print()
print(dir(math)) # ['sqrt', 'pow', 'ceil', 'floor',...]




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
print(dir()) # 
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__',
 'c1', 'disp', 'x']'''
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_'>





'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''


import cal
a = []
for name in dir(cal):
    if not (name.startswith('_') and name.endswith('_')):
        a.append(name)
print(a)





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
    
    
    
    
    
#['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']












#  Find  outputs
print(dir()) 
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__']'''
print()
import  cal
print()
print(dir())
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__', 'cal']'''



#  Find  outputs
print(dir()) 
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__']'''
print()
from  cal  import  *
print()
print(dir())
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__',
 'add', 'sub', 'mul', 'div', 'c1', 'x', 'y']'''





#  Find  outputs
print(dir())
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__']'''
print()
from  cal  import  add , mul , x
print()
print(dir())
'''['__builtins__', '__cached__', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__',
 'add', 'mul', 'x']'''

# sys . path  demo   program
import  sys
print('Original  sys.path')  # Original  sys.path
for  x  in   sys . path:
	print(x)  # path , path , path
print(len(sys . path))
import  cal




# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
print(len(sys.path))  #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append(r"C:\sairam")    #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))        #How  to  print  number  of  directories  (or)  folders  in  sys.path
print(sample.x)   #How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()   #How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
obj = sample.c1()
obj.m1()#How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder