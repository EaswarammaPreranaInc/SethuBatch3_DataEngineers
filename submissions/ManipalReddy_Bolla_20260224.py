#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#Hyd is green city
b = 'Hyd  is  "green"  city'
print(b)#Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c)#Hyd is 'green' city
print('Hyd  is  ' green  '  city')#error


import math
x=eval(input("Enter 1st integer number : "))
y=eval(input("Enter 2nd integer number : "))
print(F'{x} + {y} = {x+y}')
print(F'{x} - {y} = {x-y}')
print(F'{x} * {y} = {x*y}')
print(F'{x} / {y} = {x/y}')
print(F'{x} % {y} = {x%y}')
print(F'max({x},{y}) = {max(x,y)}')
print(F'min({x},{y}) = {min(x,y)}')
print(F'{x} ^ {y} = {x**y}')
print(F'sqrt({x}) = {math.sqrt(x)}')
print(F'gcd({x},{y}) = {math.gcd(x,y)}')
print(F'fact({x}) = {math.factorial(x)}')

'''
output
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10,7) = 10
min(10,7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10,7) = 1
fact(10) = 3628800
'''



x=(input("Enter 1st input : "))
y=(input("Enter 2nd input : "))
print(F'Before swap {x=}    and    {y=}')
x,y=y,x
print(F'After swap {x=}  and   {y=}')

'''
output
Enter 1st input : 25
Enter 2nd input : 'Hyd'
Before swap x='25'    and    y="'Hyd'"
After swap x="'Hyd'"  and   y='25'
'''


x=eval(input('Enter 1st input : '))
y=eval(input('Enter 2nd input : '))
print("largest Input : ",x) if x>y else print("largest Input : ",y)

'''
output
Enter 1st input : 10
Enter 2nd input : 20
largest Input :  20
Enter 1st input : 35.8
Enter 2nd input : 27.9
largest Input :  35.8
Enter 1st input : 'RAMA'
Enter 2nd input : 'RAJESH'
largest Input :  RAMA
Enter 1st input : [10,20,15,18,19,28]
Enter 2nd input : [10,20,25,17]
largest Input :  [10, 20, 25, 17]
'''

x=eval(input('Enter 1st input : '))
y=eval(input('Enter 2nd input : '))
z=eval(input('Enter 3rd input : '))
print("largest Input : ",x) if x>y and x>z else print("largest Input : ",y) if y>z else print("largest Input : ",z)

'''
output
Enter 1st input : 'Hyd'
Enter 2nd input : 'Sec'
Enter 3rd input : 'Cyb'
largest Input :  Sec
'''

x=eval(input('Enter 1st input : '))
y=eval(input('Enter 2nd input : '))
print("Result : >") if x>y else (print("Result : <") if x<y else print("Result : ="))

'''
output
Enter 1st input : 10
Enter 2nd input : 20
Result : <
Enter 1st input : 70
Enter 2nd input : 60
Result : >
Enter 1st input : 25
Enter 2nd input : 25
Result  : =
'''

x=int(input('Enter any number : '))
print("1") if x>0 else (print("-1") if x<0 else print("0"))

'''
output
Enter 1st number : -4
-1
Enter any number : 5
1
Enter any number : 0
0
'''


x=int(input('Enter any +ve integer : '))
print("Even number") if x%2==0 else print("Odd number")

'''
output
Enter any -ve integer : 40
Even number
Enter any number : 5
Odd number
'''
