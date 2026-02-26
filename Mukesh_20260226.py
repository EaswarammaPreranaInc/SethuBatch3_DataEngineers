#  # Find  outputs  (Home  work)
# m = 4
# match  m:
# 	case  1:
# 		print('One')
# 	case  2:
# 		print('Two')
# 	case  3:
# 		print('Three')
# print('Bye') #Bye
#  # Identify  Error
# i = 2
# match  i:# error
# 	case  1:
# 		print('One')
# 	case  _:   #Error
# 		print('None of   the  above')
# 	case  2:
# 		print('Two')
# print('Bye')
#  # Find  outputs  (Home  work)
# m = 2
# match  m:
# 	case  1:
# 		print('One')
# 	case  _:  #Error
# 		print('Hello')
# 	case  _:  #error
# 		print('Bye')
# print('End')
#  #  Find  outputs  (Home  work)
# m = 1
# match  m:
# 	case  1:
# 		print('Hyd')
# 	case  1:
# 		print('Sec')
# 	case  1:
# 		print('Cyb')
# print('Bye') #hyd Bye
#  # Find  outputs  (Home  work)
# ch = 'B'
# match  ch:
# 	case   'A':
# 		print('Apple')
# 	case  'B':
# 		print('Book')
# 	case  'C':
# 		print('Cafe')
# 	case  _:
# 		print('None of  the  above')
# print('Bye') #book bye
# '''
# 1) What  are  the  outputs  if  input  is  -6 ? ---> #sec bye
# 2) What  are  the  outputs  if  input  is  15  ?  --->#two bye
# 3) What  are  the  outputs  if  input  is  10.8  ?  ---> #india china usa bye
# 4) What  are  the  outputs  if  input  is  0  ?  --->#cyb bye
# 5) What  are  the  outputs  if  input  is  -10  ?  --->#one bye
# 6) What  are  the  outputs  if  input  is  7  ?  --->#hyd bye
# '''
# x = eval(input('Enter any  number :  '))
# match  x:
# 	case  7 |  -6  |  0:
# 		print('Hyd')
# 		print('Sec')
# 		print('Cyb')
# 	case  -10 | 15:
# 		print('One')
# 		print('Two')
# 		print('Three')
# 	case  _:
# 		print('India')
# 		print('China')
# 		print('Usa')
# # End  of  match
# print('Bye')
# '''
# 1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> 
# 2) What  is  the  output  when  input  is  (10 , 0) ?  --->
# 3) What  is  the  output  when  input  is  (0 , -20) ?  --->
# 4) What  is  the  output  when  input  is  (0 , 0) ?  --->
# 5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->
# 6) What  is  the  output  when  input  is  [10 , 20]  ?  --->
# 7) What  is  the  output  when  input  is  [0 , -25]  ?  --->
# 8) What  is  the  output  when  input  is  ()  ?  --->
# 9) What  is  the  output  when  input  is  {10 , 20} ?  --->
# 10) What  is  the  output  when  input  is  (25,) ?  --->
# 11) What  is  the  output  when  input  is  {10 : 20} ?  --->
# '''
# 1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> #quadrant
# 2) What  is  the  output  when  input  is  (10 , 0) ?  ---># x -axis
# 3) What  is  the  output  when  input  is  (0 , -20) ?  --->#y -axis
# 4) What  is  the  output  when  input  is  (0 , 0) ?  --->#origin
# 5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->#not point
# 6) What  is  the  output  when  input  is  [10 , 20]  ?  --->--->#not point
# 7) What  is  the  output  when  input  is  [0 , -25]  ?  --->--->#not point
# 8) What  is  the  output  when  input  is  ()  ?  --->--->#not point
# 9) What  is  the  output  when  input  is  {10 , 20} ?  --->--->#not point
# 10) What  is  the  output  when  input  is  (25,) ?  --->--->#not point
# 11) What  is  the  output  when  input  is  {10 : 20} ?  --->--->#not point
# '''
# tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
# match  tpl:
# 	case  (0 , 0):
# 		print('Origin')
# 	case   (0 , y):
# 		print('y - axis')
# 	case   (x , 0):
# 		print('x - axis')
# 	case   (x , y):
# 		print('Quadrant')
# 	case  _:
# 		print('Not  a  point')
# '''
# Write  a  program  to  determine  bill  amount  and  input  is  units

# Units                                                      Cost
# ------------------------------------------------------------
# First  100  units					Rs. 3.00 / unit

# Next  100  units				Rs. 3.50 / unit

# Next  200  units		    	Rs. 4.00 / unit

# Next  300  units				Rs. 4.50 / unit

# Above  700  units				Rs. 5.00 / unit
# ---------------------------------------------------------------
# Let  units  be  1200
# What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

# Hint:  Use  match  ...  case   but  not  if ... else

# units = int(input('Enter  units :   '))  
# match  units:
# 	case   100:
# 				cost = 3.00
# 	case  100:
# 				cost = 3.50 
# 	case  200:
# 				cost = 4.00
# 	case  300:
# 				cost = 4.50
# 	case  700:				
# 				cost = 5.00
# print(units*cost)
# print('Bill  amount  : units ' , cost)
# # #  Find  outputs
# while  True:
# 	print('Hello') #infinity
# print('Bye')
#  Find  outputs
# while  False: 
# 	print('Hello')
# print('Bye')#bye
