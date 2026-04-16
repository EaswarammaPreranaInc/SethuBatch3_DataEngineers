
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
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
Modify  the  program  without  using  list



#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') # Begin
print(*g)
print('End')



#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # o^2 to upto 500000000000000000-1^2



#  Find  outputs (Home  work)
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



# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  # Error more values to unpack
p , q , r , s , m = f1()



#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) # Error generator has no function len
print(g * 3)  # Error 
print(g[0])  # Error there is no indexing for generator object 
print(g[1 : 3]) # Error there is no indexing for generator object
print(*g) # 1 2 3



# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: # Error there should be statement or pass after the defining the class



# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) # id of the class 
print(type(a)) # <class '__main__.c1'>
print(a . __dict__) # {}
print(a) # type and address of class
del  a # a is deleted
print(a) # Error a is not defined



#  Find  outputs  (Home  work)
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
a . m1() # 3rd method
m1() # Function



#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method :  10 20
a . m1(30) # Error one argument is missing
a . m1() # Error two arguments is missing



#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method :  10 20
a . m1(30) # Two  argument  method :  30 2
a . m1() # Two  argument  method :  1 2



# Find  outputs  (Home  work)
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
a . m1() # Method  of  third  c1  class



# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1() # Error c1 has no attribute m1



#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) # {}
a . x = 10
print(a . __dict__) # {'x': 10}
a . y = 20
print(a . __dict__) # {'x': 10, 'y': 20}
a . x = 30
print(a . __dict__) # {'x': 30, 'y': 20}
a . y = 40
print(a . __dict__) # {'x': 30, 'y': 40}
del  a . x
print(a . __dict__) # {'y':40}
del  a . y
print(a . __dict__) # Error
del   a
print(a . __dict__) # Error a is not defined


