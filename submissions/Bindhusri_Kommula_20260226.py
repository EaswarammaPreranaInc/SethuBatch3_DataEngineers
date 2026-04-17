write a program to determine three sides form a triangle or not 

import math
a=float(input('Enter 1st side: '))
b=float(input('Enter 2nd side: '))
c=float(input('Enter 3rd side: '))
if((a+b)>c and (b+c)>a and (c+a)>b):
    if(a==b==c):
        print('Equilateral Triangle')
        print(f'Area : {math.sqrt(3)/4*(a**2):.2f}')
    elif(a==b or b==c or c==a):
        print('Isoscles Triangle')
        print('Perimeter : ',a+b+c)
    elif(a!=b!=c):
        print('Scalene Triangle')
        s=(a+b+c)/2
        print('Area : ', math.sqrt(s*(s-a)*(s-b)*(s-c)))
        print('Perimeter : ',a+b+c)
else:
    print('Not a Triangle')

output:

Enter 1st side: 3
Enter 2nd side: 4
Enter 3rd side: 5
Scalene Triangle
Area :  6.0
Perimeter :  12.0

Enter 1st side: 7
Enter 2nd side: 8
Enter 3rd side: 7
Isoscles Triangle
Perimeter :  22.0

Enter 1st side: 7
Enter 2nd side: 7
Enter 3rd side: 7
Equilateral Triangle
Area : 21.22

Enter 1st side: 7
Enter 2nd side: 8
Enter 3rd side: 16
Not a Triangle


write a program to determine roots of a quadratic equation a*x^2+b*x+c=0 where a!=0


import math
a=float(input('Enter value of a: '))
if(a==0):
    print('Value of a cannot be 0')
else:
    b=float(input('Enter value of b: '))
    c=float(input('Enter value of c: '))
    disc=b**2-(4*a*c)
    if(disc>0):
        print('Roots are Real and distinct')
        root1=(-b+math.sqrt(disc))/(2*a)
        root2=(-b-math.sqrt(disc))/(2*a)
        print(f'Root1: {root1:.2f}')
        print('Root2: ',root2)
    elif(disc==0):
       print('Roots are Real and Equal')
       root=-b/(2*a)
       print('Root1 : ',root)
       print('Root2 : ',root)
    elif(disc<0):
       print('Roots are Imaginary or Complex')
       real=-b/(2*a)
       imag=math.sqrt(-disc)/(2*a)
       root1=complex(real,imag)
       root2=complex(real,-imag)
       print('Root1 : ',root1)
       print('Root2 : ',root2)

output:

Enter value of a: 5
Enter value of b: 6
Enter value of c: 5
Roots are Imaginary or Complex
Root1 :  (-0.6+0.8j)
Root2 :  (-0.6-0.8j)

Enter value of a: 5
Enter value of b: 10
Enter value of c: 5
Roots are Real and Equal
Root1 :  -1.0
Root2 :  -1.0

Enter value of a: 3
Enter value of b: 10
Enter value of c: 3
Roots are Real and distinct
Root1: -0.33
Root2:  -3.0

Enter value of a: 0
Value of a cannot be 0


write a program to determine a point(x,y) lies inside, outside or on the circle. Center is origin and radius is 'r'

import math
x=int(input('Enter value of x: '))
y=int(input('Enter value of y: '))
radius=int(input('Enter radius of circle: '))
distance=math.sqrt(x**2+y**2)
if(distance>radius):
    print('point is Outside the circle')
elif(distance<radius):
    print('Point is Inside the circle')
else:
   print('point is on the circle')


output:

Enter value of x: 3
Enter value of y: 4
Enter radius of circle: 5
point is on the circle


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

Output: 
Bye


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:    # cannot be used in middle, it should be used at end
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')


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

Output:
Hello
End


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

Output:
Hyd
Bye


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

Output:
Book
Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd
                                                     Sec
                                                     Cyb
                                                     Bye
2) What  are  the  outputs  if  input  is  15  ?  --->One
                                                      Two
                                                      Three
                                                      Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India
                                                        china
                                                        Usa
                                                        Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd
                                                     Sec
                                                     Cyb
                                                     Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One
                                                      Two
                                                      Three
                                                      Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd
                                                     Sec
                                                     Cyb
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-aixs
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y-aixs
8) What  is  the  output  when  input  is  ()  ?  --->Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not  a  point
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

Write  a  program  to  determine  bill  amount  and  input  is  units

units = int(input('Enter  units :   '))

match units:
    case u if u <= 100:
        total = u * 3.00

    case u if u <= 200:
        total = 100 * 3.00 + (u - 100) * 3.50

    case u if u <= 400:
        total = 100 * 3.00 + 100 * 3.50 + (u - 200) * 4.00

    case u if u <= 700:
        total = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (u - 400) * 4.50

    case _:
        total = (100 * 3.00 +
                 100 * 3.50 +
                 200 * 4.00 +
                 300 * 4.50 +
                 (units - 700) * 5.00)

print('Bill  amount  :  ', total)


output:

Enter  units :   1200
Bill  amount  :   5300.0


#  Find  outputs
while  True:
	print('Hello')   # prints Hello continuously 
print('Bye') # Bye


#  Find  outputs
while  False:
	print('Hello')
print('Bye')

Output:
Bye
