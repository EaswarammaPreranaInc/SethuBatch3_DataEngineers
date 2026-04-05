# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)	#25 <next> 10.8 <next> Hyd
for  x  in  f1():
	print(x)	#25 <next> 10.8 <next> Hyd
for  x  in  f1():
	print(x)	#25 <next> 10.8 <next> Hyd



#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)	#0<next> 1 <next> 4 <next> 9 <next> 16
print(type(l))	#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)	#0<next> 1 <next> 4 <next> 9 <next> 16
print(type(s))	#<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)	#0:0 <next> 1:1 <next> 2:4 <next> 3:9 <next> 4:16
print(type(d))	#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)	#type and address of generator object
print(type(g))	#<class 'generator'>








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
print(f1())	#10
print(f1())	#10
print(f1())	#10
print()		#next line
g = f2()
print(next(g))	#10
print(next(g))	#20
print(next(g))	#30
print(next(g))	#error stop iteration error


def operations(a, b):
    yield ("Sum", a + b)
    yield ("Difference", a - b)
    yield ("Product", a * b)
    
    if b != 0:
        yield ("Division", a / b)
    else:
        yield ("Division", "Undefined (division by zero)")


# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Using generator and for loop
for op_name, result in operations(num1, num2):
    print(f"{op_name}: {result}")



def generate_numbers(x, y):
    while x <= y:
        yield x
        x += 1   # manually increment


# Taking input
start = int(input("Enter starting value (x): "))
end = int(input("Enter ending value (y): "))

# Using generator with for loop
for num in generate_numbers(start, end):
    print(num)



def fibonacci(x):
    a, b = 0, 1
    while a < x:
        yield a
        a, b = b, a + b


# Value of x
x = 10

# Using generator with for loop
for num in fibonacci(x):
    print(num, end=" , ")



def word_generator(text):
    words = text.split()   # split string into words
    for word in words:
        yield word


# Taking input
sentence = input("Enter a sentence: ")

# Using generator with for loop
for w in word_generator(sentence):
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
	print(type(x))

outputs:
[10,20]
<class 'list'>
{30,40,50}
<class 'set'>
60,70,80,90
<class 'tuple'>
100
<class 'int'>



#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))	#execution of the program time
print(timeit('( x * x   for  x  in  range(500) )'))	#execution of the program time



# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))	#size of the list object
print(sys . getsizeof(gen))	#size of the generator object

