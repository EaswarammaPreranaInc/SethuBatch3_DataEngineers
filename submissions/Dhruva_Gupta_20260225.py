1)
a=(complex(input("Enter 1st number: ")))
b=(complex(input("Enter 2nd number: ")))
sum=a+b 
print("Sum : ",sum)
diff=a-b
print("Diff : ",diff)
product=a*b
print("Product : ",product)
div=a/b
print("Division : “,div)

2)
l=eval(input("Enter length: "))
b=eval(input("ENter breath: "))
a=l*b 
p=2*(l+b)
print("Area ",a)
print("Perimeter ",p)

3)
import math
r=eval(input("Enter radius: "))
v=round(4/3*math.pi*r**3,2)
print("Vol: ",v)

4)
p=eval(input("Enter principle: "))
r=eval(input("Enter rate of interest: "))
t=eval(input("Enter time: "))
si=(p*r*t)/100
ci=round(p * (1  +  r  /  100)**t  -  p,2)
print("Simple interest: ",si)
print("Compound interest: ",ci)


5)
a=eval(input("Enter 1st input: "))
b=eval(input("Enter 2nd input: "))
print(f"Before swapping: {a=},{b=}")
c=a 
a=b 
b=c 
print(f"After swapping: {a=},{b=}")

6)
a=eval(input("Enter 1st input: "))
b=eval(input("Enter 2nd input: "))
print(f"Before swapping: {a=},{b=}")
a=a+b 
b=a-b
a=a-b
print(f"After swapping: {a=},{b=}”)

7)
a=eval(input("Enter 1st input: "))
b=eval(input("Enter 2nd input: "))
print(f"Before swapping: {a=},{b=}")
a=a*b 
b=a/b
a=a/b
print(f"After swapping: {a=},{b=}”)

8)
a=eval(input("Enter input: "))
if a%2==0:
    print("Even")
else:
    print(“Odd")

9)
try:
    a = int(input("Enter month number: "))

    if a == 1:
        print("Jan")
    elif a == 2:
        print("Feb")
    elif a == 3:
        print("Mar")
    elif a == 4:
        print("Apr")
    elif a == 5:
        print("May")
    elif a == 6:
        print("Jun")
    elif a == 7:
        print("Jul")
    elif a == 8:
        print("Aug")
    elif a == 9:
        print("Sep")
    elif a == 10:
        print("Oct")
    elif a == 11:
        print("Nov")
    elif a == 12:
        print("Dec")
    else:
        print("Enter number between 1 and 12")

except ValueError:
    print("Enter valid input”)

10)
a=int(input("Enter the input: "))
if a==0:
    print("Zero")
if a==1:
    print("One")
if a==2:
    print("Two")
if a==3:
    print("Three")
if a==4:
    print("Four")
if a==5:
    print("Five")
if a==6:
    print("Six")
if a==7:
    print("Seven")
if a==8:
    print("Eight")
if a==9:
    print("Nine")
if a==10:
    print(“Invalid")

11)
a=int(input("Enter 4 digits year"))
if ((a%4==0 and a%100!=0) or a%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year”)

12)
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
if a > b:
    if a > c:
        print(f"Highest is {a}")
    else:
        print(f"Highest is {c}")
else:
    if b > c:
        print(f"Highest is {b}")
    else:
        print(f"Highest is {c}")

13)
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a > b and a > c:
    max = a
elif b > c:
    max = b
else:
    max = c

min_val = min(a, b, c)
mid = (a + b + c) - (max + min_val)

print(f"Maximum is {max}")
print(f"Minimum is {min_val}")
print(f"Middle number is {mid}")

14)
try:
    Option = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ")
    temp = float(input("Enter temperature value: "))
    if choice == "C":
        fahrenheit = 1.8 * temp + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}")
    elif choice == "F":
        celsius = (temp - 32) / 1.8
        print(f"Temperature in Celsius: {celsius}")
    else:
        print("Invalid choice. Please enter C or F only.")
except ValueError:
    print("Enter a valid numeric temperature.”)

15)
# Identify  error
else:
		print('else  suite')
print(‘Outside’). #Error is no If clause

16)
# Identify  error
if  9 > 5
	print('Hello')
print(‘Bye') #No colon

17)
# Identify  error
if  9 > 12:
	print('Hyd')
else
	print(‘Sec’) #No colon is Else

18)
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print(‘Sec') #No indentation

19)
# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print(‘Bye') #if and else has to have same indentation

20)
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
print(‘Bye') #Curly braces not needed

21)
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
print(‘Bye') #Indentation issue

22)
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print(‘Bye')

#One
#Two
#Three
#Bye

23)
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print(‘Bye')

#Hyd
#Sec
#Cyb
#Bye

24)
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print(‘Bye')

#Bye