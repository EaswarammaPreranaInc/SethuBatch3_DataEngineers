'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61										   
'''


a = complex(input('Enter First complex number : '))
b = complex(input('Enter Second complex number : '))
print(f'sum : {a+b}')
print(f'Difference : {a-b}')
print(f'Product : {a*b}')
print(f'Division : {a/b}')



'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''



l = float(input('Enter Length of Rectangle :'))
w = float(input('Enter the Width of Rectangle : '))
area = l*w
perimeter = 2*(l+w)
print(f'Area : {area}')
print(f'Perimeter : {perimeter}')


'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''



r = float(input('Enter the Radius : '))
pi = 3.14159
volume = (4/3)*pi*r**3
print(f'Volume : {volume}')


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

p = float(input('Enter the Principle : '))
t = float(input('Enter the time : '))
r = float(input('Enter Rate of Interest'))
si = (p*t*r)/100
ci = p*(1+r/100)**t-p
print(f'Simple interest : {si}')
print(f'Compound interest : {ci}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

x = input('Enter 1st input : ')
y = input('Enter 2nd input : ')
print(f'Before swap : {x=}\t{y=}') 
temp = x 
x = y 
y = temp
print(f'After Swap : {x=}\t{y=}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''


x = int(input('Enter 1st input : '))
y = int(input('Enter 2nd input : '))
print(f'Before Swap : {x=}\t{y=}')
x = x + y #x = 25+10 = 35
y = x - y #35-10 = 25
x = x - y #35-25 = 10
print(f'After Swap : {x=}\t{y=}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

x = int(input('Enter 1st input : '))
y = int(input('Enter 2nd input : '))
print(f'Before Swap : {x=}\t{y=}')
x = x * y #x = 25*10 = 250
y = x / y #250/10 = 25
x = x / y #250/25 = 10
print(f'After Swap : {x=}\t{y=}')



# Identify  error
#else:    #we can't write else  statement without if statement
#	print('else  suite')
#print('Outside')


# Identify  error
#if  9 > 5    #colun (:) mandatory for if cond: statements 
#	print('Hello')
#print('Bye')

# Identify  error
#if  9 > 12:   
#	print('Hyd')
#else      #colun (:) mandatory for else: statements
#	print('Sec')

# Identify  error
#if  (10,20,15):  #After if cond: statement should be start with tab or space (indentation error)
#print('Hyd')
#else:
#print('Sec')


# Identify  error
#if  ():      #if and else must be on same indent (indentation error )
#	print('Hyd')
#	else:
#		print('Sec')
#print('Bye')


# Identify  error
#if  { }: #inside if condition Braces are not allowed 
#{
#	print('One')
#	print('Two')
#	print('Three')
#}
#else:
#{
#	print('Four')
#	print('Five')
#	print('Six')
#}




# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement


a = int(input('Enter 1st number : '))
if a%2==0:
    print(f'{a} is Even number ')
else:
    print(f'{a} is odd number ')



# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')  #One<next line > Two <nextline> Three <nextline> Bye <nextline>



# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') #Hyd <next line > Sec <nextline> Cyb <nextline> Bye <nextline>


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye 



# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


    
a = int(input('Enter Month Number (1-12) : '))
if a == 1:
    print('January')
elif a ==2:
    print('Febrary')
elif a ==3 :
    print('March')
elif a ==4 : 
    print('April')
elif a == 5:
    print('May')
elif a ==6 :
    print('June')
elif a == 7:
    print('July')
elif a == 8 :
    print('August')
elif a == 9:
    print('September')
elif a == 10 :
    print('October')
elif a == 11:
    print('November')
elif a == 12:
    print('December')


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''




a = int(input('Enter any Digit (0-9) : '))
if a == 0:
    print('Zer0')
else:
    if a == 1:
        print('One')
    else :
        if a == 2:
            print('Two')
        else:
            if a == 3 :
                print('Three')
            else:
                if a == 4:
                    print('four')
                else:
                    if a == 5:
                        print('Five')
                    else:
                        if a == 6:
                            print('Six')
                        else:
                            if a == 7 :
                                print('seven')
                            else:
                                if a == 8:
                                    print('Eight')
                                else:
                                    if a == 9:
                                        print('Nine')
                                    else:
                                        print('Invalid')



'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''


y = int(input('Enter any four digit number : '))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(f'{y} is Leap year')
else :
    print(f'{y} is not Leap year ')




'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = int(input('Enter 1st number : '))
b = int(input ('Enter 2nd number : '))
c = int(input('Enter 3rd number : '))

if a > b and a > c :
    print(f'{a} is largest number ')
else:
    if b > c:
        print(f'{b} is largest number ')
    else:
        print(f'{c} is largest number')



'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''



a = int(input('Enter 1 to convert celsius to ferhenheit and 2 to convert ferhenheit to celsius :'))  

if a == 1:
    temp = float(input('Enter celsius temperature : '))
    ferhenheit = 1.8 * temp +32
    print(f'ferhenheit equalent : {ferhenheit}')
else :
    if a == 2:
        temp1 = float(input('Enter Ferhenheit Temperature : '))
        celsius = (temp1  - 32) / 1.8
        print(f'celsius equalent : {celsius}')
    else :
        print(' Invalid input please enter 1 0r 2 only')

        



'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''

a = int(input('Enter value of x co-ordinate : '))
b = int(input('Enter value of y co-ordinate : '))

if a > 0 and b > 0 :
    print('1st quadrant')
elif a < 0 and b > 0:
    print('2nd quadrant')
elif a < 0 and b < 0 :
    print('3rd quadrant')
elif a > 0 and b < 0:
    print('4th quadrant')



'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program
'''



x = int(input('Enter 1st number : '))
y = int(input ('Enter 2nd number : '))
z = int(input('Enter 3rd number : '))
max = x
min = x
if y > max :
    max = y
elif z > max :
    max = z
if y < min :
    min = y
elif z < min :
    min = z
mid = (x+y+z) -(max+min)
print(f'{max = }')
print(f'{min = }')
print(f'{mid = }')
