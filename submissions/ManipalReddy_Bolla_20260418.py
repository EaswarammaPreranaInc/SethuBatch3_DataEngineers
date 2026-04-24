# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable
		z = 30   #  What  is  variable   'z'  --->local variable method m1
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable class c1
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->instance variable
	c1 . q = 60   #  What  is  variable   'q'  --->static variable to class c1
	s = 70   #  What  is  variable   's'  --->local variable to function f1
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable
c1 . l = 90   #  What  is  variable  'l'  --->static variable to class c1
b = c1()
b . n = 100   #  What  is  variable  'n' --->instance variable


# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''#instance variable 'name' with value ''(empty string is created and beacuse 'name' is assignment triggers the Setter.
	@property
	def   name(self):
		print('getter  method')#getter method <next assignment> getter method <next accessing> getter method
		return  self . _name#return backup value which stored by setted method i.e ''# same process but now the modified p.__name backup variable value is return i.e Vamsi#now __name is not present inside self object i.e object p so attribute error raises
	@name . setter
	def   name(self , value):
		print('Setter  Method')#Setter Method <next assignment>#Setter Method
		self .  _name = value#__name='' is stored as backup value for getter method #same process now p.__name='Vamsi'
	@name . deleter
	def  name(self):
		print('Deleter  method ')#Deleter method
		del  self .  _name#p.__name is with value is deleted
	def   __del__(self):
		print('Destructor')#Destructor
# End  of  the  class
p = Person()#object created so __init__ executes 
print(p . name)#beacuse of accessing 'name' getter method executed
p . name = 'Vamsi'#beacuse variable assignment setter method is executed again
print(p . name)#beacuse accessing then getter method again
del   p . name#now name instance variable deleted and deleter is executed 
print(p . name)# accessing then getter method executed again 
del   p#object p is deleted so destructor executes


# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))#(5,25) <nextiteration with 1 sec pause> (6,10.8) <nextiteration with 1 sec pause> (7,'Hyd') <nextiteration with 1 sec pause> (8,True) 
		time . sleep(1)
	except  StopIteration:
		break# for nextiteration enumerate is traversed completly so stop iteration error raises then this except block break the loop and come out of it
print(list[5])#error


'''  
(Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))#(0,'H') <nextiteration with 1 sec pause> (1,'y') <nextiteration with 1 sec pause> (2,'d')
		time . sleep(1)
	except  StopIteration:
		break
		
		
#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a)#prints set a in any order
b = enumerate(a)
while   True:
	try:
		print(next(b))#iterates b which is set a and will be traversed in same order how set 'a' is printed and prints pair (0,set value)....
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
disp(e1)#(0, 'Empno') <nextiteration> (1, 'Emp Name') <nextiteration> (2, 'Sal')
e2 = enumerate(dict . values())
disp(e2)#(0, 25) <nextiteration> (1, 'Rama Rao') <nextiteration> (2, 10000.0)
e3 = enumerate(dict . items())
disp(e3)#(0, ('Empno', 25)) <nextiteration> (1, ('Emp Name', 'Rama Rao')) <nextiteration> (2, ('Sal', 10000.0))
e4 = enumerate(dict , start = 5)
disp(e4)#(5, 'Empno') <nextiteration> (6, 'Emp Name') <nextiteration> (7, 'Sal')




