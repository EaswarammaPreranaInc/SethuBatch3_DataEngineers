'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
# Program:

x = int(input("Enter value of x : "))

# First two terms
a = 0
b = 1

count = 1

print("Fibonacci series")

# Print fibonacci series
while count <= x:
    print(a, end=" , ")
    
    # next term = sum of previous two terms
    c = a + b
    a = b
    b = c
    
    count += 1

# output
Enter value of x : 10
Fibonacci series 
0
1
1
2
3
5
8

#Find  outputs  (Home  work)
for x in [10, 20, 15, 18]:
    print(x)
#Output:
10
20
15
18

for x in 'Hyd':
    print(x)
#Output:
H
y
d

for x in range(5):
    print(x)
#outputs:
0
1
2
3
4

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)# 10
                  30
                  50

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#20
                 40
                 60
print()
#
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10, 20)
                   (30, 40)
                   (50, 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)# defult iteration gives keys 10
                                              30
                                              50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') #10...20
                                    30...40
                                    50...60
for  x ,  y  in   a:
	print(x , y # Error 
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error Because iterating dictionary returns only keys, not (key,value) pairs.


# Identify  error  (Home  work)
for  x  in   123:
        print(x) # TypeError because 'int' object is not iterable


# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # 
for  x   in  []:
        print(x) #
for  x   in   {}:
        print(x) # 
for  x   in   set():
        print(x) #
for  x   in   '':
        print(x) #
for  x  in  range(10 , 10):
	print(x) # No output (start == stop)
for  x  in   range():
	print(x) # TypeError Because range expected at least 1 argument
for  x  in   (25):
	print(x) # TypeError Because 'int' object is not iterable

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

# Output:
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye

# How to print each element and the corresponding index a = [25 , 10.8 , 'Hyd' , True] print('Indexed based for loop') How to print each element and the corresponding index with index based for loop print('For each loop') How to print each element and the corresponding index with for ... each loop (Do not use 2nd variable)

# Program:

a = [25, 10.8, 'Hyd', True]

print('Indexed based for loop')

# Index based for loop
for i in range(len(a)):
    print(i, a[i])

print('For each loop')

# For-each loop using enumerate
for x in enumerate(a):
    print(x)

print('For each loop (without 2nd variable)')

# For-each loop without using second variable
for x in enumerate(a):
    print(x[0], x[1])

# Output:
Indexed based for loop
0 25
1 10.8
2 Hyd
3 True

For each loop
(0, 25)
(1, 10.8)
(2, 'Hyd')
(3, True)

For each loop (without 2nd variable)
0 25
1 10.8
2 Hyd
3 True

'''
 How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
'''
#Program:

a = [25, 10.8, 'Hyd', True]


print('Indexed for loop')

# Reverse using index-based for loop
for i in range(len(a) - 1, -1, -1):
    print(a[i])

print('For each loop')

# Reverse using for-each loop (no slice, no 2nd variable)
for x in reversed(a):
    print(x)

# Output:

Indexed for loop
True
Hyd
10.8
25

For each loop
True
Hyd
10.8
25

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
'''
# Program Using Indexed Based For Loop:

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

# indexed based for loop
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list : ', c)

# Output:
Enter 1st list : [10,20,15,18]
Enter 2nd list : [30,40,35,12,100,200,300]
3rd list :  [40, 60, 50, 30]

# Program Using For Each Loop (No 2nd variable):

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

# for-each loop without 2nd variable
for x in zip(a, b):
    c.append(x[0] + x[1])

print('3rd list : ', c)

#outputs:

(10,30)
(20,40)
(15,35)
(18,12)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')

# indexes 2 to 4
for i in range(2, 5):
    print(a[i])
print('For each loop')

for x in enumerate(a):
    if 2 <= x[0] <= 4:
        print(x[1])
#Output:

Indexed for loop
Hyd
True
(3+4j)

For each loop
Hyd
True
(3+4j)

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

#output:

a :  [11, 21, 16, 19]
b :  [10, 20, 15, 18]

#Write  a  program  to  print  full  pyramid

#program:

# input
n = int(input("How many lines ? : "))

for i in range(1, n + 1):
    
    # print spaces
    for s in range(n - i):
        print(" ", end="")
    
    # print stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()   # move to next line
# Output:
How many lines ? : 5
    *
   ***
  *****
 *******
*********

# Write a program to print first 20 even numbers

# Program:

i = 1

while i <= 20:
    print(2 * i)
    i += 1
    print("First 20 even numbers")
print("Bye")
#Output:
First 20 even numbers
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
Bye

# Write  a  program  to  print  first  20  odd  numbers

#Program:

i = 1

while i <= 20:
    print(2 * i - 1)
    i += 1
    print("First 20 odd numbers")

#output:
First 20 odd numbers
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39

# Write a program to print natural numbers 1 , 2 , 3 .... n and ask user to input value of 'n'

# Program:

n = int(input("Enter value of n : "))

i = 1

# while loop
while i <= n:
    print(i)
    i += 1

#Output:
Enter value of n : 5
1
2
3
4
5

#Write a program to print 10 , 9 , 8 , ..... 1

#program:

i = 10

while i >= 1:
    print(i)
    i -= 1
    print("Numbers from 10 downto 1 in steps of -1")

#Output:
Numbers from 10 downto 1 in steps of -1
10
9
8
7
6
5
4
3
2
1

# Write a program to determine 1.1 + 2.2 + 3.3 + .... n terms

Program:

# input
n = int(input("How many terms would you like to add : "))

sum = 0

# for loop
for i in range(1, n + 1):
    sum += 1.1 * i

print("Sum =", sum)

#Outpput:
How many terms would you like to add : 5
Sum = 16.5

# Write a program to determine sum of first 20 even numbers

#Program:

sum = 0

for i in range(1, 21):
    sum += 2 * i

print("Sum of first 20 even numbers :", sum)

#output:
Sum of first 20 even numbers : 420

# Write a program to determine sum of first 20 odd numbers

#Program:

sum = 0

for i in range(1, 21):
    sum += (2 * i - 1)

print("Sum of first 20 odd numbers :", sum)

#output:
Sum of first 20 odd numbers : 400

# Write a program to determine 1 + 2 + 3 + .... + n without using formula n * (n + 1) / 2

#Program:

n = int(input("How many terms would you like to print : "))

sum = 0

# for loop
for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

# Output:

How many terms would you like to print : 5
Sum = 15

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
print('Outside loop')

#Output:
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
Outside loop
#For i = 3 and i = 6, continue skips:

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')
#SyntaxError: 'continue' not properly in loop


# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
print('Outside loop')

#output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
#SyntaxError: 'break' outside loop





