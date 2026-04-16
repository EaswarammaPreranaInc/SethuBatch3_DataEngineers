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

output:
25
10.8
Hyd
25
10.8
Hyd
25
10.8
Hyd

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

#
[0,1,4,9,16]
<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))

##
{0 ,1 , 4 , 9 ,16}
<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))

##
{0:0,1:1,2:4,3:9,4:16}
<class 'dictionary'>


g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
#type and address of generator
<class 'genrator'>

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
print(f1()) #10
print(f1()) #10
print() # <space>
g = f2()
print(next(g))#10
print(next(g))#20
print(next(g))#30
print(next(g))#si error


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
##
[10,20]
<class 'list'>
{30,40,50}
<class 'set'>
(60,70,80,90)
<class 'tuple'>
100
<class 'int'>

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def f1(a,b):
    yield "sum:",a+b
    yield "Difference:",abs(a-b)
    yield "Product:",a*b
    if b==0:
        yield "Division by 0 is not permitted"
    else:
        yield "Division:",a/b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
g=f1(a,b)
for x in g:
    print(x)


#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))#gets the approximate execution time of the statement
#
print(timeit('( x * x   for  x  in  range(500) )'))#gets the approximate execution time of the statement


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) #Returns the size of object in bytes
print(sys . getsizeof(gen)) #Returns the size of object in bytes


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

import time
def f1(a,b):
    while a<=b:
        yield a
        time.sleep(2)
        a+=1
a=int(input('enter stating value: '))
b=int(input('enter end value: '))
g=f1(a,b)
for x in g:
    print(x)

'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''


import time
def f1(n):
    a = 0
    b = 1
    while a< n:
        yield a
        time.sleep(1)
        a, b = b, a + b
n = int(input('enter number of terms: '))
g = f1(n)
for x in g:
    print(x)

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

import time
def f1():
    b=a.split(" ")
    for i in b:
        yield i
        time.sleep(1)
a=input('enter a string: ')
g=f1()
for x in g:
    print(x)



