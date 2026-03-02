1) Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
#Program
for i in range (65,91):
    print(chr(i),end=' ')
    
print()
for i in range (97,123):
    print(chr(i),end=' ')
	
(or)
i=65
while i<=90:
    print(chr(i), end=' ')
    i+=1
print()
i=97
while i<=122:
    print(chr(i), end=' ')
    i+=1
2) Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
#Program
x=int(input("Enter value of x:"))
a=0
b=1
count=0
while count<=x:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1

3) Write  a  program  to  search  for  'x'  in  fibonacci  series

	1) Let  input  be   10
   	 What  is  the  output ? --->	Not  found

	2) Let  input  be   21
   	 What  is  the  output ? --->  Found

	3) Do  not  generate  fibonacci  series

4) outputs 
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
#1
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

5) outputs  
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
#1
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

6) Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
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
#Program
x = eval(input("Enter any list:"))
y = int(input("Enter the element to be searched:"))
z=0
for i in range(len(x)):
    if x[i]==y:
        print(F'Found at index:{i}')
        z=1
        break
if not z:
        print('Not Found')

7) Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  5
												   15 is  found  at  index  8
												   15 is  found   3  times
#Program
x = eval(input("Enter any list:"))
y = int(input("Enter the element to be searched:"))
z=0
count = 0
for i in range(len(x)):
    if x[i] == y:
        print(y, "is found at index", i)
        count += 1

if count > 0:
    print(y, "is found", count, "times")
else:
    print(y, "is not found")

8) Walrus   operator (:=)  demo  program
print(a := 25)#25
print(a = 25)#Error because it is not valid
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)#13
print(a)#6
print((a = 6) + 7)#Error because it is not valid

9) outputs 
a = 0
if  a == 0:
	print('Hyd')#Hyd
else:
	print('Sec')#Sec
if  b := 0:
	print('Hyd')#Hyd
else:
	print('Sec : ' , b)#Sec
if  c = 0:
	print('Hyd')#Error because of '='
else:
	print('Sec')#Error

10) Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
#Program
sum = 0
a = 0

y=eval(input("Enter values (Press Ctrl+Z and Enter to stop):"))

try:
    while True:
        x = input()
        value = eval(x)    
        sum = sum + value
        a = a + 1
except EOFError:
    pass

if a > 0:
    print("Average =", sum / a)
else:
    print("No inputs given")


11) del  operator  demo program  (Home  work)
a = 25
print(a)  #25
del   a 
print(a)#Error because ref is not found

12) outputs  
a = b = c = 25
print(a , b , c)# 25 25 25
del   a
print(b , c)# 25 25
print(a)  #Error because ref a is deleted
del   b
print(c)#25
print(b)#Error because ref b is deleted
del   c

13)  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#25 10.8 Hyd
del   a , b , c
print(a) #Error because ref a is deleted
print(b) #Error because ref b is deleted
print(c) #Error because ref c is deleted

14) outputs  
a = [10 , 20 , 15 , 18]
print(a)  #10 20 15 18
del  a[2]  
print(a) #10 20  18
del  a
print(a) #Error ref is deleted

15) outputs 
a = (10 , 20 , 15 , 18)
print(a)  #10 20 15 18
print(a[0]) #10
del  a[2] #error because of tuple
del  a 
print(a)  #error
print(a[0])#error