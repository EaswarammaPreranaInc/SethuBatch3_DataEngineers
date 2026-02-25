
'''Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
def rectangle():
    l=float(input("enter the lenght of rectangle :"))
    b=float(input("enter the breadth of rectangle :"))
    print(f'perimeter of rectangle: {2*(l+b)}')
    print(f'perimeter of rectangle: {l*b}')
#rectangle()


'''Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
def sphere():
    r=float(input("enter the radius :"))
    print(f'Volume : {4/3*math.pi*r**3:.2f}')
#sphere()



'''Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p'''
def interest():
    p=float(input("enter principle amt"))
    t=float(input("enter time"))
    r=float(input("enter rate of interest"))
    print(f'simple interset : { p*t*r / 100}')
    print(f'compound interset : { p * (1  +  r  /  100) **  t  -  p:.2f}')
    
#interest()

'''(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10'''
def swap():
    print("give string in double or single qoutes")
    a=eval(input("enter the first value"))
    b=eval(input("enter the second value"))
    print(f'before Swap :{a=}\t{b=}')
    temp=a
    a=b
    b=temp
    print(f'before Swap :{a=}\t{b=}')
    
#swap()
def evenOrOdd():
    i=int(input("enter +ve integer : "))
    if(i%2==0):
        print(f"{i} is Even Number ")
    if(i%2!=0):
        print(f"{i} is Odd Number ")
#evenOrOdd()
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')         # else block is executed
        print('Two')
        print('Three')
print('Bye')                  #bye this always printes


if{10 : 20 , 30 : 40}:
        print('Hyd')               # hyd
        print('Sec')               # sec
        print('Cyb')               # Cyb
print('Bye')                       # Bye
''' Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)'''
def month():
     m=int(input("enter month number between(1-12) : "))
     if(m<1 or m>12):
          print("enter month number between(1-12) ")
     elif m == 1:
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
#month()

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
def leap():
      y=int(input("enter Year : "))
      if((y%4==0 and y%100!=0)or (y%400==0)):
            print(f'{y} is leap Year')
      else:
            print(f'{y} is not leap Year')
#leap()


'''Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
''' 
def tempTofreh():
      c=int(input(' enter 1 convert  celsius  temperature  to  farenheit\n enter 2 convert  farenheit to celsius temperature : '))
      if(c==1):
            temp=float(input('enter celsius temperatur : '))
            print(f' farenheit temp : {1.8 * temp + 32:.2f}')
      if(c==2):
            temp=float(input('enter ferhinheit temperatur : '))
            print(f'celsius degrees : { (temp - 32) / 1.8:.2f}')
#tempTofreh()

'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers'''
def program():
      a=float(input("enter number 1  : "))
      b=float(input("enter number 2  : "))
      c=float(input("enter number 3  : "))
      ma=max(a,b,c)
      mi=min(a,b,c)
      mid=(a+b+c)-(ma+mi)
      print(f'Largest input  : {ma}')
      print(f'smallest input : {mi}')
      print(f'middle input   : {mid}')
      
#program()