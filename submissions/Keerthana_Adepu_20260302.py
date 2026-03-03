#Programming Homework #1
'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
for i in range(65, 91):
    print(chr(i) , end = ' ')
    i += 1
print()
for j in range(97, 123):
    print(chr(j) , end = ' ')
    j += 1



#Programming Homework #2
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n = int(input('Enter the number of terms:'))
print(f'The first {n} terms of Fibonacci Series are:')
if n == 0:
    print('')
elif n == 1:
    print(0)
else:
    a = 0
    b = 1
    c = a + b

    i = 1

    while i <= n:
        print(a)
        a = b
        b = c
        c = a + b
        i += 1


#Programming Homework #3
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x = int(input('Enter the number:'))

a = 0
b = 1
c = a + b
found = False

while a <= x:
    if a == x:
        found = True
        break
    a = b
    b = c
    c = a + b

if found:
    print('Found')
else:
    print('Not Found')
    


#Outputs Homework #1
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
'''



#Outputs Homework #2
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
Outside loop
'''



#Programming Homework #4
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

5) What action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
																														do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop
'''
a = eval(input('Enter a list without duplicates:'))
x = int(input('Enter the element to be searched:'))

for i in range(len(a)):
    if a[i] == x:
        print(f'{x} found at {i}')
        break
else:
    print(f'{x} is not an element in the given list.')




#Programming Homework #5
'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
				  15 is  found  at  index  5											   15 is  found  at  index  8
				  15 is  found   3  times
'''
a = eval(input('Enter a list without duplicates:'))
x = int(input('Enter the element to be searched:'))
count = 0

for i in range(len(a)):    
    if a[i] == x:
        print(f'{x} found at {i}')
        count += 1

if count == 0:
    print(f'{x} is not an element in the list.')
else:
    print(f'{x} is found {count} times in the list.')



#Walrus Operator (:=) Homework
print(a := 25) # 25
print(a = 25) # error because '=' only assigns the volume, the result of it is nothing in python
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7)
print(a) # 6
print((a = 6) + 7) # error



#Outputs Homework #3
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec') # 'Hyd'
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) # 'Sec' = 0
if  c = 0:
	print('Hyd')
else:
	print('Sec') # error because c is not defined



#Programming Homework #6
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
sumx = 0
ctr = 0
try:
    while True:
        a = eval(input('Enter the value:'))
        sumx = sumx + a
        ctr += 1
except EOFError:
    print('End of inputs.')

if ctr > 0:
    avg = sumx/ctr
    print(f'Average of all inputs = {avg}')
else:
    print('No inputs were given.')

# works for ctrl + d, not ctrl + z
        


#del Operator Program
a = 25
print(a) # 25 
del   a 
print(a) # error because reference a has been deleted and because object a has no reference, even it is deleted because object can't be without a reference in python



#Outputs Homework #4
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a) # error because a is not a defined object
del   b
print(c) # 25
print(b) # error because b is not a defined object
del   c
print(c) # error because c is not a defined object and because 25 does not have anymore references, that object is also deleted



#Can  multiple  objects  be  deleted  with  same  del  operator?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # error because a is not a defined object
print(b) # error because b is not a defined object
print(c) # error because c is not a defined object



#Outputs Homework #5
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2]  
print(a) # [10 , 20 , 18]
del  a
print(a) # error because a is not a defined object
print(a[0]) # error because a is not a defined object



#Outputs Homework #6
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18) 
print(a[0]) # 10
del  a[2] # error # an object in tuple cannot be deleted because it is immutable
del  a 
print(a) # error because a is not a defined object
print(a[0]) # error because a is not a defined object
