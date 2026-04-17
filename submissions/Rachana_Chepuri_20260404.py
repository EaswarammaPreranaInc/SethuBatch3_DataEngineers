'''Find  outputs (Home  work)'''
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
'''output'''
# 25
# 20.8
# Hyd
# 25
# 20.8
# Hyd
# 25
# 20.8
# Hyd
'''Find  outputs (Home  work)'''
l = [x * x   for   x   in   range(5)]
print(l) # [0, 1, 4, 9, 16]
print(type(l))  # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0, 1, 4, 9, 16}
print(type(s)) < class'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) < class'dict'>

g = (x * x   for   x   in   range(5))
print(g) #Type and address
print(type(g)) # <class 'generator'>
'''find outputs'''
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
print(next(g)) #10
print(next(g))#20
print(next(g))#30
print(next(g))#stop iteration Error
'''Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator'''
def f1(x,y):
   yield x+y
   yield x-y
   yield x*y
   yield x/y
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
for result in f1(x, y):
    print(result)
'''Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop        ,Hint:  Do  not  use  range  object '''

def f1(x,y):
    while x<=y:
        yield x
        x+=1
x = int(input("Enter first number: "))
y = int(input("Enter 2nd number: "))   
for result in f1(x,y):
    print(result)  
'''Write  a   generator  to  generate  fibonacci  series  upto  'x'
Let  'x'  be  10
What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
Hint:  Use  generator  function  and  for  loop
'''  
def f1(x):
    a=0
    b=1
    while a<=x:
        yield a
        a ,b = b, a + b
x = int(input("Enter first number: "))        
for result in f1(x):
    print(result) 
'''Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class'''
def f1(x):
    words = x.split()
    for y in words:
        yield y
s = input("Enter a string: ")
for word in f1(s):
    print(word)
'''Find  outputs'''
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
'''output'''
# [10 , 20]
# <class'list'>
# {30 , 40 , 50} 
# <class'set'>
# (60  , 70 , 80 , 90) 
# <class'tuple'> 
# 100   
# <class'int'>
'''Find  outputs'''
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
'''Find  outputs'''
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
