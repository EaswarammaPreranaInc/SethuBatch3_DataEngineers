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


a = eval(input("Enter first complex number : "))
b = eval(input("Enter second complex number : "))

print(f'sum = {a+b}')
print(f'Difference = {a-b}')
print(f'Product = {a*b}')
print(f'Divison = {a/b}')

      
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

try:
    a = float(input("Enter length of rectangle : "))
    b  = float(input("Enter breath of rectangle : "))
    print(f'Area = {a*b}')
    print(f'Perimeter = {2*(a+b)}')
except:
    print("enter only integer or float numbers")

import math

a = float(input("Enter radius : "))
print(" Volume = ", 4/3*3.14159265359*a**3)

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

try:
    p = float(input("Enter principle = "))
    t = float(input("Enter time = "))
    i = float(input("Enter rate of interest = "))
    print("Simple interest : ",(p*t*i)/100)
    print("Compound Intrests : ", p * (1+i/100) ** t-p)
except:
    print("Don't enter string values only integers or floats")
    


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

a = input("Enter 1st input = ")
b = input("Enter 2nd input = ")
print("Before swapping values : ", a , b)
temp = a
a = b
b = temp

print("After swapping values : ",a,b)



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''


a = input("Enter 1st input : ")
b = input("Enter 2nd input : ")
print(a,b)
a = a+b
b = b-a
a = a-b
print(a,b)


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''



'''# Identify  error
else:
		print('else  suite')#without if block we cannot right else
print('Outside') #


# Identify  error
if  9 > 5 #No (:) colon is specified here. it gives Error.
	print('Hello')
print('Bye')


# Identify  error
if  9 > 12: #False goes to else.
	print('Hyd')
else    #No (:) colon is specified here it gives Error
	print('Sec')


	
# Identify  error
if  (10,20,15): #everything is right 
print('Hyd') # After (:) No indentation is specified here so it gives Error
else:
print('Sec')# After (:) No indentation is specified here so it gives Error


# Identify  error
if  ():
			print('Hyd')
	else:  #else is not in the same line as if so it gives error. here
					print('Sec')
print('Bye')


# Identify  error
if  { }: #Everything is fine the {} it's an empty dict gives false.
{
	print('One')
	print('Two')
	print('Three')
}
else: #In python we don't use curly braces in if and else statement so it gives Error.
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
if  []: #it gives indentatio Error. After (:) colon need to specify space.
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:#it gives indentatio Error. After (:) colon need to specify space.
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a = int(input("Enter a number to check whether Even or Odd number = "))

if(a % 2 == 0):
    print(f' it\'s is an Even :{a}')
else:
    print(f'it\'s is an Odd : {a}')
    
'''


# Find outputs  (Home  work)
if(): # it will skiped because no condition is specified  
        print('Hyd')
        print('Sec')
        print('Cyb')
else: # Else block is executed 
        print('One')
        print('Two')
        print('Three')
print('Bye')

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:  # it is True so the statments of if block is executed.
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')


# Find outputs  (Home  work)
if { }: # Empty dict with space is True so the if statments are executed.
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') 


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


try:
    a = int(input("Enter month number (1-12) : "))
    if(a == 1):
        print("January")
    elif(a == 2):
        print("Febuary")
    elif(a == 3):
        print("March")
    elif(a == 4):
        print("April")
    elif(a == 5):
        print("May")
    elif( a == 6):
        print("June")
    elif(a == 7):
        print("July")
    elif(a == 8):
        print("August")
    elif(a == 9):
        print("September")
    elif(a == 10):
        print("October")
    elif(a == 11):
        print("November")
    elif(a == 12):
        print("December")
    elif(a >12):
        print("Enter a number (1-12)")    
except ValueError:
    print("Enter a valid number")

    
    


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

a = int(input("Enter any digit (0-9):"))

if(a == 0):
    print("Zero")
else:
    if(a==1):
        print("One")
    else:
        if(a==2):
            print("Two")
        else:
            if(a==3):
                print("Three")
            else:
                if(a==4):
                    print("Four")
                else:
                    if(a==5):
                        print("Five")
                    else:
                        if(a==6):
                            print("Six")
                        else:
                            if(a==7):
                                print("Seven")
                            else:
                                if(a==8):
                                    print("Eight")
                                else:
                                    if(a==9):
                                        print("Nine")
                                    
                                


 
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''


a = int(input("Enter 4-digit year : "))

if(a %4 ==0 and a% 100 !=0) or ( a %400==0):
    print("Leap year")
else:
    print("Not a Leap year")



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))


if(a>b):
    if(a>c):
        print(f'Biggest is = {a}')
else:
    if(b>c):
        print(f'Biggest is = {b}')
    else:
        if(c>a):
            print(f'Biggest is = {c}')

    
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

a = int(input("Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : "))
if(a == 1):
    b = int( input("Enter fahrenheit temperature : "))
    result = (b*5/9)+32
    print(f'Celsius equivalent : {result}')
if(a == 2):
    c = int(input("Enter celsius temperature :"))
    Result = (c-32)*5/9
    print(f'Fahrenheit Equivalent : {Result} ')

if(a>2):
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

a = int(input("Enter value of X co-ordinate : "))
b = int(input("Enter value of Y co-ordinate : "))

if(a > 0 and b >0):
    print("1st quadrant")
elif( a < 0 and b > 0):
    print("2nd quadrant")
elif( a < 0 and b < 0):
    print("3rd quadrant")
elif(a >0 and b < 0):
    print("4th quadrant")
elif(a != 0 and b ==0 ):
    print("X - axis")
elif( a ==0 and b != 0):
    print("Y - axis")
else:
    print("Origin")



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
    
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

max = a
if(b>max):
    max = b
    
    
    
    
    
    
    























