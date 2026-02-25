#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)#'Hyd  is  green  city'
b = 'Hyd  is  "green"  city'
print(b)# Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c)#  error
print('Hyd  is  ' green  '  city')


# Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  print(f"sum:{a+b}")--> 10+7=17		
What  is  the  difference ?  --->  print(f"difference:{a-b}")--> 3
What  is  the  product ?  --->   print(f"product:{a*b}")--> 70
What  is  the  quotient ?  --->   print(f"quotient:{round(a/b,2)}"-->1.42
What  is  the  remainder ?  ---> print(f"remainder:{a%b}")--> 3
What  is  the  largest  number ?  --->  print(f"largest:{max(a,b)}")-->10
What  is  the  smallest  number ?  --->  print(f"smallest:{min(a,b)}")-->7
What  is  the  sqrt  of  1st  input ?  --->  print(f" sqrt  of  1st  input:{round(math.sqrt(a),2)}")-->3.16
What  is  the  result  of  power ?  --->  print(f"result  of  power(10^7):{a**b}")-->10000000
What  is  the  gcd  of  2  numbers ?  ---> print(f"gcd:{math.gcd(a,b)}")-->1
What  is  the  factorial   of  1st  input ?  --->  print(f"factorial of 1st:{math.factorial(a)}")-->10!

#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> y, x

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  print(f"1) 10 and 20: {find_largest(10, 20)}")-->20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> print(f"2) 35.8 and 27.9: {find_largest(35.8, 27.9)}")--->35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  print(f"3) 'RAMA' and 'RAJESH': {find_largest('RAMA', 'RAJESH')}")--->  'RAMA'  becoz  'M' > 'J'


4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   ---> print(f"4) Lists: {find_largest([10, 20, 15, 18, 19, 28], [10, 20, 25, 17])}")--> [10 , 20 , 25 , 17]  becoz  25 > 15

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use   ternary  operator


# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  print(find_largest(10, 20, 15))# 20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> print(find_largest(35.8,42.8,27.9))#42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  print(find_largest( 'RAMA'  , 'RAKESH'  , 'RAJESH'))#'RAKESH'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  print(find_largest( [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17]))#[10 , 20 , 32, 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator


# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> # Compare two inputs

                                                                                           a = eval(input("Enter first value: "))#10
                                                                                           b = eval(input("Enter second value: "))#20
                                                                                           print('>' if a > b else '<' if a < b else '=') #20
                                                                                               
2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  # Compare two inputs
                                                                                             a= eval(input("Enter first value: "))#70
                                                                                              b = eval(input("Enter second value: "))#60
                                                                                               print('>' if a > b else '<' if a < b else '=')#70

3) What  is  the  result  if  inputs  are  25  and  25 ?  --->  # Compare two inputs
                                                                                             a= eval(input("Enter first value: "))#25
                                                                                              b = eval(input("Enter second value: "))#25
                                                                                               print('>' if a > b else '<' if a < b else '=')#=

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator


Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->n = float(input("Enter number: "))#-25
                                                                          result = 1 if n > 0 else

2) What  is  the  result  if  input  is  75 ?  ---> n = float(input("Enter number: "))#75
                                                                        result = 1 if n > 0 else

3) What  is  the  result  if  input  is  0 ?  ---> n = float(input("Enter number: "))#0
                                                                        result = 1 if n > 0 else

4) Use  nested  ternary  operator


Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->num = int(input("Enter a number: "))#6
                                                           result = "Even Number" if num % 2 == 0 else "Odd Number"
                                                              print(result)#6

2) What  is  an  odd  number  ?  ---> num = int(input("Enter a number: "))#3
                                                            result = "Even Number" if num % 2 == 0 else "Odd Number"
                                                         print(result)#3

3) Use  ternary  operator




