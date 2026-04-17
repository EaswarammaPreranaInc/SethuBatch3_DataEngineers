print("program  to  determine  three  sides  form  a  triangle  or  not")
import math
x=int(input("Enter 1st side"))
y=int(input("Enter 2nd side"))
z=int(input("Enter 3rd side"))
if(x+y>z and y+z>x and x+z>y):
    if(x==y==z):
        print("Equilateral triangle")
        print(f"Area:{math.sqrt(3) / 4 * a ^ 2}")
    elif(x==y or y==x or x==z):
        print("Isosceles triangle")
        print(f"Perimeter:{a+b+c}")
    else:
        print("Scalene triangle")
        s=a+b+c
        print(f"Area:{math.sqrt(s * (s - a) * (s - b) * (s - c))}")

print("program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0")
x=int(input("Enter value of a:"))
if(a==0):
    print("value of a cannot be zero")
else:
    y=int(input("Enter 2nd side"))
    z=int(input("Enter 3rd side"))
    d=b**2-4*a*c
    if(d>0):
        print("Real and distinct")
        print(f"Root 1:{(-b + math.sqrt(d)) / (2*a)}")
        print(f"Root 2:{(-b - math.sqrt(d)) / (2*a)}")
    elif(d==0):
        print("Real and same")
        print(f"Root 1:{-b / (2*a)}")
        print(f"Root 2:{-b / (2*a)}")
    else:
        print("Complex or Imaginary")
        r=-b/(2*a)
        i= sqrt(-d) / (2*a)
        print(f"Root 1:{r}+{i}j")
        print(f"Root 2:{r}-{i}j")

        
print("program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.")
x=int(input("Enter value of x"))
y=int(input("Enter value of y"))
r=int(input("Enter radius of circle"))
d= math.sqrt(x ** 2 + y ** 2)
if(d>r):
    print("point is Outside the circle")
elif(d<r):
    print("point is inside the circle")
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
print('Bye')
#Output:Bye


''' # Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  :  #Error case should be at end 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')'''


# Find  outputs  (Home  work)
'''m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:  
		print('Bye')
print('End')'''
#Output:case _ are not allowed twice
#End


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
#Output:Hyd
#Bye

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
#Output:Book
#Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->
India
China
Usa
Bye
2) What  are  the  outputs  if  input  is  15  ?  --->
One
Two
Three
Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->
India
China
Usa
Bye 
4) What  are  the  outputs  if  input  is  0  ?  --->
Hyd
Sec
Cyb
Bye 
5) What  are  the  outputs  if  input  is  -10  ?  --->
One
Two
Thre
Bye 
6) What  are  the  outputs  if  input  is  7  ?  --->
Hyd
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
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->not a point 
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Not a point 
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Not a point 
8) What  is  the  output  when  input  is  ()  ?  --->Not a point 
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not a point 
10) What  is  the  output  when  input  is  (25,) ?  --->Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->
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


print("program  to  determine  bill  amount  and  input  is  units")
units = int(input('Enter  units :   '))  
match  True:
	case  _ if units <= 100:
				cost = units * 3.00
	case  _ if units <= 200:
				cost = 100 * 3.00 + (units - 100) * 3.50
	case  _ if units <= 400:
				cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
	case  _ if units <= 700:
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
	case  _:				
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print('Bill  amount  :  ' , cost)



#  Find  outputs
while  True:
	print('Hello')
print('Bye')
#it enters infinite loop since while(True) is always true the control never comes out

#  Find  outputs
while  False:
	print('Hello')
print('Bye')
#Output: Bye



        
        
    
    
