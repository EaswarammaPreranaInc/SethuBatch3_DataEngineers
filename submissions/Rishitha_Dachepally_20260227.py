# Write  a  program  to  print  fibonacci  series  upto   x

# Let  input  be   10

# What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

# 1) What  is  10th  term ?  --->  9th  term + 8th  term
     # What  is  3rd  term ?  ---> 2nd  term + 1st  term
     # What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

# 2) What  are  the  first  two  terms ?  --->  0  and  1

# 3) Hint:  Use  while  loop

x = int(input("Enter  value  of  x  :  "))
print("Fibonacci  Series") # Fibonacci  Series

a = 0
b = 1

if x == 0:
	print(a) # 0

else:
	print(a) # 0
	print(b) # 1
	while True:
		c = a + b
		if c > x:
			break
		print(c) # 1
		         # 2
		         # 3
		         # 5
		         # 8
		a = b
		b = c

#--------------------------------------------------------------------------------

# Find  outputs  (Home  work)

# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
# print()
# How  to  print  each  character  of   string  'Hyd'  with  for  loop
# print()
# How  to  print  each  element  of   range(5)  with  for  loop

for x in [10 , 20 , 15 , 18]:
	print(x) # 10
	         # 20
	         # 15
	         # 18
print()

for x in 'Hyd':
	print(x) # H
	         # y
	         # d
print()

for x in range(5):
	print(x) # 0
	         # 1
	         # 2
	         # 3
	         # 4

#--------------------------------------------------------------------------------

# Find  outputs  (Home  work)

# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	# print(x)
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	# print(x)
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	# print(x)
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	# print(x)

for x in {10 : 20 , 30 : 40 , 50 : 60}.keys():
	print(x) # 10
	         # 30
	         # 50
print()

for x in {10 : 20 , 30 : 40 , 50 : 60}.values():
	print(x) # 20
	         # 40
	         # 60
print()

for x in {10 : 20 , 30 : 40 , 50 : 60}.items():
	print(x) # (10, 20)
	         # (30, 40)
	         # (50, 60)
print()

