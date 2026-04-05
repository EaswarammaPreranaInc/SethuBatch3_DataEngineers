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

25
10.8
Hyd
25
10.8
Hyd
25
10.8
Hyd



# Find  outputs (Home  work)
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

[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x00000251A3A535E0>
<class 'generator'>


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
print(next(g))

10
10
10

10
20
30
# Error

# Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
# Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
def operations(a, b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b
for result in operations(10, 5):
    print(result)



# Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
# Hint:  Use  generator  function  and  for  loop
# Hint:  Do  not  use  range  object
def generate_xy(x, y):
    while x <= y:
        yield x
        x += 1
for num in generate_xy(10, 20):
    print(num, end=" ")


# Write  a   generator  to  generate  fibonacci  series  upto  'x'
# Let  'x'  be  10
# What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
# Hint:  Use  generator  function  and  for  loop
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num, end=" ")



# Write  a  generator  to  divide  a  string  into  words
# Hint1:  Use  generator  function  and  for   loop
# Hint2:  Use  split()  method  of  str  class
def words_generator(s):
    for word in s.split():
        yield word
for word in words_generator("Python generators are powerful"):
    print(word)


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

[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>


# Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))