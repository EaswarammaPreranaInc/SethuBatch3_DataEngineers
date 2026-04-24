# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable
		z = 30   #  What  is  variable   'z'  --->local variable
		c1 . m = 40   #  What  is  variable   'm'  --->static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->instance variable
	c1 . q = 60   #  What  is  variable   'q'  --->static variable
	s = 70   #  What  is  variable   's'  --->local
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable
c1 . l = 90   #  What  is  variable  'l'  --->static variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->instance variable
------------------------------------------------------------------------------------------------------
# Find  outputs (Home work)
class  Person:
	def  _init_(self):
		self . name  =  ''            #Setter Method
	@property                             #getter method
	def   name(self):                     #""
		print('getter  method')       #Setter Method  stores backup variable with vamsi
		return  self . _name          #getter method
	@name . setter                        #Vamsi
	def   name(self , value):             #Deleter method  deletes backup variable
		print('Setter  Method')       #getter method error    
		self .  _name = value         #Destructor
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
	def   _del_(self):
		print('Destructor')
# End  of  the  class
p = Person()
print(p . name) #
p . name = 'Vamsi'
print(p . name)
del   p . name
print(p . name)
del   p
--------------------------------------------------------------------------------
 # Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:                      #(5,25)
	try:                       #(6,10.8)
		print(next(e))     #(7,Hyd)
		time . sleep(1)    #(8,True)
	except  StopIteration:
		break
print(list[5])   #error because no index 5
-----------------------------------------------------------------------------
'''  (Home  work)
Can  string  be  enumerated ?  #Yes
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)                      #(0,H)
while   True:                         #(1,y)
	try:                          #(2,d)
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
---------------------------------------------------------------------------
 #  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a)     #{25 , 10.8 , 'Hyd' , True , 3+4j}
b = enumerate(a)                  #(0,25)
while   True:                     #(1,10.8)
	try:                      #(2,Hyd)
		print(next(b))    #(3,True)
		time . sleep(1)   #(4,3+4j)
	except  StopIteration:
		break
-----------------------------------------------------------------------------
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
e1 = enumerate(dict . keys())   #(0,Empno)/n(1,Emp Name)/n(2,Sal)
disp(e1)
e2 = enumerate(dict . values())  #(0,25)/n(1,Rama Rao)/n(2,10000.0)
disp(e2)
e3 = enumerate(dict . items())   #(0,(Empno,25))/n(1,(Emp Name,Rama Rao))/n(2,(Sal,10000.0))
disp(e3)
e4 = enumerate(dict , start = 5)  #(5,Empno)/n(6,Emp Name)/n(7,Sal)
disp(e4)
------------------------------------------------------------------------------
 # Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)