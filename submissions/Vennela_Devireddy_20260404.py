#1
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25 <next line> 10.8 <next line> Hyd <next line>
for  x  in  f1():
	print(x) # 25 <next line> 10.8 <next line> Hyd <next line>
for  x  in  f1():
	print(x) # 25 <next line> 10.8 <next line> Hyd <next line>


#2
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0,1,4,9,16]
print(type(l)) # <class'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0,1,4,9,16}
print(type(s)) # <class'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) # <class'dict'>

g = (x * x   for   x   in   range(5))
print(g) # type and address of generator
print(type(g)) # <class'generator'>


#3
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
print(next(g)) # Error , stopiteration


#4
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
import time 
def gen(a,b):
    sum = a+b
    print("Sum :", end=" " )
    yield sum
    diff = a-b
    print("Difference :", end=" ")
    yield diff
    prod = a*b
    print("Product :", end=" ")
    yield prod
    div = a/b
    print("Division :", end=" ")
    yield div

    
a = int(input("enter a num:"))
b = int(input("enter a num:"))
g = gen(a,b)
try:
     for x in g:
        print(x) 
        time.sleep(1)
except:
    print("Division by zero is not possible")    
       
    
    
#5
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
import time 
def gen(x,y):
    while x<=y:
        yield x
        x+=1
x = int(input("Enter start value :"))
y = int(input("Enter end value : "))

g = gen(x,y)

for i in g:
    print(i)
    time.sleep(1)
        

#6
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time 
def str(s):
    a = s.split()
    for x in a:
        time.sleep(5)
        yield x
        
s = input("Enter any string")
print("Words of the string")
for x in str(s):
    print(x)        
    
    
       
#7
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
import time 
def fib(n):
    a = 0
    b = 1
    while a<n:
        yield a
        temp = a+b
        a = b
        b = temp
n = int(input("Enter a num :"))
for x in fib(n):
    time.sleep(1)
    print(x)
print("End")           


#8
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
[10 , 20]
<class'list'>
{30 , 40 , 50}
<class'set'>
(60  , 70 , 80 , 90)
<class'tuple'>
100
<class'int'>
'''


#9
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) # returns execution time of list
print(timeit('( x * x   for  x  in  range(500) )')) # returns execution time of generator


#10
# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # returns memory size of list 
print(sys . getsizeof(gen)) # returns memory size of generator
