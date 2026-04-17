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

#25
#10.8
#Hyd
#25
#10.8
#Hyd
#25
#10.8
#Hyd


#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

#[0, 1, 4, 9, 16]
#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))

#{0,1,4, 9,16}
#<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))

#{0:0, 1:1, 2:4, 3:9, 4:16}
#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)
print(type(g))

#type and address
#<class "genexp">

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
print(f1())
#type and address
print(f1())
#type and address
print(f1())
#type and address
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#10
#20
#30
#Error

 '''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
def arith_operations(a,b):
	yield f"Sum : {a+b}"
	yield f"Difference : {abs(a-b)}"
	yield f"product : {a*b}"
	try:
		d = a/b
		yield f"Division : {d}"
	except:
		yield "zero division error"
a = int(input())
b = int(input())

g = arith_operations(a,b)

for i in g:
	print(i)


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def yield_gen(x,y):
	while (x <=y):
		yield x
		x +=1


x = int(input())
y = int(input())

g = yield_gen(x,y)

for i in g:
	print(i)



'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''

def fib(n):
	a, b = 0, 1
	if n ==0:
		yield ""
	while(n>0):
		yield a
		a,b = b, a+b
		n -=1
		

n = int(input())

g = fib(n)

for i in g:
	print(i)



 '''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

def divide(string):
	list = string.split()
	for word in words:
        	yield word
	
string = (input())

g = divide(string)

for i in g:
	print(i)




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

#[10 , 20]
#<class 'list'>
#{30 , 40 , 50}
#<class set'>
#(60  , 70 , 80 , 90)
#<class 'tuple'>
#100
#<class 'int'>

 #  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))

#time that it willl take to excute [x * x   for  x  in  range(500) ] without executing statement
#0


 # Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))

#10000
#0