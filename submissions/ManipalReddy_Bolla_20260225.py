x=complex(input("Enter first complex number : "))
y=complex(input("Enter second complex number : "))
print(F'Sum : {x+y}')
print(F'Difference : {x-y}')
print(F'Product : {x*y}')
print(F'Division : {x/y}')

'''
output
Enter first complex number : 3+4j
Enter second complex number : 5+6j
Sum : (8+10j)
Difference : (-2-2j)
Product : (-9+38j)
Division : (0.6393442622950819+0.03278688524590165j)
'''




length=float(input("Enter length of rectangle : " ))
breadth=float(input("Enter breadth of rectangle : " ))
print(F'Area : {length*breadth:.2f}')
print(F'Perimeter : {2*(length+breadth):.2f}')

'''
output
Enter length of rectangle : 4
Enter breadth of rectangle : 5
Area : 20.00
Perimeter : 18.00
'''





Radius=float(input("Enter radius : "))
pi=3.1416
print(F'Volume : {4/3*pi*Radius*Radius*Radius:.2f}')

'''
output
Enter radius : 3.5
Volume : 179.59
'''




p=float(input("Enter principle : "))
t=float(input("Enter time : "))
r=float(input("Enter rate of interest : "))
print(F'Simple Interest : {p*t*r/100:.2f}')
print(F'Compound Interest : {p*(1+r/100)**t-p:.2f}')

'''
output
Enter principle : 10000
Enter time : 3
Enter rate of interest : 7.5
Simple Interest : 2250.00
Compound Interest : 2422.97
'''




x=input("Enter 1st input : ")
y=input("Enter 2nd input : ")
print(F'Before swap : {x=} \t {y=}' )
temp=x
x=y
y=temp
print(F'After swap : {x=} \t {y=}')

'''
output
Enter 1st input : 25
Enter 2nd input : Hyd
Before swap : x='25'     y='Hyd'
After swap : x='Hyd'     y='25'
'''




x=int(input("Enter 1st input : "))
y=int(input("Enter 2nd input : "))
print(F'Before swap : {x} \t {y}')
x=x+y
y=x-y
x=x-y
print(F'After swap : {x} \t {y}')

'''
output
Enter 1st input : 4
Enter 2nd input : 8
Before swap : x=25       y=10
After swap : x=10        y=25
'''





x=int(input("Enter 1st input : "))
y=int(input("Enter 2nd input : "))
print(F'Before swap : {x} \t {y}')
x=x*y
y=x//y
x=x//y
print(F'After swap : {x} \t {y}')

'''
output
Enter 1st input : 25
Enter 2nd input : 10
Before swap : x=25       y=10
After swap : x=10        y=25
'''




'''
# Identify  error
else:#without if block will give error
		print('else  suite')
print('Outside')
# Identify  error
if  9 > 5#without ':' will give error
	print('Hello')
print('Bye')
# Identify  error
if  9 > 12:
	print('Hyd')
else# without ':' will give error
	print('Sec')
# Identify  error
if  (10,20,15):
print('Hyd')# there should be indentation under if: which is not there so will give error
else:
print('Sec')#same indentation error
# Identify  error
if  ():
			print('Hyd')
	else:#indentation error
					print('Sec')
print('Bye')
# Identify  error 
if  { }:
{#{
statements
} #is not valid in python for if else statements
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
if  []:#indentation error for nested-if-else
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
output
One
Two
Three
Bye
'''




x=int(input("Enter Integer : "))
if (x%2==0):
    print("Even number")
else:
    print("Odd number")
	
'''
output
Enter Integer : 4
Even number
'''




# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

