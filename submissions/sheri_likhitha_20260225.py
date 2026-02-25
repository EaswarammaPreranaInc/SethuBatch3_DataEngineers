#1 complex numbers
#Taking inputs
a= eval(input("Enter 1st complex number: "))
b= eval(input("Enter 2nd complex number: "))
#Printing result using f-strings
print(f"sum = {a+b}")
print(f"Difference = ({a-b})")
print(f"Product = {a*b}")
print(f"Division = {a/b}")


#2 area & perimeter of rectangle
length=float(input("Enter length of rectangle: "))
breadth=float(input("Enter breadth of rectangle: "))
#defining the formulas
area=length*breadth
perimeter=2*(length+breadth)
#printing the outputs of rectangle
print(f"Area  :  {area}")
print(f"Perimeter  :  {perimeter}")


#3 Volume of sphere
import math
radius=eval(input("Enter radius: "))
#volume of sphere formula
volume_of_sphere=(4/3)*math.pi*(radius**3)
print(f"volume : {volume_of_sphere}")



#4 simple interest & compound interest
p=eval(input("Enter principle: "))
t=eval(input("Enter time: "))
r=eval(input("Enter rate of interest: "))
#simple interest formula
simple_interest=(p*t*r)/100
#compound interest formula
compound_interest=p*(1+r/100)**t-p
print(f"Simple interest : {simple_interest}")
print(f"compound interest : {compound_interest}")


#5 swapping using 3rd variable
x=input("Enter 1st input: ")
y=input("Enter 2nd input: ")
#Before swap
print(f"Before swap : {x=} , {y=}")
#swapping using 3rd variable
temp=x
x=y
y=temp
#After swap
print(f"After swap : {x=} , {y=}")



#5 swapping two numbers
x=eval(input("Enter 1st input: "))
y=eval(input("Enter 2nd input: "))
#Before swap
print(f"Before swap : {x=}  {y=}")
y=y+x
x=y-x
y=y-x
#After swap
print(f"After swap : {x=}  {y=}")


#6 swapping two numbers using multiplication & division
x=int(input("Enter 1st input: "))
y=int(input("Enter 2nd input: "))
#Before swapping
print(f"Before swapping : {x=} , {y=}")
#swapping without 3rd variable
x=x*y
y=x//y
x=x//y
#After swapping
print(f"After swapping : {x=} , {y=}")


#7 Identify  error
else:
	print('else  suite') #invalid syntax beacause statement should start with if condition
print('Outside')



# Identify  error
if  9 > 5
	print('Hello') #invalid syntax because after if condition colon ":" should be present
print('Bye')


# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec') #invalid syntax because after else colon":" should be present


# Identify  error
if  (10,20,15):
print('Hyd')      #invalid missing indentation
else:
print('Sec')


# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')   #invalid beacause there is no condition for 'if'
print('Bye')


# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')  #invalid syntax braces is not used for 'if-else condition'
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
	print('One')     #invalid syntax because no indentation & paranthesis
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



#7 finding even or odd using if statement
num=int(input("Give a number: "))
if num%2==0:
     print(f"'{num}' is Even number")
else:     
    print(f"'{num}' is Odd number")


# Find outputs  (Home  work)
if():
        print('Hyd')    #True because empty string
        print('Sec')
        print('Cyb')
else:
        print('One')    #One
        print('Two')    #Two
        print('Three')  #Three
print('Bye')            #Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')    #'Hyd'
        print('Sec')    #'Sec'
        print('Cyb')    #'Cyb'
print('Bye')     	#'Bye'


# Find outputs  (Home  work)
if { }:
	print('Hyd')   #False beacuse of empty dictionary
	print('Sec')
	print('Cyb')
print('Bye')           #'Bye'



#8 finding month
try:
    month=int(input("Enter month number (1-12): "))
    if month==1:
        print("january")
    elif month==2:
        print("February")
    elif month==3:
        print("March")
    elif month==4:
        print("April")
    elif month==5:
        print("May")
    elif month==6:
        print("June")
    elif month==7:
        print("July")
    elif month==8:
        print("August")
    elif month==9:
        print("September")
    elif month==10:
        print("October")
    elif month==11:
        print("November")
    elif month==12:
        print("December")
    else:
        print("Month number should be betweeen 1 and 12")
except ValueError:
    print("input should be an integer") 


#program to print digit in words (using if-else only) 
num=int(input("Enter any digit (0-9):  "))
if num==0:
    print("Zero")
else:
    if num==1:
        print("One")
    else:
        if num==2:
            print("Two")
        else:
            if num==3:
                print("Three")
            else:
                if num==4:
                    print("Four")
                else:
                    if num==5:
                        print("Five")
                    else:
                        if num==6:
                            print("Six")
                        else:
                            if num==7:
                                print("Seven")
                            else:
                                if num==8:
                                    print("Eight")
                                else:
                                    if num==9:
                                        print("Nine")
                                    else:
                                        print("Invalid")



# leap year
year= int(input("Enter a year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")                                    

                                        
# program to determine largest using if and else
a=int(input("Enter 1st value: "))                
b=int(input("Enter 2nd value: "))                
c=int(input("Enter 3rd value: ")) 
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)                       


#celsius to fahrenheit & fahrenheit to celsius
num=int(input("Enter 1 to convert celsius to farenheit & 2 to convert farenheit to celsius: "))
if num==1:
    c_temp=eval(input("Enter celsius temperature: "))
    celsius=(1.8*c_temp)+32
    print(f"Fahrenheit Equivalent : {celsius}")
elif num==2:
    f_temp=eval(input("Enter fahrenheit temperature: "))
    fahrenheit=(f_temp-32)/1.8
    print(f"celsius equivalent : {fahrenheit}")
else:
    print("Invalid input")


#co-ordinate program
x=float(input("Enter value of x co-ordinate: "))
y=float(input("Enter value of y co-ordinate: "))
if x==0 and y==0:
    print("The point is at the origin.")
elif x==0:
    print("The point lies on the y-axis")
elif y==0:
    print("The point lies on the x-axis")
elif x>0 and y>0:
    print("The point lies in 1st quadrant")
elif x<0 and y>0:
    print("The point lies in 2nd quadrant")
elif x<0 and y<0:
    print("The point lies in 3rd quadrant")
elif x>0 and y<0:
    print("The point lies in 4th quadrant")



#Taking input from the user
a=float(input("Enter 1st number a : "))
b=float(input("Enter 2nd number b : "))
c=float(input("Enter 3rd number c : "))
#Initialize max,min
largest=a
smallest=a
#logic for largest
if b>largest:
    largest=b
if c>largest:
    largest=c
#logic for smallest
if b<smallest:
    smallest=b
if c<smallest:
    smallest=c
#logic for middle 
middle=(a+b+c)-(largest + smallest)

print(f"Largest input : {largest}")
print(f"Smallest input : {smallest}")
print(f"Middle input : {middle}")                         
        
                                    

                                    
                                                                            


