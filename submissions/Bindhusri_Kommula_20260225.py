Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

a=complex(input('Enter first complex number : '))
b=complex(input('Enter second complex number : '))
print(f' sum : {a+b}')
print(f' Difference : {a-b}')
print(f' product : {a*b}')
print(f' Division : {a/b}')

output:

Enter first complex number : 3+4j
Enter second complex number : 5+6j
 sum : (8+10j)
 Difference : (-2-2j)
 product : (-9+38j)
 Division : (0.6393442622950819+0.03278688524590165j)


Write  a  program  to  determine  area  and  perimeter  of  rectangle

a=float(input('Enter length of rectangle: '))
b=float(input('Enter breadth of rectangle: '))
print(f'Area : {a*b}')
print(f'perimeter: {2*(a+b)}')

output:

Enter length of rectangle: 4
Enter breadth of rectangle: 5
Area : 20.0
perimeter: 18.0


Write  a  program  to  determine  volume  of  a  sphere

import math
r=float(input('Enter radius: '))
print(f'Volume: {(4/3)*math.pi*(r**3):.2f}')

output:

Enter radius: 3.5
Volume: 179.59


Write  a  program  to  determine  simple  interest  and  compound  interest

p=float(input('Enter principle: '))
t=float(input('Enter time : '))
r=float(input('Enter rate of interest : '))
print(f'simple interest: {(p*t*r)/100}')
print(f'compund interest: {(p*(1+r/100)**t-p):.2f}')

output:

Enter principle: 10000
Enter time : 3
Enter rate of interest : 7.5
simple interest: 2250.0
compund interest: 2422.97


Write  a  program  to  swap  values  of  two   objects   using  3rd  object

a=(input('Enter 1st input: '))
b=(input('Enter 2nd input : '))
print(f'Before swap: x=\'{a}\'  y=\'{b}\'')
temp=a 
a=b
b=temp 
print(f'After swap: x=\'{a}\' y=\'{b}\'')

output:

Enter 1st input: 25
Enter 2nd input : Hyd
Before swap: x='25'  y='Hyd'
After swap: x='Hyd' y='25'

Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

a=int(input('Enter 1st input: '))
b=int(input('Enter 2nd input : '))
print(f'Before swap: x={a}  y={b}')
a=a+b 
b=a-b 
a=a-b
print(f'After swap: x={a} y={b}')

output:

Enter 1st input: 25
Enter 2nd input : 10
Before swap: x=25  y=10
After swap: x=10 y=25


Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

a=float(input('Enter 1st input: '))
b=float(input('Enter 2nd input : '))
print(f'Before swap: x={a}  y={b}')
a=a*b 
b=a/b 
a=a/b
print(f'After swap: x={a} y={b}')

output:

Enter 1st input: 25
Enter 2nd input : 10
Before swap: x=25.0  y=10.0
After swap: x=10.0 y=25.0


# Identify  error
else: # no if statement so error
		print('else  suite')
print('Outside')


# Identify  error
if  9 > 5  # no :  after condition so error 
	print('Hello')
print('Bye')


# Identify  error
if  (10,20,15):
print('Hyd')    # after : next line there should tab or space, so indentation error
else:
print('Sec')  # after : next line there should be tab or space, so indentation error


# Identify  error
if  ():
			print('Hyd') # we get  indentation error
	else:  # it should in same column, so indentation error
					print('Sec')
print('Bye')


