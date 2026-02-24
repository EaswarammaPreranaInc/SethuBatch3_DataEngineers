# Topic 1
'''
#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  'green'  city
#print('Hyd  is  ' green  '  city') # error green is object
'''
#Topic 2
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
x = int(input("Enter 1st integer number : "))
y = int(input("Enter 2nd integer number : "))

print(F"{x} + {y} = {x+y}")
print(F"{x} - {y} = {x-y}")
print(F"{x} * {y} = {x*y}")
print(F"{x} / {y} = {x/y}")
print(F"{x} % {y} = {x%y}")
print(F"max({x}, {y}) = {max(x,y)}")
print(F"min({x}, {y}) = {min(x,y)}")
print(F"{x} ^ {y} = {pow(x,y)}")
print(F"sqrt({x}) = {math.sqrt(x)}")
print(F"gcd({x}, {y}) = {math.gcd(x,y)}")
print(F"fact({x}) = {math.factorial(x)}")
'''

#Topic 3
'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
'''
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")
print(F'Before swap : x={x}\t y={y}')
x, y = y, x
print(F'After swap : x={x}\t y={y}')
'''

#Topic 4
'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''

'''
H = eval(input("Enter 1st input : "))
I = eval(input("Enter 2nd input : "))
print(f'Largest Input:\t {H if H>I else I}')
'''
#Topic 5
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
"""
M = eval(input("Enter 1st input : "))
N = eval(input("Enter 2nd input : "))
O = eval(input("Enter 3rd input : "))
print(f'Largest Input:\t {M if M > N else N if M > O else O if N > O else O}')
"""
#Topic 6
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
"""
M = eval(input("Enter 1st input : "))
N = eval(input("Enter 2nd input : "))
print(f'Result :\t {">" if M > N else '<' and "=" if M == N else '<'}')
"""
#Topic 7
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
"""
P = int(input("Enter any number: "))
print(f'result: {1 if P>0 else 0 or -1 if P<0 else 0}')
"""

#Topic 8

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
"""
Eo = int(input("Enter any +ve integer : "))
print("Even number" if Eo%2 == 0 else "Odd number")
"""