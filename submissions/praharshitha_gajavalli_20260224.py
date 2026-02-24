#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) #Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) #Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)# Hyd is 'green' city
print('Hyd  is  ' green  '  city')#error

#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

import math
x = int(input("Enter 1st integer number: "))
y = int(input("Enter 2nd integer number: "))
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")
print(f"{x} % {y} = {x%y}")
print(f"max({x},{y}) = {max(x,y)}")
print(f"min({x},{y}) = {min(x,y)}")
print(f"{x} ^ {y} = {x**y}")
print(f"sqrt({x}) = {math.sqrt(x)}")
print(f"gcd({x},{y}) = {math.gcd(x,y)}")
print(f"fact({x}) = {math.factorial(x)}")

#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f"Before swap: {x=}   {y=}")
x,y = y,x
print(f"After swap: {x=}    {y=}")

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

a = float(input("Enter 1st input: "))
b = float(input("Enter 2nd input: "))
res = a if a>b else b
print(f"Largest Input: {res}")

#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

a = eval(input("Enter 1st input: "))
b = eval(input("Enter 2nd input: "))
c = eval(input("Enter 2nd input: "))
res = (a if a > b and a > c) else (b if b > c else c)
print(f"Largest Input: {res}")

#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
res = '>' if x>y else '<' if x<y else '='
print(f"Result: {res}")

#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

x = int(input("Enter any number: "))
res = '1' if x>0 else '-1' if x<0 else '0'
print(f"Result: {res}")

#Write  a  program  to  test  input  is  even  number  or  odd  number

x = int(input("Enter any +ve integer: "))
res = 'Even number' if x%2==0 else 'Odd number'
print(f"Result: {res}")