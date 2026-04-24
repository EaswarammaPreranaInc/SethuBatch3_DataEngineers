# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  # static variable of class c1 with value 10
	def    m1(self):	# method
		self . y = 20   #  What  is  variable  'y'  ---> instance variable becoz creating variable w.r.t object 'self'
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  --->  static variable of class c1 with value 40
#end of the class
def    f1():	# function
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable of class c1 with value 60
	s = 70   #  What  is  variable   's'  ---> local variable
#end of the function
k = 80        #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable of class c1 with value 90
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable of object b with value 100

# static variable  ---> it is global to all objects in same class	 (classname.variable)
# local variable   ---> it is global to that method or function defined  (methodname.variable)
# global variable  ---> it is global to all objects , function , methods of a class (variable)

#=================================================================================================================================

# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''	# instance variable with empty string
	@property	# getter
	def   name(self):
		print('getter  method')
		return  self . _name	# return ""  , it is backup variable
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self .  _name = value	# backup variable with value vamsi
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name	# deletes backup variable
	def   __del__(self):
		print('Destructor')
# End  of  the  class
p = Person()
print(p . name)		# Setter method
p . name = 'Vamsi'
print(p . name)		# setter method , vamsi
del   p . name		# deletes backup variable vamsi
# print(p . name)		# error name method is deleted
del   p			    # object p is deleted and __del__ is excuted before deleting the class.

# Setter  Method
# getter  method

# Setter  Method
# getter  method
# Vamsi
# Deleter  method 
# Destructor

#=================================================================================================================================

# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)     # index starts with 5
while   True:
	try:
		print(next(e))      # due to next output returns in the form of tuples.
		time . sleep(1)
	except  StopIteration:
		break
# print(list[5])    # error , becoz list have only 4 elements

# (5, 25)
# (6, 10.8)
# (7, 'Hyd')
# (8, True)

#=================================================================================================================================

'''  (Home  work)
Can  string  be  enumerated ?  --->  YES
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))      # due to presence of next, result will return in tuples
		time . sleep(1)
	except  StopIteration:
		break

# (0, 'H')
# (1, 'Y')
# (2, 'D')

#=================================================================================================================================

#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a) 
b = enumerate(a)
while   True:
	try:
		print(next(b))
		time . sleep(1)
	except  StopIteration:
		break

# (0 , 25)
# (1 , 10.8)
# (2 , 'Hyd')
# (3 , True)
# (4 , 3+4j)
# but order will be changed, because set is unorderd.

#=================================================================================================================================

# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except  StopIteration:
			break
	print()
dict = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
e1 = enumerate(dict . keys())
disp(e1)
e2 = enumerate(dict . values())
disp(e2)
e3 = enumerate(dict . items())
disp(e3)
e4 = enumerate(dict , start = 5)
disp(e4)

# (0 , 'Empno')
# (1 , 'Emp name')
# (2 , 'Sal')

# (0 , 25)
# (1 , 'Rama rao')
# (2 , 10000.0)

# (0 , ('Empno',25))
# (1 , ('Emp name','Rama Rao'))
# (2 , ('Sal',10000.0))

# (5 , 'Empno')
# (6 , 'Emp name')
# (7 , 'Sal')

#=================================================================================================================================

# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)
	
# Telangana             ...  Hyderabad
# Andhra  Pradesh       ...  Amaravathi
# Karnataka             ...  Bangalore
# TamilNadu             ...  Chennai
# Maharastra            ...  Mumbai