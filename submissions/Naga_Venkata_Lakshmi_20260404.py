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
#outputs
25
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
print(l) #[0, 1, 4, 9, 16]
print(type(l)) #<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) #{0, 1, 4, 9, 16}
print(type(s)) #<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) #<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) #<generator object <genexpr> at 0x000001EDEED78E10>
print(type(g)) <class 'generator'>


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
print(next(g)) #stopIteration Error.



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
#outputs
[10, 20]
<class 'list'>
{30, 40, 50}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>





#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #11.762757000000079

print(timeit('( x * x   for  x  in  range(500) )')) #0.14598399999999856


# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) #85176

print(sys . getsizeof(gen)) #208



def gen_words(s):
    for word in s.split():
        yield word

text = input("Enter a string:  ")

for w in gen_words(text):
    print(w)



def fibonacci(x):
    a , b = 0 , 1
    for i in range(x):
        yield a
        a , b = b , a + b

n = int(input("Enter how many numbers:  "))
for num in fibonacci(n):
    print(num)


def operations(a,b):
    yield f'sum:{a + b}'
    yield f'difference:{a-b}'
    if b != 0:
        yield f'Division:{a / b}'
    else:
        yield "Error: Division by zero" 

a = int(input("Enter first number:  "))
b = int(input("Enter second number:  "))
for op in operations(a,b):
    print(op)


def generate_numbers(x,y):
    while x <= y:
        yield x
        x += 1

x = int(input("Enter value of x:  "))
y = int(input("Enter value of y:   "))
for num in generate_numbers(x,y):
    print(num)



