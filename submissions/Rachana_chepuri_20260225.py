
# Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

# First  complex  number   --->  3 + 4j
# 2nd   complex  number   --->  5 + 6j
# What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
# What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
# What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
# What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
# 											=  (15 -18j + 20j + 24) /  (25 + 36)
a = eval(input("Enter first complex number: "))
b = eval(input("Enter second  complex number: "))
print(f'sum : {a+b}')
print(f'Difference : {a-b}')
print(f'product : {a*b}')
print(f'Division : {a/b}')

'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
length = eval(input('Enter the length of the rectangle: '))
breadth = eval(input('Enter the breadth of the rectangle: '))
print(f'Area: {length*breadth}')
print(f'perimeter: {2*(length+breadth)}')


'''
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
r = eval(input('Enter radius: '))
print(f'volume : {4 / 3  * 3.1415 *  r ** 3}')

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
p = eval(input('Enter principle: '))
t = eval(input('Enter time: '))
r = eval(input('Enter rate of interest: '))
print(f'Simple Interest : {p*t*r/100}')
print(f'Compound Interest : {p * (1  +  r  /  100) **  t  -  p} ')


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
x = eval(input('Enter 1st input: '))
y = eval(input('Enter 2nd input: '))
print(f'Before swap: {x=}       {y=}')
temp = x
x = y
y = temp
print(f'After swap: {x=}       {y=} ')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = eval(input('Enter 1st input: '))
y = eval(input('Enter 2nd input: '))
print(f'Before swap: {x=}       {y=}')
x = x+y
y = x-y
x = x-y
print(f'After swap: {x=}       {y=} ')
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = eval(input('Enter 1st input: '))
y = eval(input('Enter 2nd input: '))
print(f'Before swap: {x=}       {y=}')
x = x*y
y = x/y
x = x/y
print(f'After swap: {x=}       {y=} ')


# Identify  error
# else:
# 		print('else  suite') #if condition is missing
# print('Outside')
# # Identify  error
# if  9 > 5  # : is missing
# 	print('Hello')
# print('Bye')  
# # Identify  error
# if  9 > 12:
# 	print('Hyd')
# else # : is missing and : is mandatory after the condition
# 	print('Sec')
# # Identify  error
# if  (10,20,15):
# print('Hyd') #indetation error
# else:
# print('Sec')
# # Identify  error
# if  ():
# 			print('Hyd')
# 	else: #indetation error
# 					print('Sec')
# print('Bye')
# # Identify  error
# if  { }:
# {
# 	print('One') # {} are not allowed in conditionals
# 	print('Two')
# 	print('Three')
# }
# else:
# {
# 	print('Four')
# 	print('Five')
# 	print('Six')
# }
# print('Bye')
# # Identify  error
# if  ():
# 	print('One')
# 	print('Two')
# 	print('Three')
# else:
# if  []: # indetation erroe
# 	print('Four')
# 	print('Five')
# 	print('Six')
# else:
# if  {}:
# 	print('Seven')
# 	print('Eight')
# 	print('Nine')
# else:
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# print('Bye')

        
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
 
x = eval(input('EWnter a number: '))
if x%2==0:
    print("Even number")
if x%2!=0:
     print("Odd number")

# Find outputs  (Home  work)
# if():
#         print('Hyd')
#         print('Sec')
#         print('Cyb')
# else:
#         print('One')        #One
#         print('Two')        #Two
#         print('Three')      #Three
# print('Bye')                #Bye
# # Find  outputs  (Home  work)
# if{10 : 20 , 30 : 40}:
#         print('Hyd') #Hyd
#         print('Sec') #Sec
#         print('Cyb') #Cyb
# print('Bye')         #Bye
# # Find outputs  (Home  work)
# if { }:
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# print('Bye') #Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


        
         


try:
    month = eval(input("Enter month number (1-12): "))

    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
    else:
        print("Input should be between 1 and 12")

except ValueError:
    print("Input should be an integer")

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
digit = eval(input('Enter any digit: '))
if digit == 0:
    print("Zero")
else:
     if digit == 1:
        print("One")
     else:
         if digit == 2:
            print("Two")
         else :
            if digit == 3:
               print("Three")
            else:
                if digit == 4:
                   print("Four")
                else: 
                    if digit == 5:
                       print("Five")
                    else:
                        if digit == 6:
                           print("six")
                        else:
                            if digit == 7:
                               print("seven")
                            else:
                                if digit == 8:
                                   print("Eight")
                                else:
                                   print("Nine")


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
year = eval(input('Enter 4 digit: '))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year")
else:
    print("Not  a Leap Year")

# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

input_1=eval(input('Enter 1st input: '))
input_2=eval(input('Enter 2nd input: '))
input_3=eval(input('Enter 3rd input: '))
if input_1>input_2 and input_3:
    print('Largest Input: ', input_1)
else:
    if input_2>  input_3 and input_1:
        print('Largest Input: ', input_2)
    else:
        print('Largest Input: ', input_3)

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''


temp = eval(input('Enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius: '))
if temp==1:
    b = eval(input('Enter celsius  temperature: '))
    print(f'celsius equivalent : {(1.8 * b) + 32}')
elif temp == 2:
    c = eval(input('Enter farenheit   temperature: '))
    print(f'celsius equivalent : {(c - 32 )/ 1.8}')
else:
    print("Invalid input")

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
x =  eval(input('Enter values of x co-ordinate: '))
y =  eval(input('Enter values of y co-ordinate: '))
if x>0 and y>0:
    print('1st quadrant')
elif x>0 and y<0:
    print('4th quadrant')
elif x<0 and y>0:
    print('2nd qdrant')
elif x<0 and y<0:
    print('3rd quadrant')
elif x!=0 and y == 0:
    print('X-Axis')
elif x==0 and y!=0:
    print('Y-Axis')
else:
    print('Origin')

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

a = eval(input('Enter first number: '))
b = eval(input('Enter second number: '))
c = eval(input('Enter third number: '))
max = a
if max > b and c:
    max = a
    
if max < b and c:
    max = b
if max < c:
    max = c
print('Largest input: ',max)
min = a
if min < b and c:
    min = a
    
if min > b and c:
    min = b
if min > c:
    min = c
print('Smallest input: ',min)
print('Middle input: ',(a+b+c)-(max+min))