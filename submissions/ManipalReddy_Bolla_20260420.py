# How to iterate zip object in different ways (Home work)
import time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1)) # <class 'zip'>
print(z1) # <zip object at 0x...>

print('Iterate thru zip object with next() function') # Iterate thru zip object with next() function
z1 = zip(a , b)
print(next(z1)) # ('Telangana', 'Hyderabad')
time.sleep(1)
print(next(z1)) # ('Andhra Pradesh', 'Amaravathi')
time.sleep(1)
print(next(z1)) # ('Karnataka ', 'Bangalore')
time.sleep(1)
print(next(z1)) # ('Tamilnadu', 'Chennai')
time.sleep(1)

print('Iterate thru zip object with _next_() method') # Iterate thru zip object with _next_() method
z1 = zip(a , b)
print(z1.__next__()) # ('Telangana', 'Hyderabad')
print(z1.__next__()) # ('Andhra Pradesh', 'Amaravathi')
print(z1.__next__()) # ('Karnataka ', 'Bangalore')
print(z1.__next__()) # ('Tamilnadu', 'Chennai')

print('Iterate thru zip object with for loop') # Iterate thru zip object with for loop
for x in zip(a , b):
	print(x)
	# ('Telangana', 'Hyderabad')
	# ('Andhra Pradesh', 'Amaravathi')
	# ('Karnataka ', 'Bangalore')
	# ('Tamilnadu', 'Chennai')
	time.sleep(1)

print('Elements of each tuple in zip object') # Elements of each tuple in zip object
for x , y in zip(a , b):
	print(x , y)
	# Telangana Hyderabad
	# Andhra Pradesh Amaravathi
	# Karnataka  Bangalore
	# Tamilnadu Chennai
	time.sleep(1)

print('Unpacks zip object with * operator : ' , *zip(a , b)) # Unpacks zip object with * operator : ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')
print()
print('zip object in the form of list : ' , list(zip(a , b))) # zip object in the form of list : [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]
print()
print('zip object in the form of dictionary : ' , dict(zip(a , b))) # zip object in the form of dictionary : {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}


#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))#('Empno',25) <nextiteration with 1 sec pause> ('Emp Name','Rama Rao') <nextiteration with 1 sec pause> ('Salary',10000.0)
		time . sleep(1)
	except  StopIteration:
		break
		
		
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)#('Telangana', 'Hyderabad', 50000000) <nextiteration with 1 sec pause> ('Andhra  Pradesh', 'Amaravathi', 40000000) <nextiteration with 1 sec pause> ('Karnataka', 'Banglore', 70000000) <nextiteration with 1 sec pause> ('TamilNadu', 'Chennai', 60000000) <nextiteration with 1 sec pause> ('Maharastra', 'Mumbai', 30000000)
	time . sleep(1)
	
	
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)#5 <nextiteration with 1 sec pause> 7 <nextiteration with 1 sec pause> 9 >
	time . sleep(1)
	
	
# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1)#(10,1) <nextiteration with 1 sec pause> (20,3) <nextiteration with 1 sec pause> (30,5)
z2 = zip(a , b . values())
disp(z2)#(10,2) <nextiteration with 1 sec pause> (20,4) <nextiteration with 1 sec pause> (30,6)
z3 = zip(a , b . items())
disp(z3)#)#(10,(1,2)) <nextiteration with 1 sec pause> (20,(3,4)) <nextiteration with 1 sec pause> (30,(5,6))
z4 = zip(a , b)
disp(z4)#(10,1) <nextiteration with 1 sec pause> (20,3) <nextiteration with 1 sec pause> (30,5)
z5 = zip(a)
disp(z5))#(10,) <nextiteration with 1 sec pause> (20,) <nextiteration with 1 sec pause> (30,)
z6 = zip(b)
disp(z6))#(1,) <nextiteration with 1 sec pause> (3,) <nextiteration with 1 sec pause> (5,)
z7 = zip()
disp(z7)#Empty


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)#[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]


#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))#class 'reversed'
print(r1)#reversed object at 0x....
print('Iterate  thru  reversed  object  with   next   function')
print(next(r1))
print(next(r1))
print(next(r1))
print('Iterate  thru  reversed  object  with   __next__   method')
r1 = reversed(a)
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print('Iterate  thru  reversed  object  with   for  loop')
for x in reversed(a):
	print(x)
print('Unpack  reversed  object  : ' ,  *reversed(a))
print('List  of  chars  in  reverse  order  :  ' , list(reversed(a)))
print('Reverse  string   :   ' , a[::-1])


# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))#class 'reversed'
print(b)#reversed object at 0x....
print(id(b))#address of object b
print(*b)#D Y H
print(b[0])#error
print(b[1 : 3])#error
print(b * 2)#error
print(len(b))#error


# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
	
	
# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))#class 'reversed'
for  x  in   b:
	print(x)#True <nextiteration with 1 sec pause> Hyd <nextiteration with 1 sec pause> 10.8 <nextiteration with 1 sec pause> 25
	time . sleep(1)
	

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)


# How to print list_reverseiterator object in different ways (Home work)
import time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1)) # <class 'list_reverseiterator'>
print(r1) # <list_reverseiterator object at 0x...>
print('next() function iterates thru list_reverseiterator object') # next() function iterates thru list_reverseiterator object
r1 = reversed(lst)
print(next(r1)) # True
time.sleep(1)
print(next(r1)) # Hyd
time.sleep(1)
print(next(r1)) # 10.8
time.sleep(1)
print(next(r1)) # 25
time.sleep(1)

print('_next_() method iterates thru list_reverseiterator object') # _next_() method iterates thru list_reverseiterator object
r1 = reversed(lst)
print(r1.__next__()) # True
print(r1.__next__()) # Hyd
print(r1.__next__()) # 10.8
print(r1.__next__()) # 25

print('for loop iterates thru list_reverseiterator object') # for loop iterates thru list_reverseiterator object
for x in reversed(lst):
	print(x)
	time.sleep(1)

print('Unpack list_reverseiterator object :  ' , *reversed(lst)) # Unpack list_reverseiterator object : True Hyd 10.8 25
print('Reverse list :  ' , lst[::-1]) # Reverse list : [True, 'Hyd', 10.8, 25]


# Can set be reversed ? (Home work)
a = {10, 20, 15 , 18}
# r = reversed(a) # Error





