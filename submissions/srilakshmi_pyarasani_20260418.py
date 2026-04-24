1) What  are  k , l ,  x , y , z , m , n , p , q , s ?
class   c1:
	x = 10  #  What  is  variable  'x'  ---> Static Variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> Instance Variable
		z = 30   #  What  is  variable   'z'  ---> Local Variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static Variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> Instance Variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static Variable
	s = 70   #  What  is  variable   's'  ---> Local Variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> Global Variable
c1 . l = 90   #  What  is  variable  'l'  ---> static Variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> Instance Variable

2) outputs 
class  Person:
	def  _init_(self):
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
	def   _del_(self):
		print('Destructor')
# End  of  the  class
p = Person()#setter method
print(p . name)#getter method
p . name = 'Vamsi'#setter method
print(p . name)#getter method
del   p . name#deleter method
print(p . name)#Error because it is not vlaid
del   p#Destructor

3) outputs 
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
print(list[5])#Error because enumerate works on indexes, but not list indexes
#(5, 25)
(6, 10.8)
(7, 'Hyd')
(8, True)

4) Can  string  be  enumerated ? Yes, string can be enumerated
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
#(0, 'H')
(1, 'y')
(2, 'd')

5) Can  set  be  enumerated  ?  Yes, set an be enumerated 
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
#{25, 10.8, 'Hyd',True, (3+4j)}
(0, 25)
(1, 10.8)
(2, 'Hyd')
(3, True)
(4, (3+4j))

6) Can  dictionary  be  enumerated ?    Yes, dictionary can be enumerated
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
disp(e1)#(0, 'Empno')
         (1, 'Emp Name')
	 (2, 'Sal')
e2 = enumerate(dict . values())
disp(e2)#(0, 25)
	 (1, 'Rama Rao')
	 (2, 10000.0)
e3 = enumerate(dict . items())
disp(e3)#(0, ('Empno', 25))
	 (1, ('Emp Name', 'Rama Rao'))
	 (2, ('Sal', 10000.0))
e4 = enumerate(dict , start = 5)
disp(e4)#(5, 'Empno')
	 (6, 'Emp Name')
	 (7, 'Sal')

7) outputs 
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)
#Telangana             ...  Hyderabad
Andhra  Pradesh       ...  Amaravathi
Karnataka             ...  Bangalore
TamilNadu             ...  Chennai
Maharastra            ...  Mumbai