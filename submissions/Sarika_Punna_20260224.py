#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)#'Hyd  is  "green"  city
'''c = 'Hyd  is  \'green\'  city'
print(c)#Error
print('Hyd  is  ' green  '  city')#Error'''

#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
import math
x=eval(input("enter 1st integer input:"))
y=eval(input("enter 2nd integer input:"))
print(f'{x}+{y}={x+y}')
print(f'{x}-{y}={x-y}')
print(f'{x}*{y}={x*y}')
print(f'{x}/{y}={x/y}')
print(f'{x}%{y}={x%y}')
print(f'max({x},{y})={max(x,y)}')
print(f'min({x},{y})={min(x,y)}')
print(f'{x}^{y}={x**y}')
print(f'sqrt({x})={math.sqrt(x)}')
print(f'gcd({x},{y})={math.gcd(x,y)}')
print(f'fact({x})={math.factorial(x)}')



#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
print("swapping of Objects")
x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))
print(f"Before swap: x={x} y={y}")
x,y=y,x
print(f"after swap: x={x} y={y}")

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
print("Largest of two numbers")
x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))
print(f"largest input:{x}") if (x>y) else print(f"largest input:{y}")

#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
print("Largest of three numbers")
x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))
z=eval(input("enter 3rd input:"))
print(f"largest input:{x}") if(x>y and x>z) else print(f"largest input:{y}") if(y>x and y>z) else print(f"largest input:{z}")


#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and'='  if  inputs  are  same
x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))
print(">") if(x>y) else print("<") if(x<y) else print("=")


#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
print("positive,negative,zero")
x=eval(input("enter any number:"))
print("1") if(x>0) else print("-1") if(x<0) else print("0")


#Write  a  program  to  test  input  is  even  number  or  odd  number
print("even or odd number")
x=eval(input("enter any positive number:"))
print("Even number") if(x%2==0) else print("Odd number")
