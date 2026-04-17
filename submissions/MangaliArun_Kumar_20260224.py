#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

import math
a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"max({a} , {b}) = {max(a,b)}")
print(f"min({a} , {b}) = {min(a,b)}")
print(f"{a} ^ {b} = {a**b}")
print(f"sqrt({a}) = {math.sqrt(a)}")
print(f"gcd({a} , {b}) = {math.gcd(a,b)}")
print(f"fact({a}) = {math.factorial(a)}")

#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")
print(f"Before swap :{x=} \t {y=}")
x,y = y,x
print(f"After swap : {x=} \t {y=}")

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
print("Largest Input : ", x if x>y else y)

#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
z = eval(input("Enter 3rd input : "))
print("Lagest Input : " , x if x>y and x>z  else y if y>z else z)

#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and '='  if  inputs  are  same
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print("Result : ", ">" if x>y else "<" if x<y else "=" )

#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
x = int(input("Enter any number : "))
print("Result : ",1 if x>0 else -1 if x<0 else 0 )

#Write  a  program  to  test  input  is  even  number  or  odd  number
x = int(input("Enter any +ve integer : "))
print("Even number"  if x%2==0 else "Odd number")