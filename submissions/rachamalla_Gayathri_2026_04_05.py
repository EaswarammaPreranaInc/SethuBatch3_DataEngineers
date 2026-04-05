 # Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)# 25 10.8 'hyd'
for  x  in  f1():
	print(x)#25 10.8 'hyd'
for  x  in  f1():
	print(x) #25 10.8 'hyd'
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)#[0,1,4,9,16]
print(type(l))<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)#{0,1,2,3,4}
print(type(s))#<class 'dict'>

d = {x : x * x    for   x   in   range(5)}
print(d)#{ 0:0,1:1,2:4,3:9,4:16}
print(type(d))#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
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
print(f1())#10
print(f1())#10
print(f1())#10
print()
g = f2()
print(next(g))#20 30
print(next(g))#20 30
print(next(g))#20 30
print(next(g)) '''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
 '''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
''' '''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
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
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))
[1:24 pm, 04/04/2026] SRINIVAS Sir Maths: # Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))