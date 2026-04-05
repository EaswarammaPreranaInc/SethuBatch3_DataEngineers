# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25 10.8 Hyd
for  x  in  f1():
	print(x) # 25 10.8 Hyd
for  x  in  f1():
	print(x) # 25 10.8 Hyd



#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [1,4,9,16]
print(type(l)) # <class list>

s = {x * x   for   x   in   range(5)}
print(s) # {1,4,9,16}
print(type(s)) # <class set>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0:0, 1:1, 2:4, 3:9, 4:16}
print(type(d)) # <class dict>

g = (x * x   for   x   in   range(5))
print(g) 
print(type(g)) # <class gen>




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
print(next(g)) # 



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def operations(a,b):
   yield a + b
   yield a - b
   yield a * b
   yield a/b
  
 g = f(10,5)
 for value in g:
     print(value)


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

def values(x, y):
    for i in iter(lambda: x, y+1):
        yield i
        x += 1

g = values(10, 20)

for v in g:
    print(v)


'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''

def values(x,y):
   yield a+b
 g = Fibonacci(10)
 for i in g:
     print(num)


# Find  outputs
def   f1():
        yield   [10 , 20] # [10,20]
        yield  {30 , 40 , 50} # [30 40 50]
        yield  60  , 70 , 80 , 90 # [60 70 80 90]
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x) # [10,20]# [30 40 50]# [60 70 80 90]

	print(type(x))<class list> <class set><class tuple>



#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))