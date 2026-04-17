#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  'green'  city
print('Hyd  is  ' green  '  city') #Error

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

import math
X = eval(input("Enter a 1st number: "))
Y = eval(input("Enter a 2nd number: "))
Sum = X + Y
print(F'Sum = {Sum}')
Difference = X - Y
print(F'Difference = {Difference}')
Product = X * Y
print(F'Product = {Product}')
quotient = X / Y
print(F'quotient = {quotient}')
remainder = X % Y
print(F'remainder = {remainder}')
max_value = max(X,Y)
print(f'max_value = {max_value}')
min_value = min(X,Y)
print(f'min_value = {min_value}')
sqr = math.sqrt(X)
print(F'sqrt {X} = {sqr}')
power = math.pow(X,Y)
print(F'{X}^{Y} = {power}')
gcd = math.gcd(X,Y)
print(F'gcd{X , Y} = {gcd}')
fact = math.factorial(X)
print(F'factorial ({X}) = {fact}')

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects

'''
X,Y = 25,'Hyd'
print(f'Before swap values: {X} {Y} ')
X,Y = Y,X
print(f'After swap values: {X} {Y}')

'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''

a = eval(input("Enter the a value:"))
b = eval(input("Enter the b value:"))
print(F'{a} is the largest among both inputs ') if a>b else print(F'{b} is the largest among both inputs')
    
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
a = eval(input("Enter the value a:"))
b = eval(input("Enter the value b:"))
c = eval(input("Enter the value c:"))
print(F'a={a} is the largest among three inputs ') if a>b and a>c else print(F'b={b} is the largest among three inputs ') if b>a and b>c else print(F'c={c} is the largest among three inputs ')

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))
result = '>' if a > b else '<' if a < b else '='
print(result)

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''

a = eval(input("Enter the value:"))
print("+1") if a>0 else print("-1") if a<0 else print("0") 

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''

a = eval(input("Enter the value:"))
print(F'{a} is even')if a%2==0 else print(F'{a} is odd')



