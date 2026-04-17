#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)#Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)#Hyd  is  'green'  city
print('Hyd  is  ' green  '  city')#SyntaxError: invalid syntax

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
import math
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Sum of {a}+{b} = {a+b}")
print(f" {a}-{b} ={a-b}")
print(f"{a} *{b} = {a*b}")
print(f" {a}/{b} = {a/b}")
print(f" {a} % {b} = {a%b}")
print(f"max({a},{b})={max(a,b)}")
print(f"min({a},{b})={min(a,b)}")
print(f"sqrt({a})={math.sqrt(a)}")
print(f"{a}**{b}={a**b}")
print(f"gcd({a},{b})={math.gcd(a,b)}")
print(f"fact({a})={math.factorial(a)}")

#for string
a=input("Enter 1st Input:")
b=input("enter 2nd input:")
print(f'Before swap :a={a}  b={b}')
a,b=b,a
print(f'After swap :a={a}  b={b}')

#for int and float list
a=eval(input("Enter 1st Input:"))
b=eval(input("enter 2nd input:"))
print(f'Before swap :a={a}  b={b}')
a,b=b,a
print(f'After swap :a={a}  b={b}')

#for int and float list
a=eval(input("Enter 1st number: "))
b=eval(input("Enter 2nd number: "))
print(f'Largest Input:{a if a>b else b}')

#for string
a=input("Enter 1st number: ")
b=input("Enter 2nd number: ")
print(f'Largest Input:{a if a>b else b}')

#for string
a=input("enter 1st string")
b=input("enter 2nd string")
c=input("enter 3rd string")
print(f'largest input :{a if a>b and a>c else b if b>c and b>a else c}')
#int float list tuple 
a=input("enter 1st input:")
b=input("enter 2nd input:")
print(f'Result:{'<' if a<b else '>' if a>b else '=='}')
#string
a=input("enter 1st input:")
b=input("enter 2nd input:")
print(f'Result:{'<' if a<b else '>' if a>b else '=='}')


checker=int(input("enter a number:"))
print(f'Result:{-1 if checker<0 else 1 if checker>0 else 0}')


evenorodd=int(input("enter a number:"))
print(f'Result:{"Even" if evenorodd%2==0 else "Odd"}')

