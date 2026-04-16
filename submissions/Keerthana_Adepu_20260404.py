# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)
'''
25
10.8
Hyd
25
10.8
Hyd
25
10.8
Hyd
'''


#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0 , 1 , 4 , 9 , 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0 , 1 , 4 , 9 , 16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0 : 0 , 1 : 1 , 2 : 4 , 3 : 9 , 4 : 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # type and address of the generator expression
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
print() # <next line>
g = f2()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # StopIteration Error


#1
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
def operations(a , b):
    print('sum')
    yield a + b
    print('difference')
    yield a - b
    print('product')
    yield a * b
    print('division')
    yield a / b

a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))

g = operations(a , b)

for x in g:
    print(x)

#2
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def range(x , y):
    while x <= y:
        yield x
        x += 1

x = int(input('Enter starting value:'))
y = int(input('Enter ending value:'))

g = range(x , y)

for x in g:
    print(x)


#3
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def fib(x):
    
    a , b = 0 , 1
    
    while a <= x:
            yield a
            a , b = b , a + b

x = int(input('Fibonacci series uptil:'))

g = fib(x)

for x in g:
    print(x)


#4
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def divs(s):
    s = s.split(' ')
    for x in s:
        yield x

s = input('Enter the string:')

g = divs(s)

for x in g:
    print(x)
    


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

'''
[10 , 20]
<class 'list'>
{30 , 40 , 50}
<class 'set'>
(10 , 20 , 30 , 40)
<class 'tuple'>
100
<class 'int'>
'''


#  Find  outputs
from  timeit  import timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # time it takes to exceute the list comprehenstion without exceuting it
print(timeit('( x * x   for  x  in  range(500) )')) # time it takes to exceute the generator expression without exceuting it


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)] 
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # size of list object in bytes
print(sys . getsizeof(gen)) # size of generator expression in bytes
