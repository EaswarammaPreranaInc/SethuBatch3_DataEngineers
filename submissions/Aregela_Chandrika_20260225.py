'''Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61										   
'''

Enter first complex number: 3+4j
Enter second complex number: 5+6j
 sum = (8+10j)
 difference = (-2-2j)
 product = (-9+38j)
 division = (0.6393442622950819+0.03278688524590165j
 
 '''
 Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

l = float(input("Enter length of rectangle : "))
b = float(input("Enter breath of rectangle : "))
print(F' area = {l * b}' )
print(F' perimeter = {2*(l+b)}' )



'''
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r = float(input("Enter radius : "))
print(F' volume = {4 / 3  * math. pi *  r ** 3:.2f}' )

'''
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p '''

p = int(input("Enter principle : "))
t = int(input("Enter time : "))
r = float(input("Enter rate of intrest : "))
print(f'Simple Intrest : {(p*t*r / 100)}')
print(f'Compound  Intrest : {p*(1+r/100)**t-p:.2f}')

'''Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
print(f'Before swap : {a=} \t {b=}')
temp = a
a = b
b = temp
print(f'After swap : {a=} \t {b=}')


'''Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
print(f'Before swap : {a=} \t {b=}')
a = a + b # 25 + 10 = 35
b = a - b # 35 - 10 = 25
a = a - b # 35 - 25 = 10
print(f'After swap : {a=} \t {b=}')


'''Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10 '''

a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
print(f'Before swap : {a=} \t {b=}')
a = a * b # 25 * 10 = 250
b = a // b # 250//10 = 25
a = a // b # 250//25 = 10
print(f'After swap : {a=} \t {b=}')


# Identify  error
else:
		print('else  suite')
print('Outside') # SyntaxError: invalid syntax



# Identify  error
if  9 > 5
	print('Hello')
print('Bye') #SyntaxError : expected ':'



# Identify  error
if  9 > 12:
	print('Hyd')
else                # SyntaxError : expected ':'
	print('Sec')
    


# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') # IndentationError: expected an indented block after'if' statement on line


# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')  # IndentationError : unindent does not match any outer indentation level




# Identify  error
if  { }:
{                       # IndentationError: expected an indented block after'if' statement on line
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')



# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:      # IndentationError: expected an indented block after'else' statement on line
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')



# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

num = float(input("Enter a number : "))
if(num%2==0):
    print("Even Number")
else:
        print("Odd Number")




# Find outputs  (Home  work)
if():
        print('Hyd') 
        print('Sec')
        print('Cyb')
else:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
print('Bye')            # Bye
    


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') # Hyd
        print('Sec') # Sec
        print('Cyb') # Cyb
print('Bye')         # Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye



# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    month = int(input("Enter month number (1-12) : "))
    if month == 1:
        print('January')
    elif month == 2:
        print('February')
    elif month == 3:
        print('March')
    elif month == 4:
        print('April')
    elif month == 5:
        print('May')
    elif month == 6:
        print('June')
    elif month == 7:
        print('July')
    elif month == 8:
        print('August')
    elif month == 9:
        print('September')
    elif month == 10:
        print('October')
    elif month == 11:
        print('November')
    elif month == 12:
        print('December')
    else:
        print('Input should be between 1 and 12')
except:
    print(" Input should be integer")

    


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

digit = int(input("Enter any digit (0-9) : "))
if digit == 0:
    print("Zero")
else:
    if digit == 1:
        print("One")
    else:
         if digit == 2:
             print("Two")
         else:
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
                                   print("Six")
                               else:
                                     if digit == 7:
                                         print("Seven")
                                     else:
                                           if digit == 8:
                                               print("Eight")
                                           else:
                                                if digit == 9:
                                                    print("Nine")
                                                else:
                                                    print("Invalid")
        
 
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nt Number : "))
c = int(input("Enter 3rd Number : "))
if a > b and a > c:
    print(f' Largest Number : {a}')
else:
    if b > a and b > c:
        print(f'Largest Number : {b}')
    else:
         print(f'Largest Number : {c}')
        





'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

select = int(input("Enter 1 to  convert  celsius  to  farenheit and to  convert  farenheit  to  celsius  :"))
if select == 1:
    c = int(input("Enter celsius temperature : "))
    print(f' farenheit temperature : {1.8 * c + 32}')
else:
    if select ==2:
        f = int(input("Enter farenheit temperature : "))
        print(f'celsius temperature : {1.8 * f + 32}')
    else:
        print("Invalid")
        
    


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
x = eval(input("Enter value of x co-ordinate : "))
y = eval(input("Enter value of y co-ordinate : "))
if x>0 and y>0:
    print("1st quadrant ")
else:
    if x<0 and y>0:
        print("2nd quadrant ")
    else:
        if x<0 and y<0:
            print("3rd quadrant ")
        else:
            print("4st quadrant ")
        


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
a = int(input("Enter First input  : "))
b = int(input("Enter Second input : "))
c = int(input("Enter Third input  : "))

max = a

if b > max:
    max = b
if c > max:
    max = c


min = a
if b < min:
    min = b
if c < min:
    min = c


mid = (a + b + c) - (max + min)
print(f'{max :}')
print(f'{min :}')
print(f'{mid :}')


    
