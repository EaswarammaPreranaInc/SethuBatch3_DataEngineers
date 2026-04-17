#Find Outputs

a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  'green'  city
#print('Hyd  is  ' green  '  city') # Error because string literals are separated incorrectly and quotes are mismatched

#--------------------------------------------------------

#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.

#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

x = int(input('Enter 1st integer number : '))  # Enter 1st integer number : 10
y = int(input('Enter 2nd integer number : '))  # Enter 2nd integer number : 7

import math

print(f"{x} + {y} = {x + y}")  # 10 + 7 = 17
print(f"{x} - {y} = {x - y}")  # 10 - 7 = 3
print(f"{x} * {y} = {x * y}")  # 10 * 7 = 70
print(f"{x} / {y} = {x / y}")  # 10 / 7 = 1.4285714285714286
print(f"{x} % {y} = {x % y}")  # 10 % 7 = 3
print(f"max({x} , {y}) = {max(x, y)}")  # max(10 , 7) = 10
print(f"min({x} , {y}) = {min(x, y)}")  # min(10 , 7) = 7
print(f"{x} ^ {y} = {x ** y}")  # 10 ^ 7 = 10000000
print(f"sqrt({x}) = {math.sqrt(x)}")  # sqrt(10) = 3.1622776601683795
print(f"gcd({x} , {y}) = {math.gcd(x, y)}")  # gcd(10 , 7) = 1
print(f"fact({x}) = {math.factorial(x)}")  # fact(10) = 3628800

#--------------------------------------------------------

#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

#Let  'x'  be  25  and  'y'  be   'Hyd'

#What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

#Hint:  Swap  references  but  not  objects

x = input('Enter 1st input : ')  # Enter 1st input : 25
y = input('Enter 2nd input : ')  # Enter 2nd input : Hyd
print(f"Before swap : {x = } \t {y = }")  # Before swap : x = '25' 	 y = 'Hyd'
x, y = y, x 
print(f"After swap : {x = } \t {y = }")  # After swap : x = 'Hyd' 	 y = '25'

#--------------------------------------------------------

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

#1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

#2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

#3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

#4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

#5) Inputs  can  be  integers , floats , strings  and  so  on

#6) Use   ternary  operator

x = eval(input('Enter 1st input : '))  # Enter 1st input : 10
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : 20
Largest = x if x > y else y 
print(f'Largest Input : {Largest}')  # Largest Input : 20

x = eval(input('Enter 1st input : '))  # Enter 1st input : 35.8
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : 27.9
Largest = x if x > y else y
print(f'Largest Input : {Largest}')  # Largest Input : 35.8

x = eval(input('Enter 1st input : '))  # Enter 1st input : 'RAMA'
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : 'RAJESH'
Largest = x if x > y else y  
print(f'Largest Input : {Largest}')  # Largest Input : RAMA

x = eval(input('Enter 1st input : '))  # Enter 1st input : [10 , 20 , 15 , 18 , 19 , 28]
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : [10 , 20 , 25, 17]
Largest = x if x > y else y 
print(f'Largest Input : {Largest}')  # Largest Input : [10, 20, 25, 17]

#--------------------------------------------------------

#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,                              '<'  if  1st  input  <  2nd  input  and                            '='  if  inputs  are  same

#1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

#2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

#3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

#4) Inputs  can  be  integers , floats , strings  and  so  on

#5) Use  nested  ternary  operator

x = eval(input('Enter 1st input : '))  # Enter 1st input : 10
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : 20
z = '>' if x > y else '<' if x < y else '=' 
print('Result : ', z)  # Result : <

x = eval(input('Enter 1st input : '))  # Enter 1st input : 70
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : 60
z = '>' if x > y else '<' if x < y else '=' 
print('Result : ', z)  # Result : >

x = eval(input('Enter 1st input : '))  # Enter 1st input : 25
y = eval(input('Enter 2nd input : '))  # Enter 2nd input : 25
z = '>' if x > y else '<' if x < y else '=' 
print('Result : ', z)  # Result : =

#--------------------------------------------------------

#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

#1) What  is  the  result  if  input  is  -25 ?  ---> -1

#2) What  is  the  result  if  input  is  75 ?  ---> 1

#3) What  is  the  result  if  input  is  0 ?  ---> 0

#4) Use  nested  ternary  operator

x = eval(input('Enter any number : '))  # Enter any number : -25
y = 1 if x > 0 else -1 if x < 0 else 0 
print('Result : ', y)  # Result :  -1

x = eval(input('Enter any number : '))  # Enter any number : 75
y = 1 if x > 0 else -1 if x < 0 else 0 
print('Result : ', y)  # Result :  1

x = eval(input('Enter any number : '))  # Enter any number : 0
y = 1 if x > 0 else -1 if x < 0 else 0 
print('Result : ', y)  # Result :  0

#--------------------------------------------------------

#Write  a  program  to  test  input  is  even  number  or  odd  number

#1) What  is  an  even  number  ?  ---> Divisible  by  2

#2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

#3) Use  ternary  operator

x = int(input('Enter any positive integer : '))  # Enter any positive integer : 50
y = 'Even number' if x % 2 == 0 else 'Odd number' 
print(y)  # Even number

x = int(input('Enter any positive integer : '))  # Enter any positive integer : 95
y = 'Even number' if x % 2 == 0 else 'Odd number' 
print(y)  # Odd number

