# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) # 1,2,3,4,5,6,7
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')

1
sec
Hello
2
sec
Hello
4
Sec
Hello
5
sec
Hello
7
sec
Hello
else suite
outside loop

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) #1,2,3,4,5,6,7
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

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
Outside loop


'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
for i in range(65,91):
  print(chr(i), end=" ")
print()
for j in range(97,123):
    print(chr(j), end=" ")


'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

n = int(input("Enter n: "))
a = 0
b = 1
count = 0
while count < n:
    print(a, end=" , ")
    c = a + b
    a = b
    b = c
    count += 1

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
n = int(input("enter a n: "))
a = 0
b = 1
found = False
for i in range(1, n+1):
 if a == n:
    found = True
    break
 c = a + b
 a = b
 b = c
 if found:
    print("found")
else:
   print("not found")


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
list = [10,20,15,12,18]
n = int(input("enter searched number: "))
found = false
for i in range(len(list)):
    if lst[i] == n:
    print("found at index", i)
    found = True
  break
if not found:
   print("Not Found")

'''

Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
15 is  found  at  index 5
 15 is  found  at  index  8
15 is  found   3  times
'''

lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
n = int(input("Enter element to search: "))

count = 0

for i in range(len(lst)):
    if lst[i] == n:
        print(n, "is found at index", i)
        count = count + 1

if count > 0:
    print(n, "is found", count, "times")
else:
    print(n, "is NOT FOUND")


#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # 25
print(a) # 25
print(a := 6 + 7) 
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 13
print((a = 6) + 7) #error


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec') # Sec
if  b := 0:
	print('Hyd') # Hyd
else:
	print('Sec : ' , b) # error
if  c = 0:
	print('Hyd') # error
else:
	print('Sec') # error


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

total = 0
count = 0

while True:
    try:
        x = input("Enter a value: ")
        value = eval(x)      # 25, 10.8, True ni correct type ga marchadaniki
        total = total + value
        count = count + 1
    except EOFError:
        break

if count > 0:
    avg = total / count
    print("Average =", avg)
else:
    print("No inputs given")


#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a 
print(a)


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a)  
del   b
print(c) 
print(b) 
del   c
print(c)

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25, 10.8, Hyd
del   a , b , c
print(a) #error
print(b) #error
print(c) # error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10, , 20 , 15 , 18]
del  a[2]  
print(a) #[10, 20, 18]
del  a
print(a) # error
print(a[0]) # error


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #(10, 20, 15, 18) 
print(a[0]) #10
del  a[2] 
del  a 
print(a) # error 
print(a[0])