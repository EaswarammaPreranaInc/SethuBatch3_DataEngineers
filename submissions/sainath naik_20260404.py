1.# Find  outputs (Home  work)
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



2.#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))

d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))

g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
'''
[0,1,4,9,16]
<class 'list'>
{0,1,4,9,16}
<class 'set'>
{0:0, 1:1, 2:4 , 3:9 , 4:16}
<class 'dict'>
<generator object <genexpr> at 0x0000022277698040>
<class 'generator'>
'''



3.#  Find  outputs (Home  work)
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())# 10
print(f1())# 10
print(f1())# 10
print()
g = f2()
print(next(g))# 10
print(next(g))# 20
print(next(g))# 30
print(next(g)) #StopIteration error




'''
4.Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
def f1(a,b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b
 #End of the function
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
g = f1(a,b)
for x in g:
    print(x)
'''
15
5
50
2.0
'''



'''
5.Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f1 (x,y):
    while x <=y:
        yield x
        x +=1
# End of the function
x = int(input('Enter 1st number: '))
y = int(input('Enter 2nd number: '))
g = f1(x,y)
for x in g:
    print(x)




'''
6.Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def f1(x):
    a,b = 0,1
    while a <=x:
        yield a
        a,b = b,a+b
# End of the function
x = int(input('Enter the number: '))
g = f1(x)
for x in g:
    print(x)




'''
7.Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1(s):
    for x in s.split():
        yield x
        # End of the function
s = input('Enter a string: ')
g = f1(s)
for x in g:
    print(x)




8.# Find  outputs
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
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''



9.#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''
27.052444000000833
0.5931411999918055
'''


10.# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
'''
85176
208
'''

04