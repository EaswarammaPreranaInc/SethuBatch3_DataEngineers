import math
a=float(input("Enter 1st side : "))
b=float(input("Enter 2nd side : "))
c=float(input("Enter 3rd side : "))
if (a+b>c) and (a+c>b) and (b+c>a):
    if a==b==c:
        print("Equilateral triangle")
        print(F'Area : {math.sqrt(3)/4*(a**2):.2f}')
    else:
        if a==b or b==c or a==c:
            print("Isosceles  triangle")
            print(F'Perimeter : {a+b+c}')
        else:
            print("Scalene triangle")
            s=(a+b+c)/2
            print(F'Area : {math.sqrt(s * (s - a) * (s - b) * (s - c)):.2f}')
            print(F'Perimeter : {a+b+c}')
else:
    print("Not a triangle")
	
'''
output
Enter 1st side : 7
Enter 2nd side : 7
Enter 3rd side : 7
Equilateral triangle
Area : 21.22
Enter 1st side : 7
Enter 2nd side : 8
Enter 3rd side : 7
Isosceles  triangle
Perimeter : 22.0
Enter 1st side : 3
Enter 2nd side : 4
Enter 3rd side : 5
Scalene triangle
Area : 6.00
Perimeter : 12.0
Enter 1st side : 7
Enter 2nd side : 8
Enter 3rd side : 16
Not a triangle
'''




import math
a=float(input("Enter value of a : "))
if a!=0:
    b=float(input("Enter value of b : "))
    c=float(input("Enter value of c : "))
    disc=b**2 - 4*a*c
    if disc>0:
        print("Roots are real and distinct")
        print(F'Root 1 :{(-b+math.sqrt(disc))/(2*a):.2f}')
        print(F'Root 2 :{(-b-math.sqrt(disc))/(2*a):.2f}')
    elif disc<0:
        print("Roots are imaginary (or) complex")
        real=-b/(2*a)
        imag=math.sqrt(-disc)/(2*a)
        print(F'Root 1 : {real}+{imag}j')
        print(F'Root 2 : {real}-{imag}j')
    elif disc==0:
        print("Roots are real and same")
        root=-b/(2*a)
        print(F'Root 1 :{root}')
        print(F'Root 2 :{root}')
else:
    print("Value of a can not be 0")
	
'''
output
Enter value of a : 3
Enter value of b : 10
Enter value of c : 3
Roots are real and distinct
Root 1 :-0.33
Root 2 :-3.00
Enter value of a : 5
Enter value of b : 10
Enter value of c : 5
Roots are real and equal
Root 1 :-1.0
Root 2 :-1.0
Enter value of a : 5
Enter value of b : 6
Enter value of c : 5
Roots are imaginary (or) complex
Root 1 : -0.6+0.8j
Root 2 : -0.6-0.8j
Enter value of a : 0
Value of a can not be 0
'''




try:
    import math
    x = float(input("Enter value of x : "))
    y = float(input("Enter value of y : "))
    r = float(input("Enter radius of circle : "))
    distance = math.sqrt(x**2 + y**2)
    if distance == r:
        print("Point is on the circle")
    elif distance > r:
        print("Point is Outside  the  circle")
    elif distance < r:
        print("Point is Inside  the  circle")
except:
    print("Enter valid inputs")

'''
output
Enter value of x : 3
Enter value of y : 4
Enter radius of circle : 5
Point is on the circle
Enter value of x : -1
Enter value of y : -1
Enter radius of circle : 2
Point is Inside  the  circle
Enter value of x : 1
Enter value of y : 1
Enter radius of circle : 1
Point is Outside  the  circle
'''




# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')

'''
output
Bye
'''




'''
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: #wildcard makes remaining patterns unreachable#wildcard must be the last case
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
'''




'''
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')


#wildcard makes remaining patterns unreachable
'''




#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')

'''
output
Hyd
Bye
'''




# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')

'''
output
Book
Bye
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
output
Enter any  number :  -6
Hyd
Sec
Cyb
Bye
Enter any  number :  15
One
Two
Three
Bye
Enter any  number :  10.8
India
China
Usa
Bye
Enter any  number :  0
Hyd
Sec
Cyb
Bye
Enter any  number :  -10
One
Two
Three
Bye
Enter any  number :  7
Hyd
Sec
Cyb
Bye
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
		
'''
output
Enter  any  point  in  the  form  of  (x , y) :  (-10,-20)
Quadrant
Enter  any  point  in  the  form  of  (x , y) :  (10,0)
x - axis
Enter  any  point  in  the  form  of  (x , y) :  (0,-20)
y - axis
Enter  any  point  in  the  form  of  (x , y) :  (0,0)
Origin
Enter  any  point  in  the  form  of  (x , y) :  (10,20,30)
Not  a  point
Enter  any  point  in  the  form  of  (x , y) :  [10,20]
Quadrant
Enter  any  point  in  the  form  of  (x , y) :  [0,-25]
y - axis
Enter  any  point  in  the  form  of  (x , y) :  ()
Not  a  point
Enter  any  point  in  the  form  of  (x , y) :  {10,20}
Not  a  point
Enter  any  point  in  the  form  of  (x , y) :  (25,)
Not  a  point
Enter  any  point  in  the  form  of  (x , y) :  {10:20}
Not  a  point
'''




units = int(input('Enter units : '))

match units:
    case _ if 0 <= units <= 100:
        cost = units * 3.00

    case _ if 101 <=units <= 200:
        cost = 100 * 3.00 + (units- 100) * 3.50

    case _ if 201 <= units <= 400:
        cost = 100 * 3.00 + 100 * 3.50 + (units- 200) * 4.00

    case _ if 401 <= units <= 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units- 400) * 4.50

    case _:
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            300 * 4.50 +
            (units - 700) * 5.00
        )

print('Bill amount :', cost)

'''
output
Enter units : 1200
Bill amount : 5300.0
'''


#  Find  outputs
while  True:
	print('Hello')
print('Bye')

'''
output
Hello
prints 'Hello' infinity times
'''

#  Find  outputs
while  False:
	print('Hello')
print('Bye')

'''
output
Bye
'''
