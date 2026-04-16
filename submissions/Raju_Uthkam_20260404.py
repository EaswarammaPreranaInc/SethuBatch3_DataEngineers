# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1(): #25 <nextline> 10.8 <nextline> 'Hyd'
	print(x)
for  x  in  f1(): #25 <nextline> 10.8 <nextline> 'Hyd'
	print(x)
for  x  in  f1(): #25 <nextline> 10.8 <nextline> 'Hyd'
	print(x)



#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) #[0,1,4,9,16]
print(type(l)) #<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) #{0,1,4,9,16}
print(type(s)) #<class 'set()'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0:0,1:1,2:4,3:9,4:16}
print(type(d)) #<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) #Type and address 
print(type(g)) #<class 'generator'>



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
print(f1()) #10 
print(f1()) #10
print(f1()) #10
print() #Nothing empty space 
g = f2()
print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) #stop iteration error 


'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def gen(a,b):
    try:
        yield a + b
        yield a - b
        yield a * b
        yield a / b 
    except :
        print('Division by zero is not permitted ')
i = int(input('Enter 1st number : '))
j = int(input('Enter 2nd number : '))
g = gen(i,j)
print(f'SUM : {next(g)}')
print(f'DIFFERENCE : {next(g)}')
print(f'PRODUCT : {next(g)}')
print(f'DIVISION  : {next(g)}')



'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

def g1(a,b):
    while a <= b:
        yield a 
        a += 1
        
r = int(input('Enter 1st number : '))
s = int(input('Enter 2nd number : '))
for x in g1(r,s):
    print(x)


'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''

def fib(x):
    a, b = 0, 1
    for _ in range(x):
        yield a
        a, b = b, a + b
x= int(input('Enter any number : '))
for x in fib(x):
    print(x)


'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''


def word(y):
    for x in y:
        yield x
y = input('Enter a sentence : ').split()
for i in word(y):
    print(i)
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #time taken of execution before the execution of a list 
print(timeit('( x * x   for  x  in  range(500) )')) #time taken of execution before the execution of a generator expression  


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
#[10,20]
#<class 'list'>
#{30 , 40 , 50}
#<class 'set'>
#(60  , 70 , 80 , 90)
#<class 'tuple'>
#100
#<class 'int'>


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) #size of list 
print(sys . getsizeof(gen)) #size of generator 



