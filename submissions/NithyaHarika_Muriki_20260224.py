#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#output: Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b))#output: Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c))#output: error
print('Hyd  is  ' green  '  city')#output:  error




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
a=int(input ("Enter 1st integer number:"))
b=int(input ("Enter 2nd integer number:"))
print(f'{a}+{b}={a-b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'max({a},{b})= {max(a,b)}')
print(f'min({a},{b})= {min(a,b)}')
print(f'{a}^{b}={a**b}')
print(f'sqrt({a})={math.sqrt(a.2f)}')
print(f'{a}^{b}={a**b}')
print(f'gcd({a},{b})={math.gcd(a,b)}')
print(f'fact{a} = {math.factorial(a)})


#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

#Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
a=int(input ("Enter 1st input number:"))
b=int(input ("Enter 2nd input number:"))
print(f'Before swap: {a=} , {b=}')
a,b=b,a
print(f'After swap: {a=} , {b=}')


'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''
a=int(input ("Enter 1st input number:"))
b=int(input ("Enter 2nd input number:"))
print("Largest Input: " ,a if a > b else b)

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
a=eval(input ("Enter 1st input number:"))
b=eval(input ("Enter 2nd input number:"))
b=eval(input ("Enter 3rd input number:"))
print("Largest Input: " ,a if a > b else b if b > c else c)

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
a=eval(input ("Enter 1st input number:"))
b=eval(input ("Enter 2nd input number:"))
c=eval(input ("Enter 3rd input number:"))
print("Result: " ,'>' if a > b else '<' if b > c else '=')
#output:
Enter 1st input number:10
Enter 2nd input number:20
Enter 3rd input number:20
Result:  =


'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
a=eval(input ("Enter any number:"))
print("Result: " , '-1' if -a else '+1' if a else '0')


'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
a=eval(input ("Enter any integer:"))
print(Even number if a%2 == 0 else odd number)


