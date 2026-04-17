# Write  a  program  to  print  upper  and  lower  case  alphabets
Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
for i in range(65, 91):     
    print(chr(i), end=" ")
print()
for i in range(97, 123):
    print(chr(i), end=" ")
'''
# Write  a  program  to  print  first  'n'  terms  of  fibonacci  series ,Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
...
n = int(input("Enter number of terms: "))
a = 0
b = 1
count = 1
while count <= n:
    print(a,end=",")
    c = a + b
    a = b
    b = c
    count += 1
'''
# Write  a  program  to  search  for  'x'  in  fibonacci  series
1) Let  input  be   10
    What  is  the  output ? --->	Not  found
2) Let  input  be   21
    What  is  the  output ? --->  Found
3) Do  not  generate  fibonacci  series
'''
x = int(input("Enter number: "))
a = 0
b = 1
while a < x:
    c = a + b
    a = b
    b = c
if a == x:
    print("Found")
else:
    print("Not found")
...
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
...
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
else suite
Outside loop
...
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
...
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
else suite
Outside loop
...
# Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2
2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found
3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  ---> Compare  'x'  with  next  element  of  list
4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and do not  search  for  'x'  in  rest  of  the  list
5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message
6) Hint: Use  for  loop
'''
a = [10, 20, 15, 12, 18]
print("Enter any list :",a)
x = int(input("Enter the element to be searched : "))
found = False
for i in range(len(a)):
    if a[i] == x:
        print("Found at index :", i)
        found = True
        break  
if not found:
    print("Not found")
...
# Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found
List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
Search  for  15
What  are  the  outputs ?  --->   15 is  found  at  index 2  
15 is  found  at  index 2
15 is  found  at  index 8
15 is  found   3  times 
'''
list = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Enter the number to search for: "))
count = 0
for i in range(len(list)):
    if list[i] == x:
        print(x, "is found at index", i)
        count += 1
if count > 0:
    print(x, "is found", count, "times")
else:
    print(x, "was not found in the list")
...
# Walrus   operator (:=)  demo  program
print(a := 25)#25
print(a = 25)# Error
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
print((a = 6) + 7) # Error
...

...
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
if  c = 0:
	print('Hyd')
else:
	print('Sec')
...
Error
'''
# (Home  work) Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z (without  walrus operator)
Let inputs  be  25 , 10.8 , True ,  ctrl + z
sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1
1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs
2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError
3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''
try:
    sum=0
    c=0
    while True:
        n = eval(input("enter a value : "))
        c+=1
        sum += n
except(EOFError):
    avg = sum / c
    print(avg)
...
#  del  operator  demo program  (Home  work)
a = 25
print(a)  
del   a 
print(a)
...
25
Error
...
# Find  outputs  (Home  work)
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
...
25 25 25
25 25
Error
...
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a) 
print(b) 
print(c)
...
25 10.8 Hyd
Error
...
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  
del  a[2]  
print(a) 
del  a
print(a) 
print(a[0])
...
[10 , 20 , 15 , 18]
[10 , 20 , 18]
Error
...
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  
print(a[0]) 
del  a[2] 
del  a 
print(a)  
print(a[0])
...
(10 , 20 , 15 , 18)
10
Error
...
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) # Sec:0
if  c = 0:
	print('Hyd')
else:
	print('Sec') # Error