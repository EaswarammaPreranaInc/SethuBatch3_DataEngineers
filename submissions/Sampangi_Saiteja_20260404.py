# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)        # 25
	                # 10.8
	                # Hyd
for  x  in  f1():
	print(x)        # 25
	                # 10.8
	                # Hyd
for  x  in  f1():
	print(x)        # 25
	                # 10.8
	                # Hyd


#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)          # [0, 1, 4, 9, 16]
print(type(l))    # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)          # {0, 1, 4, 9, 16}
print(type(s))    # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d))    # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)          # <generator object <genexpr> at ...>
print(type(g))    # <class 'generator'>


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

print(f1())       # 10
print(f1())       # 10
print(f1())       # 10

print()           # (blank line)

g = f2()
print(next(g))    # 10
print(next(g))    # 20
print(next(g))    # 30
print(next(g))    # StopIteration (Error)




from time import sleep

def calc(a, b):
	yield ("sum", a + b)
	yield ("difference", a - b)
	yield ("product", a * b)
	yield ("division", a / b)

def main():
	a = int(input("Enter first number-"))
	b = int(input("Enter second number-"))
	
	for name, value in calc(a, b):
		sleep(1)
		print(f"{name} - {value}")

main()


def generate(x, y):
	while x <= y:
		yield x
		x += 1

# Input
x = int(input("Enter starting number-"))
y = int(input("Enter ending number-"))

# Iteration
for i in generate(x, y):
	print(i)



# Write  a   generator  to  generate  fibonacci  series  upto  'x'

def fib(x):
	a = 0
	b = 1
	count = 0
	while count < x:
		yield a
		a, b = b, a + b
		count += 1

# Let  'x'  be  10
x = 7

for i in fib(x):
	print(i)      # 0
	              # 1
	              # 1
	              # 2
	              # 3
	              # 5
	              # 8


# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)          # [10, 20]
	                  # {40, 50, 30}  (order may vary)
	                  # (60, 70, 80, 90)
	                  # 100
	print(type(x))    # <class 'list'>
	                  # <class 'set'>
	                  # <class 'tuple'>
	                  # <class 'int'>

#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))   # some float value (e.g., 0.02...)
print(timeit('( x * x   for  x  in  range(500) )'))  # smaller float value (e.g., 0.0001...)

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))   # around 85176 (may vary slightly by system)
print(sys . getsizeof(gen))    # around 112