# Identify  error
if  { }:
{         # there should not be {} because it represents set, so error
	print('One')
	print('Two')
	print('Three')
}
else:
{           # there should not be {} because it represents set, so error
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')


# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:     # error because no tab space before if condition 
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:  # error because no tab space before if condition 
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a=int(input('Enter any input: '))
if a%2==0:
    print('Even number')
else:
    print('Odd number')

output:

Enter any input: 26
Even number


# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')

Output:
One 
Two
Three
Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

Output:
Hyd
Sec
Cyb 
Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

Output: 
Bye


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


try:
    a=int(input('Enter month number(1-12): '))
    if a==1:
        print('January')
    elif a==2:
        print('February')
    elif a==3:
        print('March')
    elif a==4:
        print('April')
    elif a==5:
        print('May')
    elif a==6:
        print('June')
    elif a==7:
        print('July')
    elif a==8:
        print('August')
    elif a==9:
        print('September')
    elif a==10:
        print('October')
    elif a==11:
        print('November')
    elif a==12:
        print('December')
    else:
        print('Input should be between 1 and 12')
except:
    print('Input should be an integer')



output:

Enter month numberr(1-12): 6
June

Enter month numberr(1-12): 13
Input should be between 1 and 12

Enter month number(1-12): 5.0
Input should be an integer

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

a=int(input('Enter any digit(0-9): '))
if a==1:
    print('One')
else:
    if a==2:
        print('Two')
    else:
        if a==3:
            print('Three')
        else:
            if a==4:
                print('Four')
            else:
                if a==5:
                    print('Five')
                else:
                    if a==6:
                        print('six')
                    else:
                        if a==7:
                            print('Seven')
                        else:
                            if a==8:
                                print('Eight')
                            else:
                                if a==9:
                                    print('Nine')
                                else:
                                    print('Invalid')
    
output:

Enter any digit(0-9): 4
Four

Write  a  program  to  test  year  is  leap  year  or  not

year=int(input('Enter 4-digit year: '))
if(year%4==0 and year%100!=0) or (year%400==0):
    print('Leap year')
else:
    print('Not a Leap year')

output:

Enter 4-digit year: 1992
Leap year


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a=eval(input('Enter 1st number: '))
b=eval(input('Enter 2nd number: '))
c=eval(input('Enter 3rd number: '))
if a>b and a>c:
    print('Larger input: ',a)
elif b>c:
    print('Larger input: ',b)
else:
    print('Larger input: ',c)

output:

Enter 1st number: 10
Enter 2nd number: 20
Enter 3rd number: 39
Larger input:  39


Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

a=int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if a==1:
    c=float(input('Enter celsius tempature: '))
    f=(1.8*c)+32
    print(f'Celsius equivalent: {f:.1f}')
elif a==2:
    f=float(input('Enter fahrenheit tempature: '))
    c=(f-32)/1.8
    print(f'Fahrenheit equivalent: {c:.2f}')

output:

Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : 2
Enter fahrenheit tempature: 100
Fahrenheit equivalent: 37.78

Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : 1
Enter celsius tempature: 30
Celsius equivalent: 86.0


Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

x=int(input('Enter value of x co-ordinate : '))
y=int(input('Enter value of y co-ordinate : '))
if x>0 and y>0:
    print('1st quadrant')
elif x>0 and y<0:
    print('4th quadrant')
elif x<0 and y>0:
    print('2nd quadrant')
elif x<0 and y<0:
    print('3rd quadrant')

(or) 

x=int(input('Enter value of x co-ordinate : '))
y=int(input('Enter value of y co-ordinate : '))
if x>0:
    if y>0:
        print('1st quadrant')
    else:
        print('4th quadrant')
else:
    if y>0:
        print('2nd quadrant')
    else:
        print('3rd quadrant')

output:

Enter value of x co-ordinate : -10
Enter value of y co-ordinate : 20
2nd quadrant


Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers


a=int(input('Enter 1st input : '))
b=int(input('Enter 2nd input : '))
c=int(input('Enter 3rd input : '))
max=a
if b>max:
    max=b
if c>max:
    max=c
    
min=a
if b<min:
    min=b
if c<min:
    min=c
    
middle=(a+b+c)-(max+min)
print('Largest input: ',max)
print('Smallest input : ',min)
print('middle input : ', middle)
    
    
output:

Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 7
Largest input:  20
Smallest input :  7
middle input :  10








