a = int(input("Enter the number:  "))
b = int(input("Enter the number:  "))
print(F'{a+b=}')
print(F'{a-b=}')
print(F'{a*b=}')
print(F'{a/b=}')
print(F'{a%b=}')
print(F'{max(a,b)=}')
print(F'{min(a,b)=}')


import math
print(math.sqrt(a))
print(math.gcd(a,b))
print(math.factorial(a))
print(math.pow(a,b))


a = eval(input())
b = eval(input())
largest = a if a>b else b
print("Largest is:", largest)



num = int(input("Enter positive integer:  "))
result = "Even" if num % 2 ==0 else "odd"
print(f" The number is {result}")

num = int(input("Enter a number:  "))
result = 1 if num>0 else(-1 if num<0 else 0)
print(result)

a = int(input("Enter first input:  "))
b = int(input("Enter second input: "))
result = '>' if a>b else('<' if a<b else '=')
print(result)
            
x = int(input("Enter the number:  "))
y = input("Enter name:  ")
print("Before swap: x =", x, "y =", y)
x, y = y , x
print("After swap: x =", x, "y =", y)


#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) #Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) #Hyd id "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) #Hyd is 'green' city
print('Hyd  is  ' green  '  city') #Hyd is 'green' city 



a = eval(input("Enter 1st input:   "))
b = eval(input("Enter 2nd input:   "))
c = eval(input("Enter 3rd input:   "))
largest = a if a>b and a>c else (b if b>c else c)
print("Largest input:", largest)

