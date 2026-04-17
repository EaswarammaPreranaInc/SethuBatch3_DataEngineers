#1
'''
Modify  the  program  without  using  list

import time
def   words(s):
	list = s . split()  #  ['Hyd' , 'is' , 'green' , 'city']
	for  x  in  list:
		yield  x
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string')
for  y  in   g:
	print(y)  #  Hyd , is , green , city
	time . sleep(1)
'''
import time
def words(s):
    yield from (x for x in s.split()) 
s = input('Enter any string : ') 
g = words(s)
print('Words of the string')
for y in g:
    print(y) 
    time.sleep(1)



#2
# Find outputs (Home work)
def f1():
    x = 1
    while x <= 100000000000000000000:
        yield x
        x += 1
g = f1()
print('Begin') # Begin
# print(*g) Error as MemoryError or Hangs indefinitely
print('End') #End



#3
#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
# print(*g) # Error as MemoryError / Hangs



#4
# Find outputs (Home work)
def f1():
    print('One')
    yield 1
    print('Two')
    yield 2
    print('Three')
    yield 3
    print('End')
g = f1()
for m in g:
    print(m) # One <next line> 1 <next line> Two <next line> 2 <next line> Three <next line> 3 <next line> End

x, y, z = f1() # Unpacking again! # One <next line> Two <next line> Three <next line> End
print(x) # 1
print(y) # 2
print(z) # 3



#5
# Identify error (Home work)
def f1():
    yield 10
    yield 20
    yield 30
    yield 40
# a, b, c = f1() 
# Error as having too many values to unpack (expected 3)
# p, q, r, s, m = f1() 
# Error as not having enough values to unpack (expected 5, got 4)



#6
# Find outputs (Home work)
def f1():
    yield 1
    yield 2
    yield 3
g = f1()
# print(len(g)) # Error as object of type 'generator' has no len()
# print(g * 3)  # Error as unsupported operand type(s) for *: 'generator' and 'int'
# print(g[0])   # Error as 'generator' object is not subscriptable
# print(g[1 : 3]) # Error as 'generator' object is not subscriptable
print(*g) # 1 2 3



#7
# Identify error (Home work)
class c1:
    def m1(self):
        pass
class c2:
    pass
class c3:
# Error as expected an indented block after class definition on line ...
    
    

#8
# Find outputs (Home work)
class c1:
    pass
a = c1()
print(id(a)) # Unique memory address (e.g., 1407...)
print(type(a)) # <class '__main__.c1'>
# print(a._dict_) # Error as 'c1' object has no attribute '_dict_'
print(a) # <__main__.c1 object at ...>
del a
# print(a) #Error as name 'a' is not defined



#9
# Find outputs (Home work)
def m1():
    print('Function')
class c1:
    def m1(self):
        print('1st method')
    def m1(self):
        print('2nd method')
    def m1(self):
        print('3rd method')
a = c1()
a.m1() # 3rd method 
m1() # Function



#10
# Find outputs (Home work)
class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method : ', x)
    def m1(self, x, y):
        print('Two argument method : ', x, y)
a = c1()
a.m1(10, 20) # Two argument method : 10 20
# a.m1(30)   # Error as m1() missing 1 required positional argument: 'y'
# a.m1()     # Error as m1() missing 2 required positional arguments: 'x' and 'y'



#11
# Find outputs (Home work)
class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    def m1(self):
        print('Method of third c1 class') 
a = c1()
a.m1() # Method of third c1 class



#12
# Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of second c1 class')
class c1:
    pass 
a = c1()
# a.m1() # Error as 'c1' object has no attribute 'm1'



#13
# Find outputs (Home work)
class c1:
    pass
a = c1()
# print(a.__dict__) # {} (Empty dict)
a.x = 10
# print(a.__dict__) # {'x': 10}
a.y = 20
# print(a.__dict__) # {'x': 10, 'y': 20}
a.x = 30 # Updates existing key
# print(a.__dict__) # {'x': 30, 'y': 20}
del a.x
# print(a.__dict__) # {'y': 20}
del a
# print(a.__dict__) # Error as name 'a' is not defined.