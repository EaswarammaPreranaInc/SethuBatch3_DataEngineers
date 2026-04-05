# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)#25<\n>10.8<\n>Hyd
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)
 
 #  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)#0<\n>1<\n>4<\n>9<\n>16
print(type(l))#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)#0<\n>1<\n>4<\n>9<\n>16
print(type(s))#<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)#0:0<\n>1:1<\n>2:4<\n>3:9<\n>4:16
print(type(d))#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)#0<\n>1<\n>4<\n>9<\n>16
print(type(g))#<class 'generator'>

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
print(f1())#10
print(f1())#10
print(f1())#10
print()
g = f2()
print(next(g))#10
print(next(g))
print(next(g))
print(next(g))

# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)#[10,20]
	print(type(x))#<class 'list'>
 
 #  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))#0<\n>1<\n>4<\n>9........
print(timeit('( x * x   for  x  in  range(500) )'))#0<\n>1<\n>4.....

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
def generator_yield():
    yield a+b
    yield a-b
    yield a*b
    yield a/b
a=int(input('Enter 1st  number ='))
b=int(input('Enter 2nd number ='))
for x in generator_yield():
    print(x)

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def generator_yield(x,y):
    while x<=y:
        yield x
        x+=1
x=int(input('Enter a number'))
y=int(input('Enter a number'))
for num in generator_yield(x,y):
	print(num)

 
'''
Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class
'''
def generator(string):
    a=string.split('')
    for word in a:
        yield word
string=input('Enter a sentence =')
for i in generator(string):
        print(i)

        
    
    






    