#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c)# Hyd is 'green' city
#print('Hyd  is ' green  '  city')# Error



import math
a=int(input("Enter the nnumber:"))
b=int(input("Enter the nnumber:"))
c= a+b
d=a-b
e=a*b
z=a/b
g=a%b
h=max(a,b)
m= math.sqrt(a)
i=min(a,b)
j=pow(a,b)
k=math.gcd(a,b)
l=math.factorial(a)

print(f"{c}")
print(f"{d}")
print(f"{e}")
print(f"{z:.2f}")
print(f"{g}")
print(f"{h}")
print(f"{i}")
print(f"{m:.2f}")
print(f"{j}")
print(f"{k}")
print(f"{l}")


a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("The number before swap are",a,b)
a,b=b,a
print("The number after swap are",a,b)



a=eval(input("enter 1st input:"))
b=eval(input("enter 2nd input:"))
print("Before swap: a=",a,"\t","y=",b)
a,b=b,a
print("After swap: a=",a,"\t","y=",b)




a = eval(input("Enter 1st value: "))
b = eval(input("Enter 2nd value: "))
c = a if a > b else b
print(f" Largest value : {c}")


()
a = eval(input("Enter 1st value: "))
b = eval(input("Enter 2nd value: "))
result = ">" if a > b else ("<" if a < b else "=")
print(f"Result :   {result}")



n = eval(input("Enter a number: "))
result = 1 if n > 0 else (-1 if n < 0 else 0)
print(f"Result ---> {result}")


n = int(input("Enter a number: "))
result = "Even Number" if n % 2 == 0 else "Odd Number"
print(f"{result}")

