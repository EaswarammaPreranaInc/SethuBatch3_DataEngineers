#Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers


a=complex(input("enter first complex number : "))
b=complex(input("enter second complex nimber : "))
sum=a+b
difference=a-b
product=a*b
division=a/b
print("sum : ",sum)
print("difference : ",difference)
print("product : ",product)
print("division : ",division)



#(Home  work)
#Write  a  program  to  determine  area  and  perimeter  of  rectangle
try:
    l=float(input("enter length of rectangle : "))
    b=float(input("enter beardth of rectangle : "))
    Area=l*b
    perimeter=2*(l+b)
    print("Area :",Area)
    print("perimeter :",perimeter)
except :
    print("input must be  number" )



#(Home  work)
#Write  a  program  to  determine  volume  of  a  sphere
#) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
try:
    from math import pi
    r=float(input("Enter radius : "))
    volume=4/3*(pi*r**3)
    print("volume : ",volume)
except:
    print("input must be a number")
_____
#(Home  work)
#Write  a  program  to  determine#What  is  simple  interest  formula ?  --->  ptr / 100  and 
#What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p  simple  interest  and  compound  interest

try:        
    p=int(input("Enter price :"))
    t=int(input("Enter time : "))
    r=float(input("Enter rate of intrest : "))
    simple_intrest=(p*t*r)/100
    compound_intrest=p*(1+r/100)**t-p
    print("simple intrest :",simple_intrest)
    print("compound intrest : ",compound_intrest)
except:
    print("inputs must be number")


#(Home  work)
#Write  a  program  to  swap  values  of  two   objects   using  3rd  object
#Let  x = 10  and  y = Hyd
#What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

try:
    a=eval(input("Enter 1st input : "))
    b=eval(input("Enter 2nd input : "))
    print(f'Before swap : {a=} \t {b=} ' )
    temp=0
    temp=b
    b=a
    a=temp
    print(f'After swap : {a=} \t {b=} ' )
except NameError:
    print("inputs must be string")
except :
    print("Enter valid inputs.")


#(Home  work)
#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
#Hint: One  addition  and  two  subtractions
#x = 25
#y =  10
try:
    a=int(input("Enter 1st input : "))
    b=int(input("Enter 2nd input : "))
    print(f'Before swap : {a=} \t {b=} ' )
    a=a+b
    b=a-b
    a=a-b
    print(f'After swap : {a=} \t {b=} ' )
except :
    print("Enter valid inputs")

#(Home  work)
#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
#Hint: One  multiplication  and  two  divisions
#x =  25
#y =  10
try:
    a=int(input("Enter 1st input : "))
    b=int(input("Enter 2nd input : "))
    print(f'Before swap : {a=} \t {b=} ' )
    a=a*b
    b=int(a/b)
    a=int(a/b)
    print(f'After swap : {a=} \t {b=} ' )
except :
    print("Enter valid input numbers")


_______________________________________
# Identify  error
else:
		print('else  suite')
print('Outside')
####syntax error  without if else not used .
_______________________________________
# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
###colon":"missing after the if condition
______________________________

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
###colon":"missing after the  else condition

_____________________________
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
#after the end of  colon ":"  next line should start with <space>or <tab> key
________________

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
#if and else should be in same indentation i.e in same column
________________________________________
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
#both syntax error and indentation error 
_________________________
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
#After an else: statement, expects an indented block, but due to  another if at the same level, so indentation error 
______________________________
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')#One
        print('Two')#Two
        print('Three')#Three

        
print('Bye')#Bye
_______
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')#Hyd
        print('Sec')#Sec
        print('Cyb')#Cyb
print('Bye')#Bye
____________________________________
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')#Bye
__________________________
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
    a=int(input("Enter Number: "))
    if (a%2==0): 
         print(a ,"is even Number")
    if (a%2!=0):
        print(a,"it is odd Number ")
except :
    print("enter valid input Number")


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
    month=int(input("Enter Month Number(1-12) : "))
    if(month==1):
        print("January")
    elif(month==2):
        print("February")
    elif(month==3):
        print("March")
    elif(month==4):
        print("April")
    elif(month==5):
        print("May")
    elif(month==6):
        print("June")
    elif(month==7):
        print("July")
    elif(month==8):
        print("August")
    elif(month==9):
       print("Septumber")
    elif(month==10):
        print("October")
    elif(month==11):
        print("November")
    elif(month==12):
       print("December")
    else:
        print("Input should be between 1 and 12")
except:
    print(" Input should be integer  ")


#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
#0 - Zero
#1 - One
#2 - Two
#....
#9 - Nine
#10 - Invalid
try:
    digit=int(input("Enter digit (0-9) : "))
    if( digit==0):
        print("zero")
    else:
        if( digit==1):  
             print("one")
        else:
            if( digit==2):
                print("Two")
            else:
                if(digit==3):
                    print("Three")
                else:
                    if(digit==4):
                        print("Four")
                    else:
                        if(digit==5):
                            print("Five")
                        else:
                            if(digit==6):
                                 print("Six")
                            else:
                                if(digit==7):
                                     print("Seven")
                                else:
                                        if(digit==8):
                                         print("Eight")
                                        else:
                                            if(digit==9):
                                              print("Nine")
   
                                            else:
                                                print("Input should be between 1 and 12")
except:
    print(" Input should be (0-9) ")


#Write  a  program  to  test  year  is  leap  year  or  not
#Hint:  3  conditions
year=int(input("Enter 4 digit year : "))
if((year%4==0) or (year%400==0 and year%100!=0)):
    print("leap year")
else:
    print("it is not a leap year")   



#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
#Hint:  Write  multiple  conditions
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
if(a>b)and(a>c):
    print(a,"is largest Number amoung three numbers")
else :
    if b>c and b>a :
        print(b,"is largest Number amoung three numbers")

    else :
        print(c,"is largest Number amoung three numbers")


#Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

#1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

#2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8


temp=int(input(" Enter 1 to convert  celcius to farenheit and 2 to convert fahrenheit to celsius :"))
if(temp==1):
    a=int(input("enter celsius temperature:"))
    print(" fahrenheit temperature : ",1.8*a+32)
elif(temp==2):
     b=int(input(" enter fahrenheit temperature:"))
     print(" celcius temperature : ",(b-32)/1.8)
else:
     print("invalid input  ")

