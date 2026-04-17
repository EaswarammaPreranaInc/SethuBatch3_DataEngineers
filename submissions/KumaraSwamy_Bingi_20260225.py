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
#program:

a = complex(input('Enter 1st complex number: ')) #Enter 1st complex number: 3 + 4j
b = complex(input('Enter 2nd complex number: ')) #Enter 2nd complex number: 5 + 6j
print('sum is: ', a + b) #sum is:  (8+10j)
print('difference is: ', a - b) #difference is:  (-2-2j)
print('product is: ', a * b) #product is:  (-9+38j)
print('division is: ', a / b) #division is:  (0.3934426229508197+0.03278688524590164j)






'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
#program:

length = float(input('Enter length of rectangle: ')) #Enter length of rectangle: 4  
breadth = float(input('Enter breadth of rectangle: ')) #Enter breadth of rectangle: 5
area = length * breadth
perimeter = 2 * (length + breadth)
print('Area is: ', area) #Area is:  20.0
print('Perimeter is: ', perimeter) #Perimeter of rectangle is:  18.0






'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
#program:
import math
radius = float(input('Enter radius: ')) #Enter radius: 3.5
volume = 4 / 3 * math.pi * radius ** 3
print('Volume is: ', volume) #Volume is: 179.59438003021647







'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
#program:

principle = float(input('Enter principle: ')) #Enter principle: 10000
time = float(input('Enter time:')) #Enter time: 3
rate = float(input('Enter rate of interest: ')) #Enter rate of interest: 7.5
simple_interest = principle * time * rate / 100
compound_interest = principle * (1 + rate / 100) ** time - principle
print('Simple interest: ', simple_interest) #Simple interest:  2250.0
print('Compound interest: ', compound_interest) #Compound interest:  2421.875





'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

#program:

x = input('Enter 1st input: ') #Enter 1st input: 10
y = input('Enter 2nd input: ') #Enter 2nd input: Hyd
print('Before swap: ', x, y) #Before swap:  10 Hyd
temp = x
x = y
y = temp

print('After swap: ', x, y) #After swap:  Hyd 10








'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
#program:

x = int(input('Enter 1st number: ')) #Enter 1st number: 25
y = int(input('Enter 2nd number: ')) #Enter 2nd number: 10
x = x + y
y = x - y
x = x - y
print('After swap: ', x, y) #After swap:  10 25






'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
#program:

x = int(input('Enter 1st number: ')) #Enter 1st number: 25
y = int(input('Enter 2nd number: ')) #Enter 2nd number: 10
x = x * y
y = x // y
x = x // y
print('After swap: ', x, y) #After swap:  10 25



# Identify  error
else:
		print('else  suite')
print('Outside') #IndentationError



# Identify  error
if  9 > 5                    # : is  missing
	print('Hello')
print('Bye')




# Identify  error
if  9 > 12:
	print('Hyd')
else                    # : is  missing
	print('Sec')



# Identify  error
if  ():
			print('Hyd')
	else:                      #IndentationError
					print('Sec')     
print('Bye')



# Identify  error
if  { }:   
{              # indentationError
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
if  []:            #IndentationError
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:             #IndentationError
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')




# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

n = int(input('Enter a number: ')) #Enter a number: 10
if n % 2 == 0:
	print('Even number')
else:
	print('Odd number')
	

# Find outputs  (Home  work)
if():                               #False
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                               #Executed
        print('One')
        print('Two')
        print('Three')
print('Bye')


'''
output of above code is:
-------------------------
One
Two
Three
Bye

'''



# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:       #True
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')


'''
output of above code is:
-------------------------
Hyd
Sec
Cyb
Bye

'''


# Find outputs  (Home  work)
if { }:               #False
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')             #Executed


'''
output of above code is:
-------------------------
Bye

'''













# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
  month_number = int(input('Enter month number (1 - 12): ')) #Enter month number: 5
  
  if month_number > 12 or month_number < 1:
    print('Input should be between 1 and 12')

  elif month_number == 1:
    print('January')
  elif month_number == 2:
    print('February')
  elif month_number == 3:
    print('March')    
    
  elif month_number == 4:
    print('April')
    
  elif month_number == 5:
    print('May')
  elif month_number == 6:
    print('June')
  elif month_number == 7:
    print('July')
  elif month_number == 8:
    print('August')
  elif month_number == 9:
    print('September')
  elif month_number == 10:
    print('October')
  elif month_number == 11:
    print('November')
  elif month_number == 12:
    print('December')
  else:
    print('Invalid month number')

except ValueError:
  print('input should be an integer')














'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

x = int(input('Enter any digit (0-9): ')) #Enter any digit (0-9): 3

if x == 0:
  print('Zero')
else:
  if x == 1:
    print('One')
  else:
    if x == 2:
      print('Two')
    else:
      if x == 3:
        print('Three')
      else:
        if x == 4:
          print('Four')
        else:
          if x == 5:
            print('Five')
          else:
            if x == 6:
              print('Six')
            else:
              if x == 7:
                print('Seven')
              else:
                if x == 8:
                  print('Eight')
                else:
                  if x == 9:
                    print('Nine')
                  else:
                    print('Invalid digit')











'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''


#program:

year = int(input('Enter 4-digit year: ')) #Enter 4-digit year: 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('leap year')
else:
    print('not a leap year')



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

#program:
a = int(input('Enter 1st number: ')) #Enter 1st number: 10
b = int(input('Enter 2nd number: ')) #Enter 2nd number: 20
c = int(input('Enter 3rd number: ')) #Enter 3rd number: 15
if a >= b and a >= c:
    print('Largest number is: ', a) #Largest number is:  10 
elif b >= a and b >= c:
    print('Largest number is: ', b) #Largest number is:  20
else:
    print('Largest number is: ', c) #Largest number is:  15









'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

#program:

temp = float(input('Enter 1 to convert celsius to farenheit, 2 to convert farenheit to celsius: ')) #Enter temperature: 100

if temp == 1:
  celsius = float(input('Enter celsius temperature: '))
  farenheit = (celsius * 1.8) + 32
  print('farenheit equivalent: ', farenheit)
elif temp == 2:
  farenheit = float(input('Enter faurenheit temperature: '))
  celsius = (farenheit - 32) / 1.8
  print('celsius equivalent: ', celsius)
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

#program:
x = float(input('Enter value of x coordinate: ')) #Enter value of x coordinate: 0
y = float(input('Enter value of  y coordinate: ')) #Enter value of  y coordinate: 0

if x > 0 and y > 0:
    print('1st quadrant')   

elif x < 0 and y > 0:
    print('2nd quadrant')

elif x < 0 and y < 0:
    print('3rd quadrant')

elif x > 0 and y < 0:
    print('4th quadrant')

elif x != 0 and y == 0:
    print('Point lies on x-axis')

elif x == 0 and y != 0:
    print('Point lies on y-axis')

elif x == 0 and y == 0:
    print('Point lies at origin')

else:
    print('Invalid input')  












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


#program:
a = float(input('Enter 1st number: ')) 
b = float(input('Enter 2nd number: ')) 
c = float(input('Enter 3rd number: ')) 
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
print('Largest input:', max)
print('Smallest input:', min)
print('Middle input:', mid)    





