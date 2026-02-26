# '''
# Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

# First  complex  number   --->  3 + 4j
# 2nd   complex  number   --->  5 + 6j
# What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
# What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
# What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
# What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
# 												=  (15 -18j + 20j + 24) /  (25 + 36)
# 												=  39 / 61 + 2j / 61										   
# '''


# # x=complex(input("First comples number : "))
# # y= complex(input("2nd Complex number :"))
# # print(F"{(x)} +{(y)} = {x+y} ")
# # print(F"{ (x)} - {(y)} = {x-y}")
# # print(F"{ (x)} * {(y)} = {x*y} ")
# # print(F"{ (x)} / {(y)} = {x/y} ")

# '''
# (Home  work)
# Write  a  program  to  determine  area  and  perimeter  of  rectangle

# 1) What  are  the  inputs ?  --->  length  and   breadth

# 2) What  are  the  outputs  ?  ---> area  and  perimeter

# 3) What  is  the  area  of  rectangle  ?  ---> length * breadth

# 4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
# '''

# # x=eval(input("Enter the Lenght :"))
# # y=eval(input("Enter the breadth"))

# # print(F" Area = {  x *y} ")
# # print(F" Permeterc= { 2*(x+y)}")

# '''
# (Home  work)
# Write  a  program  to  determine  volume  of  a  sphere

# 1) What  is  the  input ?  ---> radius

# 2) What  is  the  output ?  ---> volume

# 3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
# '''
# # import math
# # x=eval(input("Enter the radius :"))
# # #y=eval(input("Enter the Sphere"))
# # print(F"{(4/3)* (math.pi)*(x**3)}")

# '''
# (Home  work)
# Write  a  program  to  determine  simple  interest  and  compound  interest

# 1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

# 2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

# 3) What  is  simple  interest  formula ?  --->  ptr / 100

# 4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
# '''
# # a=eval(input("enter the  principle"))
# # b=eval(input("enter the  Time"))
# # c=eval(input("enter the  rate of interest"))
# # print(F" Simple interset = {(a*b*c)/100 }")
# # print(F" Compound interst ={a * (1  +  c  /  100) ** b  -  a}")

# '''
# (Home  work)
# Write  a  program  to  swap  values  of  two   objects   using  3rd  object

# Let  x = 10  and  y = Hyd
# What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
# '''

# # x=eval(input("Enter the 1st Number"))
# # y=eval(input("Enter the 2nd number"))
# # print(F"Before swap {x=}, {y=}" )
# # temp=x
# # x=y
# # y=temp
# # print(F" After swap{x=}, {y=}")

# # # Identify  error
# # else:
# # 		print('else  suite')
# # print('Outside')  #if is missing 
#  # Identify  error
# # if  9 > 5 #: is missing
# # 	print('Hello') 
# # print('Bye')
#  # Identify  error
# # if  9 > 12:
# # 	print('Hyd')
# # else  #: Missing
# # 	print('Sec')
# # Identify  error
# # if  (10,20,15):
# # print('Hyd') #idenation error
# # else:
# # print('Sec')
#  # Identify  error
# # if  ():
# # 			print('Hyd')
# #   else: #indiadion error 
# # 					print('Sec')
# # print('Bye')
# #  # Identify  error
# # if  { }:
# # {
# # 	print('One')
# # 	print('Two')
# # 	print('Three')
# # }
# # else:
# # {
# # 	print('Four')
# # 	print('Five')
# # 	print('Six')
# # }
# # print('Bye')
# #  # Identify  error
# # if  ():
# # 	print('One')
# # 	print('Two')
# # 	print('Three')
# # else:
# # if  []:
# # 	print('Four')
# # 	print('Five')
# # 	print('Six')
# # else:
# # if  {}:
# # 	print('Seven')
# # 	print('Eight')
# # 	print('Nine')
# # else:
# # 	print('Hyd')
# # 	print('Sec')
# # 	print('Cyb')
# # print('Bye')
# # # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
# # a=int(input("Enter the number "))
# # if(a%2==0) :
# #     print("even Number")
# # else:
# #     print("Odd number")
# #  # Find outputs  (Home  work)
# # if():
# #         print('Hyd')
# #         print('Sec')
# #         print('Cyb')
# # else:
# #         print('One')
# #         print('Two')
# #         print('Three')
# # print('Bye')  #one two three bye
# #  # Find  outputs  (Home  work)
# # if{10 : 20 , 30 : 40}:
# #         print('Hyd')
# #         print('Sec')
# #         print('Cyb')
# # print('Bye') #print 4 statemnets
# #  # Find outputs  (Home  work)
# # if { }:
# # 	print('Hyd')
# # 	print('Sec')
# # 	print('Cyb')
# # print('Bye') #bye 
# # Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
# # import calendar
# # a=int(input("Enter the Month  number :"))
# # if(a==1):
# #     print("Jan")
# # elif (a==2):
# #     print("feb")  
# # elif (a==3):
# #     print("march")    
# # elif (a==4):
# #     print("April")    
# # elif (a==5):
# #     print("May")    
# # elif (a==6):
# #     print("June")    
# # elif (a==7):
# #     print("July")  
# # elif (a==8):
# #     print("Aug")    
# # elif (a==9):
# #     print("Sept")    
# # elif (a==10):
# #     print("Oct")    
# # elif (a==11):
# #     print("Nov")
# # elif (a==12):
# #     print("Dec")    
# # else:
# #     print("Invalid month")                
                
# '''Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
# 0 - Zero
# 1 - One
# 2 - Two
# ....
# 9 - Nine
# 10 - Invalid
# '''
# # b=int(input("Enter the number(0-9) : "))
# # a={0:"Zero",
# #     1:"One",
# #     2:"two",
# #     3:"Three",
# #     4:"Four",
# #     5:"Five",
# #     6:"six",
# #     7:"seven",
# #     8:"eight",
# #     9:"nine"
# # }
# # if 0<=b<=9 :
# #     print(a[b])
# # else :
# #     print("Invlid number")
# '''
# Write  a  program  to  test  year  is  leap  year  or  not

# 1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

# 2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

# 3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

# 4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

# 5) Hint:  3  conditions
# '''
        
# # a=int(input("enter the year : "))
# # if((a%4==0 or a%400==0)  and  a%100!=0 ):
# #   print("It is Leap year")
# # else:
# #     print("Not leap year")  
# '''
# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

# Hint:  Write  multiple  conditions
# '''
# a=int(input("enter the number 1 :"))
# b=int(input("enter the 2 number"))
# c=int(input("Enter the 3rd number :"))
# if(a>b and a>c):
#     print(a)
# elif(b>c and b<a):
#     print(b)    
# else :
#     print(c)    
