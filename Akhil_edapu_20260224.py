"""
#find outputs

a = 'Hyd is green city'

print(a)

b = 'Hyd is "green" city'
print(b)

c = 'hyd is \' green\' city'
print(c)

#print('Hyd is 'green' city')


#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

#Hint:  Use  F  string  to  print  results


'''let input be 10 and 7
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

a = int(input('Enter a number_1: '))
b = int(input('Enter a number_2: '))

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} =  {a-b}')
print(f'{a} * {b} = {a * b }')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b}= {a%b}')
print(f'Max({a} {b}) = ',max(a,b))
print(f'min {a} {b} = ',min(a,b))
print(f'sqrt {a} = ',math.sqrt(a))
print(f'gcd {a} =', math.gcd(a))
print(f'fact {a} = ',math.factorial(a))


'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''



a = 25
b = 'hyd'
print('Before swapping')
print(a,b)
a,b=b,a
print('After swapping')
print(a,b)



'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
'''


a = eval(input('Enter a 1st input : '))
b = eval(input('Enter a 2nd input: '))

print(a if(a>b) else b)


a = input('Enter 1st String: ')
b = input('Enter 2nd String: ')

print(a if(a>b) else b)


#[2,3,5,25,6,8,8] list comparsion [25,56,5] the second list is printed because 25>2 in list comparsion
a = eval(input('Enter a 1st input : '))
b = eval(input('Enter a 2nd input: '))

print(a if(a>b) else b)





'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

#while inputting string as input put the string in quotes.
a = eval(input('Enter 1st input : '))
b = eval(input('Enter 2nd input : '))
c = eval(input('Enter 3rd input : '))

print(a if(a>b>c) else b if(b>c) else c)
'''




'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
"""

a = int(input("Enter 1st input : "))
b = int(input("Enter 2nd input : "))


print(f'Result= {'>' if(a > b ) else '<'}')







'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''



a = int(input("Enter 1st input : "))


print(f' Result : {-1 if(a<0) else 1 if(a > 0) else 0}')
      




'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''



a = int(input("Enter 1st input : "))

print('Even' if(a%2==0) else 'odd')






















