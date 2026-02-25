'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)											=  39 / 61 + 2j / 61										   
'''



c1 = complex(input("Enter first complex number: "))
c2 = complex(input("Enter second complex number: "))
sum_result = c1 + c2
diff_result = c1 - c2
product_result = c1 * c2
division_result = c1 / c2
print("Sum :", sum_result)
print("Difference :", diff_result)
print("Product :", product_result)
print("Division :", division_result)


 '''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area :", format(area, ".2f"))
print("Perimeter :", format(perimeter, ".2f"))

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math
radius = float(input("Enter radius: "))
volume = (4/3) * math.pi * radius**3
print("Volume :", format(volume, ".2f"))

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

principal = float(input("Enter principal: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time : "))
simple_interest = (principal * rate * time) / 100
compound_interest = principal * ((1 + rate/100) ** time - 1)
print("Simple Interest :", format(simple_interest, ".2f"))
print("Compound Interest :", format(compound_interest, ".2f"))

'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''


x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f"Before swap: x='{x}' y='{y}'")
temp = x
x = y
y = temp
print(f"After swap: x='{x}' y='{y}'")

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print(f"Before swap: x='{x}' y='{y}'")
x = x + y
y = x - y
x = x - y
print(f"After swap: x='{x}' y='{y}'")


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = float(input("Enter 1st input: "))
y = float(input("Enter 2nd input: "))
print(f"Before swap: x='{x}' y='{y}'")
x = x * y
y = x / y
x = x / y
print(f"After swap: x='{x}' y='{y}'")

# Identify  error
'''else:
		print('else  suite')
print('Outside')'''
#Else without if  also indentation error

# Identify  error
'''
if  9 > 5
	print('Hello')
print('Bye')'''
# No colon at if statement

# Identify  error
'''
if  9 > 12:
	print('Hyd')
else
	print('Sec')'''
#no colon at else 


# Identify  error
'''
if  (10,20,15):
print('Hyd')
else:
print('Sec')'''
#Indentation Error


# Identify  error
'''
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')'''
#Indentation Error


# Identify  error
'''
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
}
print('Bye')'''
# {} are allowed only in set and dictionary


# Identify  error
'''
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
if  {}:#indentation error
	print('Seven')
	print('Eight')
	print('Nine')
else:#indentation error
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')'''

print("program  to  determine  a  number  is  even  or  odd  with   if  statement")
x=int(input("Enter input:"))
if(x%2==0):
    print("Even Number")
else:
    print("Odd Number")


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
'''output:
One
Two
Three
Bye'''

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
'''output:
Hyd
Sec
Cyb
Bye'''

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#output:Bye



# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
month = input("Enter month number (1-12): ")
if month.isdigit():
    month = int(month)
    if 1 <= month <= 12:
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
        print("Input should be between 1 and 12.")
else:
    print(" input should be an integer.")





print("a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif")
try:
    x=int(input("Enter input:"))
    if(x==0):
        print("Zero")
    else:
        if(x==1):
            print("One")
        else:
            if(x==2):
                print("two")
            else:
                if(x==3):
                    print("three")
                else:
                    if(x==4):
                        print("Four")
                    else:
                        if(x==5):
                            print("Five")
                        else:
                            if(x==6):
                                print("Six")
                            else:
                                if(x==7):
                                    print("Seven")
                                else:
                                    if(x==8):
                                        print("Eight")
                                    else:
                                        if(x==9):
                                            print("Night")
                                        else:
                                            print("invalid")
except ValueError:
    print("Input should be integer value")


print("program  to  test  year  is  leap  year  or  not")
year=int(input("Enter 4 digit year:"))
if(year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year")
else:
    print("Not a leap year")
                                
            
        
print("Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else")
x=int(input("Enter first input:"))
y=int(input("Enter second input:"))
z=int(input("Enter third input:"))
if(x>y and x>z):
    print(f"largest input:{x}")
elif(y>x and y>z):
    print(f"largest input:{y}")
else:
    print(f"largest input:{z}")


print("program  to  convert  celsius  temperature  to  farenheit  and  vice-versa")
a=int(input("Enter 1 to convert celsius to fahrenheit and 2 to convert fahreheit to celsius"))
if(a==1):
    c=float(input("Enter celsius temperature"))
    print(f"falrenheit equivalent:{1.8 * c + 32}")
elif(a==2):
    c=float(input("Enter fahrenheit temperature"))
    print(f"celsius equivalent:{(temp - 32) / 1.8}")


print("program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant")
x=int(input("Enter value of x-coordinate:"))
y=int(input("Enter value of y-coordinate:"))
if(x>0 and y>0):
    print("first quadrant")
elif(x<0 and y>0):
    print("second quadrant")
elif(x<0 and y<0):
    print("third quadrant")
elif(x>0 and y<0):
    print("fourth quadrant")
elif(x!=0 and y=0):
    print("x-axis")
elif(x=0 and y!=0):
    print("y-axis")


print(" program  to  determine  largest , smallest  and  middle  of  three  numbers")
x=float(input("Enter first input:"))
y=float(input("Enter second input:"))
z=float(input("Enter third input:"))
max_val=x
min_val=x
if y>max_val:
    max_val=y
if z>max_val:
    max_val=z
if y<min_val:
    min_val=y
if z< min_val:
    min_val=z
mid_val=(x+y+z)-(max_val+min_val)
print(f"Largest input:{max_val}")
print(f"Smallest input:{min_val}")
print(f"Middle input:{mid_val}")    
