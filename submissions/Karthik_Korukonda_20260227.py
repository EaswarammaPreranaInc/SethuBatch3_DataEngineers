# # a = int(input("Enter the value of a : "))

# # first = 0
# # second = 1

# # print(first)

# # while True:
# #     temp = first + second
# #     if temp > a:
# #         break
# #     print(temp)
# #     first = second
# #     second = temp


# a = eval(input("Enter the values of the list : "))

# for i in a :
#     print(i)


# a = eval(input("Enter the values of the list : "))

# for i in a :
#     print(i, end=", ")


# # a = int(input("enter the range : "))
# # for i in range(a) :
# #     print(i)

# # Find  outputs  (Home  work)
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
# 	print(x) #10 \n 30 \n 50
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
# 	print(x) #20 \n 40 \n 60
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
# 	print(x) {10:20} {30:40} {50:60}
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
# 	print(x) # 10 30 50

# # Find outputs  (Home  work)
# a = {10 : 20 , 30 : 40 , 50 : 60}
# for  x , y  in   a . items():
# 	print(x , y ,) sep = '...' 10...20 30...40 50...60
# for  x ,  y  in   a:
# 	print(x , y) # Error
# for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
# 	print(x , y , sep = '...') #only keys are returned
# # Identify  error  (Home  work)
# for  x  in   123:
#         print(x) # Error 123 is integer
# # Find  outputs  (Home  work)
# for  x   in   ():
#         print(x) #Empty tuple
# for  x   in  []:
#         print(x)# empty list
# for  x   in   {}:
#         print(x) empty dict
# for  x   in   set():
#         print(x) empty set
# for  x   in   '':
#         print(x) empty string
# for  x  in  range(10 , 10):
# 	print(x) No output as start is 10 and end is 9 and step would be +1 
# for  x  in   range():
# 	print(x) error
# for  x  in   (25):
# 	print(x) error as 25 is int not tuple
# #  Nested  Loop  demo  program
# for  i  in  range(1 , 4):
# 	for  j  in  range(1 , 5):
# 			print(i ,  j)  #
# 	print('Hello')
# print('Bye')
# 1 1
# 1 2
# 1 3
# 1 4
# Hello
# 2 1
# 2 2
# 2 3
# 2 4
# Hello
# 3 1
# 3 2
# 3 3
# 3 4
# Hello
# Bye
# '''
# (Home  work)
# Write  a  program  to  print  first  20  even  numbers 

# 1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

# 2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

# 3) Hint:  Do  not  use  range  object

# 4) Use  while  loop
# '''
# i = 1
# while i <= 20:
#     print(2 * i)
#     i += 1
# '''
# Write  a  program  to  print  first  20  odd  numbers

# 1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

# 2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

# 3) Hint:  Do  not  use  range  object

# 4) Use  while  loop
# '''
# i = 1
# while i <= 20:
#     print(2 * i - 1)
#     i += 1
# '''
# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

# What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

# 1) Hint:  Do  not  use  range  object

# 2) Use  while  loop
# '''
# n = int(input("Enter value of n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1
#  '''
# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

# What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

# 1) Hint:  Do  not  use  range  object

# 2) Use  while  loop
# '''
# '''
# Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

# 1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

# 2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

# 3) Use  for  loop
# '''
# n = int(input("Enter n: "))
# total = 0

# for i in range(1, n + 1):
#     total += 1.1 * i

# print("Sum =", total)
# '''
# Write  a  program  to  determine  sum  of  first  20  even  numbers

# 1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

# 2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

# 3) Use  for  loop
# '''
# total = 0

# for i in range(1, 21):
#     total += 2 * i

# print("Sum =", total)
# '''
# Write  a  program  to  determine  sum  of  first  20  odd  numbers

# 1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

# 2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

# 3) Use  for  loop
# '''
# total = 0

# for i in range(1, 21):
#     total += 2 * i - 1

# print("Sum =", total)
#  '''
# Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

# What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

# Hint:  Use  for  loop
# '''
# n = int(input("Enter n: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print("Sum =", total)
# # Find  outputs  (Home  work)
# for  i   in   range(1 , 8):
# 	print(i)
# 	if  i % 3  == 0:
# 			continue
# 	else:
# 			print('Sec')
# 	print('Hello')
# # End of loop
# print('Outside loop')
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
# Outside loop
#  # Identify Error  (Home  work)
# if ():
# 	print('Hyd')
# 	continue
# 	print('Sec') Error

# # Find outputs (Home  work)
# for  i   in   range(1 , 8):
# 	print(i)
# 	if   i % 3 == 0:
# 		break
# 	else:
# 		print('Sec')
# 	print('Hello')
# # End  of  the  loop
# print('Outside loop')
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# Outside loop
# # Identify Error  (Home  work)
# if(10 , 20 , 30):
# 	print('Hyd')
# 	break
# 	print('Sec') #error as break 

