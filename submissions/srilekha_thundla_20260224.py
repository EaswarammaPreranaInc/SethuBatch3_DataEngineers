
#  Find outputs  (Home  work)
# a = 'Hyd  is  green  city'
# print(a)#Hyd  is  green  city
# b = 'Hyd  is  "green"  city'
# print(b)# Hyd  is  "green"  city
# c = 'Hyd  is  \'green\'  city'
# print(c)#Hyd  is  'green'  city
# print('Hyd  is  ' green  '  city') error

# Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
# Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

# Hint:  Use  F  string  to  print  results

# Let  inputs  be  10  and  7
# input_1=int(input('Enter First integer Number: '))
# input_2=int(input('Enter second integer Number: '))
# What  is  the  sum ?  --->  17
# print(f'{input_1}+{input_2} = ',input_1+input_2)


# What  is  the  difference ?  --->  3
# print(f'{input_1}-{input_2} = ',input_1-input_2)

# What  is  the  product ?  --->  70
# print(f'{input_1}*{input_2} = ',input_1*input_2)

# What  is  the  quotient ?  --->  1.42
# print(f'{input_1}/{input_2} = ',input_1/input_2)

# What  is  the  remainder ?  ---> 3
# print(f'{input_1}%{input_2} = ',input_1%input_2)

# What  is  the  largest  number ?  --->  10
# print(f'max({input_1},{input_2}) = ',max(input_1,input_2))


# What  is  the  smallest  number ?  --->  7
# print(f'min({input_1},{input_2}) = ',min(input_1,input_2))


# What  is  the  sqrt  of  1st  input ?  --->  3.16
# import math
# print(f'sqrt{input_1}) = ',math.sqrt(input_1))


# What  is  the  result  of  power ?  --->  10000000
# print(f'10^7({input_1},{input_2}) = ',math.pow(input_1,input_2))


# What  is  the  gcd  of  2  numbers ?  --->  1
# print(f'gcd({input_1},{input_2}) = ',math.gcd(input_1,input_2))

# What  is  the  factorial   of  1st  input ?  --->  10!
# print(f'fact({input_1}) = ',math.factorial(input_1))

# Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

# Let  'x'  be  25  and  'y'  be   'Hyd'
# x = eval(input('give your first input: '))
# y = eval(input('give your second input: '))

# What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25
# print(f'before swap: x={x} y = {y}')
# x,y=y,x
# print(f'afer swap: x={x} y = {y}')

# Hint:  Swap  references  but  not  objects

# Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

# 1) What  is  the  output  if  inputs  are  10  and  20 ?   --->
# 2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8
# 3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'
# 4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15
# 5) Inputs  can  be  integers , floats , strings  and  so  on


# input_1=eval(input('Enter first input: '))
# input_2=eval(input('Enter second input: '))
# if input_1>input_2:
#     print(f'Largest Input : {input_1}')
# else:
#     print(f'Largest Input : {input_2}')

# 6) Use   ternary  operator
# print('Largest Input: ', input_1 if  input_1>input_2 else input_2)

# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
# # 1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20
# 2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8
# 3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'
# 4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]
# 5) Inputs  can  be  integers , floats , strings  and  so  on
# input_1=eval(input('Enter 1st input: '))
# input_2=eval(input('Enter 2nd input: '))
# input_3=eval(input('Enter 3rd input: '))
# if input_1>input_2 and input_3:
#     print('Largest Input: ', input_1)
# else:
#     if input_2>  input_3 and input_1:
#         print('Largest Input: ', input_2)
#     else:
#         print('Largest Input: ', input_3)


# 6) Use  nested  ternary  operator
# print('Largest Input: ', input_1 if input_1>input_2 else input_2 if input_2>input_3 else input_3)


# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
#                                                '<'  if  1st  input  <  2nd  input  and
#                                                '='  if  inputs  are  same

# 1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

# 2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

# 3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

# 4) Inputs  can  be  integers , floats , strings  and  so  on
# input_1=eval(input('Enter first input: '))
# input_2=eval(input('Enter second input: '))
# if input_1>input_2:
#     print(f'Result : >')
# else:
#     if input_2==input_1:
#         print(f'Result : =')
#     else:
#         print(f'Result : <')


# 5) Use  nested  ternary  operator
# print(">" if input_1>input_2 else "<" if input_2>input_1 else "=")

# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
# 1) What  is  the  result  if  input  is  -25 ?  ---> -1
# 2) What  is  the  result  if  input  is  75 ?  ---> 1
# 3) What  is  the  result  if  input  is  0 ?  ---> 0
# input_=eval(input('Enter any number: '))

# if input_>0:
#     print('Result : ',1)
# else:
#     if input_==0:
#         print('Result : ',0)
#     else:
#         print('Result : ',-1)


# 4) Use  nested  ternary  operator
# print(1 if input_>0 else -1 if input_<0 else 0)

# Write  a  program  to  test  input  is  even  number  or  odd  number
# 1) What  is  an  even  number  ?  ---> Divisible  by  2
# 2) What  is  an  odd  number  ?  ---> Not  divisible  by  2
# x = eval(input('Enter positive integer: '))
# if x%2==0:
#     print("Even number")
# else:
#     print("odd number")

# 3) Use  ternary  operator
# print("Even number" if x%2==0 else "Odd number")
