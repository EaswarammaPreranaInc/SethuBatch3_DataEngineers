'''Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

print("Upper and Lower case alphabets")
# Uppercase pattern
for ch in range(65, 91):
    print(chr(ch), end='')
print()
# Lowercase alphabets
for ch in range(97, 123):
    print(chr(ch), end='')
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
x=int(input("Enter a Input value:")
a=0
b=1
print("First" x "Terms:")
for i in range(x):
   print(a,end='')
   a,b=b,a+b
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
x=int(input("Enter a Input value:")
a=0
b=1
while (b<x):
  a,b=b,a+b
if (b==x):
  print("Found")
else:
  print("Not Found")
'''
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
'''#Output
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
Outside Loop
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
''' Output:
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
'''
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
lst = [10, 20, 15, 12, 18]

x = int(input("Enter element to search: "))

found = False

for i in range(len(lst)):
    if x == lst[i]:
        print("Found at index", i)
        found = True
        break          # Stop searching after found

if not found:
    print("Not found")

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
lst = eval(input("Enter List:"))
x = int(input("Enter element to search: "))
found = False
count=0
for i in range(len(lst)):
    if x == lst[i]:
        print("Found at index", i)
        found = True
        count=count+1
        continue
        print("Found times", count)
if count > 0:
    print(x, "is found", count, "times")
else:
    print(x, "is not found") 
#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25)  #Error
print(a)       # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7)  #13
print(a)    #6
print((a = 6) + 7)  #error
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


# output : Hyd
Sec :  0
SyntaxError


'''(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''


# output : sum = 0
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
print(a)  
del   a 
print(a)

# output : 25
NameError: name 'a' is not defined


# 11 . # Find  outputs  (Home  work)
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

# output : 25 25 25


# 12 . #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a) 
print(b) 
print(c)

# output : 25 10.8 Hyd
NameError: name 'a' is not defined

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  
del  a[2]  
print(a) 
del  a
print(a) 
print(a[0])

# output : [10, 20, 15, 18]

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  
print(a[0]) 
del  a[2] 
del  a 
print(a)  
print(a[0])

# output : (10, 20, 15, 18)
10
TypeError: 'tuple'

























