# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable
		z = 30   #  What  is  variable   'z'  ---> local variable 
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> local variable 
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable 
b = c1()
b . n = 100   #  What  is  variable  'n' --->instance variable
'''

'''


# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self .  _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
	def   __del__(self):
		print('Destructor')
# End  of  the  class
p = Person() 
print(p . name) # getter method 
p . name = 'Vamsi'
print(p . name) # vamsi 
del   p . name # deleter method and desructor 
print(p . name) # getter method 
del   p # destructor


# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
print(list[5])
'''
(5, 25)
(6, 10.8)
(7, 'Hyd')
(8, True)
Error
'''


'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
'''
(0, 'H')
(1, 'Y')
(2, 'D')
'''

	
#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a) # {25, 10.8 'Hyd', True, 3+4j}
b = enumerate(a)
while   True:
	try:
		print(next(b))
		time . sleep(1)
	except  StopIteration:
		break
'''
(0, 25)
(1, 10.8)
(2, 'Hyd')
(3, True)
(4, 3+4j)
'''

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
disp(e1) # (0, 'Empno')<next line>(1, 'Empname')<next line>(3, 'sal')
e2 = enumerate(dict . values())
disp(e2) # (0, 25) <next line> (1, 'Rama Rao') <next line> (2, 10000.0)
e3 = enumerate(dict . items())
disp(e3) # (0,('Empno', 25)) (1,('Empname', 'RamaRao')) (2 ('Sal' 10000.0))
e4 = enumerate(dict , start = 5)
disp(e4) # (5, 'Empno')<next line>(6, 'Empname')<next line>(7, 'sal')


# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)
'''
Telangana   ...Hyderabad
Andhra  Pradesh   ...Amaravathi
Karnataka   ...Bangalore
TamilNadu   ...Chennai
Maharastra  ...Mumbai
'''