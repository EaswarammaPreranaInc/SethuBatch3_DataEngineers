#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd is 'green' ciry
print('Hyd  is  ' green  '  city') # Error

'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

'''

import math
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))

print(f" sum is: {a + b}")
print(f"Product is: {a * b}")
print(f"difference is: {a -b}")
print(f"quotient is: {a/b}")
print(f"remainder is: {a % b}")
print(f"Maximum num is: {max(a,b)}")
print(f"Min num is: {min(a,b)}")
print(f"Sqrt num is:  {math.sqrt(a)}")
print(f"Power is: {pow(a,b)}")
print(f"gcb is: {math.gcd(a,b)}")
print(f"factorial is: {math.factorial(a)}")

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x= int(input("Enter 1st input :"))
y= input("Enter 2nd input :")
print(f"Before swap:  {x=}     {y=}")
x,y =y,x
print(f"after swap: {x=} {y=}")



# Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

x = eval(input("Enter 1st input :"))
y = eval(input("Enter 2nd input :"))
largest= x if x > y else y
print(f"largest input : {largest}")


# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

# Largest of 3 values
x = eval(input("Enter 1st input :"))
y = eval(input("Enter 2nd number :"))
z=  eval(input("Enter 3rd number :"))
largest = x if x>y else y if y>z else z
print(f"Largesr input : {largest}")


# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

X= eval(input("Enter 1st input :"))
Y= eval(input("Enter 2nd input :"))

Result= ">" if X>Y else "<" if X<Y else "=" 
print(f" Result  : {Result} ")


# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

X= eval(input("Enter 1st input :"))

Result= "1" if X>0  else "-1" if X<0 else 0 
print(f" Result  : {Result} ")


# Write  a  program  to  test  input  is  even  number  or  odd  number 

X= eval(input("Enter 1st input :"))
Result = "Even number" if X%2==0 else "Odd number"
print(f"{Result}")

