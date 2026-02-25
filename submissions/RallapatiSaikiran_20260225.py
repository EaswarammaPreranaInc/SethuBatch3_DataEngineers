


 #  Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

a = eval(input("Enter first input : "))
b = eval(input("Enter second input : "))

print(F'{a}+{b} = {a+b}') 
print(F'{a}-{b} = {a-b}')
print(F'{a}*{b} = {a*b}')
print(F'{a}/{b} = {a/b}')




#  Write  a  program  to  determine  area  and  perimeter  of  rectangle

a = float(input("Enter length : ")
b = float(input("Enter breadth : ")

print(F'{a}*{b} = {a*b}')
print(F'2*{a}*{b} ={2*a*b}')



# Write  a  program  to  determine  volume  of  a  sphere


a = float(input("Enter radius : ")

print(F'4/3*({3.14}*{a}**{3}) = {4/3*(3.14*a**3)}')



# Write  a  program  to  determine  simple  interest  and  compound  interest

def calculate_intrest():
 a = float(input(Enter principle : '))
 b = int(input(Enter Time : '))
 c = float(input(Rate Of intrest : ')) 
Si = (a*b*c)/100
Ci = a*((1+c/100)**b)-a
print(F'Simple Intrest :{Si: .2f}')
print(F'Compound Intrest :{Ci: .2f}')



 # Identify  error
else:
		print('else  suite')
print('Outside')  # there is no if function


 # Identify  error
if  9 > 5
	print('Hello')
print('Bye') # Error bcz of no colon
 

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')  # Error missing colon


 # Identify  error
if  (10,20,15):
print('Hyd')    # Print () should have some space 
else:
print('Sec')



 # Identify  error								
if  ():
	  print('Hyd')  # Error Else should be in the first place
	else:
	  print('Sec')
print('Bye')



 # Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')   # condition is not Given
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
if  []:                 # if condition should have paranthesis not square brackets
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





 # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

num = int(input("Enter a number : "))
if num % 2 ==0
    print(f'{num} is even')
else : 
    print(f'{num} is odd')






 # Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                  #  condition is not there
        print('One')
        print('Two')
        print('Three')
print('Bye')




# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')  # Hyd<next line>Sec<next line>Cyb<next line>Bye


 # Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  # False




 # Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)



month_num = int(input("Enter month number (1-12): "))
if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
elif month_num == 4:
    print("April")
elif month_num == 5:
    print("May")
elif month_num == 6:
    print("June")
elif month_num == 7:
    print("July")
elif month_num == 8:
    print("August")
elif month_num == 9:
    print("September")
elif month_num == 10:
    print("October")
elif month_num == 11:
    print("November")
elif month_num == 12:
    print("December")
else:
    print("Invalid month number")







# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa


def convert_temp():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter choice (1/2): "))
    
    if choice == 1:
        c = float(input("Enter Celsius: "))
        f = (c * 1.8) + 32
        print(f"{c}°C = {f}°F")
    elif choice == 2:
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) / 1.8
        print(f"{f}°F = {c}°C")
    else:
        print("Invalid choice")

convert_temp()




"Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin




def check_quadrant():
    x = float(input("Enter x-coordinate: "))
    y = float(input("Enter y-coordinate: "))
    
    if x > 0 and y > 0:
        print(f"({x}, {y}) is in 1st quadrant")
    elif x < 0 and y > 0:
        print(f"({x}, {y}) is in 2nd quadrant")
    elif x < 0 and y < 0:
        print(f"({x}, {y}) is in 3rd quadrant")
    elif x > 0 and y < 0:
        print(f"({x}, {y}) is in 4th quadrant")
    elif x == 0 and y == 0:
        print(f"({x}, {y}) is at origin")
    elif x == 0:
        print(f"({x}, {y}) is on y-axis")
    elif y == 0:
        print(f"({x}, {y}) is on x-axis")

check_quadrant()












































