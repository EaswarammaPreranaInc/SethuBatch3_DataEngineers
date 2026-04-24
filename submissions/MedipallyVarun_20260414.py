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
from Waste import rat
a = rat()
b = rat()
c = rat()
a.get()
b.get()
c = a+b
print(c)
c = a-b
print(c)
c = a*b
print(c)
c = a/b
print(c)




'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
a = []
for i in range(6):
    b = rat()
    a.append(b)
c = []
i = 0
while i < len(a):
    if i < 2:
        a[i].get()
        i+=1
        c.append(a[i])
    elif i == 2:
        a[i] = (a[0]+a[1])
        i+=1
    elif i == 3:
        a[i] = (a[0]-a[1])
        i+=1
    elif i == 4:
        a[i] = (a[0]*a[1])
        i+=1
    elif i == 5:
        a[i] = (a[0]/a[1])
        i+=1

for x in a:
    print(x)



# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')
'''
Hyd
Sec
Cyb'''


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
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')#error-mod1 in strings
reload(mod1)#error-no importlib
'''
Hyd 
Sec
Cyb

Hyd 
Sec
Cyb

Hyd 
Sec
Cyb
'''

#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))
'''
[functions,environment variables, objects , classes] of sys module

[functions,environment variables, objects , classes] of time module

[functions,environment variables, objects , classes] of math module
'''


#  Find  outputs  (Home  work)
import  cal
print(dir(cal))
'''
[x,y,add,sub,__mul__,__div__,__c1__]
'''




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
[x,disp,c1,environment variable]
<class 'list'>
<class 'function'>
'''



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
members = dir(cal)
for item in members:
    if not (item.startswith('__') or item.endswith('__')):
        a.append(item)
print(a)


#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())
'''
[functions,classes,objects,environment variables] of current module


[functions,classes,objects,environment variables] of current module and cal module'''




#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())
'''
[functions, classes, objects, environmental variable] of current module


[functions,classes,objects,environmental variables]of current module and also of cal modules if there are no same names'''


#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())
'''
[functions,objects,classes, environmental variables] of current module


[functions,objects,classes, environmental variables,add,mul,x]
'''



# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal
'''
Original sys.path
path of cwd
path of python313.zip
path of DLLs
path of Lib
path of Python313
path of site-packages
path of site-packages
7
'''



# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
for x in sys.path:
        print(x)#How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam')#How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))#How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
#import sys.path[3] 
print(sample.x)#How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()#How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = sample.c1()
a.m1()#How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder