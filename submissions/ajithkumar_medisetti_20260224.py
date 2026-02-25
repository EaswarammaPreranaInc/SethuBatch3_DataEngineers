#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  \'green\'  city
print('Hyd  is  ' green  '  city') # Error

# Write a program to determine sum , difference , product , quotient , largest and smallest of two numbers.
Also find remainder, sqrt of first input , power, gcd and factorial of first input.

# Program

import math

num1 = int(input("Enter 1st integer number: "))
num2 = int(input("Enter 2nd integer number: "))

print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}/{num2}={num1/num2}")
print(f"{num1}%{num2}={num1%num2}")
print(f"max({num1},{num2})={max(num1,num2)}")
print(f"min({num1},{num2})={min(num1,num2)}")
print(f"10**7={10**7}")
print(f"sqrt({num1})={math.sqrt(num1)}")
print(f"fact({num1})={math.factorial(num1)}")
print("Press any key to continue.")

#OUTPUT:
Enter 1st integer number: 10
Enter 2nd integer number: 7
10+7=17
10-7=3
10*7=70
10/7=1.4285714285714286
10%7=3
max(10,7)=10
min(10,7)=7
10**7=10000000
sqrt(10)=3.1622776601683795
fact(10)=3628800
Press any key to continue.


# Write a program to swap values of any two objects in a single statement without using 3rd object

Let 'x' be 25 and 'y' be 'Hyd'
What are 'x' and 'y' after swap ?

# Program 

x = input("Enter 1st input.   : ")
y = input("Enter 2nd input. : ")

print(f"Before swap :  x='{x}'            y=\" '{y}' \"")
# Single statement swap - Python's tuple unpacking swaps references atomically
x, y = y, x
print(f"After swap :  x=\"'{y}'\"          y='{x}'")
print("Press any key to continue.....")

# OutPut :

Enter 1st input.   : 25
Enter 2nd input. : 'Hyd'
Before swap :  x='25'            y=" 'Hyd' "
After swap :  x="'Hyd'"          y='25'
Press any key to continue.....



# Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

def largest(a, b):
    return a if a > b else b

# Test cases as specified
print(largest(10, 20))          # Output: 20
print(largest(35.8, 27.9))      # Output: 35.8
print(largest('RAMA', 'RAJESH'))# Output: 'RAMA' ('M' > 'J')
print(largest([10, 20, 15, 18, 19, 28], [10, 20, 25, 17]))  # Output: [10, 20, 25, 17] (25 > 15 at index 2)


#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function


a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
c = eval(input("Enter 3rd input : "))

largest = a if (a > b and a > c) else (b if b > c else c)

print("Largest Input :", largest)

#Output:

Enter 1st input : 'Hyd'

Enter 2nd input : 'Sec'

Enter 3rd input : 'Cyb'

Largest Input : Sec

# Write a program to print '>' if 1st input > 2nd input, '<' if 1st input < 2nd input and '=' if inputs are same.

a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))

result = '>' if a > b else ('<' if a < b else '=')

print("Result  :  ", result)


#Output: 

Enter 1st input : 10
Enter 2nd input : 20
Result  :   <


# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

n = int(input("Enter any number : "))

result = 1 if n > 0 else (-1 if n < 0 else 0)

print("Result :", result)

#Output: 

Enter any number : -25
Result : -1


# Write  a  program  to  test  input  is  even  number  or  odd  number

n = int(input("Enter any +ve integer : "))

result = "Even number" if n % 2 == 0 else "Odd number"

print(result)

#Output:

Enter any +ve integer : 26
Even number





 