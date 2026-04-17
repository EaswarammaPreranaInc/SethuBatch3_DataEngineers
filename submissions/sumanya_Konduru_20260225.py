Write a program to add , subtract , multiply and divide two complex numbers

First complex number ---> 3 + 4j
2nd complex number ---> 5 + 6j
What is the sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What is the difference ? ---> (3 + 4j) - (5 + 6j) = -2 - 2j
What is the product ? ---> (3 + 4j) * (5 + 6j) = 15 + 18j + 20j - 24 = -9 + 38j
What is the division ? ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
            = (15 -18j + 20j + 24) / (25 + 36)
            = 39 / 61 + 2j / 61             
'''
'''
x = complex(input('Enter first complex number : '))
y = complex(input('Enter second complex number : '))
print(f'sum : {x + y}')
print(f'Difference : {x - y}')
print(f'Product : {x * y}')
print(f'Division : {x /y}')
'''

'''
Write a program to determine area and perimeter of rectangle

1) What are the inputs ? ---> length and breadth

2) What are the outputs ? ---> area and perimeter

3) What is the area of rectangle ? ---> length * breadth

4) What is the perimeter of rectangle ? ---> 2 * (length + breadth)
'''
'''
x = float(input('Enter length of number : '))
y = float(input('Enter breadth number : '))
print(f'Area : {(x*y):.2f}')
print(f'Perimeter : {2*(x+y):.2f}')
'''

'''
Write a program to determine volume of a sphere

1) What is the input ? ---> radius

2) What is the output ? ---> volume

3) What is the volume of sphere ? ---> 4 / 3 * pi * r ^ 3
'''
'''
import math
x = float(input('Enter radius : '))
print(f'Volume : {(4/3*(math.pi)*x**3):.2f}')
'''

'''
Write a program to determine simple interest and compound interest

1) What are the inputs ? ---> principle , time and rate of interest

2) What are the outputs ? ---> Simple interest and compound interest

3) What is simple interest formula ? ---> ptr / 100

4) What is compound interest formula ? ---> p * (1 + r / 100) ^ t - p
'''
'''
p = float(input('Enter principle : '))
t = float(input('Enter time : '))
r = float(input('Enter rate of interest : '))
print(f'Simple Interest : {(p*t*r/100):.2f}')
print(f'Compound Interest : {(p*(1+r/100)**t-p):.2f}')
'''

'''
Write a program to swap values of two objects using 3rd object

Let x = 10 and y = Hyd
What are the values of x and y after swap ? ---> x = Hyd and y = 10
'''
'''
x = eval(input('Enter 1st input : '))
y = eval(input('Enter 2nd input : '))
print(f'Before Swap : {x=} \t {y=}')
temp = x 
x = y 
y = temp 
print(f'After Swap : {x=} \t {y=}')
'''

'''
Write a program to swap values of two objects without using 3rd object

Hint: One addition and two subtractions

x = 25
y = 10
'''
'''
x = eval(input('Enter 1st input : '))
y = eval(input('Enter 2nd input : '))
print(f'Before Swap : {x =} \t {y = }')
x = x + y 
y = x - y 
x = x - y
print(f'After swap : {x = } \t {y =}')
'''

'''
Write a program to swap values of two objects without using 3rd object

Hint: One multiplication and two divisions

x = 25
y = 10
'''
'''
x = eval(input('Enter 1st input : '))
y = eval(input('Enter 2nd input : '))
print(f'Before Swap : {x =} \t {y = }')
x = x * y 
y = x / y 
x = x / y
print(f'After swap : {x = } \t {y =}')
'''

# Identify error
else:
  print('else suite')
print('Outside')
#Answer : Error due to there is no 'if' statement 

# Identify error
if 9 > 5
 print('Hello')
print('Bye')
# Answer : Error due to there is no ':' after if condition 

 # Identify error
if 9 > 12:
 print('Hyd')
else
 print('Sec')
#Answer : Error due to there is no ':' after else condition

 # Identify error
if (10,20,15):
print('Hyd')
else:
print('Sec')
#Answer : Error due to indentation error 

# Identify error
if ():
   print('Hyd')
 else:
     print('Sec')
print('Bye')
#Answer : Error due to indentation error

# Identify error
if { }:
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
Answer : Error due to curly braces 

# Identify error
if ():
 print('One')
 print('Two')
 print('Three')
else:
if []:
 print('Four')
 print('Five')
 print('Six')
else:
if {}:
 print('Seven')
 print('Eight')
 print('Nine')
else:
 print('Hyd')
 print('Sec')
 print('Cyb')
print('Bye')
# Answer : Error due to there is no condition 

# Write a program to determine a number is even or odd with if statement
'''
a = int(input('Enter input : '))
if a%2 ==0 :
    print('Even number')
if a % 2 != 0 :
    print('Odd Number')
'''

# Find outputs (Home work)
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

# Find outputs (Home work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
'''
Hyd
Sec
Cyb
Bye
'''

# Find outputs (Home work)
if { }:
 print('Hyd')
 print('Sec')
 print('Cyb')
print('Bye')
#Bye

# Write a program to print month name for input month number by using if and elif (Home work)
'''
x = int(input('Enter month number (1-12) : '))
if x == 1:
    print('January')
