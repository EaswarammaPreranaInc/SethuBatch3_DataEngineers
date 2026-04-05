# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) --> 25
		     10.8
		     Hyd
for  x  in  f1():
	print(x) --> 25
		     10.8
		     Hyd
for  x  in  f1():
	print(x) --> 25
		     10.8
		     Hyd



#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))
--> [0, 1, 4, 9, 16]
<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))
--> {0, 1, 4, 9, 16}
<class 'set'>


d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>


g = (x * x   for   x   in   range(5))
print(g)
print(type(g))
<generator object <genexpr> at 0x7c9b7991dd80>
<class 'generator'>



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
print(f1()) --> 10
print(f1()) --> 10
print(f1()) --> 10
print()
g = f2()
print(next(g)) --> 10
print(next(g)) --> 20
print(next(g)) --> 30
print(next(g)) --> error



'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def operations(a, b):
    yield a + b    
    yield a - b      
    yield a * b      
    yield a / b      

g = operations(10, 5)
for value in g:
    print(value)




Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
def numbers(a,b):
    while a <= b:
        yield a
        a += 1
g = numbers(10,20)
for numbers in g:
    print(numbers)



'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''




'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

def split_words(s):
    words = s.split()   # split string into words
    for w in words:
        yield w

for word in split_words(text):
    print(word)



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

[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>




#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) --> 20.417648856004234
print(timeit('( x * x   for  x  in  range(500) )')) --> 0.2625409070169553




# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) --> 85176
print(sys . getsizeof(gen)) --> 208















