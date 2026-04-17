#1
'''
Write a program to determine three sides form a triangle or not

1) Find area if it is an equilatera triangle
    What is an equilateral triangle? ---> All the three sides should be same
    What is the area of equilateral triangle? ---> sqrt(3) / 4 * a ^ 2

2) Find perimeter if it is an isosceles triangle
    What is an isoscles triangle? ---> Any two sides are same
    What is the perimeter of isoscles triangle? ---> a + b + c

3) Find both if it is scalene triangle
    What is a scalene triangle?  ---> All the three sides are different
    What is the area of scalene triangle? ---> sqrt(s * (s - a) * (s - b) * (s - c))
    What is the value of 's'?  ---> (a + b + c) / 2
    What is the perimeter of scalene triangle ? --->  a + b + c

4) What is the qualification of triangle? ---> Sum of every two sides should be > 3rd side

5) Hint: Use nested if
'''
import math

try:
    a = float(input("Enter 1st side : "))
    b = float(input("Enter 2nd side : "))
    c = float(input("Enter 3rd side : "))

    # Check for Triangle Qualification
    if (a + b > c) and (a + c > b) and (b + c > a):
        
        if a == b == c:
            print("Equilateral triangle")
            area = (math.sqrt(3) / 4) * (a ** 2)
            print(f"Area : {area:.2f}")
            
        elif a == b or b == c or a == c:
            print("Isosceles triangle")
            perimeter = a + b + c
            print(f"Perimeter : {perimeter:.1f}")
            
        else:
            print("Scalene triangle")
            perimeter = a + b + c
            s = perimeter / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"Area : {area:.2f}")
            print(f"Perimeter : {perimeter:.1f}")
            
    else:
        print("Not a triangle")

except ValueError:
    print("Invalid input! Please enter numeric values for the sides.")


#2
'''
Write a program to determine roots of a quadtratic equation a * x ^ 2 + b * x + c = 0 where a != 0

1) What is the value of discriminant? ---> b ^ 2 - 4ac

2) What are the roots called if disc > 0 ?  ---> Real and distinct
   What is the formula for root1? ---> (-b + sqrt(disc)) / 2a
   What is the formula for root2? ---> (-b - sqrt(disc)) / 2a

3) What are the roots called if disc is 0? ---> Real and same
   What is the formula for root? --->  -b / 2a

4) What are the roots called if disc < 0 ? ---> Complex (or) Imaginary roots
   What is the formula for real part? ---> -b / 2a
   What is the formula for imag part? ---> sqrt(-disc) / 2a
   What is root1 if real part is 3 and imag part is 4? ---> 3 + 4j
   What is root2 if real part is 3 and imag part is 4? ---> 3 - 4j
'''
import math
try:
    a = float(input("Enter value of a: "))
    if a == 0:
        print("Value of a can not be 0")
    else:
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))
        
        disc = b**2 - 4*a*c

        if disc > 0:
            print("Roots are real and distinct")
            r1 = (-b + math.sqrt(disc)) / (2*a)
            r2 = (-b - math.sqrt(disc)) / (2*a)
            print(f"Root 1: {r1:.2f}")
            print(f"Root 2: {r2:.2f}")

        elif disc == 0:
            print("Roots are real and equal")
            rt = -b / (2*a)
            print(f"Root 1: {rt:.1f}")
            print(f"Root 2: {rt:.1f}")

        else:
            print("Roots are imaginary (or) complex")
            rp = -b / (2*a)
            ip = math.sqrt(abs(disc)) / (2*a) 
            print(f"Root 1: {rp:.1f} + {ip:.1f}j")
            print(f"Root 2: {rp:.1f} - {ip:.1f}j")

except ValueError:
    print("Invalid input! Please enter numbers only.")



#3
'''
Write a program to determine a point (x , y) lies inside , outside or on the circle.
Center is origin and radius is 'r'

1) What is the distance between origin and point (x , y)? ---> sqrt(x ^ 2 + y ^ 2)

2) Where is the point if distance > raidus? ---> Outside the circle

3) Where is the point if distance < raidus? ---> Inside the circle

4) Where is the point if distance and raidus are same? ---> On the circle
'''
import math
try:
    x = int(input("Enter 'x' value: "))
    y = int(input("Enter 'y' value: "))
    r = int(input("Enter radius of the circle: "))
    d = math.sqrt(x**2 + y**2)
    if d == r:
        print("Point is on the circle")
    elif d < r:
        print("Point is inside the circle")
    else:
        print("Point is outside the circle")
