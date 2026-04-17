1.'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
def   words(s):
	#list = s . split()  #  ['Hyd' , 'is' , 'green' , 'city']
	for  x  in  s.split():
		yield x
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string')
for  y  in   g:
	print(y)  #  Hyd , is , green , city
	time . sleep(1)





2.#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)
print('End')
'''
Begin
MemoryError
'''



3.#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
'''
MemoryError
'''



4.#  Find  outputs (Home  work)
def  f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)
'''
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
'''



5.# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  
p , q , r , s , m = f1()
'''
ValueError: too many values to unpack (expected 3)

ValueError: not enough values to unpack (expected 5, got 4)
'''



6.#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))   # TypeError: object of type 'generator' has no len()
#print(g * 3)    # TypeError: unsupported operand type(s) for *: 'generator' and 'int'
#print(g[0])     # TypeError: 'generator' object is not subscriptable
#print(g[1 : 3]) # TypeError: 'generator' object is not subscriptable
print(*g)
'''
1 2 3
'''




7.# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
'''
IndentationError: expected an indented block after class definition on line 130
'''



8.# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))# Address  of the c1 class
print(type(a)) # <class '__main__.c1'>
print(a . __dict__) # {}
print(a) # <__main__.c1 object at 0x000001592081C210>
del  a
print(a) # NameError: name 'a' is not defined




9.#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()
a . m1()
m1()
'''
3rd method
Function
'''




10.#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two arguments method : 10 20

a . m1(30) # TypeError: c1.m1() missing 1 required positional argument: 'y'
a . m1()   # TypeError: c1.m1() missing 2 required positional arguments: 'x' and 'y'





11.#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()
'''
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2
'''




12.# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()
'''
Method of thrd c1 class
'''



13.# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
#a . m1() # AttributeError: 'c1' object has no attribute 'm1'




14.#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)
a . x = 10
print(a . __dict__)
a . y = 20
print(a . __dict__)
a . x = 30
print(a . __dict__)
a . y = 40
print(a . __dict__)
del  a . x
print(a . __dict__)
del  a . y
print(a . __dict__)
del   a
#print(a . __dict__) # NameError: name 'a' is not defined

'''
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}
'''