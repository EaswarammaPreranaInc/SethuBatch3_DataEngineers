########################################################################
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
-----output----
25
10.8
Hyd
25
10.8
Hyd
25
10.8
Hyd
########################################################################
 #  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)#[0,1,4,9,16]
print(type(l))#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)#{0,1,4,9,16}
print(type(s))#<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)#{0:0,1:1,2:4,3:9,4:16}
print(type(d))##<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)#<generator object <genexpr> at some address>
print(type(g))#class <generator>
########################################################################
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
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))#error
-----output----
10
10
10

10
20
30
error
########################################################################
 '''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
------Code-----
a=int(input("enter 1st value:"))
b=int(input("enter 2nd value:"))
def f1(a,b):
    yield "sum:",a+b
    yield "subtraction:",a-b
    yield "multiplication:",a*b
    yield "division:",a/b
g=f1(a,b)
for i,j in g:
    print(i,j)
########################################################################
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

a=int(input("Enter the start value:"))
b=int(input("Enter the End Value:"))
def f1(a,b):
    for i in range(a,b+1):
        yield i
g=f1(a,b)
for i in g:
    print(i)
########################################################################
 '''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def fibonacci(x):
    a, b = 0, 1
    while a <= x:
        yield a
        a, b = b, a + b

# given x = 10
x = int(input("x:"))

for num in fibonacci(x):
    print(num, end=" ")
########################################################################
 '''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def div(a):
    for i in a:
        yield i
a=input().split()
g=div(a)
for i in g:
    print(i)
########################################################################
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
-------output------
[10 , 20]
<class 'list'>
{30 , 40 , 50}
<class 'set'>
60  , 70 , 80 , 90
<class 'tuple'>
########################################################################
 #  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
----output---

########################################################################
 # Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))#85176
print(sys . getsizeof(gen))#200
