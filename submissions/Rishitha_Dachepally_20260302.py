'''

Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'

'''

print("Upper  case  alphabets")
for i in range(65 , 91):
	print(chr(i) , end = ' ') # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
print()

print("Lower  case  alphabets")
for i in range(97 , 123):
	print(chr(i) , end = ' ') # a b c d e f g h i j k l m n o p q r s t u v w x y z
print()

#-----------------------------------------------------------------------------------------------------

'''

Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5

'''

n = int(input("Enter  number  of  terms  :  "))
print("Fibonacci  Series") # Fibonacci  Series

a = 0
b = 1
count = 1

while count <= n:
	print(a) # 0
	         # 1
	         # 1
	         # 2
	         # 3
	         # 5
	c = a + b
	a = b
	b = c
	count += 1
#-----------------------------------------------------------------------------------------------------

'''

Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series

'''

x = int(input("Enter  value  to  be  searched  :  "))

a = 0
b = 1
found = False

while a <= x:
	if a == x:
		found = True
		break
	c = a + b
	a = b
	b = c

if found:
	print("Found") # Found  (if input = 21)
else:
	print("Not  Found") # Not  Found  (if input = 10)

#-----------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

for  i  in  range(1 , 8):
	print(i) # 1
	if   i % 3 == 0:
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
else:
	print('else  suite') # else  suite
# End  of  the  loop
print('Outside  loop') # Outside  loop

#-----------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

for  i  in  range(1 , 8):
	print(i) # 1
	if  i == 8:
		break
	else:
		print('Sec') # Sec
	print('Hello') # Hello
	         # 2
	         # Sec
	         # Hello
	         # 3
	         # Sec
	         # Hello
	         # 4
	         # Sec
	         # Hello
	         # 5
	         # Sec
	         # Hello
	         # 6
	         # Sec
	         # Hello
	         # 7
	         # Sec
	         # Hello
else:
	print('else  suite') # else  suite
# End  of  the  loop
print('Outside loop') # Outside loop

#-----------------------------------------------------------------------------------------------------

'''

Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  searched ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  searched ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																												Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
																														do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop

'''

a = eval(input("Enter  any  list:  "))
x = eval(input("Enter  the  element  to  be  searched  :  "))

for i in range(len(a)):
	if a[i] == x:
		print("Found  at  index  :  ", i) # Found  at  index  :   2  (if 15 is searched)
		break
else:
	print("Not  Found") # Not  Found  (if 19 is searched)

#-----------------------------------------------------------------------------------------------------

'''

Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  5
												   15 is  found  at  index  8
												   15 is  found   3  times

'''

a = [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

key = 15
count = 0

for i in range(len(a)):
	if a[i] == key:
		print(key , "is  found  at  index" , i) # 15 is  found  at  index 2
		                                       # 15 is  found  at  index 5
		                                       # 15 is  found  at  index 8
		count += 1

print(key , "is  found" , count , "times") # 15 is  found  3  times

#-----------------------------------------------------------------------------------------------------

#  Walrus   operator (:=)  demo  program

print(a := 25) # 25
#print(a = 25) # Error because assignment '=' is not allowed inside print
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
#print((a = 6) + 7) # Error because assignment '=' cannot be used inside expression

#-----------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) # Sec :  0
#if  c = 0: # Error because assignment '=' cannot be used in if condition
#	print('Hyd')
#else:
#	print('Sec')

#-----------------------------------------------------------------------------------------------------

'''

Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d

'''

sum = 0
ctr = 0

try:
	while True:
		x = eval(input("Enter  value  :  "))
		sum += x
		ctr += 1
except EOFError:
	pass

if ctr != 0:
	avg = sum / ctr
	print("Average  :  ", avg) # Average  :   12.266666666666667
else:
	print("No  inputs  given")
 
#-----------------------------------------------------------------------------------------------------

#  del  operator  demo program  (Home  work)

a = 25
print(a) # 25
del   a
#print(a) # Error because variable 'a' is deleted and not defined

#-----------------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)

a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
#print(a) # Error because variable 'a' is deleted
del   b
print(c) # 25
#print(b) # Error because variable 'b' is deleted
del   c
#print(c) # Error because variable 'c' is deleted

#-----------------------------------------------------------------------------------------------------

#  Can  multiple  objects  be  deleted  with  same  del  operator ?

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
#print(a) # Error because variable 'a' is deleted
#print(b) # Error because variable 'b' is deleted
#print(c) # Error because variable 'c' is deleted

#-----------------------------------------------------------------------------------------------------

# Find outputs  (Home  work)

a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
del  a[2]
print(a) # [10, 20, 18]
del  a
#print(a) # Error because variable 'a' is deleted
#print(a[0]) # Error because variable 'a' is deleted

#-----------------------------------------------------------------------------------------------------

# Find outputs  (Home work)

a = (10 , 20 , 15 , 18)
print(a) # (10, 20, 15, 18)
print(a[0]) # 10
#del  a[2] # Error because tuple does not support item deletion
del  a
#print(a) # Error because variable 'a' is deleted
#print(a[0]) # Error because variable 'a' is deleted
