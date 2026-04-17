import math

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

a = eval(input('Enter 1st complex number :'))  #3 + 4j
b = eval(input('Enter 2nd complex number :'))  #5 + 6j
print(f'Sum : {a + b}')  #8 + 10j
print(f'Difference : {a - b}')  #-2-j
print(f'Product : {a * b}')  #(-9+38j)  (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
print(f'Division : {a / b}')  #(0.6393442622950819+0.03278688524590165j)


#=====================================================================================================

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

l = eval(input('Enter length of rectangle :'))  #4
b = eval(input('Enter breadth of rectangle :'))  #5
print(f'Area : {l * b}')  #20
print(f'perimeter : {2 * (l+b)}')  #18


#========================================================================================================


'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

r = eval(input('Enter radius :'))
print(f'Volume : {4/3 * math.pi * r ** 3}')  #179.594

#==========================================================================================================


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

p = eval(input('Enter principal :'))  #10000
t = eval(input('Enter time :'))  #3
r = eval(input('Enter rate of interest :'))  #7.5
print(f'Simple interest : {p * t * r / 100}')  #2250.0
print(f'Compound interest : {p * (1 + r / 100) ** t - p}')  #2422.968

#==========================================================================================================


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

x = eval(input('Enter 1st input :'))  #25
y = eval(input('Enter 2nd inout :'))  #Hyd
temp = x
x = y
y = temp
print('Before swap : x = 25         y = Hyd')
print(f'After swap : x = {x}        y = {y}')  #x = Hyd     y = 25

#=============================================================================================================


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y = 10
'''

#=============================================================================================================


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

#=============================================================================================================
'''
 Identify  error
else:
	print('else  suite')  #without using if condition not possible to print else condition
print('Outside')
'''
#==============================================================================================================
'''
 Identify  error
if  9 > 5    # ':' colun is not there, it gives error
	print('Hello')
print('Bye')
'''
#==============================================================================================================
'''
 Identify  error
if  9 > 12:
	print('Hyd')
else              # ':' colun is not there, it gives error
	print('Sec')
'''
#==============================================================================================================
'''
 Identify  error
if  (10,20,15):
print('Hyd')   #indentation is missing
else:
print('Sec')   #indentation is missing
'''
#==============================================================================================================
'''
# Identify  error
if  ():
			print('Hyd')
	else:                     #else indentation was missing
					print('Sec')
print('Bye')
'''
#==============================================================================================================

'''
Identify  error
if  { }:
{                             # { paranthasis is not used in python
	print('One')
	print('Two')
	print('Three')
}
else:
{                             # { paranthasis is not used in python
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')
'''

#==============================================================================================================

'''
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:                   #error because there is no else statement
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
	print('Cyb')
print('Bye')
'''

#=============================================================================================================

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a = eval(input('Enter a number :'))  #28
if a % 2 == 0:
    print('Even numnber')   #even number
else:
    print('Odd number')
    
#=============================================================================================================

# Find outputs  (Home  work)
if():
        print('Hyd')    #if condition statements are not excuted becoz there is no condition so, else excuted
        print('Sec')
        print('Cyb')
else:
        print('One')    #One
        print('Two')    #Two
        print('Three')  #Three
print('Bye')            #Bye

#=============================================================================================================

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:        # if condition statements are printed becoz there is conditional arguments
        print('Hyd')   #Hyd
        print('Sec')   #Sec
        print('Cyb')   #Cyb
print('Bye')           #Bye

#=============================================================================================================

# Find outputs  (Home  work)
if { }:             #outside condition statement is printed becoz there is no if condition arguments
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')           #Bye

#=============================================================================================================

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

month = eval(input('Enter month number (1 - 12) : '))
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
    print('Septembar')
elif month == 10:
    print('October')
elif month == 11:
    print('November')
elif month == 12:
    print('December')
else:
    print('Invalid should be between 1 - 12')
    
#==============================================================================================================

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

a = eval(input('enter any digit(0 - 9) :'))
if a == 0:
    print('zero')
if a == 1:
    print('one')
if a == 2:
    print('Two')
if a == 3:
    print('three')
if a == 4:
    print('four')
if a == 5:
    print('five')
if a == 6:
    print('six')
if a == 7:
    print('seven')
if a == 8:
    print('eight')
if a == 9:
    print('nine')
if a > 9:
    print('Invalid')

#==============================================================================================================

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

year = eval(input('Enter 4-digit year : '))
if year % 4 == 0 or  year % 400 == 0:
    print('Leap Year')
elif year % 100 == 0:
    print('Not a Leap year')
    

    
year = int(input("Enter 4-digit year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
#==============================================================================================================

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = eval(input('Enter 1st input : '))  #100
b = eval(input('Enter 2nd input : '))  #300
c = eval(input('Enter 3rd input : '))  #200
if a > b and a > c:
    print(f'Largest number : {a = }') 
if b > c:
    print(f'Largest number : {b = }')  # b = 300
else:
    print(f'Largest number : {c = }')  
    
#==============================================================================================================

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

a = eval(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if a == 1:
    tempreture = eval(input('Enter celsius tempreture : '))
    print(f'Fahrenheit equivalent : {1.8 * tempreture + 32 }')
elif a == 2:
    tempreture = eval(input('Enter Fahrenheit tempreture : '))
    print(f'Celsius equivalent : {(tempreture - 32) / 1.8}')
elif a != 1 or 2:
    print('Invalid input')
    
#==============================================================================================================

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

x = eval(input('Enter value of x-coordinate : '))  #1
y = eval(input('Enter value of y-coordinate : '))  #2

if x>0 and y>0:
    print('1st Quadrant')   #1st Quadrant
elif x<0 and y>0:
    print('2nd Quadrant')
elif x<0 and y<0:
    print('3rd Quadrant')
elif x>0 and y<0:
    print('4th Quadrant')

#==============================================================================================================

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

a = int(input("Enter first input: "))  #10
b = int(input("Enter second input: ")) #20
c = int(input("Enter third input: "))  #7

# Step 1: Assume a is max and min
max = a
min = a

# Step 2: Find maximum
if b > max:
    max = b
if c > max:
    max = c

# Step 3: Find minimum
if b < min:
    min = b
if c < min:
    min = c

# Step 4: Find middle
mid = (a + b + c) - (max + min)

print("Largest input =", max)  #20
print("Smallest input =", min) #7
print("Middle input =", mid)   #10

