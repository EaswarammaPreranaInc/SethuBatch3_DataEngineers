#1
# Find outputs (Home work)
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
for x in f1():
    print(x) # 25, 10.8, Hyd
for x in f1():
    print(x) # 25, 10.8, Hyd (Calling f1() creates a NEW generator object each time)
for x in f1():
    print(x) # 25, 10.8, Hyd (New instance starts from the beginning)



#2
# Find outputs (Home work)
l = [x * x for x in range(5)]
print(l)       # [0, 1, 4, 9, 16]
print(type(l)) # <class 'list'>

s = {x * x for x in range(5)}
print(s)       # {0, 1, 4, 9, 16}
print(type(s)) # <class 'set'>

d = {x: x * x for x in range(5)}
print(d)       # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) # <class 'dict'>

g = (x * x for x in range(5))
print(g)       # <generator object <genexpr> at ...>
print(type(g)) # <class 'generator'>



#3
# Find outputs (Home work)
def f1():
    return 10 # Function terminates immediately after first return
    return 20 # Unreachable code
    return 30 # Unreachable code
def f2():
    yield 10
    yield 20
    yield 30
# End of the function
print(f1()) # 10
print(f1()) # 10 (Every call starts f1 fresh and hits the first return)
print(f1()) # 10
print()
g = f2()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
# print(next(g)) # StopIteration error as the generator 'g' has yielded all its values and is now exhausted. 



#4
'''
Write a generator to yield sum , difference , product and division of 2 numbers

Hint: Use generator function and for loop to iterate over the generator
'''
import time
def arithmetic_gen(a, b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b if b != 0 else 'Division by zero is not permitted'

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

labels = ["Sum", "Differnece", "Product", "Division"]

for label, val in zip(labels, arithmetic_gen(a, b)):
    print(f"{label} : {val}")
    time.sleep(0.5)



#5
'''
Design a generator to yield from x (may be 10) to y (may be 20)

Hint: Use generator function and for loop

Hint: Do not use range object
'''
import time
def custom_range(start, end):
    while start <= end:
        yield start
        start += 1

start =  int(input("Enter start value: "))
end = int(input("Enter end value: "))
for num in custom_range(start, end):
    print(num)
    time.sleep(0.5)



#6
'''
Write a generator to generate fibonacci series upto 'x'

Let 'x' be 10

What are the outputs ? --> 0 , 1 , 1 , 2 , 3 , 5 , 8 

Hint: Use generator function and for loop
'''
import time
def fib_gen(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

n = int(input("Enter value of x: "))
for val in fib_gen(n):
    print(val)
    time.sleep(0.5)



#7
'''
Write a generator to divide a string into words

Hint1: Use generator function and for loop

Hint2: Use split() method of str class
'''
import time
def word_splitter(text):
    for word in text.split():
        yield word

s = input("Enter any string: ")
print("Words of the string: ")
for w in word_splitter(s):
    print(w)
    time.sleep(0.5)



#8
# Find outputs
def f1():
    yield [10, 20]             # Yields a List
    yield {30, 40, 50}         # Yields a Set
    yield 60, 70, 80, 90       # Yields a Tuple (commas create tuples automatically)
    yield 100                  # Yields an Integer
# End of generator
g = f1()
for x in g:
    print(x)       # [10, 20] | {40, 50, 30} | (60, 70, 80, 90) | 100
    print(type(x)) # <class 'list'> | <class 'set'> | <class 'tuple'> | <class 'int'>



#9
# Find outputs
from timeit import timeit
print(timeit('[x * x for x in range(500)]')) # Output: e.g., 25.4 (Slower as it builds the list)
print(timeit('(x * x for x in range(500))')) # Output: e.g., 0.5 (Faster as it only creates the object)



#10
# Find outputs
import sys
list_obj = [x * x for x in range(10000)]
gen_obj = (x * x for x in range(1000000000000000000000000))

print(sys.getsizeof(list_obj)) # Output: e.g., 85176 bytes (Size grows with number of elements)
print(sys.getsizeof(gen_obj))  # Output: e.g., 112 bytes (Size is constant regardless of range)
