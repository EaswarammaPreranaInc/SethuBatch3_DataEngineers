'''
prog10a

Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers
1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division
2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted
3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero
import math
class Rat:
    def get(self):
        self.num = int(input('Enter numerator : '))
        self.den = int(input('Enter denominator : '))
        self.test()
    def test(self):
        while self.den == 0:
            print('Denominator cannot be zero, re-enter')
            self.den = int(input('Enter denominator : '))
    def __str__(self):
        return f'{self.num} / {self.den}'
    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g
    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()
    def div(self, a, b):
        if b.num == 0:
            self.num = 0
            self.den = 1
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a.get()
b.get()
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
if b.num != 0:
    f.div(a, b)
print('Sum :', c)
print('Difference :', d)
print('Product :', e)
if b.num != 0:
    print('Division :', f)
else:
    print('Division is not permitted')
'''

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
a = Rat()
b = Rat()

a.get()
b.get()

c = Rat()
c.add(a, b)
print('Sum :', c)

c = Rat()
c.sub(a, b)
print('Difference :', c)

c = Rat()
c.mul(a, b)
print('Product :', c)

c = Rat()
if b.num != 0:
    c.div(a, b)
    print('Division :', c)
else:
    print('Division is not permitted')

'''
Repeat  prog10a  with  list  of  6  objects
Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog10a import Rat  
a = [Rat() for i in range(6)]

a[0].get()
a[1].get()

a[2].add(a[0], a[1])   
a[3].sub(a[0], a[1])  
a[4].mul(a[0], a[1])  

if a[1].num != 0:
    a[5].div(a[0], a[1])

print('Sum :', a[2])
print('Difference :', a[3])
print('Product :', a[4])
if a[1].num != 0:
    print('Division :', a[5])
else:
    print('Division is not permitted')


# mod1.py  (Home  work)
print('Hyd')
print('Sec')
print('Cyb')
print('India')
print('USA')

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
importlib . reload('mod1') # Error because argument should be mod1
reload(mod1) # Error because reload is not import so it should be used with importlib
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

# Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print(dir(time))
print()
print(dir(math))
'''
[sys module list]

[time module list]

[math module list]
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
if  __name__  ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')

#  Find  outputs  (Home  work)
import  cal
print(dir(cal)) # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) # ['c1', 'disp', 'x']]
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True
2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True
3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False
4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
Output:['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''
import cal
a = []
for name in dir(cal):
    if not (name.startswith('_') and name.endswith('_')):
        a.append(name)
print(a)

#  Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print()
import  cal
print()
print(dir()) # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'cal']

#  Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir()) # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  add , mul , x
print()
print(dir()) # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']

# sys . path  demo   program
import  sys
print('Original  sys.path') # Original sys.path
for  x  in   sys . path:
	print(x) # different paths
print(len(sys . path)) # 5
import  cal

# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append(r'c:\sairam') # How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) # How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample 
print(sample.x) # How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1() # How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
obj = sample.c1()
obj.m1() # How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder