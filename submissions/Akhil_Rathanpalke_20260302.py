Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'

# output : 

# Program to print uppercase and lowercase alphabets

print("Uppercase Alphabets:")
for i in range(65, 91):      # 65 = 'A' , 90 = 'Z'
    print(chr(i), end=" ")

print("\n")   # for new line

print("Lowercase Alphabets:")
for i in range(97, 123):     # 97 = 'a' , 122 = 'z'
    print(chr(i), end=" ")


Uppercase Alphabets:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Lowercase Alphabets:
a b c d e f g h i j k l m n o p q r s t u v w x y z


# 2 . '''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5


# output : 

# Program to print first n terms of Fibonacci series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# 3 . Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series


# output : 

import math

# Function to check perfect square
def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s * s == n

# Input
x = int(input("Enter a number: "))

# Check Fibonacci condition
if isPerfectSquare(5 * x * x + 4) or isPerfectSquare(5 * x * x - 4):
    print("Found")
else:
    print("Not Found")


# 4 . # Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')


# output : 1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else  suite
Outside  loop


# 5 . # Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop'


# output : 1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else  suite
Outside loop


# 6 . Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																												Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
																														do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop


# output : # List
lst = [10, 20, 15, 12, 18]

# Input element to search
x = int(input("Enter element to search: "))

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        break
else:
    print("Not Found")



# 7 . Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
							   15 is  found  at  index  5
							   15 is  found  at  index  8
							   15 is  found   3  times


# output : lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

x = 15
count = 0

for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        count += 1

if count > 0:
    print(x, "is found", count, "times")
else:
    print("Not Found")


15 is found at index 2
15 is found at index 5
15 is found at index 8
15 is found 3 times


# 8 . #  Walrus   operator (:=)  demo  program
print(a := 25)
print(a = 25)
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
print((a = 6) + 7)

output : 25
SyntaxError


# 9 . # Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
if  c = 0:
	print('Hyd')
else:
	print('Sec')


# output : Hyd
Sec :  0
SyntaxError



# 9 . (Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d



# output : sum = 0
ctr = 0

try:
    while True:
        x = eval(input("Enter value: "))
        sum = sum + x
        ctr = ctr + 1
except EOFError:
    pass

if ctr > 0:
    print("Average =", sum / ctr)
else:
    print("No inputs given")


# 10 . #  del  operator  demo program  (Home  work)
a = 25
print(a)  
del   a 
print(a)

# output : 25
NameError: name 'a' is not defined


# 11 . # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)
del   a
print(b , c)
print(a)  
del   b
print(c)
print(b)
del   c
print(c)

# output : 25 25 25


# 12 . #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a) 
print(b) 
print(c)

# output : 25 10.8 Hyd
NameError: name 'a' is not defined


# 13 . # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  
del  a[2]  
print(a) 
del  a
print(a) 
print(a[0])

# output : [10, 20, 15, 18]


# 14 . # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  
print(a[0]) 
del  a[2] 
del  a 
print(a)  
print(a[0])

# output : (10, 20, 15, 18)
10
TypeError: 'tuple' object doesn't support item deletion