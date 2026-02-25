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
Program				   
'''
a=complex(input("Enter 1st complex number:"))
b=complex(input('Enter 2nd complex number:'))
print(F'{a}+{b}={a+b}')
print(F'{a}-{b}={a-b}')
print(F'{a}*{b}={a*b}')
print(F'{a}/{b}={a/b}')

 '''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l=float(input("Enter lenght of the rectangle:"))
b=float(input('Enter breadth of the rectangle:'))
print("Area of the Rectangle=",(l*b))
print('Perimeter=',(2*(l+b)))


 '''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r=float(input("Enter radius:"))
print("volume=",(4/3)*math.pi*r**3)



 (Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
#Program:

Enter principle:10000
Enter time:3
Enter rate of intrest:7.5
Simple intrest= 2250.0
Compound intrest= 2422.968749999998



 '''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
#Program:

x=eval(input("Enter 1st number:"))
y=eval(input('Enter 2nd number:'))
print(f'Before Swap {x=} {y=}')
temp=x
x=y
y=temp
print(f'After swap {x=} {y=}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
#Program:
x=int(input("Enter 1st number:"))
y=int(input('Enter 2nd number:'))
print(f'Before Swap {x=} {y=}')
x=x+y
y=x-y
x=x-y
print(f'After swap {x=} {y=}')

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x=int(input("Enter 1st number:"))
y=int(input('Enter 2nd number:'))
print(f'Before Swap {x=} {y=}')
x=x*y
y=x//y
x=x//y
print(f'After swap {x=} {y=}')

# Identify  error
else:
		print('else  suite')
print('Outside') #No if block

# Identify  error
if  9 > 5  # no':'
	print('Hello')
print('Bye')

# Identify  error
if  9 > 12:
	print('Hyd')
else  # no : on else block
	print('Sec')


# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') #Indentation error

# Identify  error
if  ():
			print('Hyd')
	else: # else() block indentation error
					print('Sec')
print('Bye') 


# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}# set due to {}
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
if  []: #error
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: #error
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # indentation error 

 # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

x=int(input("Enter number:"))
if x%2==0:
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
'''
One
Two
Three
Bye
'''

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
'''
Hyd
Sec
Cyd
Bye
'''
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#Bye

 # Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
 x=int(input("Enter the month :"))
 if x==1:
    print("January")
 elif x==2:
    print("Febraury")
 elif x==3:
    print("March")
 elif x==4:
    print("April")
 elif x==5:
    print("May")
 elif x==6:
    print("June")
 elif x==7:
    print("July")
 elif x==8:
    print("August")
 elif x==9:
    print("September")
 elif x==10:
    print("October")
 elif x==11:
    print("November")
 elif x==12:
    print("December")
 else:
    print("Input should be 1-12")
except ValueError:
    print("Input should be Integer")


 '''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
x=int(input("Enter the Number:"))
if x==1:
  print("one")
else:
 if x==2:
   print("two") 
 else:
  if x==3:
    print("March")
  else:
   if x==4:
    print("April")
   else:
    if x==5:
      print("May")
    else:
     if x==6:
       print("June")
     else:
      if x==7:
        print("July")
      else:
       if x==8:
          print("August")
       else:
        if x==9:
          print("September")
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
x=int(input("Enter the Number:"))
if (x%4==0):
 if(x%400==0 or x%100!=0):
  print("leap year")
 else:
    print('Not a leap year')

 '''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions

'''
x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))
z=int(input("Enter 3rd Number:"))
if x>y and x>z :
  print(x,"is greater")
elif y>z:
    print(y,'is greater')
else:
    print(z,'is greater')




 '''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
a=int(input('Enter "1" to convert celsius to farenheit Enter "2" to convert farenheit to celsius:'))
if a==1:
    temp=int(input("Enter celsius:"))
    c=1.8*temp+32
    print("Farenheit=",c)
elif a==2:
    temp=int(input("Enter Farenheit:"))
    c=(tem-32)/1.8
    print("celsius=",c)
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

7) What  are  the  values  of  x …


x=int(input("Enter x :"))
y=int(input("Enter y :"))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd qudrant")
elif x>0 and y<0:
    print("4th qudrant")
elif x>0 or x<0 and y==0:
    print("on x-axis")
elif y>0 or y<0 and x==0:
    print("on y-axis")

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

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
max=x
if y>max and y>z:
     max=y
elif z>max:
      max=z
print(f'{max=}')
min=x
if y<min and y<z:
     min=y
elif z<min:
      min=z
print(f'{min=}')
mid=(x+y+z)-(max+min)
print(f'{mid=}')
