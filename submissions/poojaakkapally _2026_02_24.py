1.#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)
#output:- Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)
#output:-Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)
#output:-Hyd  is  'green'  city
print('Hyd  is  ' green  '  city')
#output:-error(bcz tere is no comma)

2.'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
Hint:  Use  F  string  to  print  results
'''
#for sum
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} + {num2} = {num1 + num2}")
 '''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 + 7 = 17
'''
#for difference
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} - {num2} = {num1 - num2}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 - 7 = 3
'''
#for product
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} * {num2} = {num1 * num2}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 * 7 = 70
'''

#for quotient
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} / {num2} = {num1 / num2}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 / 7 = 1.4285714285714286
'''
#for remainder
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} % {num2} = {num1 % num2}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 %7 = 3
'''
#for largest number
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"max({num1} , {num2}) = {max(num1, num2)}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
max(10 , 7) = 10
'''
#for smallest number
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"min({num1} , {num2}) = {min(num1, num2)}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
min(10 , 7) = 7
'''
#for result of power
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} ^ {num2} = {num1 ** num2}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
10 ^ 7 = 10000000
'''
#for sqrt of 1st input
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"sqrt({num1}) = {math.sqrt(num1)}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
sqrt(10) = 3.1622776601683795
'''
#for gdc if 2 num
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"gcd({num1} , {num2}) = {math.gcd(num1, num2)}")'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
gcd(10 , 7) = 1
'''
#for factorial of 1st input
import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"fact({num1}) = {math.factorial(num1)}")
'''
output:-
Enter 1st integer number : 10
Enter 2nd integer number : 7
fact(10) = 3628800
'''
'''
overall program

import math
num1 = 10
num2 = 7
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))
print(f"{num1} + {num2} = {num1 + num2}") #10 + 7 = 17
print(f"{num1} - {num2} = {num1 - num2}") # 10 - 7 = 3
print(f"{num1} * {num2} = {num1 * num2}") #10 * 7 = 70
print(f"{num1} / {num2} = {num1 / num2}") #10 / 7 = 1.4285714285714286
print(f"{num1} % {num2} = {num1 % num2}") #10 % 7 = 3
print(f"max({num1} , {num2}) = {max(num1, num2)}") #max(10 , 7) = 10
print(f"min({num1} , {num2}) = {min(num1, num2)}") #min(10 , 7) = 7
print(f"{num1} ^ {num2} = {num1 ** num2}") #10 ^ 7 = 10000000
print(f"sqrt({num1}) = {math.sqrt(num1)}") #sqrt(10) = 3.1622776601683795
print(f"gcd({num1} , {num2}) = {math.gcd(num1, num2)}") #gcd(10 , 7) = 1
print(f"fact({num1}) = {math.factorial(num1)}") #fact(10) = 3628800

'''
3.'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25
Hint:  Swap  references  but  not  objects
'''

#program
x = 25
y = 'Hyd'
x, y = y, x
print(f"x: {x}")
print(f"y: {y}")

'''
#output:-
x: Hyd
y: 25

'''

4.'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
 Use   ternary  operator
'''
#program

num1 = eval(input("Enter 1st input : "))
num2 = eval(input("Enter 2nd input : "))
largest = num1 if num1 > num2 else num2
print(f"Largest Input   : {largest}")

'''
#output:-
Enter 1st input : 10
Enter 2nd input : 20.8
Largest Input   : 20.8
'''
5.'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
 Use  nested  ternary  operator
'''
#program
X = input("Enter 1st input : ")
Y = input("Enter 2nd input : ")
Z = input("Enter 3rd input : ")
largest = X if (X > Y and X > Z) else (Y if Y > Z else Z)
print(f"Largest Input : {largest}")

'''
#output:-
Enter 1st input : hyd
Enter 2nd input : sec
Enter 3rd input : cyb
Largest Input : sec
'''
6.'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same
 Use  nested  ternary  operator
'''

#program
num1 = eval(input("Enter 1st input : "))
num2 = eval(input("Enter 2nd input : "))
result = ">" if num1 > num2 else ("<" if num1 < num2 else "=")
print(f"Result : {result}")

'''
#output:-
Enter 1st input : 10
Enter 2nd input : 10
Result : =
Enter 1st input : 10
Enter 2nd input : 20
Result : <
Enter 1st input : 20
Enter 2nd input : 10
Result : >
'''

7.'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

 Use  nested  ternary  operator
'''
#program
num = eval(input("Enter a number: "))
result = 1 if num > 0 else (-1 if num < 0 else 0)
print(f"Result: {result}")

'''
#output:-
Enter a number: 28
Result: 1
Enter a number: -25
Result: -1

''''

8.'''
Write  a  program  to  test  input  is  even  number  or  odd  number

 Use  ternary  operator
'''
num = eval(input("Enter a number: "))
result = "Even number" if num % 2 == 0 else "Odd number"
print(result)

'''
#output:-
Enter a number: 9
Odd number
Enter a number: 8
even number
'''




































