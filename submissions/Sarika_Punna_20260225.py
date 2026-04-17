print("program  to  add ,  subtract , multiply  and  divide  two  complex  numbers")
x=complex(input("Enter first complex number:"))
y=complex(input("Enter second complex number:"))
print(f'sum:{x+y}')
print(f'Difference:{x-y}')
print(f'Product:{x*y}')
print(f'Division:{x/y}')

print("program  to  determine  area  and  perimeter  of  rectangle")
x=float(input("Enter length of rectangle:"))
y=float(input("Enter breadth of rectangle:"))
print(f"Area:{x*y}")
print(f'Perimeter:{2*(x+y)}')

import math
print("a  program  to  determine  volume  of  a  sphere")
x=float(input("enter radius:"))
print(f"volume: {4*math.pi*x**3}")


print("program  to  determine  simple  interest  and  compound  interest")
p=float(input("Enter principle:"))
t=float(input("Enter time:"))
r=float(input("Enter rate of interest"))
print(f"Simple Interest: {(p*t*r)/100}")
print(f"Compound Interest: {p*(1+r/100)**t-p}")

print("program  to  swap  values  of  two   objects   using  3rd  object")
x=eval(input("Enter first input:"))
y=eval(input("Enter second input:"))
print(f"Before swap: x={x} y={y}")
t=x
x=y
y=t
print(f"after swap: x={x} y={y}")


print("program  to  swap  values  of  two  objects  without  using  3rd  object")
x=int(input("Enter first input:"))
y=int(input("Enter second input:"))
print(f"Before swap: x={x} y={y}")
x=x+y
y=x-y
x=x-y
print(f"after swap: x={x} y={y}")


print("program  to  swap  values  of  two  objects  without  using  3rd  object")
x=int(input("Enter first input:"))
y=int(input("Enter second input:"))
print(f"Before swap: x={x} y={y}")
x=x*y
y=x//y
x=x//y
print(f"after swap: x={x} y={y}")

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


print("program  to  print  month  name  for  input  month  number  by  using  if  and  elif")
try:
    x=int(input("Enter input:"))
    if(x<0 or x>12):
        print("Input should be between (1-12)")
    elif(x==1):
        print("January")
    elif(x==2):
        print("February")
    elif(x==2):
        print("February")
    elif(x==3):
        print("March")
    elif(x==4):
        print("April")
    elif(x==5):
        print("May")
    elif(x==6):
        print("June")
    elif(x==7):
        print("July")
    elif(x==8):
        print("August")
    elif(x==9):
        print("September")
    elif(x==10):
        print("October")
    elif(x==11):
        print("November")
    else:
        print("December")
except ValueError:
    print("Input should be integer value")
    

print("program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif")
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
a=int(input("Enter 1 to convert celsius to fahrenheit and 2 to convert fahreheit to celsius:"))
if(a==1):
    c=float(input("Enter celsius temperature:"))
    print(f"falrenheit equivalent:{1.8 * c + 32}")
elif(a==2):
    c=float(input("Enter fahrenheit temperature:"))
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
elif(x!=0 and y==0):
    print("x-axis")
elif(x==0 and y!=0):
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




