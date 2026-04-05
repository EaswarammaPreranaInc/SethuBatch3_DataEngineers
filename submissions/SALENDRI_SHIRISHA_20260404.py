# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)  # 25 <next line> 10.8 <next line> Hyd
for  x  in  f1():
	print(x)  # 25 <next line> 10.8 <next line> Hyd
for  x  in  f1():
	print(x)  # 25 <next line> 10.8 <next line> Hyd

	
	#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)  # [0 , 1 , 4 , 9 , 16]
print(type(l))  # <class 'list'>


s = {x * x   for   x   in   range(5)}
print(s)  # {0 , 1 , 4 , 9 , 16}
print(type(s))  # <class 'set'>


d = {x : x * x    for   x   in   range(5)}
print(d)  # {0 : 0 , 1 : 1 , 2 : 4 , 3 : 9 , 4 :16}
print(type(d))  # <class 'dict'>


g = (x * x   for   x   in   range(5))
print(g)  # 0
          # 1
          # 4
          # 9
          # 16
print(type(g))  # <class 'generator'>


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
print(f1())  # 10
print(f1())  # 10
print(f1())  # 10
print()  
g = f2()
print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30
#print(next(g))  # Error due to no elements in f2()


'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator

import time
time.sleep
def gen(a ,b):
    try:
        print('Sum')
        yield a + b
        time.sleep(1)
        print('Difference')
        yield a - b
        time.sleep(1)
        print('Product')
        yield a * b 
        time.sleep(1)
        print('Division')
        yield a / b
        time.sleep(1)
    except:
        ZeroDivisionError
        print('Division by Zero is not permitted')
a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
g = gen(a,b)
for x in g:
    print(x)
'''

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def gen(a,b):
    yield a
    yield b
g = gen(a,b)
for x in g:
    print(x)
    
def gen(a,b):
    yield a
    count = 0
    if a > 0:
        for x in a:
    count += 1
    yield b
a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
g = gen(a,b)
for x in g:
    print(x)

'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def gen():
    a,b = 0,1
    yield a
    yield b
    a,b = b,a+b
    yield b
    yield a+b
g = gen()
for x in g:
    print(x)

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def gen():
    

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
	
	
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))


