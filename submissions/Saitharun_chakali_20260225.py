1) Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

code:
val1=complex(input("Enter the 1st complex number:"))
val2=complex(input("Enter the 2nd complex number:"))
print(f"Addition: {val1+val2}")
print(f"subtract: {val1-val2}")
print(f"multiply: {val1*val2}")
print(f"division: {val1/val2}")
									   


2) Write  a  program  to  determine  area  and  perimeter  of  rectangle ?

Code:
l= float(input('Enter length : '))
b=float(input('Enter breadth : '))
print("Area of Rectangle :",l*b)
print("Perimeter of Rectngle : ",2*(l+b))


3) Write  a  program  to  determine  volume  of  a  sphere ?

code:
import math
r=float(input("Enter radius : "))
volume= (4/3)*math.pi*r**3
print("Volume of Sphere : ",round(volume,2))

4) Write  a  program  to  determine  simple  interest  and  compound  interest ?

code:
p = float(input("Enter principle amount : "))
t = float(input("Enter time in years : "))
r = float(input("Enter the rate of interest : "))
si=(p*t*r)/100
ci=p*((1+r/100)**t)-p
print(f"Simple Interest = {si}")
print(f"Compound Interest = {ci}")



5) Write  a  program  to  swap  values  of  two   objects   using  3rd  object ?

code:
x = input("Enter 1st input : ")
y =c

temp= x
x=y
y=temp
print(f"Before swap x : {x}    y : {y}")
print(f"After swap x  : {y}     y : {x}")


6) Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

code:
x = input("Enter 1st input : ")
y = input("Enter 1st input : ")

x=x+y
y=x-y
x=x-y
print(f"Before swap x : {x}    y : {y}")
print(f"After swap x  : {y}     y : {x}")




7) Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

code:
x = float(input("Enter 1st input : "))
y = float(input("Enter 1st input : "))
x=x*y
y=x/y
x=x/y
print(x,y)
print(f"Before swap x : {x}    y : {y}")
print(f"After swap x  : {y}     y : {x}")



8) # Identify  error
else:                                         # else used without if
		print('else  suite')
print('Outside')



9) # Identify  error
if  9 > 5                  # no ':'at the end of the condtion
	print('Hello')
print('Bye')


10) # Identify  error
if  9 > 12:
	print('Hyd')
else                      # no ':' after else condition

	print('Sec')


11) # Identify  error
if  (10,20,15):              
print('Hyd')      # indentation error
else:
print('Sec')      # indentation error


12) # Identify  error
if  ():                                                      # invalid syntax
			print('Hyd')
	else:
					print('Sec')         # indentation error
print('Bye')




13) # Identify  error
if  { }:                      # no condition
{
	print('One')          # invalid syntax {}
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')        
}
print('Bye')



14) # Identify  error     
if  ():                           # no condition
	print('One')
	print('Two')
	print('Three')
else:
if  []:                         # indentation error
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:                         # indentation error
	print('Seven')
	print('Eight')
	print('Nine')
else:                           # indentation error
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')






15) Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement?

code:
x=int(input("Enter a number : "))
if x%2==0: 
    print(x,"is Even number")
else:
    print(x,"is odd number")




16) Find outputs  (Home  work)

if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')                    
        print('Two')                    
        print('Three')                  
print('Bye')                            

output : One 
         Two
         Three
         Bye


17) Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}: 
        print('Hyd')                  
        print('Sec')                    
        print('Cyb')                  
print('Bye')                            

output : Hyd
         Sec
         Cyb
         Bye

18) Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')                          

Output : Bye


19)  Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif ? 


Code:

m = int(input("Enter month number (1-12): "))

if m == 1:
    print("January")
elif m == 2:
    print("February")
elif m == 3:
    print("March")
elif m == 4:
    print("April")
elif m == 5:
    print("May")
elif m == 6:
    print("June")
elif m == 7:
    print("July")
elif m == 8:
    print("August")
elif m == 9:
    print("September")
elif m == 10:
    print("October")
elif m == 11:
    print("November")
elif m == 12:
    print("December")
else:
    print("Invalid month number")



20) Write  a  program  to  test  year  is  leap  year  or  not

code:

n=int(input("Enter the 4-digit year : "))

if (n%4 == 0 or n%100 !=0) and (n%400==0):
    print(n,"is a  leap year")
else:
    print(n,"is not a leap year")




21) Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else


code:

n1=int(input("Enter the 1st number : "))
n2=int(input("Enter the 2nd number : "))
n3=int(input("Enter the 3rd number : "))

if n1>n2 and n1>n3:
    print(n1,"is largest number among three")
elif n2>n1 and n2>n3:
    print(n2,"is largest number among three")
else:
    print(n3,"is largest number among three")
    


22) Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8



code: 

a = int(input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius : "))

if a==1:
    temp = float(input("Enter Celsius temperature : "))
    print("Fahrenheit Equivalent :",1.8*temp+32)
elif a==2:
    temp = float(input("Enter Fahrenheit temperature :"))
    print("Celsius Equivalent :",(temp-32)/1.8)
else:
    print("invalid temperature ")




23) Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif


code:

x= float(input('Enter value of x co-ordinate :'))
y= float(input('Enter value of y co-ordinate :'))
if x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
elif x>0 and y<0:
    print("4th Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x==0 and y!=0:
    print("On y axis")
elif x!=0 and y==0:
    print("On x axis")
elif x==0 and y==0:
    print("Origin") 
else:
    print("Invalid inputs")






24) Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program



Code:

a=int(input("Enter input 1:"))
b=int(input("Enter input 2:"))
c=int(input("Enter input 3:"))

max = a
min = a

if b>max:
    max=b
if c>max:
    max=c

if b<min:
    min =b
if c<min:
    min =c

mid = (a+b+c)-(min+max)

print("Smallest input : ", min)
print("Middle input : ",mid)
print("largest input : ",max)
