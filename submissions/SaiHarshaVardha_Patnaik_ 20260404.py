# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25 , 10.8 , 'Hyd'
for  x  in  f1():
	print(x) # 25 , 10.8 , 'Hyd'
for  x  in  f1():
	print(x) # 25 , 10.8 , 'Hyd'

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0, 1, 4, 9, 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0, 1, 4, 9, 16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # <generator object <genexpr> at 0x...>
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
g = f2()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # StopIteration

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
import time
def  f1(a , b):
    yield  a + b
    yield  a - b
    yield  a * b
    yield  a / b
a = eval(input('Enter  first  number : '))
b = eval(input('Enter  second  number : '))
g = f1(a , b)
try:
    for  x  in  g:
        print(x)
        time.sleep(1)
except ZeroDivisionError:
    print ("division  by  zero  is  not  possible")

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
import  time
def  f1(x , y):
    while  x  <=  y:
        yield  x
        x += 1
# End  of  generator
x = eval(input('Enter  starting  number : '))
y = eval(input('Enter  ending  number : '))
g = f1(x , y)
for  z  in  g:
    print(z)
    time.sleep(1)
    
    
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
import  time
def  f1(x):
    a , b = 0 , 1
    while  a  <=  x:
        yield  a
        a , b = b , a + b
x = eval(input('Enter  the  limit : '))
g = f1(x)
for  z  in  g:
    print(z)
    time.sleep(1)
    
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import  time
def  f1(s):
    for  x  in  s.split():
        yield  x
s = input('Enter  a  string : ')
g = f1(s)
for  x  in  g:
    print(x)
    time.sleep(1)
    


# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x) # [10 , 20] , {30 , 40 , 50} , (60  , 70 , 80 , 90) , 100
	print(type(x)) # <class 'list'> , <class 'set'> , <class 'tuple'> , <class 'int'>

#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # 0.0001 
print(timeit('( x * x   for  x  in  range(500) )')) # 0.00002 

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # 800112
print(sys . getsizeof(gen)) # 112 



