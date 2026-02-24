#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b)   # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c)  #  Hyd is 'green' city
print('Hyd  is  ' green  '  city')  # error
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17 
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = a+b
print(f'Sum of a and b is {c}')

What  is  the  difference ?  --->  3
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = a-b
print(f' Difference of a and b is {c}')

What  is  the  product ?  --->  70
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = a*b
print(f'Product of a and b is {c}')

What  is  the  quotient ?  --->  1.42
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = a/b
print(f'Quotient of a and b is {c}')

What  is  the  remainder ?  ---> 3
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = a%b
print(f'Remainder of a and b is {c}')

What  is  the  largest  number ?  --->  10
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = max(a,b)
print(f'largest of a and b is {c}')

What  is  the  smallest  number ?  --->  7
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
c = min(a,b)
print(f'Smallest of a and b is {c}')

What  is  the  sqrt  of  1st  input ?  --->  3.16
import math
a=eval(input("enter a no.:"))
print(math.sqrt(a))

What  is  the  result  of  power ?  --->  10000000
import math
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
print(math.pow(a,b))

What  is  the  gcd  of  2  numbers ?  --->  1
import math
a=eval(input("enter a no.:"))
b=eval(input("enter a no.:"))
print(math.gcd(a,b))

What  is  the  factorial   of  1st  input ?  --->  10!
import math
a=eval(input("enter a no.:"))
print(math.factorial(a))
'''

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25
x=25
y='Hyd'
x,y = y,x
print(f'after swapping x and y are: {x},{y}')
Hint:  Swap  references  but  not  objects
'''

'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20
a=eval(input("Enter a no.:"))
b=eval(input("Enter a no.:"))
if a>b:
    print(a)
else:
    print(b)

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8
a=eval(input("Enter a no.:"))
b=eval(input("Enter a no.:"))
if a>b:
    print(a)
else:
    print(b)

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'
a=input("Enter str:")
b=input("Enter str:")
if a>b:
    print(a)
else:
    print(b)

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15
a=eval(input("Enter list:"))
b=eval(input("Enter list:"))
if a>b:
    print(a)
else:
    print(b)

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20
a=eval(input("Enter no.:"))
b=eval(input("Enter no.:"))
c=eval(input("Enter no.:"))
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8
a=eval(input("Enter no.:"))
b=eval(input("Enter no.:"))
c=eval(input("Enter no.:"))
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'
a=input("Enter str:")
b=input("Enter str:")
c=input("Enter str:")
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]
a=eval(input("Enter list:"))
b=eval(input("Enter list:"))
c=eval(input("Enter list:"))
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <
a=eval(input("Enter no.:"))
b=eval(input("Enter no.:"))

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('=')

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >
a=eval(input("Enter no.:"))
b=eval(input("Enter no.:"))

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('=')

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =
a=eval(input("Enter no.:"))
b=eval(input("Enter no.:"))

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('=')

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1
a=eval(input("Enter no.:"))
if a>0:
    print('1')
elif a<0:
    print('-1')
else:
    print('0')

2) What  is  the  result  if  input  is  75 ?  ---> 1
a=eval(input("Enter no.:"))
if a>0:
    print('1')
elif a<0:
    print('-1')
else:
    print('0')

3) What  is  the  result  if  input  is  0 ?  ---> 0
a=eval(input("Enter no.:"))
if a>0:
    print('1')
elif a<0:
    print('-1')
else:
    print('0')

4) Use  nested  ternary  operator
'''
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2
a=eval(input("Enter no.:"))
if a%2==0:
    print(f'{a} is even number')
else:
    print(f'{a} is odd number')


2) What  is  an  odd  number  ?  ---> Not  divisible  by  2
a=eval(input("Enter no.:"))
if a%2==0:
    print(f'{a} is even number')
else:
    print(f'{a} is odd number')


3) Use  ternary  operator
'''