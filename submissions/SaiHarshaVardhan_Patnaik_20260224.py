#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) #Hyd  is  'green'  city
print('Hyd  is  ' green  '  city') #Error

#Operations between a and b
import math
from math import *
a = int(input('Enter first input :'))
b = int(input('Enter second input :'))
print(f'{a}','+',f'{b}','=',f'{a+b}')
print(f'{a}','-',f'{b}','=',f'{a-b}')
print(f'{a}','*',f'{b}','=',f'{a*b}')
print(f'{a}','/',f'{b}','=',f'{a/b}')
print(f'{a}','%',f'{b}','=',f'{a%b}')
print('max(10 , 7)','=',f'{max(a,b)}')
print('min(10 , 7)','=',f'{min(a,b)}')
print(f'{math.sqrt(a) = }')
print('10 ^ 7', '=',f'{pow(a,b)}')
print('gcd(10,7)','=', f'{math.gcd(a , b)}')
print('fact(7)','=',f'{math.factorial(b)}')
'''
Output:
Enter first input :10
Enter second input :7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
math.sqrt(a) = 3.1622776601683795
10 ^ 7 = 10000000.0
gcd(10,7) = 1
fact(7) = 5040
'''

#Swap of two objects 
x = input('Enter First input = ')
y = input('Enter Second input = ')
print('Before Swap :',f'{x = }',f'{y = }')
x,y = y,x
print('After Swap :',f'{x = }',f'{y = }')
'''
Output:
Enter First input = 25
Enter Second input = Hyd
Before Swap : x = '25' y = 'Hyd'
After Swap : x = 'Hyd' y = '25'
'''

#Largest value between two inputs 
a = eval(input("Enter first input : "))
b = eval(input("Enter second input : "))
largest = a if a > b else b
print("The largest Output is", largest)
'''
Output:
Enter first input : 10
Enter second input : 20
The largest input is 20

Enter first input : 35.8
Enter second input : 27.9
The largest input is 35.8

Enter first input: 'RAMA'
Enter second input: 'RAJESH'
The largest number is RAMA

Enter first input: [10 , 20 , 15 , 18 , 19 , 28]
Enter second input: [10 , 20 , 25, 17]
The largest number is [10, 20, 25, 17]
'''

#Largest value between three inputs
a = eval(input("Enter first input: "))
b = eval(input("Enter second input: "))
c = eval(input("Enter third input: "))
largest = a if (a > b and a > c) else (b if (b > a and b > c) else c)
print("The largest input is:", largest)
'''
Output:
Enter first input: 10
Enter second input: 20
Enter third input: 15
The largest input is: 20

Enter first input: 35.8
Enter second input: 42.8
Enter third input: 27.9
The largest input is: 42.8

Enter first input: 'RAMA'
Enter second input: 'RAKESH'
Enter third input: 'RAJESH'
The largest input is: RAMA

Enter first input: [10 , 20 , 15 , 18]
Enter second input: [10 , 20 , 32, 19]
Enter third input: [10 , 20 , 25, 17]
The largest number is: [10, 20, 32, 19]
'''

#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and'='  if  inputs  are  same
a = eval(input('Enter first input:'))
b = eval(input('Enter second input:'))
Result = '>' if a > b else '<' if a < b else '='
print('Result:',Result) 
'''
Output:
Enter first input:10
Enter second input:20
Result: <

Enter first input:70
Enter second input:60
Result: >

Enter first input:25
Enter second input:25
Result: =
'''

#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
a = eval(input('Enter input:'))
Result = 1 if a > 0 else -1 if a < 0 else 0
print('Result:',Result) 
'''
Output:
Enter input:-25
Result: -1

Enter input:75
Result: 1

Enter input:0
Result: 0
'''

#Write  a  program  to  test  input  is  even  number  or  odd  number
d = eval(input('Enter a number:'))
Result = 'Even' if d % 2 == 0 else 'Odd'    
print(Result)   
'''
Output:
Enter a number:6
Even

Enter a number:7
Odd

'''










