Problem-1

import math

try:
    a = int(input("Enter side 1 : "))
    b = int(input("Enter side 2 : "))
    c = int(input("Enter side 3 : "))

    if a + b > c and a + c > b and b + c > a:

        if a == b == c:
            # Equilateral triangle
            area = (math.sqrt(3) / 4) * a * a
            print(f"Equilateral Triangle")
            print(f"Area : {area}")

        elif a == b or b == c or a == c:
            # Isosceles triangle
            perimeter = a + b + c
            print(f"Isosceles Triangle")
            print(f"Perimeter : {perimeter}")

        else:
            # Scalene triangle
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            perimeter = a + b + c
            print(f"Scalene Triangle")
            print(f"Area : {area}")
            print(f"Perimeter : {perimeter}")

    else:
        print("Not a triangle")

except ValueError:
    print("Enter integer input only")


Problem-2

import math
try:
    a = float(input("Enter the value of a :"))
    b = float(input("Enter the value of b :"))
    c = float(input("Enter the value of c :"))

    if a==0:
        print("value of a should not be 0")
    else :
        disc = b*b-4*a*c
        print(f"Discriminant = {disc}")

        if disc > 0:
            root1=  (-b +math.sqrt(disc)) / 2*a
            root2=  (-b -math.sqrt(disc)) / 2*a
            print("Roots are real and distinct")
            print("Root 1 :", root1)
            print("Root 2 :", root2)
        elif disc ==0:
            root = -b / 2*a
            print("Roots are real and same")
            print(F"Root is {root}")
        else:

                root1 = -b / 2*a
                root2= math.sqrt(-disc) / 2*a
                print("Roots are complex or imaginary")
                print("Root 1 :", root1)
                print("Root 2 :", root2)

except ValueError:
    print("Enter valid numeric input")

Problem-3
import math
try:
      x = float(input("Enter the value of x : "))
      y = float(input("Enter the value of y : "))
      radius=float(input("Enter the radius : "))

      distance = math.sqrt(x ** 2 + y ** 2)
      if distance==radius:
            print("Point is on the circle")
      elif distance>radius:
            print("Point is outside the circle")
      else:
            print("Point is inside the circle")

except:
      print("Enter a valid input")


#  # Find  outputs  (Home  work)
# m = 4
# match  m:
#   case  1:
#       print('One')
#   case  2:
#       print('Two')
#   case  3:
#       print('Three')
# print('Bye') # Bye

#  # Identify  Error
# i = 2
# match  i:
#   case  1:
#       print('One')
#   # case  _: 
#       print('None of   the  above')
#   case  2:
#       print('Two')
# print('Bye') # error due to anonymous object 
#  # Find  outputs  (Home  work)
# m = 2
# match  m:
#   case  1:
#       print('One')
#     #case _:  
#       print('Hello')
#   case  _:  
#       print('Bye')
# print('End') # more than one wildcard is not allowed
#  #  Find  outputs  (Home  work)
# m = 1
# match  m:
#   case  1:
#       print('Hyd')
#   case  1:
#       print('Sec')
#   case  1:
#       print('Cyb')
# print('Bye') # "Hyd" \n "Bye"
#  # Find  outputs  (Home  work)
# ch = 'B'
# match  ch:
#   case   'A':
#       print('Apple')
#   case  'B':
#       print('Book')
#   case  'C':
#       print('Cafe')
#   case  _:
#       print('None of  the  above')
# print('Bye') # Book \n Bye

Problem-4

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> 'Hyd''Sec''Cyb'
2) What  are  the  outputs  if  input  is  15  ?  --->'one''two''three'
3) What  are  the  outputs  if  input  is  10.8  ?  --->'India''China''Usa''Bye'
4) What  are  the  outputs  if  input  is  0  ?  --->
5) What  are  the  outputs  if  input  is  -10  ?  --->'one''two''three'
6) What  are  the  outputs  if  input  is  7  ?  --->'Hyd''Sec''Cyb'
'''
x = eval(input('Enter any  number :  '))
match  x:
    case  7 |  -6  |  0:
        print('Hyd')
        print('Sec')
        print('Cyb')
    case  -10 | 15:
        print('One')
        print('Two')
        print('Three')
    case  _:
        print('India')
        print('China')
        print('Usa')
# End  of  match
print('Bye')



'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> # Not a point
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> X-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->Not a point
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Error
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Not a point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Not a point
8) What  is  the  output  when  input  is  ()  ?  --->Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not a point
10) What  is  the  output  when  input  is  (25,) ?  --->Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not a point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
    case  (0 , 0):
        print('Origin')
    case   (0 , y):
        print('y - axis')
    case   (x , 0):
        print('x - axis')
    case   (x , y):
        print('Quadrant')
    case  _:
        print('Not  a  point')


units = int(input("Enter number of units : "))
bill = 0

match units:
    case u if u <= 100:
        bill = u * 3.00

    case u if u <= 200:
        bill = 100 * 3.00 + (u - 100) * 3.50

    case u if u <= 400:
        bill = 100 * 3.00 + 100 * 3.50 + (u - 200) * 4.00

    case u if u <= 700:
        bill = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            (u - 400) * 4.50
        )

    case _:
        bill = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            300 * 4.50 +
            (units - 700) * 5.00
        )

print(f"Bill Amount = Rs. {bill}")
#  Find  outputs
while  True:
	print('Hello')
print('Bye') # Prints continuously hello 
#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Prints bye


