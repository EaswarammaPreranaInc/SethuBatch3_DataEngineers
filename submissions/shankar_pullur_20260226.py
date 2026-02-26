'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side
'''
import math
def triangle():
    try:
        a=float(input("enter 1th side : "))
        b=float(input("enter 2th side : "))
        c=float(input("enter 3th side : "))
        if(a==b and a==c):
            print('it  is  an  equilateral  triangle')
            print(f'area : {(math.sqrt(3)/4)*a**2:.2f}')
        elif(a==b or a==c):
            print('it  is  an  isosceles  triangle')
            print(f'permeter : {a+b+c}')
        else:
            s=(a+b+c)/2
            print('it  is  an  scalene  triangle')
            print(f'permeter : {a+b+c}')
            print(f'area : {math.sqrt(s * (s - a) * (s - b) * (s - c)):.2f}')
    except:
        print("enter integer values or float")
        

#triangle()
'''Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  ---> b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  --->   (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  --->  (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j
'''
def equation():
    
    a=float(input("enter 1th side : "))
    b=float(input("enter 2th side : "))
    c=float(input("enter 3th side : "))
    if(a==0):
        print('a value cant be zero')
        return
    dis=b**2-(4*a*c)
    if(dis>0):
        print("roots are real and distinct")
        root1= (-b + math.sqrt(dis)) / (2*a)
        root2=(-b - math.sqrt(dis)) / (2*a)
        print(f'root1 : {root1}\nroot2 : {root2}')
    elif(dis==0):
        print("roots are real and equal")
        root= -b /(2*a)
        print(f'root1 : {root}\nroot2 : {root}')
    else:
        print("roots are imagianary")
        r=-b / (2*a)
        i= math.sqrt(-dis) / (2*a)
        print(f'root1 : {complex(r,i)}\nroot2 : {complex(r,-i)}')
#equation()
        
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

def radius():
    x=float(input("enter x : "))
    y=float(input("enter y : "))
    r=float(input("enter radius : "))
    d=math.sqrt(x**2+y**2)
    if(d>r):
        print("point is Outside the circle")
    elif(d==r):
        print("point is on the circle")
    else:
        print("point is inside the circle")

#radius()



m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')              # Bye

i = 2
match  i:
	case  1:
		print('One')
	#case  _:                               #error
	#	print('None of   the  above')
	case  2:
		print('Two')


'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units					Rs. 3.00 / unit

Next  100  units				Rs. 3.50 / unit

Next  200  units		    	Rs. 4.00 / unit

Next  300  units				Rs. 4.50 / unit

Above  700  units				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else

units = int(input('Enter  units :   '))  
match  ???:
	case  ??:
				cost = 
	case  ???:
				cost =  
	case  ???:
				cost = 
	case  ???:
				cost = 
	case  ???:				
				cost = 
print('Bill  amount  :  ' , cost)'''

def bill():
    units = int(input("Enter units: "))

    match units:
        case u if u <= 100:
            cost = u * 3.00

        case u if u <= 200:
            cost = 100 * 3.00 + (u - 100) * 3.50

        case u if u <= 400:
            cost = (100 * 3.00 +
                100 * 3.50 +
                (u - 200) * 4.00)

        case u if u <= 700:
            cost = (100 * 3.00 +
                100 * 3.50 +
                200 * 4.00 +
                (u - 400) * 4.50)

        case _:
            cost = (100 * 3.00 +
                100 * 3.50 +
                200 * 4.00 +
                300 * 4.50 +
                (units - 700) * 5.00)

    print("Bill amount:", cost)
#bill()