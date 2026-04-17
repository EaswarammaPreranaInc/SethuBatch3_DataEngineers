# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)#25 <next line> 10.8 <next line>Hyd
for  x  in  f1():
	print(x)#25 <next line> 10.8 <next line>Hyd
for  x  in  f1():#25 <next line> 10.8 <next line>Hyd
	print(x)
#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)#[0,1,4,9,16]
print(type(l))#<class 'list'>

s = {x * x   for   x   in   range(5)}
print(s)#{0,1,4,9,16}
print(type(s))#<class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d)#{0:0,1:1,2:4,3:9,4:16}
print(type(d))#<class 'dict'>

g = (x * x   for   x   in   range(5))
print(g)#type and address of generator object
print(type(g))#<class generator>

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
print()#nothing is printed 
g = f2()
print(next(g))#10
print(next(g))#20
print(next(g))#30
print(next(g))#error


# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)#[10 , 20] <nxtlne>{30 , 40 , 50}<nxtlne> (60  , 70 , 80 , 90)<nxtlne> (100,)
	print(type(x))#<class 'list'> <class 'set'> <nxtlne> <class 'tuple'><nxtlne> <class 'tuple'>
#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))#it gives the approximate time that the statements take to execute and store the elements in the list .
print(timeit('( x * x   for  x  in  range(500) )'))#it gives the time that the stmt takes to exectue with out executing the statment
# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]#
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))# size thatcan store the 10000 elents in bits
print(sys . getsizeof(gen))#0



'''Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''
from time import sleep
def generator(a,b):
    try :
        print("sum :",end="")
        sleep(1)
        yield  a+b
        print("difference:",end="")
        sleep(1)
        yield a-b
        print("product:"  ,end="") 
        sleep(1)
        yield a*b
        print("division:",end="")
        sleep(1)
        yield a/b
    except: 
        print("zero division error")
a=int (input ("enter the a value:"))
b=int (input ("enter the b value:-"))
for x in generator(a,b):
	print(x)
	
	
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
Hint:  Use  generator  function  and  for  loop
Hint:  Do  not  use  range  object
'''
from time import sleep
def genrator(a,b):
    i=a
    while i<=b:
        sleep(1)
        yield i
        i+=1

a=int (input ("enter the a value:"))
b=int (input ("enter the b value:"))
i=a
for x in genrator(a,b):
    print(x)
        



'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'
Let  'x'  be  10
What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 
Hint:  Use  generator  function  and  for  loop
'''
from time import sleep
def generator(x):
    a=0
    b=1
    yield a 
    sleep(1)
    yield b
    sleep(1)
    c=a+b
    i=0
    while c<x:
        yield c
        sleep(1)
        a,b=b,c
        c=a+b
x=int(input("enter the value of x :"))

for x in generator(x):
    print(x)
print("End")



'''
Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class
'''
from time import sleep
def generator(string):
   s=string.split()
   for x in s:
      sleep(1)
      yield x
string=input("Enter a string : ")
for x in generator(string):
   print(x)


