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
#Here for every for loop a new generator object is created and there are three generator objects are present in the program
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
#------------------------------------------------------------------------------------------
l = [x * x   for   x   in   range(5)]
print(l)#[0,1,4,9,16]
print(type(l))#<class 'list>

s = {x * x   for   x   in   range(5)}
print(s)#{0,1,4,9,16}
print(type(s))##<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)#{0:0,1:1,2:4,3:9,4:16}
print(type(d))#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)#type and address
print(type(g))#<class 'generator'>
#--------------------------------------------------------------
#  Find  outputs (Home  work)
def  f1():
	return  10 # any function after return everything is ignored
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
print(f1()) #10
print(f1()) #10
print(f1()) #10
print()#blank space
g = f2()
print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) #stop IteraionError
#--------------------------------------------------------------
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
def f1(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
a=eval(input("enter a number"))
b=eval(input("enter a number"))
g=f1(a,b)
for x in g:
    print(x)
#--------------------------------------------------------------
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

def f1(a,b):
    i=a
    while i<=b:
        yield i
        i+=1
a=eval(input("enter a start number"))
b=eval(input("enter a end number"))
g=f1(a,b)
for x in g:
    print(x)
#-----------------------------------------------
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def f1(a):
    start=0
    nxt=1
    while start<a:
        yield start
        start,nxt=nxt,start+nxt
a = int(input("enter a upto number: "))
g = f1(a)
for x in g:
    print(x)
#-----------------------------------------
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1(a):
   for x in a.split():
       yield x
a = (input("enter a string: "))
g = f1(a)
for x in g:
    print(x)
#-----------------------------------------
# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60 , 70 , 80 , 90
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
==============================================
 Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
#generates time of execution of statements
#---------------------------------------------------------
# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
#from sys module u need to import getsize to get size.

