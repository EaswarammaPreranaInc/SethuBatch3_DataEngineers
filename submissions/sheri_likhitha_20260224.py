#1  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)			    #'Hyd is green city'
b = 'Hyd  is  "green"  city'
print(b)			    #'Hyd is "green" city'
c = 'Hyd  is  \'green\'  city'
print(c)			    #'Hyd is 'green' city'
#print('Hyd  is  ' green  '  city') #error invalid syntax

#2
import math
#taking inputs from user

num_1=int(input("Enter first integer number: "))
num_2=int(input("Enter second integer number: "))

#printing the result using f-strings

print(f"{num_1}+{num_2}={num_1+num_2}")
print(f"{num_1}-{num_2}={num_1-num_2}")
print(f"{num_1}*{num_2}={num_1*num_2}")
print(f"{num_1}/{num_2}={num_1/num_2}")
print(f"{num_1}%{num_2}={num_1%num_2}")
print(f"max({num_1},{num_2})={max(num_1,num_2)}")
print(f"min({num_1},{num_2})={min(num_1,num_2)}")
print(f"{num_1}^{num_2}={num_1**num_2}")
print(f"sqrt({num_1})={math.sqrt(num_1)}")
print(f"gcd({num_1},{num_2})={math.gcd(num_1+num_2)}")
print(f"factorial({num_1})={math.factorial(num_1)}")


#3
x=(input("Enter 1st input: "))
y=(input("Enter 2nd input: "))

#Display values before swapping
print(f"Before swap:x='{x}'\t y='{y}'")

#performing swap using tuple unpacking
x,y=y,x

#Display values after swapping
print(f"After swap : x = {x} \t y = {y}")


#4
#Taking inputs
value_1=eval(input("Enter 1st input: "))
value_2=eval(input("Enter 2nd input: "))

#Terenary operator to find largest
largest=value_1 if value_1>value_2 else value_2
print(f"largest input: {largest}")


#5
#Taking inputs
value_1=eval(input("Enter 1st value: "))
value_2=eval(input("Enter 2nd value: "))
value_3=eval(input("Enter 3rd value: "))

#Terenary operator to find largest between three values
largest=value_1 if value_1>value_2 else(value_2 if value_2>value_3 else value_3)
print(f"largest input is: {largest}")


#6 Nested terenary operator
#Taking inputs

value_1=eval(input("enter 1st value: "))
value_2=eval(input("enter 2nd value: "))

#Using nested terenary operators
result='>'if value_1>value_2 else('<' if value_1<value_2 else '=')
print(f"Result: {result}")


#7 nested terenary operator
#Taking inputs
x=int(input("Enter any value: "))

#Using nested terenary operators
result='1' if x>0 else('-1' if x<0  else '0')
print(f"Result: {result}")


#8 terenary operator
#Taking inputs
x=int(input("Enter any +ve integer: "))

#finding even number or odd number
result= 'Even number' if x%2==0 else 'Odd number'
print(f"Result: {result}")



