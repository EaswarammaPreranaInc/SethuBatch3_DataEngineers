# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->class variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable
		z = 30   #  What  is  variable   'z'  --->local variable
		c1 . m = 40   #  What  is  variable   'm'  --->class variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->instance variable
	c1 . q = 60   #  What  is  variable   'q'  --->class variable
	s = 70   #  What  is  variable   's'  --->local variable
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable
c1 . l = 90   #  What  is  variable  'l'  --->class variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->instance variable






 # Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''#calls setter
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')#setter method
		self .  _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')#Deleter  method
		del  self .  _name
	def   __del__(self):
		print('Destructor')
# End  of  the  class
p = Person()#calls __init__ 
print(p . name)#getter method(prints empty string)
p . name = 'Vamsi'#calls setter 
print(p . name)#getter method <next line> Vamsi
del   p . name#calls deleter
print(p . name)#getter method and error
del   p   #destructor




# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))#(5, 25)<nextline>(6, 10.8)<nextline>(7, 'Hyd')<nextline>(8, True)
		time . sleep(1)
	except  StopIteration:
		break
print(list[5])#error (no index[5])



'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))#(0, 'H')<nextline>(1, 'y')<nextline>(2, 'd')
		time . sleep(1)
	except  StopIteration:
		break




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
'''
ouput
(0, 25)
(1, 'Hyd')
(2, True)
(3, (3+4j))
(4, 10.8)	    
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
disp(e1)#(0, 'Empno')<nextline>(1, 'Emp Name')<nextline>(2, 'Sal')
e2 = enumerate(dict . values())
disp(e2)#(0, 25)<nextline>(1, 'Rama Rao')<nextline>(2, 10000.0)
e3 = enumerate(dict . items())
disp(e3)#(0, ('Empno', 25))<nextline>(1, ('Emp Name', 'Rama Rao'))<nextline>(2, ('Sal', 10000.0))
e4 = enumerate(dict , start = 5)
disp(e4)#(5, 'Empno')<nextline>(6, 'Emp Name')<nextline>(7, 'Sal')



 # Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)
'''
output
Telangana            ... Hyderabad
Andhra Pradesh       ... Amaravathi
Karnataka            ... Bangalore
TamilNadu            ... Chennai
Maharastra           ... Mumbai
'''
	
	
