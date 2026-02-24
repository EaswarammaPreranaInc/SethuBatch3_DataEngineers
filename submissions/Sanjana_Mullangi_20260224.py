#Outputs Homework #1
a = 'Hyd  is  green  city'
print(a) # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd is 'green' city
#print('Hyd  is  ' green  '  city') # error because green is not enclosed in a string, neither it is a defined object


#Programming Homework #1

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

'''Sample Output:

Enter 1st integer number: 10

Enter 2nd integer number: 7

10 + 7 = 17
10 — 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd (10, 7) = 1
fact (10) = 3628800
Press any key to continue...

'''

'''import math

a = int(input('Enter the first integer:'))
b = int(input('Enter the second integer:'))

add = a + b
sub = a - b
mul = a * b
div = a / b
rem = a % b
lar = '''

import math
a=eval(input("enter the first input:"))
b=eval(input("enter the second input:"))
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}%{b}={a%b}")
print(f"max{a,b}={max(a,b)}")
print(f"min{a,b}={min(a,b)}")
print(f"math.pow{a,b}={a**b}")
print(f"gcd{a,b}={math.gcd(a,b)}")
print(f"sqrt{a}={math.sqrt(a)}")
print(f"fact{a}={math.factorial(a)}")


#Programming Homework #2

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''

x=eval(input("Enter the first input:"))
y=eval(input("Enter the second input:"))
print("Before Swap:", "x=",x,"y=",y)
x,y=y,x
print("After Swap:","x=",x,"y=",y)


#Programming Homework #3

'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
a=eval(input("Enter the 1st input:"))
b=eval(input("Enter the 2nd input:"))
print("Largest input:",a if a>b else b)


#Programming Homework #4

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
a=eval(input("Enter the 1st input:"))
b=eval(input("Enter the 2nd input:"))
c=eval(input("Enter the 3rd input:"))
print("Largest number:",a if a>b else b if b>c else c)





#Programming Homework #5

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
a=eval(input("Enter the 1st input:"))
b=eval(input("Enter the 2nd input:"))
print("Result:",">" if a>b else "<" if a<b else "=") #run again

#Programming Homework #6

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator op1-con1 should ber related
cond2 should be related to op2
'''
a=eval(input("Enter the input:"))
print("Result:","1" if a>0 else "-1" if a<0 else "0")


#Programming Homework #7

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
a=eval(input("Enter the input:"))
print("the given input is","Even" if a%2==0 else "Odd")

