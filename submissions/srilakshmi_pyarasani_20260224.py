1) outputs  
a = 'Hyd  is  green  city'
print(a)#Hyd is green city
b = 'Hyd  is  "green"  city'
print(b)#Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c)#Hyd is 'green' city
print('Hyd  is  ' green  '  city')#Error


2) Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

# Program 
import math

num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))

print(F'{num1} + {num2} = {num1 + num2}')
print(F'{num1} - {num2} = {num1 - num2}')
print(F'{num1} * {num2} = {num1 * num2}')
print(F'{num1} / {num2} = {num1 / num2}')
print(F'{num1} % {num2} = {num1 % num2}')
print(F'max({num1} , {num2}) = {max(num1, num2)}')
print(F'min({num1} , {num2}) = {min(num1, num2)}')
print(F'{num1} ^ {num2} = {num1 ** num2}')
print(F'sqrt({num1}) = {math.sqrt(num1)}')
print(F'gcd({num1} , {num2}) = {math.gcd(num1, num2)}')
print(F'fact({num1}) = {math.factorial(num1)}')
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


3) Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects

# Program 
x = str(input('Enter 1st input : '))
y = str(input('Enter 2nd input : '))

print(F'Before swap: {x=}, {y=}')
print(F'After swap: {y=}, {x=} ')

4)Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

	1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

	2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

	3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

	4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

	5) Inputs  can  be  integers , floats , strings  and  so  on

	6) Use   ternary  operator

# Program 
x = float(input('Enter 1st input : '))
y = float(input('Enter 2nd input : '))
if x>y:
    print(F'Largest Input: {x}')
else :
    print(F'Largest Input: {y}')



5) Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

	1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

	2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

	3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

	4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

	5) Inputs  can  be  integers , floats , strings  and  so  on

	6) Use  nested  ternary  operator

# Program 
a = str(input('Enter 1st input : '))
b = str(input('Enter 2nd input : '))
c = str(input('Enter 3rd input : '))
largest = a if (a >= b and a >= c) else (b if b >= c else c)
print(f' largest input: {largest}')



6) Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

	1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

	2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

	3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =
	
	4) Inputs  can  be  integers , floats , strings  and  so  on

	5) Use  nested  ternary  operator

# Program 
a = int(input("Enter 1st Input: "))
b = int(input("Enter 2nd Input: "))

Result = '>' if a > b else ('<' if a < b else '=')
print(F'Result : {Result}')


7) Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

	1) What  is  the  result  if  input  is  -25 ?  ---> -1

	2) What  is  the  result  if  input  is  75 ?  ---> 1

	3) What  is  the  result  if  input  is  0 ?  ---> 0

	4) Use  nested  ternary  operator

# Program 
num=int(input('Enter any Number:'))
Result= 1 if num>0 else (-1 if num < 0 else 0)
print(Result)

8) Write  a  program  to  test  input  is  even  number  or  odd  number

	1) What  is  an  even  number  ?  ---> Divisible  by  2

	2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

	3) Use  ternary  operator

# Program 
num = int(input("Enter any +ve integer:"))
if num % 2 == 0:
    print(f'Even Number Number ')
else:
    print(f'Odd Number ')