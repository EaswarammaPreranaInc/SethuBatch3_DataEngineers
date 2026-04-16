# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25,10.8,Hyd
for  x  in  f1():
	print(x) # 25,10.8,Hyd
for  x  in  f1():
	print(x) # 25,10.8,Hyd
	
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0,1,4,9,16]
print(type(l))# <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0,1,4,9,16}in any order
print(type(s)) # <class' set'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0:0,1:1,2:4,3:9,4:16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # Type and address of gen obj
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
print(f1())# 10
print(f1())# 10
print(f1())# 10
print()
g = f2()
print(next(g))# 10
print(next(g))# 20
print(next(g))# 30
#print(next(g))# StopIteration Error

#Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

#Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
def gen(a,b):
	print(f'Sum : ',end='')
	yield a+b
	print(f'Difference : ',end='')
	yield a-b
	print(f'Product : ',end='')
	yield a*b
	print(f'Division : ',end='')
	try:
		yield a/b
	except:
		print("Division by zero is not permitted")
a=eval(input("Enter a value : "))
b=eval(input("Enter b value : "))
g=gen(a,b)
for x in g:
	print(x)

# Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
#Hint:  Use  generator  function  and  for  loop
#Hint:  Do  not  use  range  object

def func(x,y):
    while x<=y:
        yield x
        x+=1
x=eval(input("Enter x value : "))
y=eval(input("Enter y value : "))
g1=func(x,y)
for c in g1:
    print(c)

#Write  a   generator  to  generate  fibonacci  series  upto  'x'
#Let  'x' be  10
#What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
	
def fib(n):
    f1,f2=0,1
    f3=f1+f2
    if n==0:
        yield f1
    elif n==1:
        yield f1
        yield f2
    else:
        yield f1
        yield f2
        while f3<=n:
            yield f3
            f1=f2
            f2=f3
            f3=f1+f2
n=eval(input("Enter n value : "))
g2=fib(n)
for f in g2:
    print(f)

#Write  a  generator  to  divide  a  string  into  words
#Hint1:  Use  generator  function  and  for   loop
#Hint2:  Use  split()  method  of  str  class

def stringtowords(s):
    for w in s.split():
        yield w
s=input("Enter input : ")
g3=stringtowords(s)
for word in g3:
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
	print(x) # [10,20]<nl><class 'list'> <nl> {30 , 40 , 50}<class 'set'> <nl> 60  , 70 , 80 , 90)<class 'tuple'> <nl> 100<class 'int'>
	print(type(x))

#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # time taken by  list to execute
print(timeit('( x * x   for  x  in  range(500) )')) # time taken by gen to yield 

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # size of list in bytes
print(sys . getsizeof(gen)) # size of gen obj in bytes