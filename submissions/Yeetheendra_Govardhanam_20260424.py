#1
# Identify Error (Home work)
class c4:
	def _iter_(self):
		print('_iter_ method ')
		return self
# End of the class
itr = c4()
for x in itr:
	print(x)
# Error as 'c4' object is not iterable, Python looks for __iter__(), but the class defines _iter_() instead.

#2
# Identify Error
class c5:
	def _iter_(self):
		print('_iter_ method ')
# End of the class
itr = c5()
for x in itr:
	print(x)
# Error as 'c5' object is not iterable, the class still does not define the required __iter__() method.

#3
# Identify Error
class c6:
	def iter(self):
		return reversed([10 , 20 , 15 , 18])
	def next(self):
		print('next method')
# End of the class
a = c6()
print(dir(c6))
for x in a:
	print(x)
# Error as 'c6' object is not iterable, iterable protocol requires __iter__() and __next__(), not iter() and next().
while True:
	print(next(a))
# Error as 'c6' object is not an iterator, next() works only on iterator objects that implement __next__().
a.next()
# This line is not reached because the loop above never ends and already fails.

#4
# Find outputs(Home work)
class c1:
	def _init_(self):
		self.x = 1
	def _iter_(self):
		print('_iter_ method')
		return self
	def _next_(self):
		value = self.x
		self.x += 1
		return value
# End of the class
a = c1()
print('Elements of iterator with for loop')
for element in a:
	print(element)
	if element == 5:
		break
# Error as 'c1' object is not iterable, for loop needs __iter__() and __next__(), but the class uses _iter_() and _next_().
print('Elements of iterator with next() function')
# This line is not reached.
while True:
	element = next(a)
	print(element)
	if element == 10:
		break
# Error as 'c1' object is not an iterator, next() requires __next__(), which is missing.
print('Elements of iterator with for loop')
# Not reached.

#5
# Find outputs (Home work)
import time
class Remote:
	def _init_(self):
		self.list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self.index = -1
	def _iter_(self):
		return self
	def _next_(self):
		self.index += 1
		if self.index == len(self.list):
			raise StopIteration
		return self.list[self.index]
# End of the class
r = Remote()
for x in r:
	print(x)
	time.sleep(1)
# Error as 'Remote' object is not iterable, class does not define __iter__() / __next__(), only _iter_() / _next_().

#6
'''
Write an iterator which yields 10 , 11 , 12 , 13 , ...... 20
Hint: Use for loop
'''
class MyIter:
	def __iter__(self):
		self.n = 10
		return self
	def __next__(self):
		if self.n > 20:
			raise StopIteration
		v = self.n
		self.n += 1
		return v
for x in MyIter():
	print(x)
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

#7
'''
Design an iterator which yields powers of two i.e. 2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7
Hint : Use for loop
'''
class PowerOfTwo:
	def __iter__(self):
		self.i = 0
		return self
	def __next__(self):
		if self.i > 7:
			raise StopIteration
		v = 2 ** self.i
		self.i += 1
		return v
for x in PowerOfTwo():
	print(x)
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128

#8
'''   (Home work)
1) 1st input ---> 'Hyd is green city'
   2nd input ---> 'Green'
   What are the outputs --->

2) 1st input ---> 'Hyd is green city'
   2nd input ---> 'red'
   What are the outputs --->
'''
import re
string = input('Enter any string : ')
pattern = input('Enter pattern : ')
m = re.search(pattern , string , re.IGNORECASE)
print(type(m))
if m:
	print(F'{m.group()} is found between indexes {m.start()} and {m.end() - 1}')
else:
	print(pattern , ' is not found ')
# For input string 'Hyd is green city' and pattern 'Green':
# Output:
# <class 're.Match'>
# green is found between indexes 7 and 11
# For pattern 'red':
# Output:
# <class 'NoneType'>
# red  is not found

#9
'''   (Home work)
1) 1st input ---> 'Hyd is green city'
   2nd input ---> 'city'
   What are the outputs --->

2) 1st input ---> 'Hyd is green city'
   2nd input ---> 'Hyd'
   What are the outputs --->

3) 1st input ---> 'Hyd is green city'
   2nd input ---> 'is'
   What are the outputs ---

4) 1st input ---> 'One for all and all for one'
   2nd input ---> 'one'
   What are the outputs --->
'''
import re
str = input('Enter any string : ')
pattern = input('Enter pattern : ')
m = re.search('^' + pattern , str , re.IGNORECASE)
if m:
	print(F'{str} starts with {m.group()}')
else:
	print(F'{str} does not start with {pattern}')
m = re.search(pattern + '$' , str , re.IGNORECASE)
if m:
	print(F'{str} ends with ' , m.group())
else:
	print(F'{str} does not end with {pattern}')
# For 'Hyd is green city' and 'city':
# Output: Hyd is green city does not start with city
# Output: Hyd is green city ends with city
# For 'Hyd' and 'Hyd':
# Output: Hyd starts with Hyd
# Output: Hyd ends with  Hyd
# For 'is':
# Output: Hyd is green city does not start with is
# Output: Hyd is green city does not end with is
# For 'one' with 'One for all and all for one':
# Output: One for all and all for one does not start with one
# Output: One for all and all for one ends with  one

#10
'''  (Home work)
What are the outputs
1st input ---> Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
2nd input ---> is
What are the outputs --->
'''
import re
string = input('Enter any string : ')
pattern = input('Enter pattern to be searched : ')
itr = re.finditer(pattern , string , re.IGNORECASE)
ctr = 0
while True:
	try:
		m = next(itr)
		print(F'{m.group()} is between indexes {m.start()} and {m.end() - 1}')
		ctr += 1
	except StopIteration:
		break
print('Found ' , ctr , ' times')
# Output for the given string and pattern 'is':
# is is between indexes 5 and 6
# IS is between indexes 17 and 18
# Is is between indexes 27 and 28
# is is between indexes 31 and 32
# Found  4  times

#11
# Find outputs (Home work)
import re
itr = re.finditer('[IEY]' , 'Hyd Is greEn citY', re.IGNORECASE)
while True:
	try:
		m = next(itr)
		print(m.group() , 'is at index : ' , m.start())
	except StopIteration:
		break
# y is at index :  1
# I is at index :  4
# E is at index :  10
# i is at index :  14
# Y is at index :  15

#12
# Find outputs (Home work)
import re
itr = re.finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while True:
	try:
		m = next(itr)
		print(m.group() , ' is at index :  ' , m.start())
	except:
		break
# m  is at index :   0
# 9  is at index :   2
# K  is at index :   4
# d  is at index :   6
# 5  is at index :   8
# E  is at index :   10