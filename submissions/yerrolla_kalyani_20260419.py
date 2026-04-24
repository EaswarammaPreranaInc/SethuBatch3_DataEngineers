 # What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable 
		z = 30   #  What  is  variable   'z'  --->local variable for the method m1
		c1 . m = 40   #  What  is  variable   'm'  --->static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->instance variable for object a
	c1 . q = 60   #  What  is  variable   'q'  --->
	s = 70   #  What  is  variable   's'  --->static variable
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable 
c1 . l = 90   #  What  is  variable  'l'  --->static variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->non_Static variable or instance variable for object b


# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property#getter method 
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter#setter method
	def   name(self , value):
		print('Setter  Method')
		self .  _name = value
	@name . deleter#deleter method
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
	def   __del__(self):#destructor
		print('Destructor')
# End  of  the  class
p = Person()#Setter  Method
print(p . name)#getter  method  <nxt>   ''
p . name = 'Vamsi'#Setter  Method
print(p . name)#getter  method  <nxt>   Vamsi
del   p . name#Deleter  method 
print(p . name)#getter  method  <nxt>   ''
del   p #   Destructor



 # Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))#(5,25)<nxt>(6,10.8)<nxt>(7,'Hyd')<nxt>(8,True)
		time . sleep(1)
	except  StopIteration:
		break
print(list[5])#error ther is no index 5 in the list only 4 elements and 3 is the last index value of the list i.e.,list index out of range


'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))#(30,'H')<nxt>(1,'y')<nxt>(2,'d')
		time . sleep(1)
	except  StopIteration:
		break

# 
#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j}
b = enumerate(a)
while   True:
	try:
		print(next(b))#(0,25)<nxt>(1,10.8)<nxt>(2,'Hyd')<nxt>(3,True)<nxt>(4,(3+4j))
		time . sleep(1)
	except  StopIteration:
		break




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
disp(e1)#(0,'Empno')<nxt>(1,'Emp Name')<nxt>(2,'Sal')<nxt> nothing
e2 = enumerate(dict . values())
disp(e2)#(0,25)<nxt>(1,'Rama Rao')<nxt>(2,10000.0)<nxt> nothing
e3 = enumerate(dict . items())
disp(e3)#( 0  ,  ('Empno',25 ) )  <nxt>   (1  ,  ('Emp Name' ,'Rama Rao' ))  <nxt>   (2  ,  ('Sal', 10000.0))<nxt> nothing
e4 = enumerate(dict , start = 5)
disp(e4)#(5, 'Empno')<nxt>(6, 'Emp Name')<nxt>(7, 'Sal')<nxt> nothing



# # Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')# Telangana   ...  Hyderabad <nxt> Andhra Pradesh    ...  Amaravathi <nxt> Karnataka     ...  Bangalore <mxt> TamilNadu     ...  Chennai <nxt> Maharastra     ...  Mumbai
	time . sleep(1)