elif x == 2:
    print('February')
elif x == 3:
    print('March')
elif x == 4:
    print('April')
elif x == 5:
    print('May')
elif x == 6:
    print('June')
elif x == 7:
    print('July')
elif x == 8:
    print('August')
elif x == 9:
    print('September')
elif x == 10:
    print('October')
elif x == 11:
    print('November')
elif x == 12:
    print('December')
else:
    print('Input should be between 1 and 12')
'''
'''
Write a program to print digit in words with else and if (do not use elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
'''
x = int(input('Enter any digit(0-9): '))
if (x == 1) :
    print('One')
    else:
       if(x == 2):
            print('Two')
            else:
                if(x == 3):
                    print('Three')
                    else:
                        if(x == 4):
                            print('Four')
                            else:
                                if(x == 5):
                                    print('Five')
                                    else:
                                        if(x == 6):
                                            print('Six')
                                            else:
                                                if(x == 7):
                                                    print('Seven')
                                                    else:
                                                        if(x == 8):
                                                           print(Eight)
                                                           else:
                                                              if(x == 9):
                                                                 print('Nine')
                                                                 else:
                                                                     print('Invalid digit')
'''

'''
Write a program to test year is leap year or not

1) What is leap year ? ---> Divisible by 4 but not by 100 (or) divisble by 400

2) Are 2016 , 2020 , 2024 leap years ? ---> Yes becoz leap year for every 4 yearrs

3) Are 1700 , 1800 , 1900 leap years ? ---> No becoz no leap year for every 100 years

4) Are 1600 , 2000 , 2400 leap years ? ---> Yes becoz leap year for every 400 years

5) Hint: 3 conditions
'''
'''
x = int(input('Enter 4-digit year : '))
if (x % 4 == 0):
    print('Leap Year')
elif (x % 100 == 0):
    print('Not a Leap Year')
elif (x % 400 == 0):
    print('Leap Year')
'''

'''
Write a program to determine largest of three numbers with if and else

Hint: Write multiple conditions
'''
'''
a = int(input('Enter 1st input : '))
b = int(input('Enter 2nd input : '))
c = int(input('Enter 3rd input : '))
if (a > b and a > c) :
    print(f'{a} is the largest')
if (b > a and b > c):
    print(f'{b} is the largest')
else:
    print(f'{c} is the largest ')
    
'''

'''
Write a program to convert celsius temperature to farenheit and vice-versa

1) What is the formula to convert celsius to farenheit ? ---> 1.8 * temp + 32

2) What is the formula to convert farenheit to celsius ? ---> (temp - 32) / 1.8
'''
'''
x = int(input('Enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius : '))
if (x ==1):
   temp = float(input('Enter celsius temperature : '))
   f = 1.8 * temp + 32 
   print(f'Farenheit Equivalent : {f}')
 elif (x == 2):
         temp  = float(input('Enter Farenheit tempture : '))
         c = (temp - 32)/1.8 
         print(f'Celsius Equivalent : {c}')
else :
     print(Invalid Input)
'''

'''
Write a program to test a point (x , y) lies in 1st quadrant , 2nd quadrant , 3rd quadrant ,
4th quadrant , x - axis , y - axis or origin

1) What are the values of x and y in 1st quadrant ? ---> Both are +ve

2) What are the values of x and y in 2nd quadrant ? ---> 'x' is -ve and 'y' is +ve

3) What are the values of x and y in 3rd quadrant ? ---> Both are -ve

4) What are the values of x and y in 4th quadrant ? ---> 'x' is +ve and 'y' is -ve

5) What are the values of x and y on x - axis ? ---> 'x' is non-zero and 'y' is 0

6) What are the values of x and y on y - axis ? ---> 'x' is 0 and 'y' is non-zero

7) What are the values of x and y if point is origin ? ---> Both are zeroes

8) Hint: Use if .. elif
'''
'''
x = int(input('Enter value of x co-ordinate : '))
y = int(input('Enter value of y co-ordinate : '))
if(x > 0 and y > 0):
   print('1st quadrant')
elif (x < 0 and y > 0) :
    print('2nd quadrant')
elif(x < 0 and y < 0):
     print('3rd quadrant')
elif(x > 0 and y < 0):
    print('4th quadrant')
elif(x != 0 and y == 0):
    print('x-axis')
elif(x == 0 and y != 0):
    print('y-axis')
else:
   print('Both are zeros') 
'''

'''
Write a program to determine largest , smallest and middle of three numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid = (10 + 20 + 7) - (20 + 7) = 10

1) What is the initial value of max ? ---> a

2) Whichever input > max, assign that input to max

3) What is the initial value of min ? ---> 'a'

4) Whichever input < min, assign that input to min

5) How to obtain middle number ? ---> Eliminate max and min from a , b , c

6) Hint : Do not use else in the program
'''
'''
a = float(input('Enter first input : '))
b = float(input('Enter second input : '))
c = float(input('Enter Thrid input : '))
max = a 
min = a 

if (b > max ) :
    max = b 
if (c > max) : 
    max = c 
if (b < min):
   min = b 
if (c < min) :
    min = c 
mid = (a + b + c) - (max - min)
print(f'Largest input : {max}')
print(f'Smallest inut : {min}')
print(f'Middle input : {mid}')
'''