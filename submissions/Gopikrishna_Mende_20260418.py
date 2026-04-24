 # What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->  10 class variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> 20 instance variable
		z = 30   #  What  is  variable   'z'  ---> 30 local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> 40 class variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> 50 instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> 60 cclass 
	s = 70   #  What  is  variable   's'  ---> 70 local variable
#end of the function
k = 80   #  What  is  variable 'k'  --->  80 global variable
c1 . l = 90   #  What  is  variable  'l'  ---> 90 local variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable

# ========================================================================

# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . _name  =  ''
	@property
	def   name(self):
		print('getter  method') # getter
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method') # setter
		self .  _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
	def   __del__(self):
		print('Destructor') # Destructor
# End  of  the  class
p = Person()
print(p . name) # Empty
p . name = 'Vamsi'
print(p . name) #  vamsi
# del   p . name # Deleted
print(p . name) # Error
del   p # nothing

# ========================================================

# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e)) #(5,25) <next line> (6,10.8) <next line> (7,'Hyd')<next line>(8,True)
		time . sleep(1)
	except  StopIteration:
		break
print(list[5]) # Error


# =====================================================

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
disp(e1) # (0, 'Empno') <next line>  (1, 'Emp Name') <next line>  (2, 'Sal')
e2 = enumerate(dict . values())
disp(e2) # (0, 25) <next line>  (1, 'Rama Rao') <next line> (2, 10000.0)
e3 = enumerate(dict . items())
disp(e3) # (0,( 'empno':25)) (1, ('Emp Name', 'Rama Rao')) (2, ('Sal', 10000.0))
e4 = enumerate(dict , start = 5)
disp(e4) # (5, 'Empno') <next line> (6, 'Emp Name') <next line> (7, 'Sal')

# ==========================================================================

# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}') # Telangana ... Hyderabad  , Andhrapradesh ...Amaravati , Karnataka...Banglore, TamilNadu ...  Chennai, Maharastra...  Mumbai
	time . sleep(1) 
	