# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->  # Class Variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->  # Instance Variable
		z = 30   #  What  is  variable   'z'  --->  # Local Variable
		c1 . m = 40   #  What  is  variable   'm'  --->  # Class Variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->  # Instance Variable
	c1 . q = 60   #  What  is  variable   'q'  --->  #  Class Variable
	s = 70   #  What  is  variable   's'  ---> Local Variable
#end of the function
k = 80   #  What  is  variable 'k'  --->  # Global Variable
c1 . l = 90   #  What  is  variable  'l'  --->  # Class Variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->  # Instance Variable




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
                # setter method
                # ''
p . name = 'Vamsi'  #   getter method
                     # setter method
                    #  Vamsi
print(p . name) # Vamsi
del   p . name  # Deleter method
                # getter  method
print(p . name)# error
del   p  # Destructor



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


(5, 25)
(6, 10.8)
(7, 'Hyd')
(8, True)
IndexError: list index out of range



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

(0, 'H')
(1, 'y')
(2, 'd')



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

{25, 10.8, 'Hyd', True, (3+4j)}
(0, 25)
(1, 10.8)
(2, 'Hyd')
(3, True)
(4, (3+4j))


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
disp(e1) #  (0, 'Empno')
           (1, 'Emp Name')
           (2, 'Sal')
e2 = enumerate(dict . values())
disp(e2)   
# (0, 25)
(1, 'Rama Rao')
(2, 10000.0)
e3 = enumerate(dict . items())
disp(e3)
# (0, 25)
(1, 'Rama Rao')
(2, 10000.0)
e4 = enumerate(dict , start = 5)
disp(e4)
# (5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')




# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)

Telangana            ...  Hyderabad
Andhra  Pradesh      ...  Amaravathi
Karnataka            ...  Bangalore
TamilNadu            ...  Chennai
Maharastra           ...  Mumbai