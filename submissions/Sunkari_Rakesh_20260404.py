# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)
for  x  in  f1(): # Stopiteration error automatically handled by for loop
	print(x)
for  x  in  f1(): # Stopiteration error automatically handled by for loop

	print(x)

# output
25
10.8
Hyd


#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

# output
[0 1 4 9 16]
class <List>

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))
 
# output
{0 1 4 9 16}
class <set>


d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))
# output
{0:0, 1:1, 2:4, 3:9, 4:16}
class <Dict>

g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
# output
type and address of generator
class <generator>



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
print() # space
g = f2() 
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # stopiteration error






Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

# program

import time 
def f1():
	a=int(input("Enter 1st number:"))
	b=int(input("Enter 2st number:"))
	yield F"sum is:{a+b}"
	yield F"difference is:{a-b}"
	yield F"Product is:{a*b}"
	if b==0:
	    yield "Division by zero is not permitted"
	else:
	    yield F"Division is: {a/b}"
g=f1()
for k in g:
	print(k)  
	time.sleep(1)



Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

# program
import time
def f1():
	a=input("enter start value: ")
	b=input("enter end value: ")
	yield a 
	time.sleep(1)	
	yield b

g=f1()
for i in g:
	print(i)




Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def febonacci():
	yeild 






Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def s():
	a=input("enter word:")
	yield a
#g=s()
for x in s.split():
    print(x)



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
# output
[10, 20]
class <generator>
{30, 40, 50}
class <generator>
60, 70, 80, 90
class <generator>
100
class <generator>


#  Find  outputs
from  timeit  import   timeit

print(timeit('[x * x   for  x  in  range(500) ]')) # gives time required to print the statement without executing the satatement
print(timeit('( x * x   for  x  in  range(500) )')) # gives time required to print the statement without executing the satatement


 # Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) # gives the size of the list
print(sys . getsizeof(gen)) # gives the size of generator











