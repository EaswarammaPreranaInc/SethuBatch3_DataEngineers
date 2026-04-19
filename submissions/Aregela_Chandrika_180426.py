# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> Instance Variable
		z = 30   #  What  is  variable   'z'  ---> Local Variable
		c1 . m = 40   #  What  is  variable   'm'  --->  static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> Instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> Local Variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> Instance variable




# Find  outputs (Home work)
class  Person:
	def  _init_(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method') # getter method
		return  self . _name  #  '' 
	@name . setter
	def   name(self , value):
		print('Setter  Method') # Setter Method
		self .  _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')  # Deleter method
		del  self .  _name
	def   _del_(self):
		print('Destructor')
# End  of  the  class
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
print(p . name) # Vamsi
del   p



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
print(list[5]) # # (5, 25) <nextline> (6, 10.8)  <nextline> (7, 'Hyd')
 (8, True)  <nextline> Error  <nextline>






'''  (Home  work)
Can  string  be  enumerated ? - YES 
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e)) # (0, 'H') <nextline>  (1, 'y') <nextline>  (2, 'd')
		time . sleep(1)
	except  StopIteration:
		break




#  Can  set  be  enumerated  ?  YES  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a) 
b = enumerate(a)
while   True:
	try:
		print(next(b)) # (0, 25) <nl> (1, 10.8) <nl> (2,'Hyd') <nl> (3, True) <nl> (3+4j)
		time . sleep(1)
	except  StopIteration:
		break





# Can  dictionary  be  enumerated ?   YES 
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
disp(e1) # (0,Empno), (1,Emp Name), (2,Sal)
e2 = enumerate(dict . values())
disp(e2) # 25, 'Rama Rao', 10000.0
e3 = enumerate(dict . items())
disp(e3) # (0,('Empno', 25)) <nl> (1,('Emp Name', 'Rama Rao')) <nl> (2,('Sal', 10000.0))
e4 = enumerate(dict , start = 5)
disp(e4) # (5, 'Empno')  (6, 'Emp Name')  (7, 'Sal')




# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)
    
'''
Telangana...  Hyderabad
Andhra  Pradesh...  Amaravathi
Karnataka...  Bangalore
TamilNadu...  Chennai
Maharastra...  Mumbai
'''