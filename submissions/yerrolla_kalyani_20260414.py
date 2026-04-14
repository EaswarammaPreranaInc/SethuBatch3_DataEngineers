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
from prog10a import *
a=Rat()
b=Rat()
a.get()
b.get()
c=Rat()
c.add(a,b)
print(c)
c.sub(a,b)
print(c)
c.mul(a,b)
print(c)
if  c.div(a,b):
	print(c)#How  to  print  object  'f
else:
	print('Division  is  not  permitted')

'''
Repeat  prog10a  with  list  of  6  objects
Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5] '''
from prog10a import *
a=[Rat(),Rat(),Rat(),Rat(),Rat(),Rat()]
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
a[5].div(a[0],a[1])
print(a[2])
print(a[3])
print(a[4])
if a[1].nr != 0:
    print(a[5])
else:
    print("Division is not permitted")


# mod1.py  (Home  work)
print('Hyd')#Hyd
print('Sec')#Sec
print('Cyb')#Cyd
print('India')#India
print('USA')#USA


# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
# out puts :=
# Hyd
# Sec
# Cyd
# India



# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1 #<nxtline>#Hyd<nxt>Sec<nxt>Cyd<nxt>India
print()#nothing is printed 
importlib . reload(mod1)#Hyd<nxt>Sec<nxt>Cyd<nxt>Indi
print()#nothing is printed
importlib . reload(mod1)#Hyd<nxt>Sec<nxt>Cyd<nxt>Indi
importlib . reload('mod1')#error due to reload takes only mod1 but not 'mod1'
reload(mod1)#error because the module importlib is imports but not the members of the module importlib are imported 



#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))#list of all the members of the sys module and environment variables [............]
print()#nothing 
print()#nothing
print(dir(time))#list of all the members of the time module and environment variables [............]
print()#nothing
print(dir(math))#list of all the members of the math module and environment variables [............]



#  Find  outputs  (Home  work)
import  cal
print(dir(cal))#list of environment variables and the members of the cal module[ '__name__', '__package__', ...., 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']


#Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#list of members and environment variable ofthe current module in alphabeic order [x,disp,c1,m1,__name__,__package__,......] 
print(type(dir()))#<class 'list'>
print(type(dir))#<class 'function'>




'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True
2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True
3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False
4) a = []
Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

import cal
from cal import *
obj=dir(cal)
a=[]
for x in a :
    if x.startswith('__'):
           pass
    elif  x.endswith('__'):
           pass
    else:
           a.append(x)
print(a)
           

cal.py
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



['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']





 #  Find  outputs
print(dir())#<class'list'>
print()#nothing is printed
import  cal
print()#nothing is printed
print(dir())#list of environment variables and the members of the cal module[ '__name__', '__package__', ...., 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

 #  Find  outputs
print(dir())#list of current module members and environmental variables 
print()#nothing 
from  cal  import  *
print()#nothing 
print(dir())#list of current module members,cal module members  and environmental variables 





#  Find  outputs
print(dir())#list of current module members and environmental variables  
print()#nothing is printed 
from  cal  import  add , mul , x
print()#nothing is printed
print(dir())#list of current module members,cal module members which are add ,mul,x only not all members ,  and environmental variables  



 # sys . path  demo   program
import  sys
print('Original  sys.path')#Original  sys.path
for  x  in   sys . path:
	print(x)#directories of the sys.path module 
print(len(sys . path))#6
import  cal



# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
# How  to  print  number  of  directories  (or)  folders  in  sys.path
# How  to  append  c:\sairam  folder  to  sys.path
# How  to  print  number  of  directories  (or)  folders  in  sys.path
# How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
# How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
# How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder


import sys
import sample 
print(len(sys.path))#How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append("c:\\sairam")#How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))# How  to  print  number  of  directories  (or)  folders  in  sys.path
print(sample.x)# How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()# How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1()# How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder