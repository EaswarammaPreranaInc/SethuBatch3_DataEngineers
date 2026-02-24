#1
#  Find outputs  (Home  work)
a = 'Hyd is green city'
print(a) #Hyd is green city
b = 'Hyd is "green" city'
print(b) #Hyd is "green" city
c = 'Hyd is \'green\' city'
print(c) #Hyd is 'green' city
print('Hyd is ' green  ' city') #Error as no object 'green' in present program #1 also no proper format, to rectify make use of comma ','



#2
'''
Write a program to determine sum , difference , product , quotient , largest and smallest of two numbers.
Also find remainder, sqrt of first input , power, gcd and factorial of first input

Hint: Use F string to print results

Let inputs be 10 and 7,
What is the sum? --->  17 
What is the difference? --->  3
What is the product? --->  70
What is the quotient? --->  1.42
What is the remainder? ---> 3
What is the largest number? --->  10
What is the smallest number? --->  7
What is the sqrt of 1st input? --->  3.16
What is the result of power ? --->  10000000
What is the gcd  of 2 numbers? --->  1
What is the factorial of 1st input ? --->  10!
'''
import math
ip1 = eval(input("Enter first integer number: ")) #10
ip2 = eval(input("Enter second integer number: ")) #7
sum = ip1 + ip2 
diff = ip1 - ip2
prod = ip1 * ip2
div = ip1 / ip2
rem = ip1 % ip2
maxv = max(ip1, ip2)
minv = min(ip1, ip2)
power = ip1 ** ip2
sqr = math.sqrt(ip1)
gcdv = math.gcd(ip1, ip2)
factv = math.factorial(ip1)
print(f"{ip1} + {ip2} = {sum}") #10 + 7 = 17
print(f"{ip1} - {ip2} = {diff}") #10 - 7 = 3
print(f"{ip1} * {ip2} = {prod}") #10 * 7 = 70
print(f"{ip1} / {ip2} = {div}") #10 / 7 = 1.4285714285714286
print(f"{ip1} % {ip2} = {rem}") #10 % 7 = 3
print(f"max({ip1} , {ip2}) = {maxv}") #max(10 , 7) = 10
print(f"min({ip1} , {ip2}) = {minv}") #min(10 , 7) = 7
print(f"{ip1} ^ {ip2} = {power}") #10 ^ 7 = 10000000
print(f"sqrt({ip1}) = {sqr}") #sqrt(10) = 3.1622776601683795
print(f"gcd({ip1} , {ip2}) = {gcdv}") #gcd(10 , 7) = 1
print(f"fact({ip1}) = {factv}") #fact(10) = 3628800



#3
'''
Write a program to swap values of any two objects in a single statement without using 3rd object

Let 'x' be 25 and 'y' be 'Hyd'
What are 'x' and 'y' after swap ? ---> Hyd  and  25

Hint: Swap references but not objects
'''
x = eval(input("Enter first input: ")) #25
y = eval(input("Enter second input: ")) #'Hyd'
print(f"Before swap:  {x = } , {y = }") #Before swap:  x = 25 , y = 'Hyd'
x, y = y, x
print(f"After swap:  {x = } , {y = }") #After swap:  x = 'Hyd' , y = 25



#4
'''
Write a program to determine largest of two inputs without using max() function

1) What is the output if inputs are 10 and 20? --->  20

2) What is the output if inputs are 35.8 and 27.9? ---> 35.8

3) What is the output if inputs are 'RAMA' and 'RAJESH'? --->  'RAMA'  becoz  'M' > 'J'

4) What is the output if inputs are [10 , 20 , 15 , 18 , 19 , 28] and [10 , 20 , 25, 17]? --->  [10 , 20 , 25 , 17]  because  25 > 15

5) Inputs can be integers , floats , strings and so on

6) Use  ternary operator
'''
x = eval(input("Enter first input: ")) #75
y = eval(input("Enter second input: ")) #90.5
l = x if x > y else y
print(f"Largest input: {l}") #Largest input:<space>90.5



#5
'''
Write a program to determine largest of three inputs without using max() function

1) What is the output if inputs are 10 , 20 and 15? --->  20

2) What is the output if inputs are 35.8 , 42.8 and 27.9 ? ---> 42.8

3) What is the output if inputs are 'RAMA' , 'RAKESH' and 'RAJESH' ? ---> 'RAMA'

4) What is the output if inputs are [10 , 20 , 15 , 18] , [10 , 20 , 32, 19] and [10 , 20 , 25, 17] ? ---> [10 , 20 , 32 , 19]

5) Inputs can be integers , floats , strings and so on

6) Use  nested  ternary  operator
'''
x = eval(input("Enter first input: ")) #'Hyderabad'
y = eval(input("Enter second input: ")) #'Secunderabad'
z = eval(input("Enter third input: ")) #'Cyberabad'
l = x if (x > y and x > z) else (y if y > z else z)
print(f"Largest input: {l}") #Largest input:<space>Secunderabad as S > H > C i.e. comparing first non-matching character among the 3 strings



#6
'''
Write a program to print '>' if 1st input > 2nd input, '<' if 1st input < 2nd input and '=' if inputs are same

1) What is the result if inputs are 10 and 20 ? --->  <

2) What is the result if inputs are 70 and 60 ? --->  >

3) What is the result if inputs are 25 and 25 ? ---> =

4) Inputs can be integers , floats , strings and so on

5) Use nested ternary operator
'''
x = eval(input("Enter first input: ")) #250
y = eval(input("Enter second input: ")) #300
res = '=' if x == y else ('>' if x > y else '<')
print(f"Result: {res}") #Result: <



#7
'''
Write a program to print 1 if input is +ve , -1 if input is -ve and 0 if input is 0

1) What is the result if input is -25? ---> -1

2) What is the result if input is 75? ---> 1

3) What is the result if input is 0? ---> 0

4) Use nested ternary operator
'''
n = eval(input("Enter any number: ")) #-75 #eval(input()) is optional as one can use int(input()) as this program #7 deals with only integer objects as inputs
res = 1 if n > 0 else (-1 if n < 0 else 0)
print(f"Result: {res}") #Result: -1



#8
'''
Write a program to test input is even number or odd number

1) What is an even number? ---> Divisible by 2

2) What is an odd number? ---> Not divisible by 2

3) Use ternary operator
'''
n = eval(input("Enter any positive number: ")) #45 #eval(input()) is optional as one can use int(input()) as this program #8 deals with only 'positive' integer objects as inputs
res = print("even number") if n % 2 == 0 else print("odd number") #odd number