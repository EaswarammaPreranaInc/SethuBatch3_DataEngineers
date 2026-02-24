#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  green  city
print('Hyd  is  ' green  '  city') # Error

# Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

# Hint:  Use  F  string  to  print  results

import math
n1 = int(input('Enter 1st integer number : '))
n2 = int(input("Enter 2nd integer number : "))
print(F'{n1} + {n2} = {n1+n2}')
print(F'{n1} - {n2} = {n1-n2}')
print(F'{n1} * {n2} = {n1*n2}')
print(F'{n1} / {n2} = {n1/n2}')
print(F'{n1} % {n2} = {n1%n2}')
print(F'max({n1} ,{n2} = {max(n1,n2)}')
print(F'min({n1} ,{n2} = {min(n1,n2)}')
print(F'{n1} ^ {n2} = {n1**n2}')
print(F'sqrt({n1}) = {math.sqrt(n1)}')
print(F'gcd({n1} , {n2}) = {math.gcd(n1,n2)}')
print(F'fact({n1}) = {math.factorial(n1)}')

# Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(F"Before swap : {x=x}\t\t {y=y}")
x,y=y,x
print(F"After swap : {x=}\t\t {y=}")

# Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(F'Largest Input : {x if x>y else y})

# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
z=eval(input("Enter 3rd input : "))
print(F'Largest Input : {x if x>y and x>z else y if y>x and y>z else z}')

# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(F'Result : { '>' if x>y else '=' if x==y else '<'}')

# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
x=eval(input("Enter any number : "))
print(F'Result : { 1 if x>0 else -1 if x<0 else 0}')

# Write  a  program  to  test  input  is  even  number  or  odd  number
x=eval(input("Enter any number : "))
print(F'Result : { 'Even number' if x%2==0 else 'Odd number'}')






