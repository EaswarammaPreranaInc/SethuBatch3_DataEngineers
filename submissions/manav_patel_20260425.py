#1
'''
Repeat prog6a with next() function.

Reuse class c1 defined in prog6a but do not rewrite class c1 again
'''
a = c1()

print('Elements of iterator with next() function')

itr = iter(a)
while True:
	try:
		element = next(itr)
		print(element)
		if element == 5:
			break
	except StopIteration:
		break



#2
'''
Design an iterator which yields powers of two i.e. 2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7
Hint : Use for loop
'''
class PowerOfTwo:
	def __iter__(self):
		self.n = 0
		return self
	def __next__(self):
		if self.n > 7:
			raise StopIteration
		v = 2 ** self.n
		self.n += 1
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



#3
# Find outputs (Home work)
import re
string = 'z7.Q-$2 b[9.a%6$G&k.%'
print(re.findall('[a-z]' , string))
print()
print(re.findall('[0-9]' , string))
print()
print(re.findall('[^A-Za-z0-9]' , string))
print()
print(re.findall('.' , string))
print()
print(re.findall('[.]' , string))
print()
print(re.findall('[$]' , string))
print()
print(re.findall('[%]' , string))
print()
print(re.findall('[az-]' , string))
# ['z', 'b', 'a', 'k']
#
# ['7', '2', '9', '6']
#
# ['.', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
#
# ['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
#
# ['.', '.', '.']
#
# ['$', '$']
#
# ['%', '%']
#
# ['z', '-', 'a']



#4
'''
1st string ---> 'Sankar dayal sarma'
2nd string ---> 'san'
What are the outputs ? --->
2) 1st string ---> 'Hyderabad'
   2nd string ---> 'Sec'
   What are the outputs ? --->
'''
import re
string = input('Enter any string : ')
pattern = input('Enter any pattern : ')
m = re.match(pattern , string , re.IGNORECASE)
if m:
	print(string , 'starts with ' , m.group())
else:
	print(string , 'does not start with' , pattern)
# For 'Sankar dayal sarma' and 'san':
# Sankar dayal sarma starts with san
# For 'Hyderabad' and 'Sec':
# Hyderabad does not start with Sec



#5
'''  (Home work)
1) What are the outputs if inputs are 'HYD' and 'hyd' ? --->
2) What are the outputs if inputs are 'HYD' and 'SEC' ? --->
'''
import re
s1 = input('Enter first string : ')
s2 = input('Enter second string : ')
m = re.fullmatch(s1 , s2 , re.IGNORECASE)
if m:
	print('Same strings after ignoring the case')
else:
	print('Different strings')
# For HYD and hyd:
# Same strings after ignoring the case
# For HYD and SEC:
# Different strings



#6
'''
Write a regular expression to validate a 10-digit mobile number

Rules:
1) It should be a 10-digit number
2) First digit can be 6, 7, 8 or 9
3) Number may start with 0 (or) +91
'''
import re
mobile = input('Enter mobile number : ')
m = re.fullmatch(r'(0|\+91)?[6789][0-9]{9}' , mobile)
if m:
	print('Valid mobile number')
else:
	print('Invalid mobile number')



#7
'''
Write a program to validate vehicle registration number

Rules:
1) First 2 characters should be TS , ts , Ts or tS
2) There are 29 circles i.e. 01 , 02 , 03 , ......29
3) Next two characters should be alphabets
4) Last four characters should be digits
'''
import re
vno = input('Enter vehicle number : ')
m = re.fullmatch(r'[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Za-z]{2}[0-9]{4}' , vno)
if m:
	print('Valid vehicle registration number')
else:
	print('Invalid vehicle registration number')



#8
'''
Write a program to validate date i.e. dd/mm/yyyy
'''
import re
date = input('Enter date : ')
m = re.fullmatch(r'([0]?[1-9]|[12][0-9]|3[01])/([0]?[1-9]|1[0-2])/([0-9]{4})' , date)
if m:
	print('Valid date')
else:
	print('Invalid date')



#9
'''
Write a program to validate address

Address format : streetname , city , State - PIN code
Eg: Khairtabad , Hyderabad , Telangana - 500004
'''
import re
addr = input('Enter address : ')
m = re.fullmatch(r'[A-Za-z ]+,\s*[A-Za-z ]+,\s*[A-Za-z ]+\s*-\s*[0-9]{6}' , addr)
if m:
	print('Valid address')
else:
	print('Invalid address')



#10
'''
Write a program to validate credit card number

Rules:
1) It must start with 4 , 5 (or) 6
2) It must be a 16 digit number
3) It should have digits from 0 to 9
4) It may have digits in a group of 4 separated by one hyphen
5) It should not have any other separator like _ , / , etc
'''
import re
card = input('Enter credit card number : ')
m = re.fullmatch(r'([456][0-9]{15}|[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4})' , card)
if m:
	print('Valid credit card number')
else:
	print('Invalid credit card number')