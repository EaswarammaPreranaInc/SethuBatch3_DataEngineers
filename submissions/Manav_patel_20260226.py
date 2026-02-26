import math
a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))

if(a+b<c or a+c<b or b+c<a):
    print("not a triangle.")
elif(a==b and b==c):
    print("The triangle is equilateral.")
    print("The area of the triangle is: ", (3**0.5/4)*a**2)
elif(((a==b and a!=c ) or(a==c and a!=b) or ((b==c and b!=a) or (b==c and c!=a)))):
    print("the triangle is issocles")
    print(f'perimeter of triangle is {a+b+c}')
elif((a!=b and a!=c and b!=c)):
    print("The triangle is scalene.")
    s=(a+b+c)/2
    f=s*((s-a)*(s-b)*(s-c))
    area=math.sqrt(s*(f))
    print("The area of the triangle is: ", area)
    print(f'perimeter of triangle is {a+b+c}')
    
#quadratic equation
a=int(input("enter value of a: "))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
disc=b*b-4*a*c
if(a==0):
    print("a value can not be zero")
elif(disc>0):
    print("roots are real and distinct")
    x=math.sqrt(disc)
    root1=(-b+x)/(2*a)
    root2=(-b-x)/(2*a)
    print(f'root1 : {'%.1f' %root1} ')
    print(f'root2 : {'%.1f' %root2}' )
elif(disc==0):
    print("roots are real and same")
    root=-b/(2*a)
    print(f'root 1 : {root}')
    print(f'root 2: {root}')
else:
    print("root are imaginary")
    x=-b/(2*a)
    y=math.sqrt(-disc)/(2*a)
    print(f'root 1 : {x}+{'%.1f' %y}j')
    print(f'root 2 : {x}-{'%.1f' %y}j')
    
    
# circle
x=int(input("enter x value"))
y=int(input("enter y value"))
r=int(input("enter the radius of circle: "))
dist=math.sqrt(x**2+y**2)
if(dist<r):
    print("the point is inside the circle")
elif(dist==r):
    print("the point is on the circle")
else:    
    print("the point is outside the circle")

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')#"bye" will be printed in all cases because it is outside the match statement.


    # Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: #this should be in last
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')#"bye"

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')#unreachable statement
print('End') #end will be printed


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')#Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')#Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')#Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')#Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> hyd sec cyb
2) What  are  the  outputs  if  input  is  15  ?  --->one two three
3) What  are  the  outputs  if  input  is  10.8  ?  --->India CHina Usa
4) What  are  the  outputs  if  input  is  0  ?  --->hyd sec cyb
5) What  are  the  outputs  if  input  is  -10  ?  --->one two three
6) What  are  the  outputs  if  input  is  7  ?  --->hyd sec cyb
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
print('Bye')#Bye

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->not a point
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->not a point
4) What  is  the  output  when  input  is  (0 , 0) ?  --->origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y-axis
8) What  is  the  output  when  input  is  ()  ?# not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->#quadrant
10) What  is  the  output  when  input  is  (25,) ?  --->not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->not a point
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
'''
x=100
a=[0]*5
i=0
py=0
n=int(input("please enter unit:"))
y=100
cost=0
copyn=n
while(n>0 and i<5):
    if(py>1):
        x=x+y
    n=n-x
    a[i]=i+3
    i+=1
    py+=1
for i in range(len(a)):
    match a[i]:
        case 3:
            x=100 if copyn> 100 else copyn 
            # print(x)
            cost+=3.0*x
            copyn-=x
            print(cost)
        case 4:
            x=100 if copyn> 100 else copyn
            cost+=3.50*x
            copyn-=x
            
            print(cost)
        case 5:
            x=200 if copyn> 200 else copyn
            cost+=4.0*x
            copyn-=x
            
            print(cost)
        case 6:
            x=300 if copyn> 300 else copyn 
            cost+=4.5*x
            copyn-=x
            
            # print(cost)
        case 7:
            cost+=5.0*copyn
            print(cost)
            
            
print('Bill  amount  :  ' , cost)

#  Find  outputs
while  True:
	print('Hello') #it will print untill we stop the program 
print('Bye')

#  Find  outputs
while  False:
	print('Hello')# it will not print because condition is false
print('Bye')#Bye

    
    





    