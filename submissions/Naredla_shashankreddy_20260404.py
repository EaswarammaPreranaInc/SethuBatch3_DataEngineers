 Find  outputs (Home  work)
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
'Hyd'
25
10.8
'Hyd'
25
10.8
'Hyd'




#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))
'''
[0,1,4,9,16]
<class "List">


s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))
'''
{0,1,4,9,16}
<class "set">
'''


d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))
'''
{0:0,1:1,2:4,3:9,4:16}
<class 'dict'>
'''


g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
'''
empty generator object
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
print(f1())#10 20 30
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
10
10
10

10
20
30
error
'''

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

'''
def operations(a, b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b

# taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for result in operations(a, b):
    print(result)
'''


'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'
Let  'x'  be  10
What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
Hint:  Use  generator  function  and  for  loop
'''
def fibonacci(x):
    a, b = 0, 1
    for _ in range(x):
        if a > x:
            break
        yield a
        a, b = b, a + b

# Using the generator
x = 10
for num in fibonacci(x):
    print(num, end=" , ")



Find  outputs
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
{30,40,50}
<class 'set'>
(60,70,80,90)
<class 'tuple'>
1000
<class 'int'>'''



#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''
23.5
0.3
returns how much time does it take to execute'''


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
'''