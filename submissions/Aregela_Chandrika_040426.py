# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25 <nextLine> 10.8 <nextLine> Hyd
for  x  in  f1():
	print(x) # stopIteration Error
for  x  in  f1():
	print(x) # stopIteration Error
    
    
    
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0,1,4,9,16]
print(type(l)) # <class 'List'>

s = {x * x   for   x   in   range(5)}
print(s) # {0,1,4,9,16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # Address
print(type(g)) # <class 'generator'>




#  Find  outputs (Home  work)
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1()) # 10
print(f1()) # 10
print(f1()) # 10
print()
g = f2()  # creates empty generator object
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30 
print(next(g)) # stopIteration Error



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''


def opr(a, b):
    yield f"Sum: {a + b}"
    yield f"Subtraction: {a - b}"
    yield f"Multiplication: {a * b}"
    
    if b != 0:
        yield f"Division: {a / b}"
    else:
        yield "Division is not permitted"
a = int(input("a:"))
b = int(input("b:"))
g = opr(a,b)
for i in g:
    print(i)





'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''


import time
def opr(a, b):
    while a <= b:
        yield a
        a += 1  
        time.sleep(1)

a = int(input("a: "))
b = int(input("b: "))

g = opr(a, b)

for num in g:
    print(num)




'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''

def fib(x):
    a,b = 0,1
    count = 0 
    
    while count < x:
        yield a 
        a,b = b,a+b  
        count += 1
x = int(input("a :"))
for n in fib(x):
    print(n)

 


'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
    
    
def gen(s):
    for i in 



w = input("enter : ")    
    
    
# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))
    
    
'''[10, 20]
<class 'list'>

{40, 50, 30}
<class 'set'>

(60, 70, 80, 90)
<class 'tuple'>

100
<class 'int'>'''
    
    
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # execution time for stmt
print(timeit('( x * x   for  x  in  range(500) )')) # execution time for stmt




# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # size in bytes
print(sys . getsizeof(gen)) # # size in bytes