1) #  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)  # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)  # Hyd  is  'green'  city
print('Hyd  is  ' green  '  city')  # Error

'''
2) Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results
'''
import math
a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))
sum_ = a + b
diff = a - b
prod = a * b
quot = a / b
rem = a % b
largest = max(a, b)
smallest = min(a, b)
power = a ** b
sqrt_a = math.sqrt(a)
gcd_val = math.gcd(a, b)
fact_a = math.factorial(a)
print(f"{a} + {b} = {sum_}")
print(f"{a} - {b} = {diff}")
print(f"{a} * {b} = {prod}")
print(f"{a} / {b} = {quot:.14f}")
print(f"{a} % {b} = {rem}")
print(f"max({a} , {b}) = {largest}")
print(f"min({a} , {b}) = {smallest}")
print(f"{a} ^ {b} = {power}")
print(f"sqrt({a}) = {sqrt_a:.15f}")
print(f"gcd({a} , {b}) = {gcd_val}")
print(f"fact({a}) = {fact_a}")
'''
3) Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = 25
y = 'Hyd'
print(f"Before swap :  x='{x}'          y=\"{y}\"")
x, y = y, x
print(f"After  swap :  x=\"{x}\"        y='{y}'")

'''
4) Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
largest = a if a > b else b
print(f"Largest Input  :  {largest}")

'''
5) Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
c = eval(input("Enter 3rd input : "))
largest = a if a > b and a > c else (b if b > c else c)
print(f"Largest Input  :  {largest}")

'''
6)Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
result = '>' if a > b else ('<' if a < b else '=')
print(f"Result  :  {result}")

'''
7) Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
n = float(input("Enter any number : "))
result = 1 if n > 0 else (-1 if n < 0 else 0)
print(f"Result  :  {result}")

'''
8)Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator

'''
n = int(input("Enter any integer number : "))
result = "Even" if n % 2 == 0 else "Odd"
print(f"Result  :  {result}")