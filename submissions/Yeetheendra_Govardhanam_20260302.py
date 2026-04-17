#Topic - 1
'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

"""
for al in range(ord('A'),(ord('Z')+1)):
    print(chr(al), end =' ')
print()
for al in range(ord('a'),(ord('z')+1)):
    print(chr(al), end =' ')
print()
"""

#Topic - 2

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

"""
n = abs(int(input("Enter the first  'n'  terms  of  fibonacci  series : ")))
a = 0
b = 1
for x in range(n):
   c = b + a
   print(a, end =" ")
   a = b
   b = c
""" 
    
#Topic - 3

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
"""
n = int(input("Enter value to be searched : "))
a = 0
b = 1
c =[]
x = 0
while n>= a:
    d = a+b
    c.append(a)   
    a = b
    b = d

for e in c:
    if(e==n):
        x = e
        
if(n==x):        
    print('Found')
else:
    print('Not Found')
"""

#Topic - 4
'''
#Topic - 4.1
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
"""
1
sec
Hello
2
sec
Hello
3
4
sec
Hello
5
sec
Hello
6
7
sec
Hello
else  suite
Outside  loop
"""
'''
#Topic - 4.2
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

"""
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
Outside  loop
"""

#Topic - 5

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
"""
c = eval(input("Enter any list: "))
n = eval(input("Enter the element to be searched : "))
x = 0
for e in range(len(c)):
    if(c[e] == n):
        x = e
        
if(x==0):        
     print('Not Found')
else:
   print('Found at the index : ', x)
"""

#Topic - 6

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

"""
c = eval(input("Enter any list: "))
n = eval(input("Enter the element to be searched : "))
x = 0
count = 0
for e in range(len(c)):
    if(c[e] == n):
        x = e
        if(x!=0):        
           print(f'{n} is found at index : {x}')  
           count +=1
if(x==0):
    print('Not Found')
print(F"{n} is found {count} times")
"""

#Topic - 7
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

"""
x = eval(input("Enter the values : "))
sum = 0
ctr = 0
for y in x:
    sum += y
    ctr = y + ctr
print("sum :", sum)
print("ctr :", ctr)
"""

#Topic - 8
"""
#Topic - 8.1
#  Walrus   operator (:=)  demo  program
print(a := 25) #25
#print(a = 25)  #error
print(a) #25
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7) #13
print(a) #6
#print((a = 6) + 7)# error


#Topic - 8.2
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd') 
else:
	print('Sec : ' , b) #Sec : 0
#if  c = 0: # error
#	print('Hyd') #Hyd
#else:
#	print('Sec')

#Topic - 8.3
#  del  operator  demo program  (Home  work)
a = 25
print(a) #25 
del   a 
#print(a) #error

#Topic - 8.4
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25 25 25
del   a
print(b , c) #25 25
#print(a) #error
del   b
print(c)#25
#print(b)#error
del   c
#print(c) #error


#Topic - 8.5
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 10.8 Hyd
del   a , b , c
#print(a) #error
#print(b) #error
#print(c) #error

#Topic - 8.6
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10 , 20 , 15 , 18]
del  a[2]  
print(a) # [10 , 20 , 18]
del  a
#print(a) # error
#print(a[0]) #error

#Topic - 8.7
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10 , 20 , 15 , 18)
print(a[0]) #10
#del  a[2] #error
del  a # whole tuple is deleted
#print(a)  #error
#print(a[0]) #error
"""