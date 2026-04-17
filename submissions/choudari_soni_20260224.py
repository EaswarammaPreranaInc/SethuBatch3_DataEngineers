
#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)#Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)#Hyd  is  'green'  city
print('Hyd  is  ' green  '  city')#Hyd  is  ' green  '  city

____________________________________________________________
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results


import math
a=int(input('Enter 1st integer number :'))
b=int(input('Enter 2nd integer number :'))
print(F'{a}+{b}={a+b}')
print(F'{a}-{b}={a-b}')
print(F'{a}*{b}={a*b}')
print(F'{a}/{b}={a/b}')
print(F'{a}%{b}={a%b}')
print(F'max({a},{b})={max(a,b)}')
print(F'min({a},{b})={min(a,b)}')
print(F'{a}**{b}={a**b}')
print(F'sqrt({a})={math.sqrt(a)}')
print(F'gcd({a,b})={math.gcd(a,b)}')
print(F'fact({a})={math.factorial(a)}')

_______________________________________________________________
'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''

x=int(input('Enter 1st input:'))
y=str(input('Enter 2nd input:'))
print(F'Before swap: x={x}  y="{y}"')
x,y=y,x
print(F'After swap: x="{x}"   y={y}')

____________________________________________________

Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function


x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
print('Largest Input :',x if x>y else y)

_____________________________________________________

Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function


x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
z=eval(input('Enter 3rd input:'))
print('Largest Input :',x if x>y else y if x>z else z)

_______________________________________________________
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

Enter 1st input:10
Enter 2nd input:20
Result : <

________________________________________________
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0


x=eval(input('Enter any number :'))
print('result :1' if x>0 else "Result : -1 " if x<0 else "0")

____________________________________________________
Write  a  program  to  test  input  is  even  number  or  odd  number


x=eval(input('Enter any +ve number :'))
print('Even number'if x%2==0 else 'odd number')
