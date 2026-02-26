# Find  outputs  (Home  work)
m = 4					#Bye
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')



# Identify  Error		
i = 2
match  i:
	case  1:
		print('One')
	case  _: 			#Name less objects are not allowed in the middle of the case it always at the end
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')



# Find  outputs  (Home  work)
m = 2
match  m:				 #Hello				
	case  1:			 #Bye
		print('One')		 #End
	case  _:  			 			
		print('Hello')
	case  _:  
		print('Bye')
print('End')



#  Find  outputs  (Home  work)
m = 1					#Hyd
match  m:				#Sec
	case  1:			#Cyb
		print('Hyd')		#Bye
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')


# Find  outputs  (Home  work)
ch = 'B'			#Book
match  ch:			#Bye
	case   'A':		
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')




1) What  are  the  outputs  if  input  is  -6 ? --->Hyd </n> Sec</n>Cyb</n>Bye
2) What  are  the  outputs  if  input  is  15  ?  --->One</n> Two</n>Three</n>Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India</n> China</n>Usa</n>Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd</n>Sec</n>Cyb</n>Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One</n> Two</n>Three</n>Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd </n> Sec</n>Cyb</n>Bye


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




#1 What is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->Quadrant
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y - axis
8) What  is  the  output  when  input  is  ()  ?  --->
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Quadrant
10) What  is  the  output  when  input  is  (25,) ?  --->
11) What  is  the  output  when  input  is  {10 : 20} ?  --->

 
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




#  Find  outputs	#Hello</n>Bye
while  True:
	print('Hello')
print('Bye')


#  Find  outputs
while  False:		#Bye
	print('Hello')
print('Bye')


#Write  a  program  to  determine  three  sides  form  a  triangle  or  not

import math
a=int(input('Enter 1st side :'))
b=int(input('Enter 2nd side :'))
c=int(input('Enter 3rd side :'))
if((a+b)>c and (b+c)>a and (a+c)>b):
    if(a==b or b==c or a==c):
        print('Isoscles triangle')
        perimeter = a+b+c
        print('perimeter=',perimeter)
    else:
        if(a!=b and b!=c and c!=a): 
            print('Scalane triangle')
            Area =math.sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))
            print('Area =',Area)
            perimeter =a + b + c
            print('perimeter =',perimeter)
        else:    
            if(a==b and b==c and a==c):
                print('Equilateral triangle')
                Area=math.sqrt(3) / 4 * a ** 2
                print('Area =',Area)
            else:
                print('Not a triangle')
else:
    print('Not a triangle') 



#Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

try:
    import math
    a=int(input('Enter value of a :'))
    if(a!=0):
        b=int(input('Enter value of b :'))
        c=int(input('Enter value of c :'))
        discriminant= b**2 - 4*a*c
    if(discriminant>0):
        print('Roots are real and distinct')
        Root1=(-b+math.sqrt(discriminant)) / (2*a)
        Root2=(-b-math.sqrt(discriminant))/ (2*a)
        print('Root 1:', Root1)
        print('Root 2:', Root2)
    elif(discriminant==0):
        print('Roots are real and equal')
        Root1=  -b / (2*a)
        Root2=  -b / (2*a)
        print('Root1',Root1)
        print('Root1',Root1)
    elif(discriminant<0):
        print('Roots are Complex  (or)  Imaginary  roots')
        Real=  -b / (2*a)
        imag=(math.sqrt(-discriminant)) / (2*a)
        Root1 = complex(Real+imag,0) 
        Root2 = complex(Real-imag,0) 
        print(F'Root1 = {Real}+{imag}j')
        print(F'Root2 = {Real}+{imag}j')
    else:
        print('')
except:
    print('Value of a cannot be 0')
    
    
   
 
#Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

try:
    import math
    x=int(input('Enter value of x :'))
    y=int(input('Enter value of y :'))
    r=int(input('Enter radius of circle :'))
    distance = math.sqrt(x**2 + y**2)
    if(distance>r):
        print('Outside  the  circle')
    elif(distance < r):
        print('Inside  the  circle')
    elif(distance==r):    
        print(' Point is on  the  circle')
    else:
        print('Not a circle')
except:
    print('Number should be an integer')



#Write  a  program  to  determine  bill  amount  and  input  is  units


units = int(input('Enter  units :   '))

match units:
    case 100:
        cost = 100*3.00
    case 200:
        cost = 100 * 3.00 + 100 * 3.50
    case 300:
        cost = 100 * 3.00 + 100 * 3.50 + 100 * 4.00
    case 400:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00
    case 500:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 100 * 4.50
    case 600:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 200 * 4.50
    case 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50
    case _:
        if units > 700:
            extra_units = units - 700
            extra_units_cost = extra_units * 5.00
            cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + extra_units_cost
print('Bill  amount  :  ', cost)
print('extra_units ', extra_units)

