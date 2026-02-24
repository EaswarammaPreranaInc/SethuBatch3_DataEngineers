#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) #Hyd  is  green  city <NEXTLINE>
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city NEXTLINE>
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  'green'  city NEXTLINE>
print('Hyd  is  ' green  '  city') # Hyd  is  ' green  '  city' NEXTLINE>
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17 
What  is  the  difference ?  --->  3
What  is  the  product ?  --->  70
What  is  the  quotient ?  --->  1.42
What  is  the  remainder ?  ---> 3
What  is  the  largest  number ?  --->  10
What  is  the  smallest  number ?  --->  7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power ?  --->  10000000
What  is  the  gcd  of  2  numbers ?  --->  1
What  is  the  factorial   of  1st  input ?  --->  10!
'''
'''

import math
def allOperations(x, y):
	print(F'{x} + {y} = {x+y}')
	print(F'{x} - {y} = {abs(x-y)}')
	print(F'{x} * {y} = {x*y}')
	print(F'{x} / {y} = {x/y}')
	print(F'{x} % {y} = {x%y}')
	print(F'max({x} , {y}) = {max(x,y)}')
	print(F'min({x} , {y}) = {min(x,y)}')
	print(F'{x} ^ {y} = {x**y}')
	print(F'sqrt({x}) = {math.sqrt(x)}')
	print(F'gcd({x} , {y}) = {math.gcd(x,y)}')
	print(F'fact({x}) = {math.factorial(x)}')

a=int(input("Enter 1st integer number :"))
b=int(input("Enter 2nd integer number :"))
allOperations(a,b)



Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
'''

def swap(x,y):
	x,y=y,x
	print(F'After swap: {x=}	{y=}')
a=input("Enter 1st input :")
b=input("Enter 2nd input :")
print(F'Before swap: {a=}	{b=}')
swap(a,b)





Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function



1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
'''

a=int(input("Enter 1st integer number :"))
b=int(input("Enter 2nd integer number :"))
print(F'Largest Input : {a}') if a>b else print(F'Largest Input : {b}')




Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
'''

a=input("Enter 1st input :")
b=input("Enter 2nd input :")
c=input("Enter 3rd input :")
print(F'Largest Input : {a}') if a>b and a>c else print(F'Largest Input : {b}') if b>c else print(F'Largest Input : {c}')


Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
'''
a=input("Enter 1st input :")
b=input("Enter 2nd input :")
print("Result : =") if a == b  else print("Result : >") if a>b else print("Result : <")


Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
'''

a=int(input("Enter any number :"))
print('Result = 1') if a>0 else print('Result = -1') if a<0 else print('Result = 0')

Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''


a=int(input("Enter any +ve integer :"))
print(F"{a} is Even number") if a%2==0 else print(F"{a} is Odd number") 