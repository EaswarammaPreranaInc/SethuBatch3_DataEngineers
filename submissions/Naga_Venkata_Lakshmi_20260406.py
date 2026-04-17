#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') #Begin
print(*g) #Error as there are too many elements to yield
print('End') #End.


#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g) #Error because when there are too many elements to yield.


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
#outputs
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


# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  #Value Error: too many values to unpack(expected 3)
p , q , r , s , m = f1()


#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) #Error because for length the argument should be sequence here g is the iterator. 
print(g * 3) #Error because repetition is not possible in iterators.
  
print(g[0]) #Error as  generator is not indexed because it is an empty object. 
print(g[1 : 3]) #Error because generator does not support slicing.
print(*g) # 1 2 3


# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: #Error expected an indented block after class definition.


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) #Address of a
print(type(a)) #<class'__main__.c1'>
print(a . _dict_) #{}
print(a) #<__main__.c1 object at address will be in hexadecimal>
del  a
print(a) #Name Error: name a is not defined.


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
a . m1(10 , 20) #Two argument method : 10 20
a . m1(30) #Error because missing one required positional argument.
a . m1() #Error because missing 2 required positional arguments.



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
a . m1(10 , 20) #Two argument method : 10 20 
a . m1(30) #Two argument method : 30 2
a . m1() #Two argument method : 1 2


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
a . m1() # Method of third c1 class.


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
a . m1() #Error because c1 object has no attribute 'm1'.



#  Find  outputs (Home  work)
class  c1:
        pass  
# End  of  class
a = c1()
print(a . _dict_) #{}
a . x = 10
print(a . _dict_) #{'x' : 10}
a . y = 20
print(a . _dict_) #{'x' : 10 , 'y' : 20}
a . x = 30
print(a . _dict_) #{'x' : 30 , 'y' : 20}
a . y = 40
print(a . _dict_) #{'x' : 30 , 'y' : 40}
del  a . x
print(a . _dict_) #{'y' : 40}
del  a . y
print(a . _dict_) #{}
del   a
print(a . _dict_) #Error



