1) outputs 
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)#25
		 10.8
		 Hyd
for  x  in  f1():
	print(x)#25
		 10.8
		 Hyd
for  x  in  f1():
	print(x)#25
		 10.8
		 Hyd

2) outputs 
l = [x * x   for   x   in   range(5)]
print(l)#[0, 1, 4, 9, 16]
print(type(l))#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)#{0, 1, 4, 9, 16}
print(type(s))#<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)#{0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d))#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)#Generator expresiion
print(type(g))#<class 'generator'>

3) outputs 
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())#10
print(f1())#10
print(f1())#10
print()
g = f2()
print(next(g))#10
print(next(g))#20
print(next(g))#30
print(next(g))

4) Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
# def op(a, b):
    yield a + b        
    yield a - b        
    yield a * b   

    if b == 0:
	yield "Division by zero is not permitted"
    else:     
    yield a / b        

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

for result in operations(x, y):
    print(result)



5)Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
#def gen(x, y):
    while x <= y:
        yield x
        x += 1

a = int(input("Enter start value: "))
b = int(input("Enter end value: "))


for num in gen(a,b):
    print(num)


6) Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
#def fibonacci(x):
    a, b = 0, 1
    while a <= x:
        yield a
        a, b = b, a + b

x = eval(input("Enter the value of x:"))
for num in fibonacci(x):
    print(num)



7) Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
#def words(s):
    for word in s.split():
        yield word

a = input("Enter a string: ")
print("Words of the string")

for w in words(a):
    print(w)

8) outputs
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
#[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>

9) outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))#Without executing the statements the time taken to execute it is shown
print(timeit('( x * x   for  x  in  range(500) )'))#Without executing the statements the time taken to execute it is shown

10) outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))#Without executing the statements the size of the statements is shown
print(sys . getsizeof(gen))#Without executing the statements the size of the statements is shown
