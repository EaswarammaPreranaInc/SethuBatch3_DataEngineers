# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x) # 25 <next line> 10.8 <next line> Hyd
for  x  in  f1():
	print(x) # 25 <next line> 10.8 <next line> Hyd
for  x  in  f1():
	print(x) # 25 <next line> 10.8 <next line> Hyd

# ===============================================================

#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # 0, 1,4,9,24
print(type(l)) # <list >

s = {x * x   for   x   in   range(5)}
print(s) #{0, 1, 4, 9, 16}
print(type(s)) # <set>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0:0,1:1,2:4,3:6,4:16}
print(type(d)) # <Dictionary>

g = (x * x   for   x   in   range(5))
print(g) # 0, 1,4,9,24
print(type(g)) # <Generator>

# ===========================================================
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
print(f1()) # 10
print(f1()) #10
print() # Empty
g = f2()
print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g))# Error

# ===========================================================================

'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
'''

def f1(n, m):
    yield ("sum",n+m)
    yield("Difference",n-m)
    yield("Product",n*m)

    if m!=0:
        yield("Division",n/m)
    else:
        yield("DIvision","undefined")

n=eval(input("Enter a number:"))
m=eval(input("Enter a number:"))

for x,y in f1(n,m):
    print(f"{x}:{y}")


# =================================================================================

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
# '''
def f1(a,b):
    current=a
    while current<=b:
        yield current
        current+=1


a=eval(input("Enter a number:"))
b=eval(input("ENter a number:"))

for x in f1(a,b):
    print(x)

# ====================================================================

'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
def f1(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
n=eval(input("ENter a number:"))
for i in f1(n):
    print(i, end=" ")


# ===================================================================

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

def f1(n):
    words=n.split()
    for word in words:
        yield word
n=eval(input("Enter a input:"))
for i in f1(n):
    print(i)

# ======================================================================

# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)  #[10,20],{30,40,50} , (60,70,80,90) , 100
	print(type(x))# <class list>,<class dict> ,<class tuple>, <class int>
         
# ====================================================================

#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]')) #20.1092
print(timeit('( x * x   for  x  in  range(500) )')) #0.13

# =======================================================================

# Find  outputs
import  sys
list = [x * x   for  x  in  range(10000)]
gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list)) #85176
print(sys . getsizeof(gen)) #200