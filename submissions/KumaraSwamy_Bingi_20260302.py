'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''

for i in range(65,91):
  print(chr(i),end = " ")
print()
for j in range(97, 123):
  print(chr(j),end = " ")















'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''


n = int(input('how many no of fibonacci numbers you want:'))

count=0
a,b = 0,1

while count<n:
  print(a, end = " ")
  a,b= b,a+b
  count+=1

















'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''



x = int(input("Enter a number: "))
a, b = 0, 1

while a < x:
    a, b = b, a + b

if a == x:
    print('Found')
else:
    print('Not Found')
















# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:                  # at i = 3 and i =6 iterattion this condition is true i.e continue is executed
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')


'''
output:

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
'''
























# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:         # i =8 is not possible range is from 0 to 7 only so this statement is never be True
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')


'''
output:
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
a= eval(input("enter the list:"))
x = int(input('Enter number to search:'))

for i in range(len(a)):
	if a[i]==x:
		print(F'Found at index {i}')
		break
else:
	print('Not Found')

















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

a= eval(input("enter the list:"))
x= int(input("enter the number to searched:"))
count = 0
for i in range(len(a)):
	if a[i]==x:
		print(F'{x} is found at index {i}')
		count+=1
		
print(F"{x} is found {count} times")























#  Walrus   operator (:=)  demo  program
print(a := 25)         # prints 25
print(a = 25)         # Error
print(a)             #25
print(a := 6 + 7)    #13
print(a)             #13
print((a := 6) + 7)   #13
print(a)               #13
print((a = 6) + 7)       # Error



















# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')                 # this is printed
else:
	print('Sec')
if  b := 0:                     # just assign refrence b to object 0
	print('Hyd')                   
else:
	print('Sec : ' , b)
if  c = 0:                      # Error
	print('Hyd')            
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
'''


total_sum = count = 0

while True:
    try:
        val = input("> ")
        # Convert "True" to 1, otherwise float; False becomes 0
        total_sum += 1.0 if val == "True" else float(val)
        count += 1
    except EOFError:
        break
    except ValueError:
        pass 

if count:
    print(f"Average: {total_sum / count}")
























#  del  operator  demo program  (Home  work)
a = 25
print(a)  # prints 25
del   a    # deletes object 25
print(a)   # error









# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  # 25 25 25
del   a           # removes refrence a pointing to 25
print(b , c)      # 25 25
print(a)          # error
del   b           # removes refrence b pointing to 25
print(c)          # print 25
print(b)          # error
del   c           # delete refrence c and also object 25
print(c)          # error object not found
























#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)      # 25 10.8 Hyd
del   a , b , c      # all three refrence along with their object are deleted
print(a)    # error
print(b)    #error
print(c)    #error





















# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)   # [10,20,15,18]
del  a[2]  # deletes 15 from list a
print(a)   # [10,20,18]
del  a     # deletes entire list
print(a)   # error a is not defined
print(a[0]) # error










# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10,20,30,40)
print(a[0]) # 10
del  a[2]  # error tuple is immutable
del  a    # tuple a is deleted
print(a)  # error a is not defined
print(a[0]) # error










