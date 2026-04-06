# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25 <nextline> 10.8 <nextline> Hyd
for  x  in  f1():
	print(x) # 25 <nextline> 10.8 <nextline> Hyd
for  x  in  f1():
	print(x) # 25 <nextline> 10.8 <nextline> Hyd 
	

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0,1,4,9,16]
print(type(l)) # <class List>

s = {x * x   for   x   in   range(5)}
print(s) # {0,1,4,9,16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0 : 0, 1 : 1, 2 : 4, 3 : 9, 4: 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # type and address of the generator 
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
print(f1()) #10
print(f1())#10
print(f1())#10
print()
g = f2()
print(next(g))#10
print(next(g))#20
print(next(g))#30
print(next(g))# stop iteration error

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
'''
import time 
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
def f1(a,b):
    try:
        yield "Sum : " ,a+b 
        yield "Diffenece : ", a-b 
        yield "Product : " ,a *b 
        yield "Division : ", a/b 
    except ZeroDivisionError:
         print('Division by zero is not permitted')

g = f1(a,b)
for name, values in g:
    print(f"{name} : {values}")
    time.sleep(1)
'''

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
'''
import time 
x = int(input('Enter start value : '))
y = int(input('Enter end value : '))
def f1():
    for i in range(x, y+1):
        yield i 
g = f1()
for x in g:
    print(x)
    time.sleep(1)
'''
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
'''
import time
n=int(input("Enter value of x:"))
def f1():
    a = 0
    b = 1 
    yield a 
    yield b 
    for i in range(n):
        c = a + b 
        if c > n:
            break
        yield c 
        a, b = b, a+b 
g = f1()
for x in g: 
    print(x)
	time.sleep(1)

'''
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
'''
n = input('Enter any string : ')
def f1():
    yield 'Words of the string'
    y = n.split(' ')
    for i in y:
        yield i 
g = f1()
for x in g : 
    print(x)
'''

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
[10,20]
<class 'list'>
{30, 40, 50}
<class 'set'>
60, 70, 80, 90
<class 'tuple'>
100
<class 'int'
'''

#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''
21.311505899997428
0.29068249999545515
'''

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
'''
85176
208
'''
