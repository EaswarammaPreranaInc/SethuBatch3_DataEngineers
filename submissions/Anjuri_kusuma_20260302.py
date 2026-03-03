'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
ch=65
while chr(ch)<='Z':
    print(chr(ch),end=" ")
    ch+=1
print()
ch1=97
while chr(ch1)<='z':
    print(chr(ch1),end=" ")
    ch1+=1
--------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n=int(input("ENter input : "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
---------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
x=int(input("Enter number to search : "))
a=0
b=1
while a<=x:
    if a==x:
        print("Found")
        break
    c=a+b
    a=b
    b=c
else:
    print("Not found")
'''
---------------------------------------------------------------------------------------------------------------
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

when i=1
Sec
Hello
when i=2
Sec
Hello
when i=3
when i=4
Sec
Hello
when i=5
Sec
Hello
when i=6
when i=7
Sec Hello
else suite
Outside loop
----------------------------------------------------------------------------------------------------------------------------
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

when i=1
Sec
Hello
when i=2
Sec
Hello
when i=3
Sec
Hello
when i=4
Sec
Hello
when i=5
Sec
Hello
when i=6
Sec
Hello
when i=7
Sec
Hello
Outside loop
--------------------------------------------------------------------------------------------------------------------
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
a=[10,20,15,12,18]
x=eval(input("Enter the element to be searched : "))
for i in range(len(a)):
    if a[i]==x:
        print("Found at index: ",i)
        break
else:
        print("Not found")
-----------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  											                                                                           15 is  found  at  index  8
												   15 is  found   3  times
'''
a=[10,20,15,12,18,15,19,14,15,14]
x=int(input("Enter number to be searched : "))
count=0
for i in range(len(a)):
    if a[i]==x:
        print(x,"found at index :",i)
        count+=1
if count==0:
    print("not found")
------------------------------------------------------------------------------------------------------------------------------------
#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25) #error
print(a) #25
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7) #13
print(a) #13
print((a = 6) + 7) #error
---------------------------------------------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd') #Hyd
else:
	print('Sec : ' , b)
if  c = 0:
	print('Hyd') #Hyd
else:
	print('Sec')
----------------------------------------------------------------------------------------------------------------------------------
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
sum=0
count=0
try:
    while True:
        x=eval(input("Enter values press (ctrl+z) to stop inputs : "))
        sum=sum+x
        count=count+1
except EOFError:
    pass
if count>0:
    print(sum/count)
else:
    print("no input")
-------------------------------------------------------------------------------------------------------------------------------------
#  del  operator  demo program  (Home  work)
a = 25
print(a)  #25
del   a 
print(a) #error
------------------------------------------------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25 25 25
del   a
print(b , c) #25 25
print(a) #error 
del   b
print(c) #25
print(b) #error
del   c
print(c) #error
--------------------------------------------------------------------------------------------------------------------------
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 10.8 Hyd
del   a , b , c
print(a) #error
print(b) #error
print(c)  #error
--------------------------------------------------------------------------------------------------------------------------
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2]  
print(a) #[10 , 20 , 18]
del  a
print(a) error
print(a[0])error
-------------------------------------------------------------------------------------------------------------------------



