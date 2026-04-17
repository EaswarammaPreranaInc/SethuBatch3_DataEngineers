#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd is 'green' city
#print('Hyd  is  ' green  '  city') # Error

print()

'''
2nd Q :
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
print("2nd Q")
import math
x1 = eval(input("Enter First integer number :")) # 11
x2 = eval(input("Enter second integer number :")) #7
sum = x1+x2
diff = x1 - x2
pro = x1*x2
div = x1/x2
rem = x1%x2
maxn = max(x1 , x2)
minn = min(x1 , x2)
pow = x1**x2
sqr = math.sqrt(x1)
gcdn = math.gcd(x1 , x2)
fact = math.factorial(x1)


print(f"{x1} + {x2} = {sum}") # 11 + 7 = 18
print(f"{x1} - {x2} = {diff}") # 11 - 7 = 4
print(f"{x1} * {x2} = {pro}") # 11 * 7 = 77
print(f"{x1} / {x2} = {div}") # 11 / 7 = 1.5714285714285714
print(f"{x1} % {x2} = {rem}") # 11 % 7 = 4
print(f"max({x1} , {x2}) = {maxn}") # max(11 , 7) = 11
print(f"min({x1} , {x2}) = {minn}") # min(11 , 7) = 7
print(f"{x1} ^ {x2} = {pow}") # 11 ^ 7 = 19487171
print(f"sqrt({x1}) = {sqr}") # sqrt(11) = 3.3166247903554
print(f"gcd({x1} , {x2}) = {gcdn}") # gcd(11 , 7) = 1
print(f"fact({x1}) = {fact}") # fact(11) = 39916800
print()
''' 
Output :
Enter First integer number :11
Enter second integer number :7
11 + 7 = 18
11 - 7 = 4
11 * 7 = 77
11 / 7 = 1.5714285714285714
11 % 7 = 4
max(11 , 7) = 11
min(11 , 7) = 7
11 ^ 7 = 19487171
sqrt(11) = 3.3166247903554
gcd(11 , 7) = 1
fact(11) = 39916800
'''
'''
3rd Q
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
print("3rd Q")

a = eval(input("Enter 1st input :"))
b = eval(input("Enter 2nd input : "))
print(f"Before swap : {a = } , {b = }")
a,b = b,a
print(f"After swap : {a = } , {b = }")


'''
Output :
Enter 1st input :25
Enter 2nd input : 87
Before swap : a = 25 , b = 87
After swap : a = 87 , b = 25
'''

'''
4th Q
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
print("4th Q")

a = eval(input("Enter 1st input :"))
b = eval(input("Enter 2nd input :"))
lar = a if a > b else b
print(f"Largest input : {lar}")

'''
4th Q
Output :
Enter 1st input :'Hydr'
Enter 2nd input :'Secr'
Largest input : Secr
'''

'''
5th Q
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
print("5th Q")

a = eval(input("Enter 1st input :"))
b = eval(input("Enter 2nd input :"))
c = eval(input("Enter 3rd input :"))

lar = a if(a > b and a > c) else (b if b > c else c)
print(f"Largest Input : {lar}")

'''
Output :
5th Q
Enter 1st input :100.8
Enter 2nd input :28.9
Enter 3rd input :65.8
Largest Input : 100.8
'''

'''
6th Q
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
print("6th Q")

a = eval(input("Enter 1st input :"))
b = eval(input("Enter 2nd input :"))
ans = '=' if a==b else ('>' if a > b else '<')
print(f"Result : {ans}")

'''
Output :
6th Q
Enter 1st input :310
Enter 2nd input :520
Result : <
'''

'''
7th Q
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
print("7th Q")

i1 = eval(input("Enter any number : "))
ans = 1 if i1 > 0 else (-1 if i1 < 0 else 0)
print(f"Result : {ans}")

'''
Output :
7th Q
Enter any number : -6.9
Result : -1
'''

'''
8th Q
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
print("8th Q")
a = eval(input("Enter any +ve number : "))
ans = print("Even number") if a%2 == 0 else print("Odd number")

'''
Output :
8th Q
Enter any +ve number : 399
odd number
'''