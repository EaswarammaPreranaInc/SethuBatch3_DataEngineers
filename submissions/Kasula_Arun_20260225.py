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

a = complex(input("Enter first complex number : "))
b  = complex(input("Enter second complex number: "))

print(f"Sum :  {a + b}")
print(f"Difference :  {a - b}")
print(f"Product:  {c1 * c2}")
print(f"Division :  {c1 / c2}")

input("Press any key to continue . . .")




'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''    



# Program to find area and perimeter of rectangle

l = float(input('Enter length of rectangle  : '))
b = float(input('Enter breadth of rectangle : '))

area = l * b
perimeter = 2 * (l + b)

print(f'Area  :  {area:.2f}')
print(f'Perimeter  :  {perimeter:.2f}')




'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
''' 

import math
r = float(input('Enter  radius  :  '))
v= (4/3) * math.pi * (r ** 3)
print(f'Volume  :  {v:.2f}')



'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''


# Program to determine Simple Interest and Compound Interest

p = float(input('Enter  principle  :  '))
t = float(input('Enter  time  :  '))
r = float(input('Enter  rate  of  interest  :  '))
si = (p * t * r) / 100
ci = p * ((1 + r / 100) ** t) - p
print(f'Simple  Interest  :  {si:.2f}')
print(f'Compound  Interest  :  {ci:.2f}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''


x = input('Enter  1st  input  :  ')
y = input('Enter  2nd  input  :  ')
print(f'Before  swap  : {x=} \t  {y=}')

temp = x
x = y
y = temp
print(f'After  swap  :  {x=} \t  {y=}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''



x = float(input('Enter 1st number : '))
y = float(input('Enter 2nd number : '))
print(f'Before  swap  : {x = } \t {y = }')

x = x + y
y = x - y
x = x - y
print(f'After   swap  : {x = }  \t {y = }')



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

x = int(input('Enter 1st number : '))
y = int(input('Enter 2nd number : '))
print(f'Before  swap  : {x = } \t {y = }')

x = x * y
y = x / y
x = x / y
print(f'After   swap  : x = {int(x)} \t y = {int(y)}')





# Identify  error
else:
		print('else  suite')
print('Outside')
                              #there is no if statement


# Identify  error
if  9 > 5
	print('Hello')
print('Bye')           
                           # ':' is missing after if statement


                           
 # Identify  error
if  9 > 12:
	print('Hyd')
else                          #':' is missing after else statement
    print('Sec')



# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')             #indentation is missing here



# Identify  error
if  ():                               #condition is empty
			print('Hyd')
	else:                             #not indented with if
					print('Sec')
print('Bye')




 # Identify  error
if  { }:      
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}                                    #{} are not permitted in python
print('Bye')





# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
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
	print('Cyb')       #there are no conditions in if and else statements
print('Bye')
 
 ''' 
 Write  a  program  to  determine  a  
 number  is  even  or  odd  with   if  statement
 '''

a = int (input('Enter a +ve number :'))

if a%2==0:
    print('Even number')
else:
	print('Odd number')




 # Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
'''
 One
Two
Three
Bye
	   
'''
# Find  outputs  (Home  work)
if {10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
'''
Hyd
Sec
Cyb
Bye

'''


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')                  #Bye              




'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

a = int(input('Enter any digit (0 - 9): '))

if a == 0:
    print('Zero')
else:
    if a == 1:
        print('One')
    else:
        if a == 2:
            print('Two')
        else:
            if a == 3:
                print('Three')
            else:
                if a == 4:
                    print('Four')
                else:
                    if a == 5:
                        print('Five')
                    else:
                        if a == 6:
                            print('Six')
                        else:
                            if a== 7:
                                print('Seven')
                            else:
                                if a == 8:
                                    print('Eight')
                                else:
                                    if any == 9:
                                        print('Nine')
                                    else:
                                        print('Invalid')



'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

a=int (input ('Enter a 4-digit year : '))
if (a%4 == 0 and a%100 != 0 ) or (a % 400 == 0):
    print ('Leap year')
else:
    print ('Not a leap year')



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

if a > b:
    if a > c:
        print('Largest is:', a)
    else:
        print('Largest is:', c)
else:
    if b > c:
        print('Largest is:', b)
    else:
        print('Largest is:', c)


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''



print('Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : ', end = "")
x = int(input())

if x == 1:
    temp= float(input('Enter celsius temperature : '))
    farenheit = 1.8 * temp + 32
    print('Fahrenheit Equivalent :', round(farenheit, 2))

else:
    if x == 2:
        temp = float(input('Enter fahrenheit temperature : '))
        celsius= (temp - 32) / 1.8
        print('celsius equivalent :', round(celsius, 2))
    else:
        print('Invalid input')
      



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

x = float(input('Enter value of x co-ordinate : '))
y = float(input('Enter value of y co-ordinate : '))

if x == 0 and y == 0:
    print('Origin')
elif x == 0:
    print('y-axis')
elif y == 0:
    print('x-axis')
elif x > 0 and y > 0:
    print('1st quadrant')
elif x < 0 and y > 0:
    print('2nd quadrant')
elif x < 0 and y < 0:
    print('3rd quadrant')
elif x > 0 and y < 0:
    print('4th quadrant')








# Taking three inputs from the user
a = float(input('Enter first input  : '))
b = float(input('Enter second input : '))
c = float(input('Enter third input  : '))
max_val = a
min_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
mid_val = (a + b + c) - (max_val + min_val)

print(f'Largest input  : {max_val}')
print(f'Smallest input : {min_val}')
print(f'Middle input   : {mid_val}')    