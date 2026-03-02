'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for i in range(65,91):
    print(chr(i), end=' ')     # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
print()
for j in range(97,123):
    print(chr(j), end=' ')     # a b c d e f g h i j k l m n o p q r s t u v w x y z
print()     
#==============================================================================================================

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

n = int(input('enter a value :'))  # 6
print('fibonacci series')
a = 0
b = 1
c = a + b
while (a <= n):
    print(a)
    c = a + b
    a = b
    b = c

'''
fibonacci series
0
1
1
2
3
5
'''

#==============================================================================================================

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

#==============================================================================================================

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
'''

#==============================================================================================================

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

#==============================================================================================================

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

x = eval(input('Enter any list :'))                       # [10 , 20 , 15 , 12 , 18]
a = int(input('Enter an element to be searched : '))
for i in range(len(x)):
	if x[i] == a:
		print(f'Found at index : {i}')
		break
else:
	print('Not Found')                   # Found at index : 4
	
#==============================================================================================================

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

a = [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
b = int(input('enter an element to be searched :'))     # 5
c = 0
for i in range(len(a)):
	if a[i] == b:
		c += 1
		print(f'{b} is found at index {i}')
print(f'{b} is found {c} times')                        # 15 is found at index 2
														# 15 is found at index 5
														# 15 is found at index 8
														# 15 is found 3 times

#==============================================================================================================

#  Walrus   operator (:=)  demo  program
print(a := 25)      # 25
#print(a = 25)       # error
print(a)            # 25       it refers same object 25
print(a := 6 + 7)   # 13
print(a)            # 13       it refers same object 13
print((a := 6) + 7) # 13
print(a)            # 6        it refers object 6
#print((a = 6) + 7)  # error

#==============================================================================================================

'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError  ^

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''

a = [25 , 10.8 , True]
b = 0
for i in a:
    b += i
print(b/len(a))      # 12.66666