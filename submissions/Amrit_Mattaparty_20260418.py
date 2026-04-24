#1
# What are k , l , x , y , z , m , n , p , q , s ? (Home work)
class c1:
	x = 10  # What is variable 'x' ---> class variable (static variable)
	def m1(self):
		self.y = 20   # What is variable 'y' ---> instance variable
		z = 30   # What is variable 'z' ---> local variable
		c1.m = 40   # What is variable 'm' ---> class variable (static variable)
#end of the class
def f1():
	a = c1()
	a.p = 50   # What is variable 'p' ---> instance variable
	c1.q = 60   # What is variable 'q' ---> class variable (static variable)
	s = 70   # What is variable 's' ---> local variable
#end of the function
k = 80   # What is variable 'k' ---> global variable
c1.l = 90   # What is variable 'l' ---> class variable (static variable)
b = c1()
b.n = 100   # What is variable 'n' ---> instance variable



#2
# Find outputs (Home work)
class Person:
	def _init_(self):
		self.name = ''
	@property
	def name(self):
		print('getter method')
		return self._name
	@name.setter
	def name(self , value):
		print('Setter Method')
		self._name = value
	@name.deleter
	def name(self):
		print('Deleter method ')
		del self._name
	def _del_(self):
		print('Destructor')
# End of the class
p = Person()
print(p.name)
# getter method
# Error as 'Person' object has no attribute '_name'
p.name = 'Vamsi'
# Setter Method
print(p.name)
# getter method
# Vamsi
del p.name # Deleter method
print(p.name)
# getter method
# Error as 'Person' object has no attribute '_name'
del p
# Destructor only if object destruction happens immediately; otherwise no guaranteed visible output.



#3
# Find outputs (Home work)
import time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while True:
	try:
		print(next(e))
		time.sleep(1)
	except StopIteration:
		break
print(list[5])
# (5, 25)
# (6, 10.8)
# (7, 'Hyd')
# (8, True)
# Error as list index out of range



#4
'''  (Home work)
Can string be enumerated ?
'''
import time
a = input('Enter any string : ') # Assume that input is 'Hyd'
e = enumerate(a)
while True:
	try:
		print(next(e))
		time.sleep(1)
	except StopIteration:
		break
# (0, 'H')
# (1, 'y')
# (2, 'd')



#5
# Can set be enumerated ? (Home work)
import time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a)
b = enumerate(a)
while True:
	try:
		print(next(b))
		time.sleep(1)
	except StopIteration:
		break
# The printed set order is unpredictable.
# enumerate() works on a set iterator, so output is like:
# (0, element1)
# (1, element2)
# (2, element3)
# (3, element4)



#6
# Can dictionary be enumerated ? (Home work)
import time
def disp(e):
	while True:
		try:
			print(next(e))
			time.sleep(1)
		except StopIteration:
			break
	print()
dict = {'Empno' : 25 , 'Emp Name' : 'Rama Rao' , 'Sal' : 10000.0}
e1 = enumerate(dict.keys())
disp(e1)
e2 = enumerate(dict.values())
disp(e2)
e3 = enumerate(dict.items())
disp(e3)
e4 = enumerate(dict , start = 5)
disp(e4)
# (0, 'Empno')
# (1, 'Emp Name')
# (2, 'Sal')
#
# (0, 25)
# (1, 'Rama Rao')
# (2, 10000.0)
#
# (0, ('Empno', 25))
# (1, ('Emp Name', 'Rama Rao'))
# (2, ('Sal', 10000.0))
#
# (5, 'Empno')
# (6, 'Emp Name')
# (7, 'Sal')



#7
# Find outputs (Home work)
import time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for index , element in e:
	print(F'{element:20}  ...  {b[index]}')
	time.sleep(1)

# Telangana            ... Hyderabad
# Andhra Pradesh       ... Amaravathi
# Karnataka            ... Bangalore
# TamilNadu            ... Chennai
# Maharastra           ... Mumbai