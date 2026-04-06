#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)       # it unpacks elements of generator. but it takes long time due to big number

#========================================================================================================================

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

# One
# 1
# Two
# 2
# Three
# 3
# End
# One
# Two
# Three
# End
# 1
# 2
# 3

#========================================================================================================================

# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
# a , b , c = f1()  
# p , q , r , s , m = f1()

# there is four objects are given. but we are trying to unpack 3 and 5 objects

#========================================================================================================================

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
# print(len(g)) 	# error len() not permitted for generator
# print(g * 3)      # error multplication not permitted for generator
# print(g[0])       # error indexing not permitted for generator
# print(g[1 : 3])   # error slicing not permitted for generator
print(*g)           # 1 2 3

#========================================================================================================================

# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
# class   c3:

# arguments or pass must be give after defining a class

#========================================================================================================================

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))		# address of an object
print(type(a))		# <class '__main__.c1'>
print(a . __dict__)	# {}
print(a)		    # type and address of an object
del  a			
# print(a)	    	# error

#========================================================================================================================

#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')    # last function is excuted becoz all functions having same name 'm1'
# End  of  class  c1
a = c1()
a . m1()
m1()

# 3rd method
# Function

#========================================================================================================================

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)   # last function is excuted , becoz all fucntions are having same name 'm1'
# End  of  class  c1
a = c1()
a . m1(10 , 20)		# Two  argument  method : 10 20
# a . m1(30)		# error becoz there is 2 argumnents are required but 1 is given
# a . m1()		    # error becoz there is 2 argumnents are required but 0 is given

#========================================================================================================================

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
a . m1(10 , 20)		# Two  argument  method : 10 20
a . m1(30)		    # Two  argumnet  method : 30 2
a . m1()		    # Two  argument  method : 1 2

#========================================================================================================================

# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')   # last class and fucntion us excuted. becoz all classes and function having same name
a = c1()
a . m1()

# Method  of  third  c1  class

#========================================================================================================================

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
a . m1()

# it raises error becoz we are not passing any function to last class and remaining classes having fucntion

#========================================================================================================================

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)		# {}
a . x = 10
print(a . __dict__)		# {x : 10}
a . y = 20
print(a . __dict__)		# {x : 10 , y : 20}
a . x = 30
print(a . __dict__)		# {x : 30 , y : 20}
a . y = 40
print(a . __dict__)		# {x : 30 , y : 40}
del  a . x
print(a . __dict__)		# {y : 40}
del  a . y
print(a . __dict__)		# {}
del   a
# print(a . __dict__)	# error whole dictionary is deleted