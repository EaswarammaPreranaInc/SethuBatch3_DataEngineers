1.
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

Program:
  '''import math
 try:
   a = float(input("Enter side a: "))
   b = float(input("Enter side b: "))
   c = float(input("Enter side c: "))
   if a == b and b == c:
        print(" Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area =", area)
    else:
        if a == b or b == c or a == c:
            print(" Isosceles Triangle.")
            perimeter = a + b + c
            print("Perimeter =", perimeter)
      else:
            print("It is a Scalene Triangle.")
            perimeter = a + b + c
            s = (a + b + c) / 2
           area = math.sqrt(s * (s - a) * (s - b) * (s - c))
           print("Perimeter =", perimeter)
           print("Area =", area)
except:
    print("The given sides do NOT form a triangle.")

2.'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
1) What  is  the  value  of  discriminant ?  ---> b ^ 2 - 4ac
2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct   What  is  the  formula  for  root1  ?  --->   (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  --->  (-b - sqrt(disc)) / 2a
3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a
4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j
''
Program:

try:
	a = float(input('Enter  value  of  a  :  '))
	b = float(input('Enter  value  of  b  :  '))
	c = float(input('Enter  value  of  c  :  '))
	if  a != 0:
		disc = b ** 2 - 4 * a * c
		if  disc > 0:
			print('Roots  are  Real  and  Distinct')
			root1 = (-b + disc ** 0.5) / (2 * a)
			root2 = (-b - disc ** 0.5) / (2 * a)
			print('Root1  =  ', root1)
			print('Root2  =  ', root2)
		elif  disc == 0:
			print('Roots  are  Real  and  Same')
			root = -b / (2 * a)
			print('Root1  =  ', root)
			print('Root2  =  ', root)
		else:
			print('Roots  are  Complex  (Imaginary)')
			real_part = -b / (2 * a)
			imag_part = (-disc) ** 0.5 / (2 * a)
			root1 = complex(real_part, imag_part)
			root2 = complex(real_part, -imag_part)
			print('Root1  =  ', root1)
			print('Root2  =  ', root2)
	else:
	 print('Coefficient  a  should  not  be  zero')
except:
	print('Input  should  be  a  number')


3.
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'
1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)
2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle
3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle
4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle

Program:

try:
	x = float(input('Enter  value  of  x  :