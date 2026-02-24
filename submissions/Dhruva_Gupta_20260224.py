Name-Dhruva Gupta			Subject-Python		Date-24/2/26

1)
#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) #Hyd  is  green  city'
b = 'Hyd  is  "green"  city'
print(b) #Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) #Hyd  is  ‘green’  city
print('Hyd  is  ' green  '  city’) #Syntax error

2)
import math
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
diff=a-b
prod=a*b
quot=a/b
rem=a%b
largest=10 if 10>7 else 7
smallest=10 if 10<7 else 7
sqrt=math.sqrt(a)
power=a**b
gcd=math.gcd(a,b)
fact=math.factorial(a)
print(f"{a}+{b}={sum}")
print(f"{a}-{b}={diff}")
print(f"{a}*{b}={prod}")
print(f"{a}/{b}={quot}")
print(f"{a}%{b}={rem}")
print(f"max({a},{b})={largest}")
print(f"min({a},{b})={smallest}")
print(f"sqrt({a})={sqrt}")
print(f"{a} to the power of {b} is {power}")
print(f"gcd({a}, {b})={gcd}")
print(f"fact({a})={fact}")

3)
a=int(input('Enter a positiove integer'))
print("even number" if a%2==0 else "odd number”)

4)
a=int(input('Enter a number: '))
print(1 if a>0 else -1 if a<0 else 0)

5)
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
print(f"Before swapping: a={a}, b={b}")
a,b=b,a
print(f"After swapping: a={a}, b={b}")


6)
a=eval(input('Enter first number: '))
b=eval(input('Enter second number: '))
c=eval(input('Enter third number: '))
print("Largest Input : ",a if a>b and a>c else b if b>a and b>c else c)

7)
a=eval(input('Enter first number: '))
b=eval(input('Enter second number: '))
print("Largest: ",a if a>b else b)

8)
a=eval(input('Enter 1st Number: '))
b=eval(input('Enter 2nd number: '))
print("Result : ",">" if a>b else "<" if a<b else "=")



