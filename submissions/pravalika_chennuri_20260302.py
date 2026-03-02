'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for i in range(65,123):
    if i <= 90:
        print(chr(i),end=" ")
    elif i>=97 and i<=122:
        print(chr(i),end=" ") 
    elif i == 91:
        print()

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

n = int(input("enter a value : "))
a=0
b=1
while n :
    print(a)
    c=a+b
    a=b
    b=c
    n-=1


'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

n = int(input("enter a value : "))
a=0
b=1
while a <= n:
    if a == n:
        print("found")
        break
    c=a+b
    a=b
    b=c
else:
    print("not found")      

	
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
print('Outside  loop') # 1 \n Sec \n Hello \n 2 \n Sec \n Hello \n 3 \n 4 \n Sec \n Hello \n 5 \n Sec \n Hello \n 6 \n 7 \n Sec \n Hello \n else suite \n outside loop

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
print('Outside loop') # 1 \n Sec \n Hello \n 2 \n Sec \n Hello \n 3 \n outside loop


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

n = eval(input("enter a list : "))
x = int(input("enter a value : "))
for i in range(len(n)):
    if x == n[i]:
        print(f"found at index {i}")
        break
else:
    print("not found")

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

n = eval(input("enter a list : "))
x = int(input("enter a value : "))
c = 0 
for i in range(len(n)):
    if x == n[i]:
        c+=1
        print(f"{x}found at index {i}")
else:
    print(f"{x} found {c} times")


#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
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
	print('Hyd') 
else:
	print('Sec : ' , b) # Sec :0
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



#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25  
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
print(b) #error
del   c
print(c) # error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # error
print(b) # error
print(c) # error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [10, 20, 15, 18]
del  a[2]  
print(a) # [10, 20, 18]
del  a
print(a) # error
print(a[0]) # error

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  # (10, 20, 15, 18)
print(a[0]) # 10
del  a[2] 
del  a 
print(a)  # error
print(a[0]) # error