except ValueError:
    print("Please enter valid numbers only. (Avoid letters or negative radius)")



#4
# Find  outputs  (Home  work)
m = 4
match m:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
print('Bye') #Bye



#5
# Identify  Error
i = 2
match i:
    case 1:
        print('One')
    case _: 
        print('None of the above')
    case 2: #Error as 'case 2' is not reachable or executed as match statement closes of decalaring 'case _'
        print('Two')
print('Bye') #Bye



#6
# Find  outputs  (Home  work)
m = 2
match  m:
    case 1:
        print('One')
    case _:  
        print('Hello')
    case _:  #Error as match..case statement can have only one anonymous value object case i.e. case _
        print('Bye')
print('End')



#7
#  Find  outputs  (Home  work)
m = 1
match  m:
    case 1:
        print('Hyd') #Hyd
    case 1:
        print('Sec')
    case 1:
        print('Cyb')
print('Bye') #Bye



#8
# Find  outputs  (Home  work)
ch = 'B'
match ch:
    case 'A':
        print('Apple')
    case 'B':
        print('Book') #Book
    case 'C':
        print('Cafe')
    case _:
        print('None of  the  above')
print('Bye') #Bye



#9
'''
1) What are the outputs if input is -6? ---> Hyd<next line>Sec<next line>Cyb<next line>
2) What are the outputs if input is 15? ---> One<next line>Two<next line>Three<next line>
3) What are the outputs if input is 10.8? ---> India<next line>China<next line>Usa<next line>
4) What are the outputs if input is 0? ---> Hyd<next line>Sec<next line>Cyb<next line>
5) What are the outputs if input is -10? ---> One<next line>Two<next line>Three<next line>
6) What are the outputs if input is 7? ---> Hyd<next line>Sec<next line>Cyb<next line>
'''
x = eval(input('Enter any number: '))
match x:
    case 7 | -6 | 0:
        print('Hyd')
        print('Sec')
        print('Cyb')
    case -10 | 15:
        print('One')
        print('Two')
        print('Three')
    case _:
        print('India')
        print('China')
        print('Usa')
# End  of  match
print('Bye')



#10
'''
1) What is the output when input is (-10 , -20)? ---> Quadrant
2) What is the output when input is (10 , 0)? ---> x - axis
3) What is the output when input is (0 , -20)? ---> y - axis
4) What is the output when input is (0 , 0)? ---> Origin
5) What is the output when input is (10 , 20 , 30)? ---> Not a point
6) What is the output when input is [10 , 20]? ---> Quadrant
7) What is the output when input is [0 , -25]? ---> y - axis
8) What is the output when input is ()? ---> Not a point
9) What is the output when input is {10 , 20}? ---> Not a point
10) What is the output when input is (25,)? ---> Not a point
11) What is the output when input is {10 : 20}? ---> Not a point
'''
tpl = eval(input('Enter any point in the form of (x , y): '))
match tpl:
    case (0 , 0):
        print('Origin')
    case (0 , y):
        print('y - axis')
    case (x , 0):
        print('x - axis')
    case (x , y):
        print('Quadrant')
    case _:
        print('Not a point')



#11
'''
Write a program to determine bill amount and input is units

Units                Cost
--------------------------------------
First 100 units      Rs. 3.00 / unit

Next 100 units       Rs. 3.50 / unit

Next 200 units       Rs. 4.00 / unit

Next 300 units       Rs. 4.50 / unit

Above 700 units      Rs. 5.00 / unit
--------------------------------------
Let units be 1200
What is the bill amount? ---> 100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint: Use match...case but not if...else
'''
units = int(input('Enter units : '))

match units:
    case u if u <= 100:
        cost = u * 3.00
    case u if u <= 200:
        cost = (100 * 3.00) + (u - 100) * 3.50
    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (u - 200) * 4.00
    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (u - 400) * 4.50
    case u:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (u - 700) * 5.00

print('Bill amount: ', cost)



#12
#  Find  outputs
while True:
    print('Hello') #Hello<next line>Hello<next line>Hello<next line>Hello<next line>.................
print('Bye') 



#13
#  Find  outputs
while  False:
    print('Hello')
print('Bye') #Bye