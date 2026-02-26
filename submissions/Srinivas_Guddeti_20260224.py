#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) #O/P:'Hyd is green city'
b = 'Hyd  is  "green"  city'
print(b) #O/P:'Hyd is "green" city'
c = 'Hyd  is  \'green\'  city'
print(c) #O/P:'Hyd is 'green' city'
print('Hyd  is  ' green  '  city') #O/P: error


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
What  is  the  factorial   of  1st  input ?  --->  10!  '''


a=int(input("Enter 1st integer number:))
b=int(input("Enter 2nd integer number:))

print(f"{a} + {b} ={a+b}")
print(f"{a} - {b} ={a-b}")
print(f"{a} * {b} ={a*b}")
print(f"{a} / {b} ={a/b}")
print(f"{a} % {b} ={a%b}")
print(f"max{a} ,{b} = max{a,b}")
print(f"mix{a} ,{b} = mix{a,b}")
print(f"{a} ^ {b} ={a**b}")
print(f"sqrt({a})={math.sqrt(a)}")
print(f"gcd({a},{b})={math.gcd(a,b)}")
print(f"fact({a},{b})={math.fact(a,b)}")



'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25
Hint:  Swap  references  but  not  objects
'''


x=input("enter 1st input:")
y=input("enter 2nd input:")

print(f"before swap:x='{x}'   y='{y}'")

x , y=y , x
print(f"after swap:x='{x}'   y='{y}'")



'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20
2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8
3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'
4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15
5) Inputs  can  be  integers , floats , strings  and  so  on
6) Use   ternary  operator
'''


x=eval(input("enter 1st input:")
y=eval(input("enter 2nd input:")

largest = x if x>y else y

print(f"Largest Input = {Largest}")




'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20
2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8
3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'
4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]
5) Inputs  can  be  integers , floats , strings  and  so  on
6) Use  nested  ternary  operator
'''

x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))
z=eval(input("enter 3rd input:"))

largest = x if x>y and x>z else (b if b>z else z)	 

print(f"Largest Input = {Largest}")




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


x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))

Result = '>' if a > b else '<' if a < b else '='

print(f"Result={Result}")



'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1
2) What  is  the  result  if  input  is  75 ?  ---> 1
3) What  is  the  result  if  input  is  0 ?  ---> 0
4) Use  nested  ternary  operator
'''

x=float(input("Enter any input:"))

result = -1 if x<0 else 1 if x>0 else 0

print(F"result={result}")



'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2
2) What  is  an  odd  number  ?  ---> Not  divisible  by  2
3) Use  ternary  operator
'''

x = int(input("Enter any +ve input:"))

result = "Even number" if x%2 == 0 else "Odd number"

print(result) 