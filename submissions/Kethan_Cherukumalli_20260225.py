a = complex(input('Enter 1st complex number :  '))
b = complex(input('Enter 2nd complex number :  ')) 
print('Sum :', a+b)
print('Difference :', a-b)
print('Product :', a*b)
print('Division :', a/b)

-------------------------------------------------------

length = float(input('Enter length of triangle :  '))
breadth = float(input('Enter breadth of triangle :  '))
area = length*breadth
perimeter =  2 * (length + breadth)
print(f' Area : {area}\n Perimeter : {perimeter}' )

-------------------------------------------------------

from math import pi
radius = float(input('Enter radius :  '))
Volume = 4 / 3  *pi*  radius**3
print(f'Volume : {Volume:.2f}')

-------------------------------------------------------

p = float(input('Enter principle :  '))
t = float(input('Enter time :  ')) 
r = float(input('Enter rate of interest :  '))
SI = p*t*r/100
CI = p * (1  +  r  /  100) ** t  -  p
print(f' simple  interest : {SI:.2f}\n compound  interest : {CI:.2f}' )

-------------------------------------------------------

a = (input('Enter 1st input :  '))
b = (input('Enter 2nd input :  ')) 

print(F'before swap :   x={a}   y={b}')

c = a
a = b
b = c
print(F'after swap :   x={a}   y={b}')

-------------------------------------------------------

x = 25
y =  10
print(F'before swap :   x={x}   y={y}')
x = x + y
y = x - y
x = x - y
print(F'after swap :   x={x}   y={y}')

-------------------------------------------------------

x = 25
y =  10
print(F'before swap :   x={x}   y={y}')
x = x * y
y = x // y
x = x // y
print(F'after swap :   x={x}   y={y}')

-------------------------------------------------------

# Identify  error
else:
		print('else  suite')
print('Outside')

# NO IF STATEMENT
-------------------------------------------------------
# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

# NO COLON After IF CONDITION

-------------------------------------------------------

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

# NO COLON After ELSE STATEMENT

-------------------------------------------------------

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# SPACE/TAB IS MISSING

-------------------------------------------------------

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# INDENTATION ERROR

-------------------------------------------------------

# Identify  error
if  { }:
{
	print('One')
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

# STATEMENTS SHOULDN'T BE IN BRACES
-------------------------------------------------------

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# INDENTATION ERROR

-------------------------------------------------------

a = int(input('Enter 1st integer number :  '))
if a%2==0:
    print('Even Number')
else:
    print('Odd Number')

-------------------------------------------------------

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

#One
Two
Three
Bye


-------------------------------------------------------

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

#Hyd
Sec
Cyb
Bye

-------------------------------------------------------

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#Bye

-------------------------------------------------------

a =int(input('Enter 1st integer number :  '))

if a==1:
    print('January')
if a==2:
    print('February')
if a==3:
    print('March')    
if a==4:
    print('April')
if a==5:
    print('May')
if a==6:
    print('June')
if a==7:
    print('July')
if a==8:
    print('August')    
if a==9:
    print('September')
if a==10:
    print('October')
if a==11:
    print('November')
if a==12:
    print('December')


elif(a>12):
    print ('Input should be between 1 and 12')



-------------------------------------------------------

a =int(input('Enter any digit (0 - 9) :  '))

if a==0:
    print('Zero')

if a==1:
     print('One')
if a==2:
     print('Two')
if a==3:
     print('Three')    
if a==4:
     print('Four')
if a==5:
     print('Five')
if a==6:
     print('Six')
if a==7:
     print('Seven')
if a==8:
     print('Eight')    
if a==9:
     print('Nine')


else:
    if(a>9):
        print ('Invalid')


-------------------------------------------------------

a = int(input('Enter 4-digit year :  '))

if (a % 400 == 0):
    print('Leap Year')
else:
    if (a % 100 == 0):
        print('Not a Leap Year')
    else:
        if (a % 4 == 0):
            print('Leap Year')
        else:
            print('Not a Leap Year')   


-------------------------------------------------------

a= int(input('Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius:'))
if a==1:
    b = float(input('Enter celsius temperature:'))
    c =  1.8 * b + 32
    print('fahrenheit equivalent:', c)
    
else:
    if a==2:
             d = float(input('Enter fahrenheit temperature:'))
             e = (d - 32) / 1.8
             print('celsius equivalent:', e)
    else:
        print('Enter 1 or 2')


-------------------------------------------------------

a = int(input('Enter value of x co-ordinate :  '))
b = int(input('Enter value of y co-ordinate :  ')) 
if(a>0 and b>0):
    print('1st quadrant')
elif(a<0 and b>0):
    print('2nd quadrant')
elif(a<0 and b<0):
    print('3rd quadrant')
elif(a>0 and b<0):
    print('4th quadrant')
elif(a==0 and b!=0):
    print('x-axis')
elif(a!=0 and b==0):
    print('y-axis')
elif(a==0 and b==0):
    print('origin')


-------------------------------------------------------

a = 10
b = 20
c = 7

max=a
if b>max:
    max=b
elif c>max:
    max=c
    
min=a
if b<min:
    min=b
elif c<min:
    min=c
    
mid =(a+b+c) - (max + min)
print('largest input :', max)
print('smallest input :', min)
print('middle input :', mid)