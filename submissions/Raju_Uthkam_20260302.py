'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for i in range(26):
    print(chr(65 + i),end = ' ')
print()
for i in range(26):
    print(chr(97 + i), end = ' ')


'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''


n = int(input('Enter any number : '))

a = 0
b = 1
count = 0
for i in range(1,n+1):
    print(a,end = ' ')
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

n = int(input('Enter a value to be searched : '))

a = 0
b = 1

for i in range(n+1):
    if a == n :
        print('found')
        break
    if a > n :
        print('Not found')
        break
    a,b = b , a+b
else:
    ('Not found')
    

# Find  outputs  (Home  work)
for  i  in  range(1 , 8): #1 sec hello 2 sec hello 3 4 sec hello 5 sec hello 6 7 sec hello else suite outside loop
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


# Find  outputs  (Home  work)
for  i  in  range(1 , 8): #1 sec hello 2 sec hello 3 sec hello 4 sec hello 5 sec hello 6 sec hello 7 sec hello  else suite 8 outside loop
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


a = eval(input('Enter any list without duplicates : '))
n = int(input('Enter the element to be searched : '))

for i in range(0,len(a)):
    if a[i] == n :
        print(f'found at index {i}')
        break
else:
    print('Not found')
        
    

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

a = eval(input('Enter any list without duplicates : '))
n = int(input('Enter the element to be searched : '))
sum = 0 
for i in range(0,len(a)):
    if a[i] == n :
        print(f'found at index {i}')
        sum += 1
        continue

print(f'{n} is found {sum} times ')



#  Walrus   operator (:=)  demo  program
print(a := 25) #25
#print(a = 25) #Error
print(a) #25
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7) #13
print(a) #6
#print((a = 6) + 7) #Error


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec')
if  b := 0: 
	print('Hyd') 
else:
	print('Sec : ' , b) #sec : 0
#if  c = 0: #Error
	#print('Hyd')
#else:
	#print('Sec')


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
n = eval(input('Enter inputs : '))
sum = 0
count = 0

for i in range(len(n)):
    if n:
        sum += n
        count += 1
print(f'{sum=},{count=}')
print(f'Average = {sum} / {count}')



#  del  operator  demo program  (Home  work)
a = 25
print(a) #25 
del   a 
print(a) #Error because there is no refrence a 



# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25,25,25
del   a
print(b , c) #25,25
#print(a)   #Error
del   b
print(c) #25
#print(b) #Error
del   c
#print(c) #error



#  Can  multiple  objects  be  deleted  with  same  del  operator ? Yes we can delete multiple objects with del operator
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25,10.8,Hyd
del   a , b , c
#print(a) 
#print(b) 
#print(c)


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10 , 20 , 15 , 18]
del  a[2]  
print(a) #[10 , 20  , 18]
del  a
#print(a) #error 
#print(a[0]) #Error


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10 , 20 , 15 , 18)
print(a[0]) #10 
#del  a[2] #Error
#del  a 
#print(a) #Error  
#print(a[0]) #Error