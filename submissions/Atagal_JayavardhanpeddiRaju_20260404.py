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
	print(x)    #25
                10.8
                Hyd
                25
                10.8
                Hyd
                25
                10.8
                Hyd
                       

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)  #[0, 1, 4, 9, 16]
print(type(l)) #<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) #{0, 1, 4, 9, 16}
print(type(s)) #<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) #<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) #generator object 
print(type(g))  #<class 'generator'>

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
print()
g = f2()
print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) stop Iteration


Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator

def calculate(a, b):
    yield ("Sum", a + b)
    yield ("Difference", a - b)
    yield ("Product", a * b)
    
    if b != 0:
        yield ("Division", a / b)
    else:
        yield ("Division", "Undefined (division by zero)")
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
for operation, result in calculate(n1, n2):
    print(f"{operation}: {result}")

Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object

def generate_numbers(x, y):
    while x <= y:
        yield x
        x += 1
x =int(input("enter the start value:"))
y =int(input("enter the end value:"))
for num in generate_numbers(x, y):
    print(num)

Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop

def fibonacci(x):
    a, b = 0, 1
    for _ in range(x):
        if a > x:
            break
        yield a
        a, b = b, a + b
x = int(input("enter the number:"))
for num in fibonacci(x):
    print(num, end=" , ")

Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

def split_words(text):
    for word in text.split():
        yield word
sentence = input("Enter a sentence: ")
for w in split_words(sentence):
    print(w)

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
	print(type(x))  #[10, 20]
                    <class 'list'>
                    {40, 50, 30}
                    <class 'set'>
                    (60, 70, 80, 90)
                    <class 'tuple'>
                    100
                    <class 'int'>

 #Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #21.4
print(timeit('( x * x   for  x  in  range(500) )')) #0.27

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) #85176
print(sys . getsizeof(gen)) #208



