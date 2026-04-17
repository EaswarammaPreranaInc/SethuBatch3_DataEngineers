#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)      # Hyd  is  green  city

b = 'Hyd  is  "green"  city'
print(b)      #  Hyd  is  "green"  city

c = 'Hyd  is  \'green\'  city'
print(c)    #Hyd  is  'green'  city

print('Hyd  is  ' green  '  city')   Error str inside str not permutated






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
a = int(input("enter 1st integer number: "))
b = int(input("enter 2nd integer number: "))

sum = a + b
diffe = a - b
product = a * b 
quotient = a / b
reminder = a % b
largest = max(a , b)
smalest = min(a , b)
sqrt_first = math.sqrt(a)
power = a ** b
gcd = math.gcd(a , b)
factorial  of  first = math.factorial(a)



print (f"{a} +{b}  ={sum}")
print (f"{a}  - {b} =(diffe}")
print (f"{a} * {b} ={product}")
print (f"{a} / {b}  ={quotient:.2f}")
print (f"{a} % {b} = {reminder}")
print (f"max({a},{b}) ={largest}")
print (f"min({a} ,{b}) ={smalest}")
print (f"{a}  ^  {b} = {power}")
print (f"sqrt({a}) = {sqrt_first :.2f}")
print (f"gcd({a} , {b}) = {gcd}")
print (f"fact({a}) = {factorial  of  first}")





output 

10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.43
10 % 7 = 3
max(10, 7) = 10
min(10, 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.16
gcd(10, 7) = 1
fact(10) = 3628800  







'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''



x = 25
y = "hyd"

print ("before swap:")
print ("x = ",x)
print ("y = ", y)

x , y = y ,x

print ("ofter swap:")
print ("x =" , x)   #"x ="  str 
print ("y = " , y)


output

Before Swap:
x = 25
y = Hyd

After Swap:
x = Hyd
y = 25






'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''



a = eval(input("enter first input: "))
b = eval(input("enter second input: "))


syntax  ternary  operator

result = value_if_true if condition else value_if_false 

largest = a if a > b else b

 print(f"Largest value is: {largest}")


output 
enter first input:10
enter second input:20
 20

enter first input:35.8
enter first input:27.1
  35.8


enter first input:RAMA
enter second input:RAJESH
 'RAMA'


enter first input:[10 , 20 , 15 , 18 , 19 , 28]
enter second input: [10 , 20 , 25, 17]

[10 , 20 , 25, 17]






'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''


nested  ternary  operator syntax:

largest = a if a > b and a > c else (b if b > c else c)

a = eval(input("Enter first value: "))
b = eval(input("Enter second value: "))
c = eval(input("Enter third value: "))

largest = a if a > b and a > c else (b if b > c else c)

print(f"Largest value is: {largest}")



Enter first value:10
Enter first value:20
Enter third value:30

                  20


Enter first value:35.8
Enter first value:42.8
Enter third value:27.9
                  42.8


Enter first value:'RAMA'
Enter first value:'RAKESH'
Enter third value:'RAKESH'
                  RAMA



Enter first value:[10,20,15,18]
Enter first value:[10,20,32,19]
Enter third value:[10,20,25,17]
                  [10, 20, 32, 19]









'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''



nested  ternary  operator syntax:

result = 1 if n > 0 else (-1 if n < 0 else 0)


n = int(input("Enter a number: "))

result = 1 if n > 0 else (-1 if n < 0 else 0)

print(f"Result is: {result}")


output
Enter a number:-25
-1

Enter a number:1
 1 

Enter a number:0
 0







'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''


Ternary Operator Syntax

result = "Even" if condition else "Odd"


n = int(input("Enter a number: "))

result = "Even Number" if n % 2 == 0 else "Odd Number"

print(f"{n} is {result}")


Enter a number:7
7 is Odd Number


