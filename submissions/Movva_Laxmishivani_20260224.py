#Outputs Homework #1
a = 'Hyd  is  green  city'
print(a) # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd is 'green' city
print('Hyd  is  ' green  '  city') # ERROR because green is not enclosed in a string, neither it is a defined object


#Programming Homework #1

'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
Hint:  Use  F  string  to  print  results
'''
'''
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
#Answer
    import math
    x=int(input('Enter 1st integer number:'))
    y=int(input('Enter 2nd integer number:'))
    sum =x+y
    difference=x-y
    product=x*y 
    quotient=x/y 
    remainder=x%y
    largest_number=max(x,y)
    smallest_number=min(x,y)
    sqrt=math.sqrt(x)
    power=math.pow(x,y)
    gcd=math.gcd(x,y)
    factorial=math.factorial(x)
    print(F'{x}+{y}={sum}')
    print(F'{x}-{y}={difference}')
    print(F'{x}*{y}={product}')
    print(F'{x}/{y}={quotient}')
    print(F'{x}%{y}={remainder}')
    print(F'max({x},{y})={largest_number}')
    print(F'min({x},{y})={smallest_number}')
    print(F'sqrt({x})={sqrt}')
    print(F'{x}^{y}={power}')
    print(F'gcd({x},{y})={gcd}')
    print(F'factorial({x})={factorial}')

'''Sample Output:

Enter 1st integer number: 10

Enter 2nd integer number: 7

10 + 7 = 17
10 — 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd (10, 7) = 1
fact (10) = 3628800
Press any key to continue...
'''


#Programming Homework #2

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
# Answer
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    print(F'Before swap: a={a},b={b}')
    a, b = b, a 
    print(F'After swap: a={a},b={b}')
'''Sample Output:
Enter 1st input : 25 
Enter 2nd input: 'Hyd' 
Before swap : x='25' y="'Hyd'"
After swap : x="'Hyd'" y='25'
Press any key to continue...
'''

#Programming Homework #3

'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
#Answer
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    print(a if a > b else b)
'''

'''

#Programming Homework #4

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
# Answer
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    c=eval(input('Enter 3rd input:'))
    print(a if a > b else b if b > c else c)

#Programming Homework #5

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
# Answer
    x=eval(input('Enter 1st input:'))
    y=eval(input('Enter 2nd input:'))
    print('Result:','>' if x > y else '<' if x < y else '=')
#Programming Homework #6

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
# Answer
    x=eval(input('Enter any number:'))
    print('Result:','1'if x > 0 else '-1' if x < 0 else '0')

#Programming Homework #7

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
# Answer
    x=int(input('Enter any number:'))
    print('Even number' if x % 2 == 0 else 'Odd Number')