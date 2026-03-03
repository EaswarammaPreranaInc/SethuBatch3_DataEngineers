# for i in range(65,91):
#     print(chr(i),end=' ',sep=" ")
# print()
# for j in range(97,123):
#     print(chr(j),end=' ',sep=" ")

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

# N = int(input("Enter the fibonacci : "))

# count=0
# a=0
# b=1
# while count<=N :
#     print(a)
#     count+=1
#     c=a+b
#     a=b
#     b=c

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

# x= int(input("Enter a number :"))

# a=0
# b=1
# while a<x:
#     c=a+b
#     a=b
#     b=c
# if a==x :
#     print("Found")
# else:
#     print("not found")

# Find  outputs  (Home  work)
# for  i  in  range(1 , 8):
# 	print(i)
# 	if   i % 3 == 0:
# 		continue
# 	else:
# 		print('Sec')
# 	print('Hello')
# else:
# 	print('else  suite')
# # End  of  the  loop
# print('Outside  loop')

# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# 7
# Sec
# Hello
# else  suite
# Outside  loop

# Find  outputs  (Home  work)
# for  i  in  range(1 , 8):
# 	print(i)
# 	if  i == 8:
# 		break
# 	else:
# 		print('Sec')
# 	print('Hello')
# else:
# 	print('else  suite')
# # End  of  the  loop
# print('Outside loop')

# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# Sec
# Hello
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# Sec
# Hello
# 7
# Sec
# Hello
# else  suite
# Outside loop


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

# x= eval(input("Enter the list : "))
# y=int(input("Enter the element in the list to be searched :"))
# b=True
# for i in range(len(x)):
#     if y==x[i]:
#         print(F'Found at index {i}')
#         b=False
#         break
# if b:
#     print("Element not found")



# x= eval(input("Enter the list : "))
# y=int(input("Enter the element in the list to be searched :"))
# b=True
# count = 0
# for i in range(len(x)):
#     if y==x[i]:
#         print(F'Found at index {i}')
#         count+=1
#         b=False
# print(count)
# if b:
#     print("Element not found")


 #  del  operator  demo program  (Home  work)
# a = 25
# print(a)  
# del   a 
# # print(a) # Error deletes a 
#  # Find  outputs  (Home  work)
# a = b = c = 25
# print(a , b , c)
# del   a
# print(b , c)
# # print(a)  # Error
# del   b
# print(c)
# # print(b)  Error
# del   c
# # print(c) Error
#  #  Can  multiple  objects  be  deleted  with  same  del  operator ?
# a , b , c = 25 , 10.8 , 'Hyd'
# print(a , b , c)
# del   a , b , c
# # print(a)  Error
# # print(b) Error
# # print(c) Error
#  # Find outputs  (Home  work)
# a = [10 , 20 , 15 , 18]
# print(a)  
# del  a[2]  
# print(a) 
# del  a
# # print(a)  Error 
# # print(a[0])  Error 
# # Find outputs  (Home work)
# a = (10 , 20 , 15 , 18)
# print(a)  
# print(a[0]) 
# # del  a[2]  Error
# del  a 
# # print(a)  Error
# # print(a[0]) Error

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
# '''
# sum=0
# counter=0
# try:
#     while True : 
#       a =  eval(input("Enter inputs : "))
#       sum+=a
#       counter+=1
# except EOFError:
#    c = sum/counter
#    print(c)


 #  Walrus   operator (:=)  demo  program
# print(a := 25)
# print(a = 25)
# print(a)
# print(a := 6 + 7)
# print(a)
# print((a := 6) + 7)
# print(a)
# # print((a = 6) + 7) Error Wrong syntax
#  # Find  outputs  (Home  work)
# a = 0
# if  a == 0:
# 	print('Hyd')
# else:
# 	print('Sec')
# if  b := 0:
# 	print('Hyd')
# else:
# 	print('Sec : ' , b)
# # if  c = 0:
# 	# print('Hyd') Error
# else:
# 	print('Sec')