#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)#Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)#Hyd  is  \'green\'  city
print('Hyd  is  ' green  '  city')#error



#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.

import math
a=eval(input('Enter 1st integer number:'))
b=eval(input('Enter 1st integer number:'))
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=max(a,b)
i=min(a,b)
j=a^b
k=math.sqrt(a)
l=math.gcd(a,b)
z=math.factorial(a)
print(f"{a}+{b}={c}")
print(f"{a}-{b}={d}")
print(f"{a}*{b}={e}")
print(f"{a}/{b}={f}")
print(f"{a}%{b}={g}")
print(f"Max({a},{b})={h}")
print(f"Min({a},{b})={h}")
print(f"{a}^{b}={j}")
print(f"math.sqrt({a})={k}")
print(f"math.gcd({a},{b})={l}")
print(f"math.factorial({a})={z}")



#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
x=eval(input('enter 1st input:'))
y=eval("input('enter 2nd input:')")
print("before swap : x =", x, " y =", y)
x,y=y,x
print("After swap : x =", x, " y =", y)

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max() function
x=eval(input('enter 1st input:'))
y=eval(input('enter 2nd input:'))
z=eval(input('enter 3nd input:'))
largest=x if (x>y and x>z) else (y if y>z else z)
print(largest)


#Write  a  program  to  print   '>'  if  1st  input  >  2nd input '<'  if  1st  input  <  2nd  input  and'='  if  inputs  are  same
x=eval(input('enter 1st input:'))
y=eval(input('enter 2nd input:'))
result = '>' if x > y else ('<' if x < y else '=')
print("Result :", result)

#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

x=eval(input('enter 1st input:'))
y=eval(input('enter 2nd input:'))
result=-1 if(x>y) -1 else(y<x)  
print(result)


#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  

x=eval(input('enter 1st input:'))
y=eval(input('enter 2nd input:'))
result=-1 if(x>y) -1 else(y<x)  
print(result)

#Write  a  program  to  test  input  is  even  number  or  odd  number
x=eval(input('enter  any +ve integer:'))
result=even_numder if(x//2==0)  odd_numder else(x//2!=0)  
print(result)


 
