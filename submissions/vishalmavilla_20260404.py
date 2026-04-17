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

''' Output:
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
print(l) # [ 0 , 1 , 4 , 9 , 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # { 0 , 1 , 4 , 9 , 16} in any order
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0 : 0 , 1 : 1 , 2 : 4 , 3 : 9 , 4 : 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # <class 'generator'> and address in hexa decimal 
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
g = f2() # empty generator object is created
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # StopIteration Error

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
# Code:
def f1(a,b):
    yield f"Sum : {a+b}"
    yield f"Difference : {a-b}"
    yield f"Product : {a-b}"
    yield f"Division : {a/b}"
try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    g = f1(a,b)
    for x in g:
        print(x)
except ZeroDivisionError:
    print("Division by zero is not permitted")

''' Outputs:
Enter first number : 10
Enter second number : 7
Sum : 17
Difference : 3
Product : 3
Division : 1.4285714285714286

Enter first number : 10
Enter second number : 0
Sum : 10
Difference : 10
Product : 10
Division by zero is not permitted
'''
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
# Code :
def f1(x,y):
    while x<=y:
        yield x
        x+=1
x = int(input("Enter start number : "))
y = int(input("Enter end number : "))
g = f1(x,y)
for x in g:
    print(x)

''' Output:
Enter start number : 10
Enter end number : 15
10
11
12
13
14
15
'''
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
# Code :
def f1(x):
    a = 0
    b = 1
    if x >=1 :
        yield a
        yield b
    while a+b <= x:
        c = a+b
        a = b
        b = c
        yield c
x = int(input("Enter value of x : "))
g = f1(x)
for x in g:
    print(x)
print("End")
''' Output:
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
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
# Code :
def f1(x):
    i = 0
    while i<len(x):
        yield x[i]
        i+=1
x = input("Enter any string : ")
g = f1(x.split())
for x in g:
    print(x)

''' Outputs:
Enter any string : Hyd is green city
Hyd
is
green
city

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

''' Outputs:
[10 , 20]
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
print(timeit('[x * x   for  x  in  range(500) ]')) # Time taken to execute the statement like few seconds
print(timeit('( x * x   for  x  in  range(500) )')) # Time taken to execute the statement like negligible seconds of time

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # 40000
print(sys . getsizeof(gen)) # 0