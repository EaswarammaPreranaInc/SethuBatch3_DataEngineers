# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)# [10 , 20] {30 , 40 , 50}
	print(type(x))#<class 'list'> <class 'set'>  <class "tuple">  <class 'int'>



  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))#0.08 seconds
print(timeit('( x * x   for  x  in  range(500) )'))#0.02



# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))#~85000 bytes (depends on system)
print(sys . getsizeof(gen))#~100–200 bytes

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1():
    for x in s:
        yield x
g = f1()
string= input("Enter:")
s= string.split()
for y in s:
    print(next(g))
'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''



'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f1(x,y):
    while x <= y:
        yield x
        x +=1

x =  int(input("Enter strat value: "))
y = int(input("Enter end value: "))
g = f1(x,y)
while True:
    try:
        print(next(g))
    except:
        break





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
print(next(g))#10
print(next(g))#20
print(next(g))#30
print(next(g))#nothing



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def f1(a,b):
    yield "sum:",(a+b)
    yield "Difference:",abs(a-b)
    yield "Product:",a*b
    if(b==0):
        yield "Division:","Cannot be divided by 0"
    else:
        yield "Division:",a/b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
g=f1(a,b)
for x in g:
    print(x[0],x[1])

























