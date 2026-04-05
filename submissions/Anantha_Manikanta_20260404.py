'''
1) def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
for x in f1():
    print(x)
for x in f1():
    print(x)
for x in f1():
    print(x)   # 25 <nextline> 10.8 <nextline> Hyd <nextline> 25 <nextline> 10.8 <nextline> Hyd <nextline> 25 <nextline> 10.8 <nextline> Hyd
'''
'''
2) l = [x * x for x in range(5)]
print(l)  # [0, 1, 4, 9, 16]
print(type(l))  # <class 'list'>
s = {x * x for x in range(5)}
print(s)  # {0, 1, 4, 9, 16}
print(type(s))  # <class 'set'>
d = {x: x * x for x in range(5)}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d))  # <class 'dict'>
g = (x * x for x in range(5))
print(g)  # <generator object at 1000>
print(type(g))  # <class 'generator'>
'''
'''
3) #  Find  outputs (Home  work)
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())  # 10
print(f1())  # 10
print(f1())  # 10
print()
g = f2()
print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30
print(next(g))  # Stop Iteration Error
'''
'''
4) Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
def operations(a, b):
    yield 'Sum :', a + b
    yield 'Difference :', a - b
    yield 'Product :', a * b
    if b != 0:
        yield 'Division :', a / b
    else:
        yield 'Division by zero is not permitted'
x = int(input('Enter first number : '))
y = int(input('Enter second number : '))
for result in operations(x, y):
    print(*result) if type(result) == tuple else print(result)
'''
5) Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range  object
'''
def generate_values(x, y):
    while x <= y:
        yield x
        x += 1
x = int(input('Enter start value : '))
y = int(input('Enter end value : '))
for value in generate_values(x, y):
    print(value)
'''
6) Write  a   generator  to  generate  fibonacci  series  upto  'x'
Let  'x'  be  10
What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
Hint:  Use  generator  function  and  for  loop
'''
def fib_upto(x):
    a = 0
    b = 1
    while a <= x:
        yield a
        a, b = b, a + b
x = int(input('Enter value of x : '))
for num in fib_upto(x):
    print(num)
print('End')
'''
7) Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class
'''
def words_generator(s):
    for word in s.split():
        yield word
s = input('Enter any string : ')
print('Words of the string')
for word in words_generator(s):
    print(word)
'''
'''
8) def f1():
    yield [10, 20]
    yield {30, 40, 50}
    yield 60, 70, 80, 90
    yield 100
# End of generator
g = f1()
for x in g:
    print(x)
    print(type(x))   # [10, 20] <nextline> <class 'list'> <nextline> {30, 40, 50} <nextline> <class 'set'> <nextline> (60, 70, 80, 90) <nextline> <class 'tuple'> <nextline> 100 <nextline> <class 'int'>
'''
'''
9) from timeit import timeit
print(timeit('[x * x for x in range(500)]'))      # Execution time is more compared to generator (ex: 8.5...)
print(timeit('(x * x for x in range(500))'))      # Execution time is less compared to list(ex: 0.4...)
'''
'''
10) import sys
list = [x * x for x in range(10000)]
gen = (x * x for x in range(100000000000000000000000000000000000000000000000))
print(sys.getsizeof(list))   # More size compared to generator (example: 73676)
print(sys.getsizeof(gen))    # Less size compared to list (example: 324)
'''