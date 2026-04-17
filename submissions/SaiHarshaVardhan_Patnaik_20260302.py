'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
n = 65
print("Upper case alphabets:")
while n <= 90:
    print(chr(n), end=" ")
    n += 1
print("\nLower case alphabets:")
n = 97
while n <= 122:
    print(chr(n), end=" ")
    n += 1
'''
Output:
Upper case alphabets:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
Lower case alphabets:
a b c d e f g h i j k l m n o p q r s t u v w x y z 
'''
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

'''
Output:
Enter the number of terms: 6
Fibonacci series:
0 1 1 2 3 5     
'''
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x = int(input("Enter the number to search in Fibonacci series: "))
a, b = 0, 1
found = False
while a <= x:
    if a == x:
        found = True
        break
    a, b = b, a + b
if found:
    print("Found")
else:    
    print("Not found")

'''
Output:
Enter the number to search in Fibonacci series: 10
Not found
'''

# Find  outputs  (Home  work)
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
Output:
1
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
Outside  loop'''

# Find  outputs  (Home  work)
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
Output:
1
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
Outside loop'''

'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
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
a = list(map(int, input("Enter the list elements : ").split()))
x = int(input("Enter the element to search: "))             
found = False
for i in range(len(a)):
    if a[i] == x:
        found = True
        print(f"Found at index {i}")
        break
if not found:
    print("Not found")

'''
Output:
Enter the list elements : 10 20 15 12 18
Enter the element to search: 15
Found at index 2   '''

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

a = list(map(int, input("Enter the list elements : ").split()))
x = int(input("Enter the element to search: "))
count = 0
for i in range(len(a)):
    if a[i] == x:
        count += 1
        print(f"{x} is found at index {i}")
if count > 0:
    print(f"{x} is found {count} times")
else:
    print("Not found")

'''
Output:
Enter the list elements : 10 20 15 12 18 15 19 14 15 14
Enter the element to search: 15
15 is found at index 2
15 is found at index 5
15 is found at index 8
15 is found 3 times '''

#  Walrus   operator (:=)  demo  program
print(a := 25)
print(a = 25)
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
print((a = 6) + 7) # error

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
if  c = 0: # Error 
	print('Hyd')
else:
	print('Sec')
	
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''
total_sum = 0
count = 0
while True:
    try:
        value = input("Enter a value (press Ctrl + Z to end): ")
        total_sum += float(value)
        count += 1
    except EOFError:
        break
if count > 0:
    average = total_sum / count
    print(f"Average: {average}")

'''
Output:
Enter a value (press Ctrl + Z to end): 13
Enter a value (press Ctrl + Z to end): 2
Enter a value (press Ctrl + Z to end): 3
Enter a value (press Ctrl + Z to end): ^Z
Average: 6.0'''

#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a 
print(a) #Error

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a) # Error
del   b
print(c) # 25
print(b) # Error
del   c
print(c) # Error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # Error
print(b) # Error
print(c) # Error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2]  
print(a) # [10 , 20 , 18]
del  a
print(a) # Error
print(a[0]) # Error

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] 
del  a 
print(a) # Error
print(a[0]) # Error