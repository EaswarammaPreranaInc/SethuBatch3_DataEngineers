#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)	--> Hyd is green city
b = 'Hyd  is  "green"  city'
print(b)	---> Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c)	---> Hyd is 'green' city
print('Hyd  is  ' green  '  city') ---> error


'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

a = int(input('enter first number : ' ))
b = int(input('enter second number : ' ))
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'max{a},{b} = max{a,b}')
print(f'min{a},{b} = min{a,b}')
print(f'{a}^{b} ={a**b}')
print(f'sqrt({a}) = {math.sqrt(a)}')
print(f'gcd({a},{b}) = {math.gcd(a,b)}')
print(f'fact({a}) = {math.factorial(a)}')
print()



Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

a = input('enter first input : ' ))
b = input('enter second input : ' ))
print(f'before swap : {a=} \t {b})
a,b=b,a
print(f'after swap : {a=} \t {b})
print ()

Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
a=input(f'enter first input : ' )
b=input(f'enter second input : ' )
print('largest of two :{a if a>b else b}' )
print()


Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
a = eval(input('enter first input : ' ))
b = eval(input('enter second input : ' ))
c = eval(input('enter third input : ' ))
print(f'largest of three : {a if a>b and a>c else b if b>a and b>c else c}')



Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

a = eval(input(f'enter the first input : ' )
b = eval(input(f'enter the second input : ' )
print(f'Result : { '>' if a>b else '<' if a<b else'='} ')




'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  ---> 1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''

 a= eval(input(f'enter the input : ' )
print(f' result : {'Positive Number' if a >= 0 else 'Negative Number'}')


Write  a  program  to  test  input  is  even  number  or  odd  number

a= eval(input('enter any number : ' )
print(f' Result : {'Even Number' if a%2==0 else 'Odd Number'}')








