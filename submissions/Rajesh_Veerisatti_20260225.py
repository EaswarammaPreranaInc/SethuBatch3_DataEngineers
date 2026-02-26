# Write  a  program  to  determine  area  and  perimeter  of  rectangle

try:
    length = float(input("Enter length of rectangle :  "))
    breadth = float(input("Enter breadth of rectangle :  "))

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area: ", area)
    print("Perimeter: ", perimeter)

except:
    print('Enter inputs should be int or float')


# Write  a  program  to  determine  volume  of  a  sphere

try:
    import math
    radius = float(input("Enter the radius of sphere :  "))
                
    volume = 4/3*math.pi*radius**3

    print("volume: ", volume)


except:
    print('Enter inputs should be int or float')


# Write  a  program  to  determine  simple  interest  and  compound  interest

try:
    principle = float(input('Enter principle: '))
    time = float(input('Enter time: '))
    rate =  float(input('Enter rate of intrest: '))

    Simple= (principle*time*rate)/100
    Compound= principle*(1+rate/100)**(time-principle)

    print("Simple Interest: ", Simple)
    print("Compound Interest: ", Compound)

except:
    print('Enter inputs should be int or float')


# Write  a  program  to  swap  values  of  two   objects   using  3rd  object



x =eval(input('Enter 1st input: '))
y =eval(input('Enter 2nd input: '))

print(f"Before swap :  {x=}  , {y=}")


temp = x
x = y
y = temp

print(f"After  swap :  {x=}  , {y=}")


# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

# Hint: One  addition  and  two  subtractions

try:

    x =int(eval(input('Enter 1st input: ')))
    y =int(eval(input('Enter 2nd input: ')))

    print(f"Before swap :  {x=}  , {y=}")

    x=x*y
    y=x//y
    x=x//y

    print(f"After  swap :  {x=}  , {y=}")

except:
    print('Enter inputs should be int or float')



# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement



a = int(input("Enter a number :  "))

if a % 2 == 0:
    print("Even")

if a % 2 != 0:
    print("Odd")


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
    a = int(input("Enter a month  number (1-12) :  "))

   
    if a==1:
        print('jan')
    elif a==2:
        print('Feb')
    elif a==3:
        print('April')
    elif a==4:
        print('March')
    elif a==5:
        print('May')
    elif a==6:
        print('June')
    elif a==7:
        print('July')
    elif a==8:
        print('Aug')
    elif a==9:
        print('Sep')
    elif a==10:
        print('otc')
    elif a==11:
        print('Nov')
    elif a==12:
        print('Dec')
    else:
        print('Enter the integer number in between 1 and 12')


except:
    print('Enter inputs should be int ')



# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)


try:
    a = int(input("Enter a digit: "))
    if a == 0:
        print("Zero")
    else:
        if a == 1:
            print("One")
        else:
            if a == 2:
                print("Two")
            else:
                if a == 3:
                    print("Three")
                else:
                    if a == 4:
                        print("Four")
                    else:
                        if a == 5:
                            print("Five")
                        else:
                            if a == 6:
                                print("Six")
                            else:
                                if a == 7:
                                    print("Seven")
                                else:
                                    if a == 8:
                                        print("Eight")
                                    else:
                                        if a == 9:
                                            print("Nine")
                                        else:
                                            print("Invalid")

except:
    print('Enter inputs should be int in between 0 to 9 ')

# Write  a  program  to  test  year  is  leap  year  or  not


try:
    a = int(input("Enter 4-digits year: "))

    if a % 4 == 0 and a % 100 != 0:
        print("Leap Year")
    else:
        if a % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
except:
    print('Enter 4-digits of in numbers')


# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else 
try:
    a = int(eval(input("Enter first number: ")))
    b = int(eval(input("Enter 2nd number: ")))
    c = int(eval(input("Enter 3rd number: ")))

    if a >= b and a >= c:
        print("Largest =", a)
    else:
        if b >= a and b >= c:
             print("Largest =", b)
        else:
            print("Largest =", c)
except:
    print('Enter  input should be float or int')


# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

try:
    a = int(input("Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : "))

    if a == 1:
        celsius = float(input("Enter celsius temperature : "))
        fahrenheit = 1.8 * celsius + 32
        print("fahrenheit  :", fahrenheit)
    else:
        if a == 2:
            fahrenheit = float(input("Enter fahrenheit temperature : "))
            celsius = (fahrenheit - 32) / 1.8
            print("celsius equivalent :", celsius)
        else:
            print("Enter only 1 or 2")

except TypeError:
    print('Enter celsius and farenheit temperature should be int or float')


#  Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
try:
    x = int(input("Enter value of x co-ordinate : "))
    y = int(input("Enter value of y co-ordinate : "))

    if x > 0 and y > 0:
        print("1st quadrant")
    elif x < 0 and y > 0:
        print("2nd quadrant")
    elif x < 0 and y < 0:
        print("3rd quadrant")
    elif x > 0 and y < 0:
        print("4th quadrant")
    elif x != 0 and y == 0:
        print("x-axis")
    elif x == 0 and y != 0:
        print("y-axis")
    else:
        print("origin")

except TypeError:
    print('Enter value should be  int ')

# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    max = a
    min = a

    if b > max:
        max = b
    if c > max:
        max = c

    if b < min:
        min = b
    if c < min:
        min = c

    mid = (a + b + c) - (max + min)

    print("Largest =", max)
    print("Smallest =", min)
    print("Middle =", mid)



except TypeError:
    print('Enter value should be  int ')
