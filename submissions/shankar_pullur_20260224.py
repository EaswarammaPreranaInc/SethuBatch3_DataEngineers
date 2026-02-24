def program():
    a = 'Hyd  is  green  city'
    print(a)                        #Hyd  is  green  city
    b = 'Hyd  is  "green"  city'   
    print(b)                        #Hyd  is  "green"  city
    c = 'Hyd  is  \'green\'  city'
    print(c)                       #  Hyd  is  'green'  city
    #print('Hyd  is  ' green  '  city')
    '''Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
    Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

    Hint:  Use  F  string  to  print  results'''

    #Let  inputs  be  10  and  7,
    x=eval(input("enter the first integer 1: "))
    y=eval(input("enter the first integer 2: "))

    #What  is  the  sum ?  --->  17 
    print(f'{x}+{y}={x+y}')
    #What  is  the  difference ?  --->  3
    print(f'{x}-{y}={x-y}')
    #What  is  the  product ?  --->  70
    print(f'{x}*{y}={x*y}')
    #What  is  the  quotient ?  --->  1.42
    print(f'{x}/{y}={x/y}')
    #What  is  the  remainder ?  ---> 3
    print(f'{x}%{y}={x%y}')
    #What  is  the  largest  number ?  --->  10
    print(f'max({x},{y})={max(x,y)}')

    #What  is  the  smallest  number ?  --->  7
    print(f'min({x},{y})={min(x,y)}')
    #What  is  the  sqrt  of  1st  input ?  --->  3.16
    import math
    print(f'sqrt({x})={math.sqrt(x)}')
    #What  is  the  result  of  power ?  --->  10000000
    print(f'pow({x},{y})={pow(x,y)}')
    #What  is  the  gcd  of  2  numbers ?  --->  1
    print(f'gcd({x},{y})={math.gcd(x,y)}')
    #What  is  the  factorial   of  1st  input ?  --->  10!
    print(f'factortial({x})={math.factorial(x)}')


    '''
    Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

    Let  'x'  be  25  and  'y'  be   'Hyd'
    What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

    Hint:  Swap  references  but  not  objects
    '''
    print("SWAP Problem")

    print(f'before swap: x={x}\ty={y}')
    x,y=y,x
    print(f'after swap: x={x}\ty={y}')

    print()
def largest():
    '''Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
    1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

    2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

    3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

    4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

    5) Inputs  can  be  integers , floats , strings  and  so  on

    6) Use  nested  ternary  operator'''

    #1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20
    a=eval(input("enter first  input:"))
    b=eval(input("enter second input:"))
    print('largest input: ',end="")
    print(f'{a}') if a>b else print(f'{b}')

#largest()

def largestAmong3():
     print('if string enter in single quotes')
     a=eval(input("enter first  input :"))
     b=eval(input("enter second input:"))
     c=eval(input("enter Third  input:"))
     print('largest input: ',end="")
     print(f'{a}') if a>b and a>c else print(f'{b}') if b>c else print(f'{c}')
#largestAmong3()


     

def symbol():
    print('if string enter in single quotes')
    a=eval(input("enter first  input:"))
    b=eval(input("enter second input:"))
    print('Result: ',end="")
    print(f'>') if a>b else print(f'=')if a==b else print(f'<')
#symbol()  


# even or odd 
def evenOrodd():
    a=int(input("enter the Positive number"))
    print('Even Number')if(a%2==0) else print('Odd Number')
#evenOrodd() 