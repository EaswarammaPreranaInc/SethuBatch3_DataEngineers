Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
output :

for i in range(65,91):
    print(chr(i),end=" ")
print()
for j in range(97, 123):
    print(chr(j), end=" ")


Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

output:

output:
 n = int(input())
 a, b = 0, 1
 i = 0
 while i < n:
     print(a, end=" ")
     a, b = b, a+b
     i+=1

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
 '''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series

n = int(input())
a, b = 0, 1
i = 0
while i <= n:
    if a == n:
        print("found")
        break
    a, b = b, a+b
    i+=1
else:
    print("Not found")




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


output:
1
sec
hello
2
sec
hello
3
4
sec
hello
5
sec
hello
6
7
sec
hello
else suite
Outside loop



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

output:
1
sec
hello
2
sec
hello
3
sec
hello
4
sec
hello
5
sec
hello
6
sec
hello
7sec
hello
else suite 
Outside loop


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

output:
n = list(map(int, input("Enter any numbers:").split()))
print(n)

b = int(input('Enter a value to be searched:' )) 
for i in range(0, len(n)):
 
  if n[i] == b:
    print("Found at index", i)
    break
else:
    print('Not found')




 Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15 is  found  at  index  2
												   15 is  found  at  index  5
												   15 is  found  at  index  8
												   15 is  found   3  times
'''



output:

n = list(input("Enter any values:"))
print(n)
a = input("Enter a value to search in the list:")
count = 0
for i in range(len(n)):
    if n[i] == a:
        count+=1
        print("Found at index", i)
    
print(f'{a} found {count} times')   



 #  Walrus   operator (:=)  demo  program
print(a := 25)  # Assign the value to a variable AND return that value at the same time
print(a = 25) # assigning the value to the reference
print(a) # 25   prints object 25 with reference

print(a := 6 + 7)  # 13
print(a)   # # 13
print((a := 6) + 7) # 13
print(a)    # 13
print((a = 6) + 7)  # Error


 # Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')  # Hyd
else:
	print('Sec')
if  b := 0:   
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec :  0
if  c = 0:
	print('Hyd')   # Error
else:
	print('Sec')



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

output:

total = 0
count = 0

while True:
    try:
        x = input("Enter value: ")

        value = eval(x)      # converts 25, 10.8, True correctly
        total += value
        count += 1

    except EOFError:
        break

if count > 0:
    print("Average =", total / count)
else:
    print("No input given")


 #  del  operator  demo program  (Home  work)

a = 25  # assigning value to object a
print(a)  # 25
del   a deleting the reference of object
print(a) # name error


 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  # 25 25 25
del   a  # reference a deleted
print(b , c)  # 25 25
print(a)  # name error
del   b  # reference b deleted
print(c)  # 25
print(b)  # name error
del   c # reference c deleted
print(c) # name error


 #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)  # 25 10.8 Hyd
del   a , b , c   # deleting references a , b ,c
print(a)   # Name error
print(b)    # Name error
print(c)   # Name error



 # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)    #  [10 , 20 , 15 , 18]
del  a[2]   # deleting reference a[2]
print(a)  # [10 , 20 , 18]
del  a   # deleting entire list
print(a)  # name error
print(a[0])  # error


 # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)    # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2]  # tuple there is no deleting reference
del  a  # deleting entire list
print(a)   # name error
print(a[0])  # name error