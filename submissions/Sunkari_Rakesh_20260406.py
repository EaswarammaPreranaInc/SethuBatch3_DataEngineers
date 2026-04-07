Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

Modify  the  program  without  using  list
 
# prog
import time
def   words(s):
	l = s . split()  #  ['Hyd' , 'is' , 'green' , 'city']
	for  x  in  l:
		yield  x
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string are')
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
print('Begin')
print(*g)
print('End')

# output
Begin
unpacking the generator
x elements are stored in the generator 
memory error
End



#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000)) # generator expression
print(*g) # generator unpack and stores all the elements in the generator and memory error




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
g = f1() # creates an empty generator
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x) 
print(y) 
print(z) 

# output
one
1
Two
2
Three
3
End
one
Two
Three 
End





# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  
p , q , r , s , m = f1()

# error





#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))  # error bec the generator is empty
print(g * 3)   # * means the repatation operator, hence generator cant be repeated
print(g[0])    # error bec there is no indexing in generator
print(g[1 : 3])# error bec there is no slicing in generator
print(*g)	# generator unpacking --> 1 <next line> 2 <next line> 3 <next line>






# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:

# error in the last class c3, bec there are no statements in class c3





 # Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) # address if class c1
print(type(a)) # class __main__.
print(a . _dict_) # coneverts a to dictionary
print(a) # key,values pairs of a
del  a # a is deleted i.e: the c1 class is deleted
print(a) # error bec there is no a, already deleted








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
a . m1()
m1()

# output
3rd method
Function





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
a . m1(10 , 20)
a . m1(30)
a . m1()

# output
Two arguement method : 10 ,20
Single  argument  method : 30
No arguement method



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
a . m1(10 , 20)
a . m1(30)
a . m1()

#output
Two  argument  method : 10 , 20






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
a . m1()


# output
 Method  of  third  c1  class





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

# output
no output bec the pass is executed






#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) 
a . x = 10
print(a . _dict_) 
a . y = 20
print(a . _dict_)
a . x = 30
print(a . _dict_)
a . y = 40
print(a . _dict_)
del  a . x
print(a . _dict_)
del  a . y
print(a . _dict_)
del   a
print(a . _dict_)


# output

error