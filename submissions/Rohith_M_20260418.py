import   time
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static varible
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance varible
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'   --->  instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static varible
	s = 70   #  What  is  variable   's'       --->local variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable



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
print(p . name)    # empty string 
p . name = 'Vamsi' # updating instance varible
print(p . name)    # Vamsi
del   p . name     # deletes backup and original varibles
#print(p . name)    # error
del   p             


import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)
'''
telangana        ... Hyderabad
Andhra Pradesh   ... Amaravathi
Karnataka        ... bangalore
tamil nadu       ... chennai
Maharastra       ... Mumbai
'''
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

'''
(0,'empno')
(1,'empname')
(2,'sal')
(0,25)
(1,'rama roa')
(2,10000.0)
(0,('empno',25))
(1,('empname','rama rao'))
(2,('sal',10000.0))
(5,'empno')
(6,'empname')
(7,'sal')
'''


a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a) 
b = enumerate(a)
while   True:
	try:
		print(next(b))
		time . sleep(1)
	except  StopIteration:
		break

'''
(0,10.8)
(1,'hyd')
(2,3+4j)
(3,True)
(4,10)


'''


list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
#print(list[5]) #error
'''
(5,25)
(6,10.8)
(7,'hyd')
(8,True)


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
(0,'h')
(1,'y')
(2,'d')
'''


