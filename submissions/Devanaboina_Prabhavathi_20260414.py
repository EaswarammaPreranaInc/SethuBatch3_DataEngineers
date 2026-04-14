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

# Importing Rational class from prog10a

from Devanaboina_prabhavathi_20260413 import Rational
a = Rational()
b = Rational()
print("Enter First Rational Number:")
a.get()
print("Enter Second Rational Number:")
b.get()
c = a + b
print("Sum:", c)
c = a - b
print("Difference:", c)
c = a * b
print("Product:", c)
c = a / b
if c is not None:
    print("Division:", c)




'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from Devanaboina_prabhavathi_20260413 import Rational
a = [Rational() for _ in range(6)]

for i in range(6):
    print("Enter Rational Number", i+1)
    a[i].get()
for i in range(0, 6, 2):
    print("\n a[", i, "] =", a[i])
    print("a[", i+1, "] =", a[i+1])

    c = a[i] + a[i+1]
    print("Sum =", c)

    c = a[i] - a[i+1]
    print("Difference =", c)

    c = a[i] * a[i+1]
    print("Product =", c)

    c = a[i] / a[i+1]
    if c != None:
        print("Division =", c)


# mod1.py  (Home  work)
print('Hyd') # Hyd
print('Sec') # Sec
print('Cyb') # Cyb
#print('India') # India
#print('USA') # USA



# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

#print("Hello from mod1")


# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1) # error
print()
importlib . reload(mod1) # error
importlib . reload('mod1') # error
reload(mod1)


#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys)) # true
print()
print()
print(dir(time)) #
print()
print(dir(math)) 



#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) # cal



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello') # Hello
class  c1:
        def  m1(self): 
                pass
print(dir()) # x
print(type(dir())) 
print(type(dir)) # builtin


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

for x in dir(cal):
    # skip environment variables (dunder names)
    if not (x.startswith('__') and x.endswith('__')):
        a.append(x)

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
if  __name__   ==  '__main__':
	print('Hyd') # Hyd
	print('Sec') # Sec
	print('Cyb') # Cyb
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']




#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())




# sys . path  demo   program
import  sys
print('Original  sys.path') #Original  sys.path
for  x  in   sys . path:
	print(x)
print(len(sys . path)) # 8
import  cal



# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder


x = 100

def f1():
    print("Hello from f1")

class c1:
    def m1(self):
        print("Hello from m1")