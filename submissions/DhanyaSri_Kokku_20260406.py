'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

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
'''
import time
def   words(s):
    a = 0
    b = s.find(' ',a)
    i = 0
    while i < len(s):
        yield s[a:b]
        i+= len(s[a:b])+1
        a = b+1
        b = s.find(' ',a)
        if b==-1:
             b=len(s)
  
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string')
for  y  in   g:
	print(y)  #  Hyd , is , green , city
	time . sleep(1)


#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') # Begin
print(*g) # More waiting time taken because all the values are stored in the generator object in unpacking
print('End') # End

#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # Memory error because all the values are appended to the generator in unpacking

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

''' Outputs:
One
1
Two
2
Three
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
a , b , c = f1() # Error because less number of variables for unpacking 
p , q , r , s , m = f1() # Error because more number of variables for unpacking

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) # Error length of generator does not exist
print(g * 3) # Error generator does not have repetation 
print(g[0])  # Error generator does not have indexing 
print(g[1 : 3]) # Error generator does not have slicing
print(*g) # 1 2 3


# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:  # class c3 should have at least a method or a pass statement then it is considered as empty class

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) # Address of class c1 object
print(type(a)) # <class '__main__.c1'>
print(a . _dict_) # {}
print(a) # <class '__main__.c1'> and address of class c1 object
del  a 
print(a) # Error name a is not defined

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
a = c1() # Object for class c1 is created
a . m1() # 3rd  method
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
a = c1() # Object of class c1 is created
a . m1(10 , 20) # Two  argument  method : 10 20
a . m1(30) # Error m1() method requires two arguments but not one
a . m1() # Error m1() method requires two arguments 

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() # Object of class c1 is created
a . m1(10 , 20) # Two  argument  method : 10 20
a . m1(30) # Two  argument  method : 30 2
a . m1() # Two  argument  method : 1 2

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
a = c1() # Object of class c1 is created
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
a = c1() # Object of class c1 is created
a . m1() # Error c1 class does not have method m1

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) # {}
a . x = 10
print(a . _dict_) # {'x' : 10}
a . y = 20
print(a . _dict_) # {'x' : 10 , 'y' : 20}
a . x = 30
print(a . _dict_) # {'x' : 30 , 'y' : 20}
a . y = 40
print(a . _dict_) # {'x' : 30 , 'y' : 40}
del  a . x
print(a . _dict_) # {'y' : 20}
del  a . y
print(a . _dict_) # {}
del   a
print(a . _dict_) # Error name a is not defined