1.'''
 Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
for i in range(65, 91):  
    print(chr(i), end=" ")
print("\n") 
for i in range(97, 123): 
    print(chr(i), end=" ")
---------------------------------------------------------------------------------------------------------------------------------------------------------
2. '''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
'''
Write  a  program  to  print  fibonacci  series  upto   x

x = int(input('Enter  value  of  x  :  '))  
a = 0
b = 1
print(f"Fibonacci series (first {n} terms):")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
---------------------------------------------------------------------------------------------------------------------------------------------------------

3. '''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x = int(input('Enter value of x: '))
a = 0
b = 1
c = a + b
while c < x:
    a = b
    b = c
    c = a + b
if c == x:
    print('FOUND')
else:
    print('NOT FOUND')

---------------------------------------------------------------------------------------------------------------------------------------------------------

4. # Find  outputs  (Home  work)
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
output:-
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
Outside  loop
---------------------------------------------------------------------------------------------------------------------------------------------------------

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
output:-
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

---------------------------------------------------------------------------------------------------------------------------------------------------------
6. '''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																												Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
																														do  not  search  for  'x'  in  rest  of  the  list
'''
list = [10, 20, 15, 12, 18]
x = int(input("Enter element to search: "))
found = False
for i in range(len(list)):
    if list[i] == x:
        print(f"Found at index {i}")
        found = True
        break 
if not found:
    print("Not found")

---------------------------------------------------------------------------------------------------------------------------------------------------------
7. '''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
			          15 is  found  at  index  5
				  15 is  found  at  index  
			          15 is  found   3  times
'''
list = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Search for: "))
count = 0
for i in range(len(list)):
    if list[i] == x:
        print(f"{x} is found at index {i}")
        count = count + 1
if count > 0:
    print(f"{x} is found {count} times")
else:
    print(f"{x} was not found in the list")
---------------------------------------------------------------------------------------------------------------------------------------------------------

8. #  Walrus   operator (:=)  demo  program
print(a := 25)#25
print(a = 25)#error()
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)# a := 6 + 7
print(a)#13
print((a = 6) + 7)#error
---------------------------------------------------------------------------------------------------------------------------------------------------------

 9.# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')#Hyd
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)# Sec :0
if  c = 0:
	print('Hyd')
else:
	print('Sec')#error
 '''
---------------------------------------------------------------------------------------------------------------------------------------------------------
10.(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------
11.#  del  operator  demo program  (Home  work)
a = 25
print(a) #25
del   a #removes value of a
print(a)#name error
---------------------------------------------------------------------------------------------------------------------------------------------------------
12 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a 
print(b , c)#25 25
print(a)  # name error
del   b
print(c)#25
print(b) # name error
del   c
print(c)# name error
---------------------------------------------------------------------------------------------------------------------------------------------------------
13. #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a) 
print(b) 
print(c)
---------------------------------------------------------------------------------------------------------------------------------------------------------
14. # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10 , 20 , 15 , 18]
del  a[2]  
print(a) [10 , 20 , 18]
del  a
print(a) # name error
print(a[0])# name error
---------------------------------------------------------------------------------------------------------------------------------------------------------
15. # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10 , 20 , 15 , 18)
print(a[0]) #10
del  a[2] #error(tuple doesn't support delete method)
del  a 
print(a) #name error  
print(a[0])#name error  










