# Find  outputs (Home  work)
def   f1():                   #25
	yield  25             #10.8
	yield  10.8           #Hyd
	yield  'Hyd'          #SI error
# End of  generator
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)
----------------------------------------------------------------------------
 #  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]             
print(l)                                          #[0,1,4,9,16]
print(type(l))                                    #<class'list'>

s = {x * x   for   x   in   range(5)}
print(s)                                           #{0,1,4,9,16} any order
print(type(s))                                     #<class'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)                                           #{0:0,1:1,2:4,3:9,4:16}
print(type(d))                                     #<class'dict'>

g = (x * x   for   x   in   range(5))
print(g)                                           #empty generator obj
print(type(g))                                     #<class'gen exp'>
-----------------------------------------------------------------------------
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
print(f1())     #10
print(f1())     #10
print(f1())     #10
print()
g = f2()
print(next(g))  #10
print(next(g))  #20
print(next(g))  #30 
print(next(g))  #SI error
---------------------------------------------------------------------------
 '''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
def operations(a,b):
    yield a+b
    yield a-b
    yield a*b
    try:
        yield a/b
    except ZeroDivisionError:
        print("division not possible")
x=int(input("Enter the first value : "))
y=int(input("Enter the second value : "))
g=operations(x,y)
s=['sum','diff','multiplication','division']
i=0
for x in g:
    print(s[i],"=",x)
    i+=1
------------------------------------------------------------------------------
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
-------------------------------------------------------------------------
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
---------------------------------------------------------------------------
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
---------------------------------------------------------------------------
 # Find  outputs
def   f1():                               #[10,20]--><class'list'>
        yield   [10 , 20]                 #{30,40,50}--><class'set'>
        yield  {30 , 40 , 50}             #(60,70,80,90)--çlass'tuple'>            
        yield  60  , 70 , 80 , 90         #100 ---><class'int'>
        yield  100
# End  of  generator
g = f1()  
for   x   in   g:
	print(x)
	print(type(x))
--------------------------------------------------------------------------
 #  Find  outputs
from  timeit  import   timeit      
print(timeit('[x * x   for  x  in  range(500) ]'))  
print(timeit('( x * x   for  x  in  range(500) )'))
------------------------------------------------------------------------
 # Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))
------------------------------------------------------------------