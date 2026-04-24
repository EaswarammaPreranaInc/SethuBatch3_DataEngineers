#1
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



#2
# Find outputs (Home work)
import time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while True:
	try:
		print(next(z))
		# ('Empno', 25)
		# ('Emp Name', 'Rama Rao')
		# ('Salary', 10000.0)
		time.sleep(1)
	except StopIteration:
		break
	# Loop stops after the third pair because zip ends when the shorter list ends.



#3
# Find outputs (Home work)
import time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for x in zip(a , b , c):
	print(x)
	# ('Telangana', 'Hyderabad', 50000000)
	# ('Andhra Pradesh', 'Amaravathi', 40000000)
	# ('Karnataka', 'Banglore', 70000000)
	# ('TamilNadu', 'Chennai', 60000000)
	# ('Maharastra', 'Mumbai', 30000000)
	time.sleep(1)



#4
# Find outputs (Home work)
import time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for x , y in zip(a , b):
	print(x + y)
	# 5
	# 7
	# 9
	time.sleep(1)



#5
# Find outputs (Home work)
import time
def disp(z):
	while True:
		try:
			print(next(z))
			time.sleep(1)
		except:
			break
	print()
a = [10 , 20 , 30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b.keys())
disp(z1)
# (10, 1)
# (20, 3)
# (30, 5)

z2 = zip(a , b.values())
disp(z2)
# (10, 2)
# (20, 4)
# (30, 6)

z3 = zip(a , b.items())
disp(z3)
# (10, (1, 2))
# (20, (3, 4))
# (30, (5, 6))

z4 = zip(a , b)
disp(z4)
# (10, 1)
# (20, 3)
# (30, 5)

z5 = zip(a)
disp(z5)
# (10,)
# (20,)
# (30,)

z6 = zip(b)
disp(z6)
# (1,)
# (3,)
# (5,)

z7 = zip()
disp(z7)
# no output



#6
# Find outputs (Home work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y in z]
print(a) # [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]



#7
# How to print reversed object in different ways (Home work)
import time
a = input('Enter any string : ')  # Assume that input is HYD
r1 = reversed(a)
print(type(r1)) # <class 'reversed'>
print(r1) # <reversed object at 0x...>
print('Iterate thru reversed object with next function') # Iterate thru reversed object with next function
r1 = reversed(a)
print(next(r1)) # D
time.sleep(1)
print(next(r1)) # Y
time.sleep(1)
print(next(r1)) # H
time.sleep(1)

print('Iterate thru reversed object with _next_ method') # Iterate thru reversed object with _next_ method
r1 = reversed(a)
print(r1.__next__()) # D
print(r1.__next__()) # Y
print(r1.__next__()) # H

print('Iterate thru reversed object with for loop') # Iterate thru reversed object with for loop
for x in reversed(a):
	print(x)
	# D
	# Y
	# H
	time.sleep(1)

print('Unpack reversed object : ' , *reversed(a)) # Unpack reversed object : D Y H
print('List of chars in reverse order : ' , list(reversed(a))) # List of chars in reverse order : ['D', 'Y', 'H']
print('Reverse string :   ' , a[::-1]) # Reverse string :   HYD



#8
# Find outputs (Home work)
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) # <reversed object at 0x...>
print(id(b)) # some integer id value
print(*b) # D Y H
# print(b[0]) # Error as 'reversed' object is not subscriptable
# print(b[1 : 3]) # Error as 'reversed' object is not subscriptable
# print(b * 2) # Error as unsupported operand type(s) for *: 'reversed' and 'int'
# print(len(b)) # Error as object of type 'reversed' has no len()



#9
# Can tuple be reversed ? (Home work)
import time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for x in b:
	print(x)
	# True
	# Hyd
	# 10.8
	# 25
	time.sleep(1)



#10
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
	# True
	# Hyd
	# 10.8
	# 25
	time.sleep(1)

print('Unpack list_reverseiterator object :  ' , *reversed(lst)) # Unpack list_reverseiterator object : True Hyd 10.8 25
print('Reverse list :  ' , lst[::-1]) # Reverse list : [True, 'Hyd', 10.8, 25]



