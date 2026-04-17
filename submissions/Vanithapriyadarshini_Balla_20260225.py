
# Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

x=eval(input("Enter First  complex  number : "))
y=eval(input("Enter second  complex  number : "))
print(F'Sum : {(x+y)}')
print(F'Difference : {(x-y)}')
print(F'Product : {(x*y)}')
print(F'Division : {(x/y)}')	

# (Home  work)Write  a  program  to  determine  area  and  perimeter  of  rectangle											=  (15 -18j + 20j + 24) /  (25 + 36)
x=float(input("Enter length of rectangle : "))
y=float(input("Enter readth of rectangle : "))	
print(f'Area : {(x*y): .2f}')
print(f'Perimeter : {(2*(x+y)):.2f}')

#(Home  work)Write  a  program  to  determine  volume  of  a  sphere
import math
r=float(input("Enter radius : "))
print(f'Volume : {4/3*(math.pi)*r**3 : .2f}')

# Write  a  program  to  determine  simple  interest  and  compound  interest
p=float(input("Enter principle : "))
t=float(input("Enter time : "))
r=float(input("Enter rate of interest : "))
print(f'Simple Interest : {(p*t*r /100) : .2f}')	
print(f'Compound Interest : {(p*(1 + r/100)**t - p) : .2f}')

# Write  a  program  to  swap  values  of  two   objects   using  3rd  object
x=eval(input("Enter 1st input : "))
y=eval(input("Enter 2nd input : "))
print(f'Before swap : {x=} \t \t {y=}')
temp=x
x=y
y=temp
print(f'After swap : {x=} \t \t {y=}')

# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x=float(input("Enter 1st input : "))
y=float(input("Enter 2nd input : "))
print(f'Before swap : {x=} \t \t {y=}')
x=x+y
y=x-y
x=x-y
print(f'After swap : {x=} \t \t {y=}')

''' # Identify  error
else:
		print('else  suite')
print('Outside')... if - else suite should be paired in case of else.

# Identify  error
if  9 > 12:
	print('Hyd')   
else                   ':' is mandatory after else suite
	print('Sec')

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')  Indetentation(<space> or <tab> missing after ':'  

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')     

if, else suites should be intendented on same column

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
print('Bye')  No '{}' for if and else suites.

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

The inner if suites should be indented with <space> or <tab> after ':' '''

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

x=int(input("Enter a number : "))
if x%2==0 :
 print("Even")
else:
 print("Odd")	

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')   # One
        print('Two')   # Two
        print('Three') # Three
print('Bye')           # Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')   # Hyd
        print('Sec')   # Sec
        print('Cyb')   # Cyb
print('Bye')           # Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')   
	print('Sec')   
	print('Cyb')   
print('Bye')           # Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
 x=int(input(" Enter month number(1 - 12) : "))
 if x==1:
  print("January")
 elif x==2:
  print("February")
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
  print("Should be between 1 and 12")
except:
 print("Input should be an integer")

# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

try:
 x=int(input("Enter any digit(0 - 9) "))
 if x==0:
     print("Zero")
 else :
     if x==1:
         print("One")
     else :
         if x==2:
             print("Two")
         else :
             if x==3:
                 print("Three")
             else :
                  if x==4:
                      print("Four")
                  else :
                       if x==5:
                           print("Five")
                       else :
                            if x==6:
                                print("Six")
                            else :
                                if x==7:
                                    print("Seven")
                                else :
                                    if x==8:
                                        print("Eight")
                                    else :
                                        if x==9:
                                            print("Nine")
                                        else :
                                            print("Invalid digit")
except:
    print("Input should be integer from 0 to 9")
         
# Write  a  program  to  test  year  is  leap  year  or  not

yr=int(input("Enter 4- digit year : "))
if ((yr % 4 == 0) and (yr % 100 !=0)) or (yr % 400 ==0):
    print("Leap year")
else:
    print("not a leap year")

# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
 
x=eval(input("Enter 1st number : "))
y=eval(input("Enter 2nd number : "))
z=eval(input("Enter 3rd number : "))
if x>y and x>z :
    print(f'Largest number is {x}')
else :
    if y>z:
        print(f'Largest number is {y}')
    else :
        print(f'Largest number is {z}')
print()

# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

x=int(input("Enter 1 to convert  celsius to farenheit and 2 to convert  farenheit to  celsius : "))
if x==1:
    cel=float(input("Enter celsius degree : "))
    fa= 1.8 * cel + 32
    print(f'Faurenheit degree : {fa}')
else :
    if x==2:
        temp=float(input("Enter celsius degree : "))
        c= (temp - 32) / 1.8
        print(f'Celsius Equivalent : {c : .2f}')
    else :
        print("Invalid input")

# 

try:
    x=int(input("Enter 1 to convert  celsius to farenheit and 2 to convert  farenheit to  celsius : "))
    if x==1:
        cel=float(input("Enter celsius degree : "))
        fa= 1.8 * cel + 32
        print(f'Faurenheit degree : {fa}')
    else :
        if x==2:
            temp=float(input("Enter celsius degree : "))
            c= (temp - 32) / 1.8
            print(f'Celsius Equivalent : {c : .2f}')
        else :
            print("Invalid input")
            
        
except:
    print("Invalid input")

# Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

x=int(input("Enter value of x co-ordinate : "))
y=int(input("Enter value of y co-ordinate : "))
if x>0 and y>0 :
    print(" 1st Quadrant")
elif x<0 and y>0 :
    print(" 2nd Quadrant")
elif x<0 and y<0 :
    print(" 3rd Quadrant")
elif x>0 and y<0 :
    print(" 4th Quadrant")
else :
    print(" Lies on Origin")

# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

try:
    x=float(input("Enter 1st input : "))
    y=float(input("Enter 2nd input : "))
    z=float(input("Enter 3rd input : "))
    max=x
    min=x
    if y > max:
        max=y
    if z > max:
        max=z
    if y < min:
        min=y
    if z < min:
        min=z
    mid= (x+y+z) - (max+min)
    print(f'Largest number : {max}')
    print(f'Smallest number : {min}')
    print(f'Middle number : {mid}')
except:
    print("Invalid input")