for x in {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10
	         # 30
	         # 50

#--------------------------------------------------------------------------------

# Find outputs  (Home  work)

# a = {10 : 20 , 30 : 40 , 50 : 60}
# for  x , y  in   a . items():
	# print(x , y , sep = '...')
# for  x ,  y  in   a:
	# print(x , y
# for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	# print(x , y , sep = '...')

a = {10 : 20 , 30 : 40 , 50 : 60}

for x , y in a.items():
	print(x , y , sep = '...') # 10...20
	                          # 30...40
	                          # 50...60

# for x , y in a:
	# print(x , y # Error because dictionary iteration returns only keys and cannot unpack into x , y and missing ')'

# for x , y in {10 : 20 , 30 : 40 , 50 : 60}:
	# print(x , y , sep = '...') # Error because dictionary iteration returns only keys, not key-value pairs

#--------------------------------------------------------------------------------

# Identify  error  (Home  work)

# for x in 123:
	# print(x) # Error because int object is not iterable

#--------------------------------------------------------------------------------

# Find  outputs  (Home  work)

for x in ():
	print(x)

for x in []:
	print(x)

for x in {}:
	print(x)

for x in set():
	print(x)

for x in '':
	print(x)

for x in range(10 , 10):
	print(x)

#for x in range():
#	print(x) # Error because range() requires at least 1 argument

#for x in (25):
#	print(x) # Error because (25) is int and int object is not iterable

#--------------------------------------------------------------------------------

#  Nested  Loop  demo  program

for i in range(1 , 4):
	for j in range(1 , 5):
		print(i , j) # 1 1
		             # 1 2
		             # 1 3
		             # 1 4
		             # 2 1
		             # 2 2
		             # 2 3
		             # 2 4
		             # 3 1
		             # 3 2
		             # 3 3
		             # 3 4
	print('Hello') # Hello
	              # Hello
	              # Hello
print('Bye') # Bye

#--------------------------------------------------------------------------------

# How  to  print  each  element  and  the  corresponding  index

# a = [25 , 10.8 , 'Hyd' , True] 
# print('Indexed based for loop') 
# How to print each element and the corresponding index with index based for loop print('For each loop') 
# How to print each element and the corresponding index with for ... each loop (Do not use 2nd variable)

a = [25 , 10.8 , 'Hyd' , True]

print('Indexed  based  for loop')

for i in range(len(a)):
	print(i , a[i]) # 0 25
	                 # 1 10.8
	                 # 2 Hyd
	                 # 3 True

print('For each loop')

for i , x in enumerate(a):
	print(i , x) # 0 25
	             # 1 10.8
	             # 2 Hyd
	             # 3 True

#--------------------------------------------------------------------------------

#  How  to  print  list  elements  in  reverse  order   without  slice

# a = [25 , 10.8 , 'Hyd' , True]
# print('Indexed for loop')
# How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

a = [25 , 10.8 , 'Hyd' , True]

print('Indexed for loop')

for i in range(len(a)-1 , -1 , -1):
	print(a[i]) # True
	             # Hyd
	             # 10.8
	             # 25

for x in reversed(a):
	print(x) # True
	         # Hyd
	         # 10.8
	         # 25

#--------------------------------------------------------------------------------

# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

# 1st  list  --->  [10 , 20 , 15 , 18]

# 2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

# 3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

# Hint:  Use  append()  method

# a = eval(input('Enter  1st  list  :  '))
# b = eval(input('Enter  2nd  list  :  '))
# c = []
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
# print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))

c = []

# Indexed  based  for  loop

for i in range(len(a)):
	c.append(a[i] + b[i])

print('3rd  list : ' , c) # 3rd  list :  [40, 60, 50, 30]


# For  each  loop  (Do  not  use  2nd  variable)

c = []

for x in a:
	c.append(x + b[a.index(x)])

print('3rd  list : ' , c) # 3rd  list :  [40, 60, 50, 30]

#--------------------------------------------------------------------------------

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice

# a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
# print('Indexed for loop')
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')

for i in range(2 , 5):
	print(a[i]) # Hyd
	             # True
	             # (3+4j)

print('For each loop')

for x in a:
	if a.index(x) >= 2 and a.index(x) <= 4:
		print(x) # Hyd
		         # True
		         # (3+4j)

#--------------------------------------------------------------------------------

#  Tricky  program

#  Find  outputs  (Home  work)

a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # a :   [11, 21, 16, 19]

b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) # b :   [10, 20, 15, 18]

#--------------------------------------------------------------------------------

# Write  a  program  to  print  full  pyramid

# <4  spaces>*
# <3  spaces>*
# <2 spaces>***
# <1  space>***
# <0  spaces>***

# Input  is  number  of  lines

n = int(input("How  many  lines  ?  :  "))

for i in range(1 , n + 1):
	print(' ' * (n - i) + '*' * (2 * i - 1)) #       *
	                                         #      ***
	                                         #     *****
	                                         #    *******
	                                         #   *********
	                                         #  ***********
	                                         # *************
#--------------------------------------------------------------------------------

# Write  a  program  to  print  first  20  even  numbers 

# 1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

# 2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

# 3) Hint:  Do  not  use  range  object

# 4) Use  while  loop

print("First  20  even  numbers") # First  20  even  numbers

i = 1

while i <= 20:
	print(2 * i) # 2
	             # 4
	             # 6
	             # 8
	             # 10
	             # 12
	             # 14
	             # 16
	             # 18
	             # 20
	             # 22
	             # 24
	             # 26
	             # 28
	             # 30
	             # 32
	             # 34
	             # 36
	             # 38
	             # 40
	i += 1

print("Bye") # Bye

#--------------------------------------------------------------------------------

# Write  a  program  to  print  first  20  odd  numbers

# 1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

# 2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

# 3) Hint:  Do  not  use  range  object

# 4) Use  while  loop

print("First  20  odd  numbers") # First  20  odd  numbers

i = 1

