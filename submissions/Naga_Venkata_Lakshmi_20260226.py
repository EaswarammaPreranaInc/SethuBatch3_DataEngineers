import math
a = int(input("Enter 1st side:  "))
b = int(input("Enter 2nd side:  "))
c = int(input("Enter 3rd side:  "))
if a + b  > c and a + c > b and b +c > a:
    print("Triangle")
    
    if a == b == c:
        print("Equilateral Triangle")
        Area = (math.sqrt(3) / 4)* (a**2)
        print(f"Area: {Area}")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
        Perimeter = a + b + c
        print(f"Perimeter: {Perimeter}")
    else:
        print("Scalene Triangle")
        s = (a +b +c) / 2
        Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        Perimeter = a + b + c
        print(f"Area: {Area}")
        print(f"Perimeter: {Perimeter}")
else:
    print("Not a triangle")





import math
a = int(input("Enter value os a:  "))
b = int(input("Enter value of b:  "))
c = int(input("Enter value of c:  "))
disc = b ** 2 - 4*a*c

if disc > 0:
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    print("Real and distinct roots:")
    print("Root 1 :", root1)
    print("Root 2 :", root2)
elif disc == 0:
    root = -b / (2*a)
    print("Real and same roots:")
    print("Root:", root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-disc) / (2*a)
    root1 = complex(real_part, imag_part)
    root2 = complex(real_part, -imag_part)
    print("Complex roots:")
    print("Root 1 :", root1)
    print("Root 2 :", root2)




import math
x = eval(input("Enter value of x: "))
y = eval(input("Enter value of y: "))
r = eval(input("Enter radius of circle: "))
distance = math.sqrt(x**2 + y**2)

if distance > r:
    print("Point is outside the circle")
elif distance < r:
    print("Point is inside the circle")
else:
    print("Point is on the circle")



units = int(input('Enter units :  '))

match units:
    case units if units <= 100:
        cost = units * 3.00
    case units if 100 < units <= 200:
        cost = 100 * 3.00 + (units - 100)*3.50
    case units if 200 < units <= 400:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case units if 400 < units <= 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:
        cost = 100* 3.00 + 100 * 3.50 + 200 * 4.00 + 300 *4.50 + (units - 700) *5.00
        
print('Bill amount : ' ,  cost) 



# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') #Bye



# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:   #Error because case_ should be last
		print('None of   the  above')
	case  2: #Error because it is placed case_:
		print('Two')
print('Bye')




# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello') #Hello
	case  _:  
		print('Bye')
print('End')  #End



#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') #Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')  #Bye



# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') #Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') #Bye



1) What  are  the  outputs  if  input  is  -6 ? --->Hyd
                                                    Sec
                                                    Cyb
                                                    Bye
2) What  are  the  outputs  if  input  is  15  ?  --->One
                                                      Two
                                                      Three
                                                      Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India
                                                        China
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
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd
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




1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->No a point
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




#  Find  outputs
while  True:
	print('Hello') #Hello
                        Bye
                        Hello
                        Bye
                        Hello
                        Bye  continues indefinitely because confition is true
print('Bye')





#  Find  outputs
while  False:
	print('Hello')
print('Bye') #Bye

  







