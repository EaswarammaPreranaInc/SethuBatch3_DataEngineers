# '''
# Write  a  program  to  determine  bill  amount  and  input  is  units

# Units                                                      Cost
# ------------------------------------------------------------
# First  100  units(0 - 99)					Rs. 3.00 / unit

# Next  100  units(100 - 199)				Rs. 3.50 / unit

# Next  200  units(200 - 399)		    	Rs. 4.00 / unit

# Next  300  units(400 - 699)				Rs. 4.50 / unit

# Above  700  units(units >= 700)		Rs. 5.00 / unit
# ---------------------------------------------------------------
# Let  units  be  1200
# What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

# Hint:  Use  match  ...  case   but  not  if ... else
# '''
# units = int(input('Enter  units :   '))   #   175
# match  units // 100:
# 	case  0:   #   units  between  0  and  99
# 				cost = units * 3.00
# 	case  1:  #  units  between  100 and  199
# 				cost =  100 * 3.00 + (units - 100) * 3.50
# 	case  2:
# 				cost = 100*3.50+(units- 199)* 3.50
# 	case  3:
# 				cost = 100*4.00+(units -399)*
# 	case  ???:				
# 				cost = 
# print('Bill  amount  :  ' , cost)


'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''

# n=int(input("Enter the number "))
# a=0
# print(a)
# b=1
# print(b)
# c=a+b
# while c<=n :
#      print(c)
#      a=b
#      b=c
#      c=a+b
    
# y=[20,49,'hi',90]
# for x in y:
#     print(x)
# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
# print()

# How  to  print  each  character  of   string  'Hyd'  with  for  loop
# print()
# How  to  print  each  element  of   range(5)  with  for  loop

# list = [10 , 20 , 15 , 18]
# for x in list :
#     print(x)
    
# string  ='Hyderbad'
# for x in string:
#     print(x)
# for x in range(5):
#     print(x)    

# # Find  outputs  (Home  work)
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
# 	print(x) #10 30 50  20 40 60
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
# 	print(x)  #20 40 60
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
# 	print(x) (10,20) (30,40) (50,60)
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
# 	print(x) # 10 30 50

# # Find outputs  (Home  work)
# a = {10 : 20 , 30 : 40 , 50 : 60}
# for  x , y  in   a . items():
# 	print(x , y , sep = '...')#(10...20) (30...40)  (50...60)
# for  x ,  y  in   a:
# 	print(x , y  # bracket is missing
# for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}: # error because no objects declare here
# 	print(x , y , sep = '...')
# Identify  error  (Home  work)

# for  x  in   123: #error 123
#         print(x)

# Find  outputs  (Home  work)
# for  x   in   ():
#         print(x) # 0
# for  x   in  []:
#         print(x) #0
# for  x   in   {}:
#         print(x) #0
# for  x   in   set():
#         print(x) #0
# for  x   in   '':
#         print(x)#0
# for  x  in  range(10 , 10):
# 	print(x)#0
# for  x  in   range():
# 	print(x) # : error
# for  x  in   (25):
# 	print(x) # (25) is error

# #  Nested  Loop  demo  program
# for  i  in  range(1 , 4):
# 	for  j  in  range(1 , 5):
# 			print(i ,  j)  
# 	print('Hello')
# print('Bye') #1 1
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

# # How  to  print  each  element  and  the  corresponding  index
# a = [25 , 10.8 , 'Hyd' , True]
# for x in range(len(a)):
#              print( F"{a[x]} -{[x]}")
# # print('Indexed  based  for loop')
# # How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
# for x in range(len(a)):
#       print( F"{a[x]} -{[x]}")
# # print('For each loop')
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
# for x in a:
#     print(x,"-",a.index(x))

  #How  to  print  list  elements  in  reverse  order   without  slice
# a = [25 , 10.8 , 'Hyd' , True]

# # for i in range(len(a)):
# #     print(a[-i-1])
# # print('Indexed for loop')
# # How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop

# for x in a:
#     print(a[::-1])
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

# a = [25 , 10.8 , 'Hyd' , True]
# for x in range(len(a)-1,-1,-1):
#     print(a[x])
'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
# '''

# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
# print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)
# '''
# a = eval(input('Enter  1st  list  :  '))
# b = eval(input('Enter  2nd  list  :  '))
# c = []
# for x in range(min(len(a),len(b))):
#     c.append(a[x]+b[x])
#     print('3rd  list :',c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
"""a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice"""
# a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
# for x in range(2,5):
#     print(a[x])
#  Tricky  program
#  Find  outputs  (Home  work)
# a = [10 , 20 , 15 , 18]
# for  i  in  range(len(a)):
# 	a[i] +=  1
# print('a :  ' , a)
# b = [10 , 20 , 15 , 18]
# for  x  in   b:
# 	x += 1
# print('b :  ' ,  b)
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
# n=int(input("enter the nuber :"))
# i=1
# while i<=n:
#     print(2*i)
#     i+=1

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

# n=int(input("enter the number : ")) 
# i=1
# while i<=n:
#     print(i*2-1)
#     i=i+1
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
    
# n=int(input("Enter the Number :"))   
# i=1
# while i<=n:
#     print( i)
#     i=i+1 
    
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
# n=int(input("ENter the number :"))
# i=n
# while 0<i<=n:
#     print(i)
# #     i=i-1

# # Find  outputs  (Home  work)
# for  i   in   range(1 , 8):
# 	print(i)
# 	if  i % 3  == 0:
# 			continue 
# 	else:
# 			print('Sec') 
# 	print('Hello')  # skips 3 and 6  hello
# # End of loop
# print('Outside loop')
# # Identify Error  (Home  work)
# if ():
# 	print('Hyd')
# 	continue  # error because the continuw will use  in for or while loop
# 	print('Sec')
#  # Find outputs (Home  work)
# for  i   in   range(1 , 8):
# 	print(i)
# 	if   i % 3 == 0: 
# 		break
# 	else:
# 		print('Sec') 
# 	print('Hello')
# # End  of  the  loop
# print('Outside loop')
 # Identify Error  (Home  work)
# if(10 , 20 , 30):
# 	print('Hyd')
# 	break #error because in if we can use
# 	print('Sec')    \
   
        