while i <= 20:
	print(2 * i - 1) # 1
	                 # 3
	                 # 5
	                 # 7
	                 # 9
	                 # 11
	                 # 13
	                 # 15
	                 # 17
	                 # 19
	                 # 21
	                 # 23
	                 # 25
	                 # 27
	                 # 29
	                 # 31
	                 # 33
	                 # 35
	                 # 37
	                 # 39
	i += 1

#--------------------------------------------------------------------------------

# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

# What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

# 1) Hint:  Do  not  use  range  object

# 2) Use  while  loop

n = int(input("Enter  value  of  n  :  "))
print("Natural  Numbers") # Natural  Numbers

i = 1

while i <= n:
	print(i) # 1
	         # 2
	         # 3
	         # 4
	         # 5
	         # 6
	         # 7
	         # 8
	         # 9
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
	         # 21
	         # 22
	         # 23
	         # 24
	         # 25
	i += 1

#--------------------------------------------------------------------------------

# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

# What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

# 1) Hint:  Do  not  use  range  object

# 2) Use  while  loop

print("Numbers  from  10  downto  1  in  steps  of  -1") # Numbers  from  10  downto  1  in  steps  of  -1

i = 10

while i >= 1:
	print(i) # 10
	         # 9
	         # 8
	         # 7
	         # 6
	         # 5
	         # 4
	         # 3
	         # 2
	         # 1
	i -= 1

#--------------------------------------------------------------------------------

# Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

# 1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

# 2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

# 3) Use  for  loop

n = int(input("How  many  terms  would  you  like  to  add  :  "))

sum = 0

for i in range(1 , n + 1):
	sum += 1.1 * i

print("Sum  :  ", sum) # Sum  :   16.5  (if n = 5)

#--------------------------------------------------------------------------------

# Write  a  program  to  determine  sum  of  first  20  even  numbers

# 1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

# 2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

# 3) Use  for  loop

sum = 0

for i in range(1 , 21):
	sum += 2 * i

print("Sum  of  first  20  even  numbers  :  ", sum) # Sum  of  first  20  even  numbers  :   420

#--------------------------------------------------------------------------------

# Write  a  program  to  determine  sum  of  first  20  odd  numbers

# 1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

# 2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

# 3) Use  for  loop

sum = 0

for i in range(1 , 21):
	sum += 2 * i - 1

print("Sum  of  first  20  odd  numbers  :  ", sum) # Sum  of  first  20  odd  numbers  :   400

#--------------------------------------------------------------------------------

# Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

# What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

# Hint:  Use  for  loop

n = int(input("How  many  terms  would  you  like  to  add  :  "))

sum = 0

for i in range(1 , n + 1):
	sum += i

print("Sum  :  ", sum) # Sum  :   55  (if n = 10)

#--------------------------------------------------------------------------------

# Find  outputs  (Home  work)

for  i   in   range(1 , 8):
	print(i) # 1
	if  i % 3  == 0:
			continue
	else:
			print('Sec') # Sec
	print('Hello') # Hello
	         # 2
	         # Sec
	         # Hello
	         # 3
	         # 4
	         # Sec
	         # Hello
	         # 5
	         # Sec
	         # Hello
	         # 6
	         # 7
	         # Sec
	         # Hello
# End of loop
print('Outside loop') # Outside loop

#--------------------------------------------------------------------------------

# Identify Error  (Home  work)

#if ():
#	print('Hyd')
#	continue # Error because continue cannot be used outside loop
#	print('Sec')


#--------------------------------------------------------------------------------

# Find outputs (Home  work)

for  i   in   range(1 , 8):
	print(i) # 1
	if   i % 3 == 0:
		break
	else:
		print('Sec') # Sec
	print('Hello') # Hello
	         # 2
	         # Sec
	         # Hello
	         # 3
# End  of  the  loop
print('Outside loop') # Outside loop

#--------------------------------------------------------------------------------

# Identify Error  (Home  work)

#if (10 , 20 , 30):
#	print('Hyd')
#	break # Error because break cannot be used outside loop
#	print('Sec')