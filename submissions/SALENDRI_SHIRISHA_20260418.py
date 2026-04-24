# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  # class variable  'x'  
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->
		z = 30   #  What  is  variable   'z'  --->
		c1 . m = 40   # class variable   'm'  
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
	def   __del__(self):
		print('Destructor')
# End  of  the  class
p = Person()
print(p . name) # ''
p . name = 'Vamsi'
print(p . name) # Vamsi
del   p . name
print(p . name) # Error due to del
del   p


# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))    # (5 , 25)
                          # (6 , 10.8)
                          # (7 , Hyd)
                          # (8 , True)
		time . sleep(1)
	except  StopIteration:
		break
print(list[5])  # 25


'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))  # (0 , H)
                        # (1 , y)
                        # (2 , d)
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
disp(e1)
e2 = enumerate(dict . values())
disp(e2)
e3 = enumerate(dict . items())
disp(e3)
e4 = enumerate(dict , start = 5)
disp(e4)


# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')  #  Telangana             ...  Hyderabad
                                             #  Andhra  Pradesh       ...  Amaravathi
                                             #  Karnataka             ...  Bangalore
                                             #  TamilNadu             ...  Chennai
                                             #  Maharastra            ...  Mumbai
	time . sleep(1)
    
    
