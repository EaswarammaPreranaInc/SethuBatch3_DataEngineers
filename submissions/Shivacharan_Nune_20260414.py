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
import prog10a
a=prog10a.rat()
b=prog10a.rat()
c=prog10a.rat()
a.get()
b.get()
c.add(a,b)
print(c.__str__())
c.sub(a,b)
print(c.__str__())
c.mul(a,b)
print(c.__str__())
c.div(a,b)
if  c.dr!=0:
	print(c.__str__())
else:
	print('Division  is  not  permitted')


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

import prog10a
a=[]
for i in range(6):
	a[i]=prog10a.Rat()
	a.append(a[i])
a[0].get()
a[1].get()
a[2].add(a,b)
a[3].sub(a,b)
a[4].mul(a,b)
a[5].div(a,b)
print(a[2].__str__())
print(a[3].__str__())
print(a[4].__str__())
if  a[5].dr!=0:
	print(a[5].__str__())
else:
	print('Division  is  not  permitted')



# mod1.py  (Home  work)
print('Hyd')  #Hyd
print('Sec')   #Sec
print('Cyb')  #Cyb
#print('India')  #India
#print('USA')  #USA


# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1
'''
Hyd
Sec
Cyb
India
USA
'''


# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')  #error-argument is modulename, not string module 
reload(mod1)  #error-current program dooesnt have reload function nor we have mentioned importlib.reload() 

'''
Hyd
Sec
Cyb
India
USA

Hyd
Sec
Cyb
India
USA

Hyd
Sec
Cyb
India
USA
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
all the members of sys module and environment variables

all the members of time module and environment variables

all the members of math module and environment variables
'''

#  Find  outputs  (Home  work)
import  cal
print(dir(cal))  #all the members of cal module and environment variables


#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())  #['disp','c1','x'] and environment variables
print(type(dir()))  #<class 'list'>
print(type(dir))  #<class 'function'>


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  --->  True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a=[]
for x in dir(cal):
	if x.startswith('__') and x.endswith('__'):
		continue
	a.append(x)
print(a)


#  Find  outputs
print(dir())  #all members of current module(0) and environment variables
print()
import  cal
print()
print(dir()) #all environment variables along with cal


#  Find  outputs
print(dir())  #list of environment variables
print()
from  cal  import  * 
print()
print(dir())  #list of environment variables along with members of cal module


#  Find  outputs
print(dir()) #list of environment variables
print()
from  cal  import  add , mul , x
print()
print(dir())  #list of environment variables along with add,mul,x


# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal

'''
Original  sys.path
list of all directories-current directory,....
6

'''

# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
print(len(sys.path))
sys.path.append('D:\\Python\\practice1.py')
print(len(sys.path))
import sairam
print(sairam.x)
sairam.f1()
a=sairam.c1()
a.m1()