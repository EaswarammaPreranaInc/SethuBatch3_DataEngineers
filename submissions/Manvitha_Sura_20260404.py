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
print(l)  #type and address of list
print(type(l))  #<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)  #type and address of set
print(type(s))  #<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)  #type and address of dictionary
print(type(d))  #<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)  #type and address of generator
print(type(g))  #<class 'generator>




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
print(f1())  #10
print(f1())  #10
print(f1())  #10
print()  #<empty line>
g = f2()  #creates new empty generator
print(next(g))  #10
print(next(g))  #20
print(next(g))  #30
print(next(g))  #StopIteration error


'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def f1():
    yield 'Sum: ',a+b
    yield 'Difference: ',a-b
    yield 'Multiplication: ',a*b
    try:
        yield 'Division: ',a/b
    except:
        print('Division by zero is not permitted')
a=int(input('Enter first number'))
b=int(input('Enter second number'))
for x in f1():
    print(*x)


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

def f1(x):
        yield x-1
x=int(input('Enter start value'))
y=int(input('Enter end value'))
while x<=y:
    x+=1
    for z in f1(x):
        print(x-1)


'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''

def fib(x):
    yield x
x=int(input('Enter a number'))
if x<=0:
    print('Enter number greater than 0')
elif x==1:
    print(0)
else:
    a=0
    b=1
    z=0
    while z<=x:
        for i in fib(z):
            print(z)
        a=b
        b=z
        z=a+b
print('End')

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f(x):
    yield x
s=input('Enter a string')
print('Words of string')
for b in s.split():
    for y in f(b):
        print(b)


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
{30 , 40 , 50}
<class 'set'>
(60  , 70 , 80 , 90)
<class 'tuple'>
100
<class 'int'>
'''


#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))  #gives execution time required
print(timeit('( x * x   for  x  in  range(500) )'))  #gives execution time required



# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))  #gives size of list in bytes
print(sys . getsizeof(gen))  #gives size of generator in bytes