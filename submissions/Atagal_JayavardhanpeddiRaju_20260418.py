# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->
		z = 30   #  What  is  variable   'z'  --->
		c1 . m = 40   #  What  is  variable   'm'  --->
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->
	c1 . q = 60   #  What  is  variable   'q'  --->
	s = 70   #  What  is  variable   's'  --->
#end of the function
k = 80   #  What  is  variable 'k'  --->
c1 . l = 90   #  What  is  variable  'l'  --->
b = c1()
b . n = 100   #  What  is  variable  'n' --->


class c1:
    x = 10        # Class variable
    def m1(self):
        self.y = 20   # Instance variable
        z = 30        # Local variable
        c1.m = 40     # Class variable
#end of the class

def f1():
    a = c1()
    a.p = 50     # Instance variable
    c1.q = 60    # Class variable
    s = 70       # Local variable
#end of the function

k = 80          # Global variable
c1.l = 90       # Class variable
b = c1()
b.n = 100       # Instance variable



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
	def   _del_(self):
		print('Destructor')
# End  of  the  class
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
print(p . name)
del   p

Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method 
getter  method
Error

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
		
Enter  any  string  :  python
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')

{True, (3+4j), 25, 10.8, 'Hyd'}
(0, True)
(1, (3+4j))
(2, 25)
(3, 10.8)
(4, 'Hyd')


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
disp(e1)
e2 = enumerate(dict . values())
disp(e2)
e3 = enumerate(dict . items())
disp(e3)
e4 = enumerate(dict , start = 5)
disp(e4)

(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

(0, 25)
(1, 'Rama Rao')


(2, 10000.0)

(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))

(2, ('Sal', 10000.0))

(5, 'Empno')
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
	
Telangana             ...  Hyderabad
Andhra  Pradesh       ...  Amaravathi
Karnataka             ...  Bangalore
TamilNadu             ...  Chennai
Maharastra            ...  Mumbai

