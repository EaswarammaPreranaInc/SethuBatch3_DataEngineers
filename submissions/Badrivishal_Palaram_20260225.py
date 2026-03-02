'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)=  (15 -18j + 20j + 24) /  (25 + 36)=  39 / 61 + 2j / 61							   
'''
x=eval(input('enter first complex number:'))
y=eval(input('enter second complex number:'))

sum = x+y 
print(f"sum : {sum}")

difference = x-y 
print(f"difference : {difference}")

product= x*y
print(f"product : {product}")

division = x/y
print(f"division:{division}")

	

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth
2) What  are  the  outputs  ?  ---> area  and  perimeter
3) What  is  the  area  of  rectangle  ?  ---> length * breadth
4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

'''


L=float(input("enter length of rectangle:"))
B=float(input("enter Breadth of rectangle:"))

Area = L*B
print(f"Area : {Area}")

Perimeter= 2*(L+B)
print(f"Perimeter : {Perimeter}")




'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius
2) What  is  the  output ?  ---> volume
3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''


import math
r=float(input("enter radius:"))
Volume = 4/3 * math.pi * r**3
print(f"Volume:{Volume}")



'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest
2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest
3) What  is  simple  interest  formula ?  --->  ptr / 100
4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

p=float(input("enter principle:"))
t=float(input("enter time:"))
r=float(input("enter rate of interest:"))

Simple_Interest = ptr/100
Compound_Interest = p * (1  +  r  /  100) **  t  -  p

print(f"Simple_Interest : {Simple_Interest}")
print(f"Compound_Interest : {Compound_Interest}")



'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''


x=input("Enter 1st number:")
y=input("Enter 2nd number:")

print(f"Before swap:x={x}   x={y}")

z = x
x=y
y=z


print(f"After swap:x={x}   x={y}")




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = 25
y =  10

x=x+y
y=x-y
x=x-y

print("x:",x)
print("y:",y)



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = 25
y =  10

x=x*y
y=x/y
x=x/y

print("x:",x)
print("y:",y)



# Identify  error
else:
		print('else  suite')
print('Outside')

#Output: Error no if stmt and Indentation error



# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

#Output:Type error , ":" is missing at end of 'if' statement




# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

#Output:Type error , ":" is missing at end of 'else' statement


# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

#Output:Indentation error , "<tab> space" is missing next line after if stmt



# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

#Output:Indentation error ,'if' and 'else' starting from diff block



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
}
print('Bye')

#Output:Type error , "()" is expected for condition in 'if' statement


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
	print('Cyb')
print('Bye')

#Output:Indentation error ,'if' expects indentation after 'else'  at line 6






# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
    month=int(input("Enter month number:"))
    if month < 1 or month > 12:
        print("Input should be between 1 and 12")
    elif month==1:
    	print("January")
    elif month==2:
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
        
except ValueError:
    print("Input should be between 1-12")
    



'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

digit = int(input("Enter a digit (0-9): "))

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


x=int(input("Enter 4-digit Year:"))
if x%4==0 or x % 4 == 0 and x % 100 != 0):
	print("leap year")
else:
	print("not leap year") 



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))
z=int(input("enter 3rd number:"))

if x>y and x>z:
	print("x is largest")
elif y>z and y>x:
	print("y is largest")
else:
	print("z is largest")


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

choice=int(input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius:"))

if choice == 1 :
	C=float(input("Enter Temperature in Celsius:"))
	F=(C * 9/5) + 32 
	print(f"Equivalent temparature in Fahrenheit is: {F}")
	
elif choice == 2 :
	F=float(input("Enter Temperature in Fahrenheit:"))
	C=(F-32) *5/9
	print(f"Equivalent temparature in Celsius is: {C}")
	
else:
	print("Invalid Choice")


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

x = float(input("Enter value of x co-ordinate: "))
y = float(input("Enter value of y co-ordinate: "))

if x > 0 and y > 0:
    print("1st Quadrant")

elif x < 0 and y > 0:
    print("2nd Quadrant")

elif x < 0 and y < 0:
    print("3rd Quadrant")

elif x > 0 and y < 0:
    print("4th Quadrant")

elif x == 0 and y == 0:
    print("Origin")

elif x == 0:
    print("Y-axis")

elif y == 0:
    print("X-axis")



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

a=float(input("Enter first input:"))
b=float(input("Enter second input:"))
c=float(input("Enter third input:"))

if a>b and a>c:
	largest = a
elif b>a and b>c:
	largest = b
else:
	largest = c 


if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c


middle = a + b + c - largest - smallest


print(f"Largest input  : {largest}")
print(f"Smallest input : {smallest}")
print(f"Middle input   : {middle}")