#11
# Can set be reversed ? (Home work)
a = {10, 20, 15 , 18}
# r = reversed(a) # Error as 'set' object is not reversible



#12
# Can dictionary be reversed ? (Home work)
import time
def disp(r):
	while True:
		try:
			print(next(r))
			time.sleep(0.5)
		except StopIteration:
			break
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
r1 = reversed(a.keys())
disp(r1)
# 18
# 15
# 20
# 10

r2 = reversed(a.values())
disp(r2)
# Amar
# Kiran
# Sita
# Rama

r3 = reversed(a.items())
disp(r3)
# (18, 'Amar')
# (15, 'Kiran')
# (20, 'Sita')
# (10, 'Rama')

r4 = reversed(a)
disp(r4)
# 18
# 15
# 20
# 10



#13
'''
Tricky program
Write a program to reverse a dictionary ?

Let input be {'Empno' : 25 , 'Emp Name' : 'Rama Rao' , 'Sal' : 10000.0}
What is the output ? ---> {'Sal' : 10000.0 , 'Emp Name' : 'Rama Rao' , 'Empno' : 25}

Hint : Both input and output are dictionaries
'''
a = {'Empno' : 25 , 'Emp Name' : 'Rama Rao' , 'Sal' : 10000.0}
b = {}
for k in reversed(list(a.keys())):
	b[k] = a[k]
print(b) # {'Sal': 10000.0, 'Emp Name': 'Rama Rao', 'Empno': 25}



#14
# Find outputs
import time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys in reverse order') # Keys in reverse order
for k in reversed(a):
	print(k)
	# 18
	# 15
	# 20
	# 10
	time.sleep(1)

print('Values in reverse order') # Values in reverse order
for v in reversed(list(a.values())):
	print(v)
	# Kiran
	# Rajesh
	# Sita
	# Rama rao
	time.sleep(1)

print('Tuples in reverse order') # Tuples in reverse order
for item in reversed(list(a.items())):
	print(item)
	# (18, 'Kiran')
	# (15, 'Rajesh')
	# (20, 'Sita')
	# (10, 'Rama rao')
	time.sleep(1)

print('Elements of each tuple in reverse order') # Elements of each tuple in reverse order
for k , v in reversed(list(a.items())):
	print(v , k)
	# Kiran 18
	# Rajesh 15
	# Sita 20
	# Rama rao 10
	time.sleep(1)

print('Keys and values in reverse order') # Keys and values in reverse order
for k in reversed(a):
	print(k , a[k])
	# 18 Kiran
	# 15 Rajesh
	# 20 Sita
	# 10 Rama rao
	time.sleep(1)



#15
# How to iterate list_iterator in different ways
import time
list = [10 , 20 , 15 , 18]
print('Iterate list with for loop') # Iterate list with for loop
for x in list:
	print(x)
	# 10
	# 20
	# 15
	# 18
	time.sleep(1)

# print(next(list)) # Error as 'list' object is not an iterator

list_itr1 = iter(list)
print(type(list_itr1)) # <class 'list_iterator'>
print(list_itr1) # <list_iterator object at 0x...>
print('Iterate thru list_iterator with next() function') # Iterate thru list_iterator with next() function
print(next(list_itr1)) # 10
print(next(list_itr1)) # 20
print(next(list_itr1)) # 15
print(next(list_itr1)) # 18

print('Iterate thru list_iterator with _next_() method') # Iterate thru list_iterator with _next_() method
list_itr1 = iter(list)
print(list_itr1.__next__()) # 10
print(list_itr1.__next__()) # 20
print(list_itr1.__next__()) # 15
print(list_itr1.__next__()) # 18

print('Iterate thru list_iterator with for loop') # Iterate thru list_iterator with for loop
for x in iter(list):
	print(x)
	# 10
	# 20
	# 15
	# 18
	time.sleep(1)

print('Unpacks List_iterator :    ' , *iter(list)) # Unpacks List_iterator : 10 20 15 18



#16
# Find outputs
a = 25
print(a) # 25
for x in a:
	# print(x) # Error as 'int' object is not iterable
# print(iter(a)) # Error as 'int' object is not iterable
# print(next(a)) # Error as 'int' object is not an iterator