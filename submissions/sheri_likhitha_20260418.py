# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->  static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->  instance variable
		z = 30   #  What  is  variable   'z'  ---> local variable inside method
		c1 . m = 40   #  What  is  variable   'm'  ---> class variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> class variable
	s = 70   #  What  is  variable   's'  ---> local variable inside function
#end of the function
k = 80   #  What  is  variable 'k'  --->   global variable 
c1 . l = 90   #  What  is  variable  'l'  ---> class variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance vaariable for object b





# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  '' #blank line
	@property
	def   name(self):
		print('getter  method')
		return  self . _name	#error because it is deleted
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
print(p . name)	#setter method \n getter method
p . name = 'Vamsi' #setter method
print(p . name)	#getter method \n vamsi
del   p . name	#deleter method
print(p . name)	#getter method
del   p		#destructor




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
print(list[5])   #(5,25) \n (6,10.8) \n (7,'Hyd') \n (8, True)  error: index out of range





'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)	#(0,'H') \n (1,'y') \n (2,'d')
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break




#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a)	# {25 , 10.8 , 'Hyd' , True , 3+4j}
b = enumerate(a)
while   True:
	try:
		print(next(b))
		time . sleep(1)
	except  StopIteration:
		break

(0, True)
(1, 3+4j)
(2, 10.8)
(3, 'Hyd')
(4, 25)




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
disp(e1)	#(0,'Empno') \n (1,'Emp name') \n (2,'sal')
e2 = enumerate(dict . values())
disp(e2)	#(0,'25') \n (1,'Rama rao') \n (2,'10000.0')
e3 = enumerate(dict . items())
disp(e3)	#(0,('Empno',25)) \n (1,('Emp name','Rama rao')) \n (2,('sal',10000.o))
e4 = enumerate(dict , start = 5)
disp(e4)	#(5,'Empno') \n (6,'Emp Name') \n (7,'sal')




# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)	#(0,'Telangana') \n (1,'Andhra Pradesh') \n (2,'Karnataka') \n (3,'Tamilnadu') \n (4,'Maharastra')
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1) 

Telangana            ...  Hyderabad
Andhra  Pradesh      ...  Amaravathi
Karnataka            ...  Bangalore
TamilNadu            ...  Chennai
Maharastra           ...  Mumbai