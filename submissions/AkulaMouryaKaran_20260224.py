import math

a=int(input("Enter 1st integer number:"))
b=int(input("Enter 2nd integer number:"))

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'max({a},{b})={max(a,b)}')
print(f'min({a},{b})={min(a,b)}')
print(f'{a}^{b}={a**b}')
print(f'sqrt({a})={math.sqrt(a)}')
print(f'gcd({a},{b})={math.gcd(a,b)}')
print(f'fact({a})={math.factorial(a)}')

a=eval(input('Enter first input:'))
b=eval(input('Enter second input:'))
largest=a if a > b else b
print("Largest=",largest)

a=eval(input('Enter first input:'))
b=eval(input('Enter second input:'))
c=eval(input('Enter third input:'))
largest=a if a>b and a>c else (b if b>c else c)
print('Largest=',largest)

a=eval(input('Enter first input:'))
b=eval(input('Enter second input:'))
result='>' if a>b else ('<' if a<b else '=')
print("Result:",result)

n=int(input('Enter a number:'))
result=1 if n>0 else (-1 if n<0 else 0)
print("Result:",result)

n=int(input('Enter a Number:'))
result='Even Number'if n%2==0 else 'Odd Number '
print(result)