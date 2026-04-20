# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)

class   c1:

	x = 10  #  What  is  variable  'x'  ---> static var

	def    m1(self):

		self . y = 20   #  What  is  variable  'y'  ---> #instance var

		z = 30   #  What  is  variable   'z'  ---># local var

		c1 . m = 40   #  What  is  variable   'm'  ---># static var

#end of the class

def    f1():

	a = c1()

	a . p = 50   #  What  is   variable  'p'  --->Instace var

	c1 . q = 60   #  What  is  variable   'q'  ---># static var

	s = 70   #  What  is  variable   's'  ---># local var

#end of the function

k = 80   #  What  is  variable 'k'  ---># global var

c1 . l = 90   #  What  is  variable  'l'  ---># static var

b = c1()

b . n = 100   #  What  is  variable  'n' ---># instance var





# Find  outputs (Home work)

class  Person:

	def  __init__(self):

		self . name  =  ''

	@property

	def   name(self):

		print('getter  method')

		return  self . _name

	@name.setter

	def   name(self , value):

		print('Setter  Method')

		self .  _name = value

	@name.deleter

	def  name(self):

		print('Deleter  method ')

		del  self .  _name

	def   __del__(self):

		print('Destructor')

# End  of  the  class

p = Person()#Setter  Method , 

print(p . name)# Getter Method , ''

p . name = 'Vamsi'# Setter Method

print(p . name)# Getter Method, Vamsi

del   p . name# Deleter Method

#print(p . name)# getter Method  and Error

#del   p# error



# Find  outputs (Home  work)

import   time

list = [25 , 10.8 , 'Hyd' , True]

e = enumerate(list , start = 5)

while   True:

	try:

		print(next(e))# (5,25), (6,10.8), (7,'Hyd'), (8,True)

		time . sleep(1)

	except  StopIteration:

		break

#Errorprint(list[5])'''



'''  (Home  work)

Can  string  be  enumerated ?



import   time

a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'

e = enumerate(a)

while   True:

	try:

		print(next(e))# (0,'H'), (1,'y'), (2,'d')

		time . sleep(1)

	except  StopIteration:

		break





# Can  dictionary  be  enumerated ?   (Home  work)

import   time

def  disp(e):

	while  True:

		try:

			print(next(e))# (0,'Empno'),(1,'Emp Name'), (2,'Sal')

			time . sleep(1)

		except  StopIteration:

			break

	print()

dict = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}

e1 = enumerate(dict . keys())

disp(e1)## (0,'Empno'),(1,'Emp Name'), (2,'Sal')

e2 = enumerate(dict . values())

disp(e2)## (0,25),(1,'Rama Rao'), (2,10000.0)

e3 = enumerate(dict . items())

disp(e3)# # (0,('Empno',25)),(1,('Emp Name','Rama Rao')), (2,('Sal',10000.0))

e4 = enumerate(dict , start = 5)

disp(e4)# (5,'Empno'),(6,'Emp Name'), (7,'Sal')





# Find  outputs  (Home  work)

import   time

a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']

b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']

e = enumerate(a)

for   index ,  element  in  e:

	print(F'{element:20}  ...  {b[index]}') 

	time . sleep(1)

# Telangana ... Hyderabad, Andhra Pradesh ... Amaravati,Karnataka : Banglore, Tamilnadu ... Chennai, Maharastra: Mumbai
