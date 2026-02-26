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
import math
a=eval(input("enter first complex number: "))
b=eval(input("enter second complex number: "))
print(f'sum of {a} +{b}={a+b}')
print(f'difference of {a} -{b}={a-b}')
print(f'product of{a}*{b}={a*b}')
print(f'division  of {a}/{b}={a/b}')

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

length=int(input("Enter length of rectangle: "))
breadth=int(input("Enter breadth of rectangle: "))
print(f'Area:  = {length*breadth}')
print(f'Perimeter: = {2*(length+breadth)}')
#volume
r=int(input("enter radius of circle: "))
ans=4/3*math.pi*r**3
print(f'volume:{'%.2f' %ans}')

#interest
p=eval(input("enter principal amount: "))
t=eval(input("enter time: "))
r=eval(input("enter rate of interest: "))
print(f'simple interest ={(p*t*r)/100}')
print(f'compound interest={(p*(1+r/100)**t)-p}')

# swap two numbers with temp variable
a=input("Enter 1st input: ")
b=input("Enter 2nd input: ")
print(f'Before swap :a={a}  b={b}')
temp=a
a=b
b=temp
print(f'After swap :a={a}  b={b}')

#swaap two numbers with + and -
a=int(input("Enter 1st input: "))
b=int(input("Enter 2nd input: "))
print(f'Before swap :a={a}  b={b}')
a=a+b
b=a-b
a=a-b
print(f'After swap :a={a}  b={b}')

#swaap two numbers with * and /
a=int(input("Enter 1st input: "))
b=int(input("Enter 2nd input: "))
print(f'Before swap :a={a}  b={b}')
a=a*b
b=a/b
a=a/b
print(f'After swap :a={a}  b={b}')


# Identify  error
else:
		print('else  suite')# because it deosnot have if block
print('Outside')# 'outside

# Identify  error
if  9 > 5 #because it does not have : at the end of if statement
	print('Hello')
print('Bye')#Bye

# Identify  error
if  (10,20,15):
print('Hyd')#there is no indentation or 4 spaces or tab
else:
print('Sec')#there is no indentation or 4 spaces or tab

# Identify  error
if  ():
			print('Hyd')
	else:#else indernation is not correct
					print('Sec')
print('Bye')

# Identify  error
if  { }: # you cant have '{}' in if statement
{
	print('One')
	print('Two')
	print('Three')
}
else:
{ # you cant have '{}' in if statement
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
if  []: #if indentation error
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: #if indentation error
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

oddoreven=int(input("Enter a number: "))
if(oddoreven%2==0):
    print(f'{oddoreven} is even')
else:    
    print(f'{oddoreven} is odd')
    
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')#one
        print('Two')#two
        print('Three')#three
print('Bye')#Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')#Hyd
        print('Sec')#Sec
        print('Cyb')#Cyb
print('Bye')#Bye
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    month=int(input("enter month number from 1 to 12:"))
    if(month==1):
        print("january")
    elif(month==2):
        print("febuaray")
    elif(month==3):
        print("march")
    elif(month==4):
        print("april")
    elif(month==5):
        print("may")
    elif(month==6):
        print("june")
    elif(month==7):
        print("july")
    elif(month==8):
        print("august")
    elif(month==9):
        print("september")
    elif(month==10):
        print("october")
    elif(month==11):
        print("november")
    elif(month==12):
        print("december")
    else:
        print("invalid month number give input from 1 to 12")
except TypeError:
    print("invalid input give month number from 1 to 12 in integer")
    
#print digit
digit=int(input("enter a digit from 0 to 9: "))
if(digit==0):
    print("zero")
else:
    if(digit==1):
        print("one")
    else:
        if(digit==2):
            print("two")
        else:
            if(digit==3):
                print("three")
            else:
                if(digit==4):
                    print("four")
                else:
                    if(digit==5):
                        print("five")
                    else:
                        if(digit==6):
                            print("six")
                        else:
                            if(digit==7):
                                print("seven")
                            else:
                                if(digit==8):
                                    print("eight")
                                else:
                                    if(digit==9):
                                        print("nine")
                                    else:
                                        print("invalid input give digit from 0 to 9")


leapyear=int(input("enter a year in 4 digit: "))
if(leapyear%4==0 and leapyear%100!=0 or leapyear%400==0):
    print(f'{leapyear} is a leap year')
else:
    print(f'{leapyear} is not a leap year')


#leap year

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if(a>b and a>c):
    print(f'{a} is largest number')
elif(b>c and b>a):
    print(f'{b} is largest number')
else:    
    print(f'{c} is largest number')
    
#temperature faranheit to celsius and vice versa
try:
    temp=int(input("enter temperature farenheit to celsius: "))   
    celsius=(temp-32)*5/9
    print(f'temperature in celsius is {celsius}')
except ValueError:
    print("Invalid input. Please enter a valid number for temperature.")


try:
    temp=int(input("enter temperature celsius to farenheit: "))
    farenheit=(temp*9/5)+32
    print(f'temperature in farenheit is {farenheit}')
except ValueError:
    print("Invalid input. Please enter a valid number for temperature.")

#quadrant
x=int(input("enter x coordinate: "))
y=int(input("enter y coordinate: "))
if(x>0 and y>0):    
    print("point is in 1st quadrant")
elif(x<0 and y>0):
    print("point is in 2nd quadrant")
elif(x<0 and y<0):
    print("point is in 3rd quadrant")
elif(x>0 and y<0):  
    print("point is in 4th quadrant")
elif(x==0 and y==0):
    print("point is at origin")
elif(x==0 and y!=0):
    print("point is on y axis")
elif(x!=0 and y==0):
    print("point is on x axis")

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if(a>b and a>c):
    max=a
elif(b>c and b>a):
    max=b
elif(c>a and c>b):
    max=c
print(f'largest input is {max}')

if(a<b and a<c):
    min=a
elif(b<c and b<a):
    min=b
elif(c<a and c<b):
    min=c
print(f'smallest input is {min}')

print(f'middle input is {a+b+c-max-min}')

    

    
    
    
