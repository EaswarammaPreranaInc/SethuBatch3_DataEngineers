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

# prog10a code
import  math
class  rat:
	def  get(self):  #  Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self): #  Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def  __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  __add__(a , b):  #  Modify  the  method
		c = rat()
		c.nr = a . nr * b . dr + a . dr * b . nr
		c.dr = a . dr * b . dr
		c.simplify()
		return c
	def  __sub__(a , b):   #  Modify  the  method
		d = rat()
		d. nr = a . nr * b . dr - a . dr * b . nr
		d. dr = a . dr * b . dr
		d. simplify()
		return d
	def  __mul__(a , b):   #  Modify  the  method
		e = rat()
		e. nr = a . nr * b . nr
		e. dr = a . dr * b . dr
		e. simplify()
		return e
	def  __truediv__(a , b):   #  Modify  the  method
		f = rat()
		f. nr = a . nr * b . dr
		f. dr = a . dr * b . nr
		f. simplify()
		return f
	def   simplify(self):   #  Do  not  modify  the  method
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

#..............................................................................................>


# prog10c code
from prog3a import *
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

Output:
Enter  numerator : 2
Enter  denominator : 3
Enter  numerator : 5
Enter  denominator : 9
Sum :  11 / 9      
Difference :  1 / 9
Product :  10 / 27 
Division  :  6 / 5 

Enter  numerator : 2
Enter  denominator : 3
Enter  numerator : 0
Enter  denominator : 9
Sum :  2 / 3
Difference :  2 / 3
Product :  0 / 27
Division is not permitted

#..............................................................................................>


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
# Code:
from prog3a import *
a = []
a.append(rat())
a.append(rat())
a[0].get()
a[1].get()
a.append(a[0]+a[1])
a.append(a[0]-a[1])
a.append(a[0]*a[1])
a.append(a[0]/a[1])
print("Sum : ",a[2])
print("Difference : ",a[3])
print("Product : ",a[4])
if a[1].nr != 0:
	print('Division  : ' , a[5])
else:
	print('Division is not permitted.')

Output:
Enter  numerator : 2
Enter  denominator : 3
Enter  numerator : 5
Enter  denominator : 9
Sum :  11 / 9
Difference :  1 / 9
Product :  10 / 27
Division  :  6 / 5

Enter  numerator : 2
Enter  denominator : 3
Enter  numerator : 0
Enter  denominator : 9
Sum :  2 / 3
Difference :  2 / 3
Product :  0 / 27
Division is not permitted

#..............................................................................................>


# mod1.py  (Home  work)

print('Hyd')
print('Sec')
print('Cyb')
#print('India')
#print('USA')

#..............................................................................................>


# Find  outputs  (Home  work)

import  mod1
import  mod1
import  mod1


Output:
         Hyd
         Sec
         Cyb

#..............................................................................................>


# reload()  function  demo  program   (Home  work)

import    importlib
import  mod1 # Hyd <nextline> Sec <nextline> Cyb
print()
importlib . reload(mod1) # Hyd <nextline> Sec <nextline> Cyb
print()
importlib . reload(mod1) # Hyd <nextline> Sec <nextline> Cyb
importlib . reload('mod1') # Error because the argument to the reload() function should be a module but not a string
reload(mod1) # Error because there is no reload() function in current program

#..............................................................................................>


#  Find  outputs  (Home  work)

import  sys , time , math
print(dir(sys)) # All the members of the sys module that is objects,functions and classes also environment in sys module
print()
print()
print(dir(time)) # All the members of the time module that is objects,functions and classes also environment in time module
print()
print(dir(math))  # All the members of the math module that is objects,functions and classes also environment in math module

#..............................................................................................>


#  Find  outputs  (Home  work)

import  cal
print(dir(cal)) # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#..............................................................................................>


#  Find  outputs  (Home  work)

x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) # ['x' , 'disp' , 'c1']
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'function'>

#..............................................................................................>


'''
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



# Code :
from cal import *
list = dir()
a = []
for x in list:
    if x.startswith('__') and x.endswith('__'):
        continue
    else:
        a.append(x)
print(a)

''' Output:
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''

#..............................................................................................>


#  Find  outputs

print(dir()) # []
print()
import  cal
print()
print(dir()) # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#..............................................................................................>


#  Find  outputs

print(dir()) # []
print()
from  cal  import  *
print()
print(dir()) # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#..............................................................................................>


#  Find  outputs

print(dir()) # []
print()
from  cal  import  add , mul , x
print()
print(dir()) # ['x' , 'add' , 'mul']

#..............................................................................................>


# sys . path  demo   program
import  sys
print('Original  sys.path') 
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal

''' Outputs:
Original  sys.path
for loop is executed 6 times
6
'''

#..............................................................................................>


# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)

import sys
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') # How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x) # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
print(sample.f1()) # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = sample.c1() 
a.m1() # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

#..............................................................................................>