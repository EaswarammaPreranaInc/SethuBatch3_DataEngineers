#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b)  # Hyd id "green" city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd is 'green' city
print('Hyd  is  ' green  '  city') # Error



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

Program:
a=eval(input('Enter 1st input number:')
b=eval(input('Enter 2nd input number:')
print(a,'+',b,'=',a+b)
print(a,'*',b,'=',a*b)
print(a,'-',b,'=',a-b)
print(a,'/',b,'=',a+b)
print(a,'%',b,'=',a+b)
print('max','(',a,',',b,')','=',max(a,b))
print('min','(',a,',',b,')','=',min(a,b))
print(a,'^',b,'=',pow(a,b))
print('sqrt','(',a,')','=',sqrt(a))
print('gcd','(',a,',',b,')','=',math.gcd(a))
print('fact','(',a,')','=',math.factorial(a))



Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects

Program:
a,b=10,7
Print('Before Swap:',a,b)
a,b=b,a
print('After swap:',a,b)


Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator
 

Program:
1)
a=eval(input('Enter 1st input:'))
b=eval(input('Enter 2nd input:'))
if a>b:
	print(a)
else:
	print(b)




Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator

program:
a=eval(input('Enter 1st input:'))
b=eval(input('Enter 2nd input:'))
c=eval(input('Enter 3rd input:'))
if a>b>c:
	print(a)
if b>c:
	print(b)
else:
	print(c)




Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator

a=eval(input('Enter 1st input:'))
b=eval(input('Enter 2nd input:'))
if a>b:
	print(>)
if b>c:
	print(<)
else:
	print(=)




Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator

Program:

a=eval(input('Enter 1st input:'))

if a>0 and a!=0:
	print('1')
if a<0:
	print('-1')
else:
	print('0')



Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator


Program:

a=eval(input('Enter 1st input:'))

if a%2==0:
	print('even')

else:
	print('odd')