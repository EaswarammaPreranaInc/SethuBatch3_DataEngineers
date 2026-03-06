'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
# Function to print upper and lower case alphabets
# Print Uppercase Alphabets
#print("Uppercase Alphabets:")
for i in range(65, 91):   # ASCII values of A-Z
    print(chr(i), end=" ")

print("\n")

# Print Lowercase Alphabets
#print("Lowercase Alphabets:")
for i in range(97, 123):  # ASCII values of a-z
    print(chr(i), end=" ")



'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
# Function to print first 'n' terms of Fibonacci series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c



'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x = int(input("Enter number to search: "))

a = 0
b = 1

if x == 0:
    print("Found")
elif x == 1:
    print("Found")
else:
    while b < x:
        c = a + b
        a = b
        b = c

    if b == x:
        print("Found")
    else:
        print("Not Found")


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
1
Sec
Hello
2
Sec
Hello
3
Hello
4
Sec
Hello
5
Sec 
Hello
6
Hello
7
Sec
Hello
else  suite

'''


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

'''


'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found
'''
lst = [10, 20, 15, 12, 18]
x = int(input("Enter element to search: "))

found = False

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        found = True
        break

if found == False:
    print("Not Found")


'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found
'''
lst = [10, 20, 15, 12, 18, 15, 10, 15]
x = int(input("Enter element to search: "))

count = 0

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        count += 1

if count == 0:
    print("Not Found")
else:
    print("Number of times found:", count)


#  Walrus   operator (:=)  demo  program
print(a := 25) #  25
print(a = 25) # error
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
print((a = 6) + 7) # error


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec') 
if  b := 0:
	print('Hyd') # 
else:
	print('Sec : ' , b) # Sec : 0
if  c = 0:
	print('Hyd')
else:
	print('Sec') # error
      

'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1
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



#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a 
print(a) # error


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a)  # error
del   b
print(c) # 25
print(b) # error
del   c
print(c) # error


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a) # error
print(b) # error
print(c) # error


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10, 20, 15, 18]
del  a[2]  
print(a)  # [10, 20, 18]
del  a
print(a)  # error
print(a[0]) # error


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  # (10, 20, 15, 18)
print(a[0]) # 10
del  a[2] 
del  a 
print(a)  # error
print(a[0]) # error
