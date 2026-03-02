'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
# Code :
for i in range(65,90) :
    print(chr(i),end=" ")
print()
for i in range(97,122) :
    print(chr(i),end=" ")
'''
Output :
A B C D E F G H I J K L M N O P Q R S T U V W X Y 
a b c d e f g h i j k l m n o p q r s t u v w x y

'''
'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
# Code :
try:
    n = int(input("Enter the number of terms to print : "))
    if n<=0:
        print("Invalid input")
    elif n==1:
        print(0)
    else:
        a = 0
        b = 1
        print(a,b,sep=",",end=",")
        i = 2
        while i < n:
            c = a + b
            if i == n-1:
                print(c)
            else:
                print(c,end=",")
            a = b
            b = c
            i+=1
except:
    print("Enter the integer input")
'''
Output:
Enter the number of terms to print : 6
0,1,1,2,3,5
'''
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
# Code :
try:
    n = int(input("Enter the value to be searched : "))
    if n<0:
        print("Invalid input")
    elif n==0 or n==1:
        print("Found")
    else:
        a = 0
        b = 1
        c = a + b
        while c <= n:
            if c ==n :
                print("Found")
                break
            a = b
            b = c
            c = a+b
        else:
            print("Not Found")
except:
    print("Enter the integer input")
'''
Output:
Enter the value to be searched : 10
Not Found

Enter the value to be searched : 21
Found
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
Output:
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
Output:
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
# Code:
try:
    list = eval(input("Enter any list : "))
    n = int(input("Enter the element to be searched : "))
    for i in range(len(list)):
        if list[i] == n:
            print(F"Found at index  :  {i}")
            break;
    else:
        print("Not Found")
except:
    print("Enter the list input")

'''
Output:
Enter any list : [10,20,15,12,18]
Enter the element to be searched : 15
Found at index  :  2

Enter any list : [10,20,15,12,18]
Enter the element to be searched : 19
Not Found
'''
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
# Code:
try:
    list = eval(input("Enter any list : "))
    n = int(input("Enter the element to be searched : "))
    count = 0
    for i in range(len(list)):
        if list[i] == n:
            print(F"{n} is found at index {i}")
            count+=1
    print(F"{n} is found {count} times")
except:
    print("Enter the list input")

'''
Output:
Enter any list : [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
Enter the element to be searched : 15
15 is found at index 2
15 is found at index 5
15 is found at index 8
15 is found 3 times
'''
#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # Error beacuse of object a 
print(a) # 25 
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
print((a = 6) + 7) # Error because of invalid syntax


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

'''
Output:
Hyd
Sec : 0
Error because of c is not defined and it is not assign equal to operator
'''
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
# Output:
try:
    sum = 0
    c = 0
    while True:
        a = eval(input("Enter value (ctrl+z for stop) : "))
        c+=1
        sum +=a
except:
    print("Sum is : ",sum)
    print("Count is : ",c)

'''
Enter value (ctrl+z for stop) : 25
Enter value (ctrl+z for stop) : 10.8
Enter value (ctrl+z for stop) : True
Enter value (ctrl+z for stop) : 
Sum is :  36.8
Count is : 3
'''

#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a 
print(a) # Error because a is not defined

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a # Reference is deleted
print(b , c) # 25 25
print(a) # Error a is not defined
del   b # Reference is deleted
print(c) # 25
print(b) # Error b is not defined
del   c # Reference is deleted
print(c) # Error c is not defined

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # Error a is not defined
print(b) # Error b is not defined
print(c) # Error c is not defined

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [ 10 , 20 , 15 , 18 ]
del  a[2]  # the element 15 is deleted
print(a) # [ 10 , 20 , 18 ]
del  a # the entire list a is deleted
print(a) # Error a is not defined
print(a[0]) # Error a is not defined 

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 18)
print(a[0]) # 10
del  a[2] # Error because tuple cannot be modified it is immutable
del  a 
print(a)  # Error a is not defined
print(a[0]) # Error a is not defined


