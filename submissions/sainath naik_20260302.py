
'''
1.Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
# print Upper case alphabets
print("upper case alphabets")
for i in range(65, 91):
      print(chr(i), end=" ")
print("\n")
# print Lower case alphabets
print("Lower case alphabets")
for i in range(97, 123):
         print(chr(i), end= " ")




'''
2.Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n = int(input("Enter the nuber of terms :"))

a = 0
b = 1
print("Fibonacci series : ", end=" ")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c




'''
3.Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
num = int(input("Enter the number to search in Fibonacci series : "))
a, b = 0, 1
found = False

while a <= num:
    if a == num:
        found = True
        break
    a, b = b, a + b

if found:
    print("Fibonacci number found")
else:
    print("Fibonacci number not found")




'''
4.# Find  outputs  (Home  work)
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

'''
#1 Sec Hello <next line>2 Sec Hello <next line> 3 <next line> 4 Sec Hello <next line> 5 Sec Hello <next line> 6 <next line> 7 Sec Hello <next line> else suite <next line> Outside loop




'''
5.# Find  outputs  (Home  work)
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
print('Outside loop')
'''
# 1 Sec Hello <next line> 2 Sec Hello <next line> 3 Sec Hello <next line> 4 Sec Hello <next line> 5 Sec Hello <next line> 6 Sec Hello <next line> 7 Sec Hello <next line> else suite <next line> Outside loop




'''
6.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
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
'''

# Given list
lst = [10, 20, 15, 12, 18]

# Input
x = int(input("Enter element to search: "))

# Search using for loop
for i in range(len(lst)):
    if x == lst[i]:
        print("Found at index", i)
        break
else:
    print("Not found")





'''
7.Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  5
												   15 is  found  at  index  8
												   15 is  found   3  times
'''

# Given list
lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

# Input
x = int(input("Enter element to search: "))
# Search using for loop
count = 0
for i in range(len(lst)):
    if x == lst[i]:
        print(f"{x} is found at index {i}")
        count += 1
if count > 0:
    print(f"{x} is found {count} times")
else:
    print("Not found")




'''
8.#  Walrus   operator (:=)  demo  program
print(a := 25)  # valid
print(a = 25)  # Error
print(a)
print(a := 6 + 7) # valid
print(a)
print((a := 6) + 7) # valid
print(a)
print((a = 6) + 7) # Error
'''
print(a := 25) # 25
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6





'''
9.# Find  outputs  (Home  work)
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
	print('Sec'
'''
# Hyd <next line> Sec : 0 <next line> SyntaxError: invalid syntax





'''
10.Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
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
        x = eval(input("Enter value: "))
        sum = sum + x
        ctr = ctr + 1
except EOFError:
    pass

if ctr > 0:
    print("Average =", sum / ctr)
else:
    print("No inputs given")





'''
11.#  del  operator  demo program  (Home  work)
a = 25
print(a)  
del   a 
print(a) 
'''
# 25
# NameError: name 'a' is not defined




'''
12.# Find  outputs  (Home  work)
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
'''
# 25 25 25
# 25 25
# NameError: name 'a' is not defined
# 25
# NameError: name 'b' is not defined
# NameError: name 'c' is not defined




'''
13.#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a) 
print(b) 
print(c)
'''
# 25 10.8 Hyd
# NameError: name 'a' is not defined
# NameError: name 'b' is not defined
# NameError: name 'c' is not defined




'''
14.# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  
del  a[2]  
print(a) 
del  a
print(a) 
print(a[0])
'''

# [10, 20, 15, 18]
# [10, 20, 18]
# NameError: name 'a' is not defined
# NameError: name 'a' is not defined




'''
15.# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  
print(a[0]) 
del  a[2] 
del  a 
print(a)  
print(a[0])
'''
# (10, 20, 15, 18)
# 10
# TypeError: 'tuple' object doesn't support item deletion
# NameError: name 'a' is not defined