#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  #Hyd is green city.
b = 'Hyd  is  "green"  city'
print(b)  #Hyd is 'green' city.
c = 'Hyd  is  \'green\'  city'
print(c)  #Hyd is 'green' city.
#print('Hyd  is  ' green  '  city')  #Hyd is green city


'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results
'''

import math
a = eval(input('Enter 1st integer number :'))  #10
b = eval(input('Enter 2nd integer number :'))  #7
print(f'10 + 7 = {a + b}')  #17
print(f'10 - 7 = {a - b}')  #3
print(f'10 * 7 = {a * b}')  #70
print(f'10 / 7 = {a / b}')  #1.4285714285714286
print(f'10 % 7 = {a % b}')  #3
print(f'max(a,b) = {max(a,b)}')  #10
print(f'min(a,b) = {min(a,b)}')  #7
print(f'10 ^ 7 = {10**7}')  #10000000
print(f'sqrt(10) = {math.sqrt(a)}')  #3.1622776601683795
print(f'gcd(10,7) = {math.gcd(a,b)}')  #1
print(f'fact(10) = {math.factorial(a)}')  #3628800



'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''

x = eval(input('Enter 1st input :'))
y = eval(input('Enter 2nd input :'))
x , y = y , x
print('Before swap :  x = 25   y = "Hyd" ')
print(f'After swap :  x = {x}   y = {y}')  #x = "Hyd"  y = 25



'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''

a = eval(input('Enter 1st input :'))  #10
b = eval(input('Enter 2nd input :'))  #20
print(f'Largest Input : {a if a>b else b}')  #20


a = eval(input('Enter 1st input :'))  #35.8
b = eval(input('Enter 2nd input :'))  #27.9
print(f'Largest Input : {a if a>b else b}')  #35.8


a = eval(input('Enter 1st input :'))  #RAMA
b = eval(input('Enter 2nd input :'))  #RAJESH
print(f'Largest Input : {a if a>b else b}')  #RAMA

a = eval(input('Enter 1st input :'))  #[10 , 20 , 15 , 18 , 19 , 28]
b = eval(input('Enter 2nd input :'))  #[10 , 20 , 25, 17] 
print(f'Largest Input : {a if a>b else b}')  #[10 , 20 , 25, 17]  becoz 25 > 15



'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''


a = eval(input('Enter 1st input :'))  #10
b = eval(input('Enter 2nd input :'))  #20
c = eval(input('Enter 3rd input :'))  #15
print(f'Largest input :{a if (a>b) else b if (b>c) else c}')  #20


a = eval(input('Enter 1st input :'))  #35.8
b = eval(input('Enter 2nd input :'))  #42.8
c = eval(input('Enter 3rd input :'))  #27.9
print(f'Largest input : {a if (a>b) else b if (b>c) else c}')  #42.8


a = eval(input('Enter 1st input :'))  #RAMA
b = eval(input('Enter 2nd input :'))  #RAKESH
c = eval(input('Enter 3rd input :'))  #RAJESH
print(f'Largest input : {a if (a>b) else b if (b>c) else c}')  #RAMA


a = eval(input('Enter 1st input :'))  #[10 , 20 , 15 , 18]
b = eval(input('Enter 2nd input :'))  #[10 , 20 , 32, 19] 
c = eval(input('Enter 3rd input :'))  #[10 , 20 , 25, 17]
print(f'Largest input :{a if (a>b) else b if (b>c) else c}')  #[10 , 20 , 32, 19] 



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

a = eval(input('Enter 1st input :'))  #10
b = eval(input('Enter 2nd input :'))  #20
print(f'Result : {'>' if a>b else '<' if a<b else '='}')  # <


a = eval(input('Enter 1st input :'))  #70
b = eval(input('Enter 2nd input :'))  #60
print(f'Result : {'>' if a>b else '<' if a<b else '='}')  # >


a = eval(input('Enter 1st input :'))  #25
b = eval(input('Enter 2nd input :'))  #25
print(f'Result : {'>' if a>b else '<' if a<b else '='}')  # =



'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''

a = eval(input('Enter any number :'))  #-25
print(f'Result : {1 if a>0 else -1 if a<0 else 0}')  #-1 becoz it is negative number

a = eval(input('Enter any number :'))  #75
print(f'Result : {1 if a>0 else -1 if a<0 else 0}')  #1 becoz input is postive number

a = eval(input('Enter any number :'))  #0
print(f'Result : {1 if a>0 else -1 if a<0 else 0}')  #0



'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''

a = eval(input('Enter any positive integer :'))  #10
print(f'{'Even Number' if a%2==0 else 'Odd Number'}')  #Even Number becoz 10 is divisible by 2

