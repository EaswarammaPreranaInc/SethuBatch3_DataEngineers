#1 Problem

# How to rotate a list to the right by k times
a = [10 , 20 , 15 , 18 , 12]
k = 3
# Output after 3 right shifts: [15 , 18 , 12 , 10 , 20]

def rotate(a):
	last = a[-1]
	for i in range(len(a)-1 , 0 , -1):
		a[i] = a[i-1]
	a[0] = last
# End of the function

# Read list 'a'
a = [10 , 20 , 15 , 18 , 12]
# Read 'k'
k = 3
# call rotate() 'k' times
for i in range(k):
	rotate(a)
	print(a)
	# After 1st call  --> [12 , 10 , 20 , 15 , 18]
	# After 2nd call  --> [18 , 12 , 10 , 20 , 15]
	# After 3rd call  --> [15 , 18 , 12 , 10 , 20]



#2 Problem

# Find outputs (Home work)
import time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda x : True , list)
while True:
	try:
		print(next(f))
		# 25
		# 10.8
		# (3+4j)
		# Hyd
		# False
		time.sleep(1)
	except:
		break



#3 Problem

# Find outputs (Home work)
import time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True]
f = filter(lambda x : False , list)
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
# no output as filter condition is False for every element, so iterator is empty.



#4 Problem

# Find outputs (Home work)
import time
list = [25 , 10.8 , False , 3 + 4j , 0 , 'Hyd' , '' , (25,) , () ]
f = filter(lambda x : x , list)
while True:
	try:
		print(next(f))
		# 25
		# 10.8
		# (3+4j)
		# Hyd
		# (25,)
		time.sleep(1)
	except:
		break



#5 Problem

# Find outputs
import time
def disp(f):
	while True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break
	print()
a = [10 , 0 , -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda x : None , list)
print('Filter f1')
disp(f1)
# no items, because lambda returns None for every element
f2 = filter(None , list)
print('Filter f2')
disp(f2)
# 10
# -25
# (25,)
# Hyd
# 10.8
# [10, 20]
# True



#6 Problem

# Find outputs (Home work)
import time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda x : len(x) >= 5 , list)
while True:
	try:
		print(next(f))
		# Rama Rao
		# Rajesh
		# Kiran
		# Manohar
		time.sleep(1)
	except:
		break



#7 Problem

# Find outputs (Home work)
import time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda x : x[1] >= 12 , list)
while True:
	try:
		print(next(f))
		# ('B', 20)
		# ('C', 15)
		# ('E', 18)
		time.sleep(1)
	except:
		break



#8 Problem

# Find outputs (Home work)
import time
list = [{'Roll Num' : 10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} ,
          {'Roll Num' : 20 , 'Stud Name' : 'Sita' , 'Marks' : 52} ,
          {'Roll Num'  : 15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} ,
          {'Roll Num'  : 18 , 'Stud Name' : 'Amar' ,  'Marks' : 48} ,
          {'Roll Num' : 5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}]
f = filter(lambda x : x['Marks'] >= 60 , list)
while True:
	try:
		print(next(f))
		# {'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
		# {'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
		# {'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
		time.sleep(1)
	except:
		break



#9 Problem

# Find outputs (Home work)
import time
def disp(f):
	while True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break
list = [{'country' : 'India' , 'sale' : 150.5} ,
          {'country' : 'china' , 'sale' : 200.2} ,
          {'country' : 'USA' , 'sale' : 300.3} ,
          {'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter(lambda x : x['country'].startswith('U') , list)
print('Filter f1')
disp(f1)
# {'country': 'USA', 'sale': 300.3}
# {'country': 'UK', 'sale': 210.4}
f2 = filter(lambda x : x['sale'] >= 200 , list)
print('Filter f2')
disp(f2)
# {'country': 'china', 'sale': 200.2}
# {'country': 'USA', 'sale': 300.3}
# {'country': 'UK', 'sale': 210.4}



#10 Problem

# How to print fliter object in different ways ?
import time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda x : x % 2 == 0 , a)
print('Iterate thru filter object with next function') # Iterate thru filter object with next function
print(next(f1)) # 10
print(next(f1)) # 20
print(next(f1)) # 18
print(next(f1)) # 26
print('Iterate thru filter object with for loop') # Iterate thru filter object with for loop
for x in filter(lambda x : x % 2 == 0 , a):
	print(x)
	# 10
	# 20
	# 18
	# 26
print('Unpack filter object : ' , *filter(lambda x : x % 2 == 0 , a)) # Unpack filter object : 10 20 18 26
print('Filter object converted to list : ' , list(filter(lambda x : x % 2 == 0 , a))) # Filter object converted to list : [10, 20, 18, 26]



#11 Problem

# Write a program to print odd numbers between 1 and 20 with filter iterator
import time
a = range(1 , 21)
f = filter(lambda x : x % 2 != 0 , a)
for x in f:
	print(x)
	time.sleep(0.5)
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19



#12 Problem

Write a program to print distinct vowels of the string using filter.
Input is string and output is set
'''
a = input('Enter a string : ')
v = set(filter(lambda x : x in 'aeiouAEIOU' , a))
print(v)
# Example output for input "education":
# {'e', 'u', 'a', 'i', 'o'}



#13 Problem

# Nested filter i.e. filter on filter
import time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda x : x[1].startswith('R') , filter(lambda x : x[2] >= 10000 , list))
while True:
	try:
		print(next(f))
		# (10, 'Rama', 10000.0)
		# (15, 'Rajesh', 15000.0)
		time.sleep(1)
	except:
		break