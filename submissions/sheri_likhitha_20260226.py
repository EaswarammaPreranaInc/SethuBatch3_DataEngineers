import math
a=float(input("Enter 1st side : "))
b=float(input("Enter 2nd side : "))
c=float(input("Enter 3rd side : "))
if (a+b>c) and (a+c>b) and (b+c>a):
    if a==b==c:
     area=(math.sqrt(3))/4*a**2
     print("Equilateral triangle")
     print(f"Area : {area}")
    elif (a==b) or (b==c) or (a==c):
     perimeter=a+b+c
     print("isoscles triangle")
     print(f"perimrter : {perimeter}")
    else:
       s=(a+b+c)/2
       area=math.sqrt(s*(s-a)*(s-b)*(s-c))
       perimeter=a+b+c
       print("scalene triangle")
       print(f"Area : {area}")
       print(f"perimeter : {perimeter}")
else:
  print("Not a triangle")



import cmath
try:
    a=float(input("Enter value a : "))
    b=float(input("Enter value b : "))
    c=float(input("Enter value c : "))
    disc=b**2-4*a*c
    root1=(-b-cmath.sqrt(disc))/(2*a)
    root2=(-b+cmath.sqrt(disc))/(2*a)
    if disc>0:
        print("Roots are real and distinct")
        print(f"Root1 : {root1.real}\nRoot2 : {root2.real}")
    elif disc==0:
        print("Roots are real and equal")
        print(f"Root1 : {root1.real}\nRoot2 : {root2.real}")
    else:
        print("Roots are imaginary (or) complex")    
        print(f"Root1 : {root1.real} + {abs(root1.imag)}j")   
        print(f"Root2 : {root2.real} + {abs(root2.imag)}j") 
except:
    print("values cannot be zero")



import math
x=float(input("Enter value x : "))
y=float(input("Enter value y : "))
r=float(input("Enter radius of circle : "))
dist=math.sqrt(x**2+y**2)
if dist<r:
    print("point is inside the circle")
elif dist<r:
    print("point is outside the circle")
else:
    print("point is on the circle")        



# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')			#'Bye'


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')    #error 'case_' can't be written in middle it should be at end
	case  2:
		print('Two')
print('Bye')


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')		#error 'case_' can't be in middle it makes remaining patterns unreachable
	case  _:  
		print('Bye')
print('End')


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')		#'Hyd'
	case  1:
		print('Sec')		#skipped
	case  1:
		print('Cyb')		#skipped
print('Bye')				#'Bye'


# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')		#'Book'
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')				#'Bye'


'''
1) What  are  the  outputs  if  input  is  -6 ? ---> # Hyd Sec Cyb
2) What  are  the  outputs  if  input  is  15  ?  ---># One Two Three
3) What  are  the  outputs  if  input  is  10.8  ?  ---># India China Usa
4) What  are  the  outputs  if  input  is  0  ?  ---># Hyd Sec Cyb
5) What  are  the  outputs  if  input  is  -10  ?  ---># One Two Three
6) What  are  the  outputs  if  input  is  7  ?  ---># Hyd Sec Cyb
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
print('Bye')				#'Bye'


'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> #quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> #x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->#y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---># origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> #not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---># quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---># y-axis
8) What  is  the  output  when  input  is  ()  ?  ---># not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---># not a point
10) What  is  the  output  when  input  is  (25,) ?  ---># not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---># not apoint
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
	print('Hello')   #Hello is printed multiple times
print('Bye') 		#it is not printed because not indented


#  Find  outputs
while  False:
	print('Hello')
print('Bye')             #Bye



units=int(input("Enter units: "))
match units:
    case u if u<= 100:
        cost=u*3.0
    case u if u<=200:
        cost=100*3.0+(u-100)*3.5
    case u if u<=400:
        cost=100*3.0+100*3.5+(u-200)*4.0
    case u if u<=700:
        cost=100*3.0+100*3.5+200*4.0+(u-400)*4.5
    case u:
        cost=100*3.0+100*3.5+200*4.0+300*4.5+(u-700)*5.0
print(f"Bill amount : {cost}")                        
          
            




       
                
    
   