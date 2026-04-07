# Find outputs (Home work)
def f1():
 yield 25
 yield 10.8
 yield 'Hyd'
# End of generator
for x in f1():
 print(x) #25
for x in f1(): 
 print(x)#10.8
for x in f1():
 print(x) #Hyd




# Find outputs (Home work)
l = [x * x for x in range(5)]
print(l)
print(type(l))


s = {x * x for x in range(5)}
print(s)
print(type(s))


d = {x : x * x for x in range(5)}
print(d)
print(type(d))


g = (x * x for x in range(5))
print(g)
print(type(g))
'''
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x7b3d22c71d80>
<class 'generator'>
'''

# Find outputs (Home work)
def f1():
 return 10
 return 20
 return 30
def f2():
 yield 10
 yield 20
 yield 30
# End of the function
print(f1()) #10
print(f1()) #10
print(f1()) #10
print()
g = f2()
print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) #Error


'''
Write a generator to yield sum , difference , product and division of 2 numbers


Hint: Use generator function and for loop to iterate over the generator
'''
def f1(a,b):
    try:
        yield "Add", a+b
        yield "Sub", a-b
        yield "Multiplication", a*b
        yield "Div", a/b
    except:
        print("Division by 0 is not possible")


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))


for name, value in f1(a,b):
    print(f"{name} = {value}")


'''
Design a generator to yield from x (may be 10) to y (may be 20)


Hint: Use generator function and for loop


Hint: Do not use range object
'''
def f1(a,b):
    i=a
    while a<=i<=b:
        yield i
        i+=1
        
    
a = int(input("Enter 1st number: "))
b = int(input("Enter last number: "))


for j in f1(a,b):
    print(j)




'''
Write a generator to generate fibonacci series upto 'x'


Let 'x' be 10


What are the outputs ? ---> 0 , 1 , 1 , 2 , 3 , 5 , 8 


Hint: Use generator function and for loop
'''
def f1(x):
    a=0
    b=1
    c=0
    yield a
    while c<=x:
        c=a+b
        a=b
        b=c
        yield a
x= int(input("Enter a number: "))
for j in f1(x):
    print(j)


'''
Write a generator to divide a string into words


Hint1: Use generator function and for loop


Hint2: Use split() method of str class
'''
def f1(a):
    b=a.split()
    yield b
a= input("Enter String number: ")
for i in f1(a):
    for j in i:
        print(j)

# Find outputs
def f1():
        yield [10 , 20]
        yield {30 , 40 , 50}
        yield 60 , 70 , 80 , 90
        yield 100
# End of generator
g = f1()
for x in g:
 print(x)
 print(type(x))
'''
[10 , 20]
class list
{30 , 40 , 50}
class set
(60 , 70 , 80 , 90)
class tuple
100
class int
'''
# Find outputs
from timeit import timeit
print(timeit('[x * x for x in range(500) ]'))
print(timeit('( x * x for x in range(500) )'))

# Find outputs
import sys
list = [x * x for x in range(10000)]
gen = (x * x for x in range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))