'''
output
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
print('Bye')

'''
output
Bye
'''




try:
 month=int(input("Enter month number (1 - 12) : "))
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
    print("Input should be between 1 and 12")
except ValueError:
    print("Input should be an interger")

'''
output
Enter month number (1 - 12) : 8
August
Enter month number (1 - 12) : 5.0
Input should be an interger
Enter month number (1 - 12) : 13
Input should be between 1 and 12
'''




x=int(input("Enter any digit (0 - 9):"))
if x==0:
    print("Zero")
else:
    if x==1:
        print("One")
    else:
        if x==2:
            print("Two")
        else:
            if x==3:
                print("Three")
            else:
                if x==4:
                    print("Four")
                else:
                    if x==5:
                        print("Five")
                    else:
                        if x==6:
                            print("Six")
                        else:
                            if x==7:
                                print("Seven")
                            else:
                                if x==8:
                                    print("Eight")
                                else:
                                    if x==9:
                                        print("Nine")
                                    else:
                                        if x==10:
                                            print("Invalid")
                                        else:
                                            print("")
'''
output
print  digit  in  words corresponding to that digit
'''




year=int(input("Enter 4-digit year : "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year")
else:
    print("Not a leap year")
	
'''
output
Enter 4-digit year : 1992
Leap Year
Enter 4-digit year : 2026
Not a leap year
'''




x=float(input("Enter 1st Number : "))
y=float(input("Enter 2st Number : "))
z=float(input("Enter 3st Number : "))
if x>y:
    if x>z:
        print(F'largest number : {x}')
else:
    if y>z:
        print(F'largest number : {y}')
    else:
        print(F'largest number : {z}')

'''
output
Enter 1st Number : 5
Enter 2st Number : 8
Enter 3st Number : 4
largest number : 8.0
'''




choice=int(input("Enter 1 to convert celsius to fahrenheit and 2 to convert farenheit to celsius :  "))
if choice==1:
    celsius=int(input("Enter celsius temperature : "))
    print(F'fahrenheit equivalent : {1.8 * celsius + 32:.2f}')
elif choice==2:
    fahrenheit=int(input("Enter fahrenheit temperature : "))
    print(F'celsius equivalent : { (fahrenheit - 32) / 1.8:.2f}')
else:
    print("Invalid input")
	
'''
output
Enter 1 to convert celsius to fahrenheit and 2 to convert farenheit to celsius :  2
Enter fahrenheit temperature : 100
celsius equivalent : 37.78
Enter 1 to convert celsius to fahrenheit and 2 to convert farenheit to celsius :  1
Enter celsius temperature : 30
fahrenheit equivalent : 86.00
Enter 1 to convert celsius to fahrenheit and 2 to convert farenheit to celsius :  8
Invalid input
'''




x=int(input("Enter value of x co-ordinate : "))
y=int(input("Enter value of y co-ordinate : "))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif x!=0 and y==0:
    print("x-axis")
elif x==0 and y!=0:
    print("y-axis")
elif x==0 and y==0:
    print("origin")
	
	
'''
output
Enter value of x co-ordinate : 4
Enter value of y co-ordinate : 4
1st quadrant
Enter value of x co-ordinate : -4
Enter value of y co-ordinate : 4
2nd quadrant
Enter value of x co-ordinate : -4
Enter value of y co-ordinate : -4
3rd quadrant
Enter value of x co-ordinate : 4
Enter value of y co-ordinate : -4
4th quadrant
Enter value of x co-ordinate : 4
Enter value of y co-ordinate : 0
x-axis
Enter value of x co-ordinate : 0
Enter value of y co-ordinate : 4
y-axis
Enter value of x co-ordinate : 0
Enter value of y co-ordinate : 0
origin
'''




a = float(input('Enter 1st number: ')) 
b = float(input('Enter 2nd number: ')) 
c = float(input('Enter 3rd number: ')) 
max=a
if b>max:
    max=b
if c>max:
    max=b

min=a
if min>b:
    min=b
if min>c:
    min=c
middle=(a+b+c)-(max+min)
print(F'Largest input :  {max}')
print(F'Smallest input : {min}')
print(F'Middle input : {middle}')    

'''
output
Enter 1st number: 10
Enter 2nd number: 20
Enter 3rd number: 7
Largest input :  20.0
Smallest input : 7.0
Middle input : 10.0
'''

