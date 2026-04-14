1) Repeat  prog10a  with  3  objects

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
import  math
class  rat:
	def  get(self):  
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self):
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def  __str__(self):  
		return  F'{self . nr} / {self . dr}'
	def  __add__(a , b): 
		c = rat()
		c.nr = a . nr * b . dr + a . dr * b . nr
		c.dr = a . dr * b . dr
		c.simplify()
		return c
	def  __sub__(a , b):   
		d = rat()
		d. nr = a . nr * b . dr - a . dr * b . nr
		d. dr = a . dr * b . dr
		d. simplify()
		return d
	def  __mul__(a , b):   
		e = rat()
		e. nr = a . nr * b . nr
		e. dr = a . dr * b . dr
		e. simplify()
		return e
	def  __truediv__(a , b): 
		f = rat()
		f. nr = a . nr * b . dr
		f. dr = a . dr * b . nr
		f. simplify()
		return f
	def   simplify(self):  
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
if __name__ == "__main__":
	a = rat()
	b = rat()
	a . get()
	b . get()
	print('Sum :  ' , a+b)
	print('Difference :  ' , a-b)
	print('Product :  ' ,  a*b)
	if b.nr != 0:
		print('Division  : ' , a/b)
	else:
		print('Division is not permitted.')

#from prog3a import *
a = rat()
b = rat()
a.get()
b.get()
c = a + b
print("Sum : ",c)
c = a - b
print("Difference : ",c)
c = a * b
print("Product : ",c)
if b.nr != 0:
	print('Division  : ' , a/b)
else:
	print('Division is not permitted.')


2) Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
#from prog10a import Rat


a = []

for i in range(6):
    n = int(input("Enter numerator: "))
    d = int(input("Enter denominator: "))
    obj = Rat(n, d)
    a.append(obj)

for i in range(6):
    print(f"a[{i}] =", a[i])

for i in range(5):
    print(f"\nBetween a[{i}] and a[{i+1}]:")

    c = a[i] + a[i+1]
    print(c)
    c = a[i] - a[i+1]
    print(c)
    c = a[i] * a[i+1]

3) mod1.py  
print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')
--> outputs  
import  mod1
import  mod1
import  mod1
#Hyd
 Sec
 Cyb

4) reload()  function  demo  program   
import    importlib
import  mod1
print()
importlib . reload(mod1)#Hyd
			 Sec
			 Cyb
print()
importlib . reload(mod1)#Hyd
			 Sec
			 Cyb
print()
importlib . reload('mod1')#Error because it is not valid
reload(mod1)

5) outputs  
import  sys , time , math
print(dir(sys))#Give all the members of sys module alongwith environment variables in the form list
print()
print()
print(dir(time))#Give all the members of time module alongwith environment variables in the form list
print()
print(dir(math))#Give all the members of math module alongwith environment variables in the form list

6) outputs  
import  cal
print(dir(cal))#['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

7) outputs  
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) # ['x' , 'disp' , 'c1']
print(type(dir()))# <class 'list'>
print(type(dir))# <class 'function'>

8) Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
9) cal.py
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

#from cal import *
list = dir()
a = []
for x in list:
    if x.startswith('__') and x.endswith('__'):
        continue
    else:
        a.append(x)
print(a)

['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

10) outputs
print(dir())#[]
print()
import  cal
print()
print(dir())#['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

11) outputs
print(dir())#[]
print()
from  cal  import  *
print()
print(dir())#['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

12) outputs
print(dir())#[]
print()
from  cal  import  add , mul , x
print()
print(dir())#['x', 'add', 'mul']

13) sys . path  demo   program
import  sys
print('Original  sys.path')#Original sys.path ...
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal

14) Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed 
import sys
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) #How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x) # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
print(sample.f1()) # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = sample.c1() 
a.m1() # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder