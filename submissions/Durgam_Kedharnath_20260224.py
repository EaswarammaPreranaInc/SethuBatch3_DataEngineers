#Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)                         # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)                         # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c,'\n')                         # Hyd  is  'green'  city 
#print('Hyd  is  ' green  '  city') # Error


1. Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
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

"""
import math
a = int(input('Enter 1st integer number : '))
b = int(input('Enter 2nd integer number : '))
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'max({a} , {b}) = {max(a,b)}')
print(f'min({a} , {b}) = {min(a,b)}')
print(f'{a} ^ {b} = {a**7}')
print(f'sqrt({a}) = {math.sqrt(a)}')
print(f'gcd({a} , {b}) = {math.gcd(a,b)}')
print(f'fact({a}) = {math.factorial(a)}')
print()

"""







'''
2. Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
"""
a = input('Enter 1st input : ')
b = input('Enter 2nd input : ')
print(f'Before Swap : {a=} \t {b=}')
a,b = b,a
print(f'After Swap : {a=} \t {b=}')
print()

"""
3.  Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ? #  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ? # 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  #  'RAMA' 

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?  #  [10 , 20 , 25 , 17] 

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
"""


a = eval(input('Enter 1st input : '))
b = eval(input('Enter 2nd input : '))
print(f'Largest Input :  {a if a>b else b}')


"""
4.    Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ? #  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?  # 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?  #  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  #  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
"""

a = eval(input('Enter 1st input : '))
b = eval(input('Enter 2nd input : '))
c = eval(input('Enter 3rd input : '))
print(f'Largest Input : {a if a>b and a>c else b if b>c and b>a else c}')
print()



"""

5.  Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
"""
a = eval(input('Enter 1st input : '))
b = eval(input('Enter 2nd input : '))
print(f'Result : {'>' if a>b else '<'}')
print()



"""
6.   Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  # -1

2) What  is  the  result  if  input  is  75 ?  # 1

3) What  is  the  result  if  input  is  0 ?  # 0

4) Use  nested  ternary  operator
"""
num = int(input('Enter any number : '))
print(f'Result : {1 if num>=1 else -1 if num<0 else 0}')
print()




"""
7.  Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  # Divisible  by  2

2) What  is  an  odd  number  ?  # Not  divisible  by  2

3) Use  ternary  operator


"""
num = int(input('Enter any +ve integer : '))
print(f'{'Even number' if num%2==0 else 'Odd number'}')

"""
