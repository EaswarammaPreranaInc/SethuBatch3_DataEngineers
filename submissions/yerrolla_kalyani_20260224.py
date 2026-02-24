#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)#Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)#Hyd  is 'green'  city
print('Hyd  is  ' green  '  city')#error invalid syntax

#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
#Hint:  Use  F  string  to  print  results
import math
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'max({a},{b})={max(a,b)}' )
print(f'min({a},{b})={min(a,b)}' )
print(f'{a}^{b}={pow(10,7)}')
print(f'sqrt({a})={math.sqrt(a)}')
print(f'gcd{a,b}={math.gcd(10,7)}')
print(f'fact ({a})={math.factorial(a)}')


#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
#Let  'x'  be  25  and  'y'  be   'Hyd'
#What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25
#Hint:  Swap  references  but  not  objects
x=int(input("Enter 1st input : "))
y=input("Enter 2nd input : ")
print(f'before swap:  x=\'{x}\'      y=\"{y}\"')
x,y=y,x
print(f'After swap: ",x=\"{x}\"     y=\'{y}\'')


#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
#Use   ternary  operator
x=eval(input("enter 1st input : "))
y=eval(input("enter 2nd input : "))
print("largest Input:",x if x>y else y)

#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
#Use  nested  ternary  operator
x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2st input : "))
z=eval(input("Enter 3rd input : "))
print("largest Input :",x if x>y else y if y>z else z )

#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
#'<'  if  1st  input  <  2nd  input  and            
#'='  if  inputs  are  same
Use  nested  ternary  operator
x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print("result : ",end="\t")
print(">" if x>y  else "<" if x<y else "=")


#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
# Use  nested  ternary  operator
x=eval(input("Enter any number : "))
print("result : ","1" if  x>0 else "-1" if x<0 else "0")


#Write  a  program  to  test  input  is  even  number  or  odd  number
#Use  ternary  operator
x=eval(input("Enter any +ve integer : "))
print("Even number"if x%2==0 else "odd number " )


