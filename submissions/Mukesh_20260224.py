import math
# a=10 
# b=7
# a=eval(input("enter 1st Integer :"))
# b=eval(input("Enter 2 nd integer :"))
# print(F'{a} + {b} = {a+b}')
# print(F'{a} - {b} = {a-b}')
# print(F'{a} * {b} = {a*b}')
# print(F'{a} % {b} = {a%b}')
# print(F'Max{a,b}',max(a,b))
# print(F'min{a,b}',min(a,b))
# print(F'{a} ^ {b} = {a**b}')
# print(F'sqrt({a})', math.sqrt(a))
# print(F'gcd({a})',math.gcd(a,b))
# print(F'factorial({a})',math.factorial (a))

# x=eval(input("Enter 1st input :"))
# y=eval(input("Enter 2nd input :"))
'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
# print(f"Before swap : {x=}")
# x,y=y,x
# print(f"After swap : {x=}")

'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
"""x=eval(input("Enter 1st input :"))
y=eval(input("Enter 2nd input :"))
print(F"{x} is largest ") if x>y else print(f'{y}' is largest)
"""
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
"""x=eval(input("Enter 1st input :"))
y=eval(input("Enter 2nd input :"))
z=eval(input("enter the 3rd Number :"))
print(F"{x} is largest ") if x>y else print(f'{y} is largest') if y>z else print(f'{z} is largest')"""

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on2

5) Use  nested  ternary  operator
'''
"""x=eval(input("Enter 1st input :"))
y=eval(input("Enter 2nd input :"))
print(f'{x is { result =">"} if x>y else "<" if x<y else "=" }')
"""

#x=eval(input("Enter 1st input :"))
#print(f'{x if x>0    else   x  }')


'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
"""x=eval(input("Enter 1st input :")) 
print("Even Number") if x%2==0 else print("Odd Number")

"""

x=eval(input("Enter the age for the vote :"))
print("your Eligible to vote ") if x>18 else print("Your not eligibe to vote")
print(F" Result= {x}")
