'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61										   
'''
a=complex(input('Enter first complex number : '))
b=complex(input('Enter second complex number : '))
print(F'sum={a+b}')
print(F'Difference={a-b}')
print(F'product={a*b}')
print(F'Division={a/b}')
________________________________________________________________________________________________________________________________________________

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l=float(input('Enter the length of Rectangle : '))
b=float(input('Enter the breadth of Rectangle : '))
Area=l*b
Perimeter=2*(l+b)
print('Area = ',Area)
print('Perimeter = ',Perimeter)
__________________________________________________________________________________________________________________________________________________
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r=float(input('Enter the radius : '))
volume=4/3*math.pi*r**3
print(F'{volume=:.2f}')
____________________________________________________________________________________________________________________________________________________
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
p=float(input('Enter principle : '))
t=float(input('Enter time : '))
r=float(input('Enter rate of intrest : '))
SI=p*t*r/100
A=p*(1+r/100)**t
CI=A-p
print(f'{SI=}')
print(f'{CI=:.2f}')
_________________________________________________________________________________________________________________________________________________________________
'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
print(f'before swap :{a=}  {b=}')
temp=a
a=b
b=temp
print(f'after swap: {a=}   {b=}')
_____________________________________________________________________________________________________________________________________________________________________
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
print(f'before swap :{a=}  {b=}')
a=a+b  #35
b=a-b  #15
a=a-b
print(f'after swap: {a=}   {b=}')
__________________________________________________________________________________________________________________________________________________________________________
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
print(f'before swap :{a=}  {b=}')
a=a*b  #35
b=a/b  #15
a=a/b
print(f'after swap: {a=}   {b=}')
_________________________________________________________________________________________________________________________________________________________________________________
# Identify  error
else:
		print('else  suite')
print('Outside')

#else cannot be without if condition
_________________________________________________________________________________________________________________________________________________________________________________
# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

#syntax error condition must have :
___________________________________________________________________________________________________________________________________________________________________________________
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
#IndentationError
___________________________________________________________________________________________________________________________________________________________________________________
# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
#else should have :
__________________________________________________________________________________________________________________________________________________________________________________
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
#IndentationError
__________________________________________________________________________________________________________________________________________________________________________________
# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
#if and else should be aligned
____________________________________________________________________________________________________________________________________________________________________________________
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

#statements should not be in{}
_____________________________________________________________________________________________________________________________________________________________________________________
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
#indendtation error
_______________________________________________________________________________________________________________________________________________________________________________________
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a=int(input('Enter a number : '))
if(a%2==0):
   print('it is an even number')
else:
   print('it is an odd number')
_________________________________________________________________________________________________________________________________________________________________________________
# Find outputs  (Home  work)
if():                 #empty means False so else block executes
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One') #One
        print('Two') #Two
        print('Three') #Three
print('Bye') #Bye
_________________________________________________________________________________________________________________________________________________________________________________
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')  #Hyd
        print('Sec')  #Sec
        print('Cyb')  #Cyb
print('Bye')   #Bye
_______________________________________________________________________________________________________________________________________________________________________________
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  #Bye
_________________________________________________________________________________________________________________________________________________________________________
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
month=int(input('Enter month number : '))
if(month==1):
    print('January')
elif(month==2):
    print('February')
elif(month==3):
    print('March')
elif(month==4):
    print('April')
elif(month==5):
    print('May')
elif(month==6):
    print('June')
elif(month==7):
    print('July')
elif(month==8):
    print('August')
elif(month==9):
    print('September')
elif(month==10):
    print('October')
elif(month==11):
    print('November')
elif(month==12):
    print('December')
else:
    default('Number should be between(1-12)')
except:
    print('Enter valid number')
_________________________________________________________________________________________________________________________________________________________________________________
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
n=int(input('Enter a number(0-9)'))
if(n==0):
    print("Zero")
else:
        if(n==1):
            print("one")
        else:
            if(n==2):
                print("Two")
            else:
                if(n==3):
                    print("Three")
                else:
                    if(n==4):
                        print("four")
                    else:
                        if(n==5):
                            print("five")
                        else:
                            if(n==6):
                                print("Six")
                            else:
                                if(n==7):
                                    print("Seven")
                                else:
                                    if(n==8):
                                        print("Eight")
                                    else:
                                        if(n==9):
                                            print("Nine")
                                        else:
                                            if(n==10):
                                                print("invalid")
                                            else:
                                                print("Enter the correct value")
___________________________________________________________________________________________________________________________________

                      


