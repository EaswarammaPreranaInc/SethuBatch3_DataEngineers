#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)  # Hyd  is  'green' city
print('Hyd  is  ' green  '  city')  # error



Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

import math
a=int(input('Enter 1st integer number: '))
b=int(input('Enter 2nd integer number: '))
print(f'{a} + {b} = ',a+b)
print(f'{a} - {b} = ',a-b)
print(f'{a} * {b} = ',a*b)
print(f'{a} / {b} = ',a/b)
print(f'{a} % {b} = ',a%b)
print(f'max({a},{b})',max(a,b))
print(f'min({a},{b})',min(a,b))
print(f'{a} ^ {b} = ',a**b)
print(f'sqrt({a})=',math.sqrt(a))
print(f'gcd({a},{b})=',math.gcd(a,b))
print(f'fact({a})=',math.factorial(a))

output:

Enter 1st integer number: 10
Enter 2nd integer number: 7
10 + 7 =  17
10 - 7 =  3
10 * 7 =  70
10 / 7 =  1.4285714285714286
10 % 7 =  3
max(10,7) 10
min(10,7) 7
10 ^ 7 =  10000000
sqrt(10)= 3.1622776601683795
gcd(10,7)= 1
fact(10)= 3628800



Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

x=eval(input('Enter 1st input : '))
y=eval(input('Enter 2nd input : '))
print(f"Before swap : x='{x}'  y=\"'{y}'\" ")
x,y=y,x
print(f"After swap : x=\"'{x}'\" y='{y}' ")

output:

Enter 1st input : 25
Enter 2nd input : 'Hyd'
Before swap : x='25'  y="'Hyd'" 
After swap : x="'Hyd'" y='25' 


Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
if a>b:
    print('Largest input : ',a)
else:
    print('Largest input : ',b)

output:

Enter 1st input : 10
Enter 2nd input : 20.8
Largest input :  20.8

Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
c=eval(input('Enter 3rd input : '))
if a>b:
    print('Largest input : ',a)
elif(b>c):
    print('Largest input : ',b)
else:
    print('Largest input : ',c)

output:

Enter 1st input : 'Hyd'
Enter 2nd input : 'Sec'
Enter 3rd input : 'Cyb'
Largest input :  Sec

Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
if a>b:
    print('Result :  >')
elif(a<b):
    print('Result :  <')
else:
    print('Result :  =')

output:

Enter 1st input : 10
Enter 2nd input : 20
Result :  <


Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

a=eval(input('Enter any number : '))
if a>0:
    print('Result :  1')
elif(a<0):
    print('Result :  -1')
else:
    print('Result :  0')

output:

Enter any number : -25
Result :  -1

Write  a  program  to  test  input  is  even  number  or  odd  number

a=int(input('Enter any +ve integer : '))
if a%2==0:
    print('Even number')
else:
    print('Odd number')

output:

Enter any +ve integer : 26
Even number







