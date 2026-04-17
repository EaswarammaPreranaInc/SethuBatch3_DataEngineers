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
print(l)# [0, 1, 4, 9, 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0, 1, 4, 9, 16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # <generator object ...>
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
print(next(g)) # Stop Iteration Error

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator

Sample output:
Enter first number : 10
Enter second number : 7
Sum : 17
Difference : 3
Product : 70
Division : 1.4285714285714286

Enter first number : 10
Enter second number : 0
Sum : 10
Difference : 10
Product : 0
Division by zero is not permitted
'''
import time
def op(a, b):
    time.sleep(1)
    print('Sum :', a + b)
    time.sleep(1)
    print('Difference :', a - b)
    time.sleep(1)
    print('Product :', a * b)    
    time.sleep(1)
    try:
        print('Division :', a / b)
    except ZeroDivisionError:
        print('Division by zero is not permitted')
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
op(a, b)

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range  object

Sample output:
Enter start value : 10
Enter end value : 20
10
11
12
13
14
15
16
17
18
19
20
'''
import time
def num(start, end):
    while start <= end:
        yield start
        start += 1
x = int(input('Enter start value : '))
y = int(input('Enter end value : '))
for num in num(x, y):
    time.sleep(0.5)
    print(num)
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'
Let  'x'  be  10
What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
Hint:  Use  generator  function  and  for  loop

Sample output:
Enter value of x : 10
0
1
1
2
3
5
8
End
'''
import time
def fibonacci(x):
    a, b = 0, 1
    while a <= x:
        yield a
        a, b = b, a + b
x = int(input("Enter value of x : "))
for num in fibonacci(x):
    time.sleep(0.5)
    print(num)
print('End')
'''
Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class

Sample output:
Enter any string : Hyd is green city
Words of the string
Hyd
is
green
city
'''
import time
def word(s):
    words = s.split()
    for w in words:
        yield w
s = input('Enter any string : ')
print('Words of the string')
for word in word(s):
    time.sleep(1)
    print(word)
    

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
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # 0.15
print(timeit('( x * x   for  x  in  range(500) )')) # 0.08

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # 85176
print(sys . getsizeof(gen))  # 208