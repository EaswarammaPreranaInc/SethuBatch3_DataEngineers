#8 Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except:
    print("enter valid num")

#9 Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif
try:
    mon = int(input("Enter month (1-12) : "))
    if mon==1:
        print("Jan")
    elif mon==2:
        print("Feb")
    elif mon==3:
        print("Mar")
    elif mon==4:
        print("Apr")
    elif mon==5:
        print("May")
    elif mon==6:
        print("Jun")
    elif mon==7:
        print("Jul")
    elif mon==8:
        print("Aug")
    elif mon==9:
        print("Sep")
    elif mon==10:
        print("Oct")
    elif mon==11:
        print("Nov")
    elif mon==12:
        print("Dec")
    else:
        print("enter between (1-12)")
except:
    print("enter a valid mon num")

#10 Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
try :
    num = int(input("Emter any num(0-9) : "))
    if num >= 0 and num <=9 :
        if num == 0:
            print("Zero")
        else:
            if num == 1:
                print("One")
            else:
                if num == 2:
                    print("Two")
                else:
                    if num == 3:
                        print("Three")
                    else:
                        if num == 4:
                            print("Four")
                        else:
                            if num == 5:
                                print("Five")
                            else:
                                if num == 6:
                                    print("Six")
                                else:
                                    if num == 7:
                                        print("Seven")
                                    else:
                                        if num == 8:
                                            print("Eight")
                                        else:
                                            if num == 9:
                                                print("Nine")
    else :
        print("Enter between 0-9")
except:
    print("input must be an integer")

#11 Write a program to print is given num is a leap year or not 
try:
    year = int(input("Enter 4-Digit year : "))
    if year%4 == 0 and year%100 != 0 or year%400 == 0 :
        print("Not a Leap year")
    else:
        print("Not a Leap year")
except:
    print("input should be an integer")    

#12 Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
try:
    a = eval(input("Enter 1st num : "))
    b = eval(input("Enter 2nd num : "))
    c = eval(input("Enter 3rd num : "))
    if a>=b and a>=z :
        print("Largest input : ", a)
    elif b>c:
        print("Largest input : ", b)
    else :
        print("Largest input : ", c)
except NameError:
    print("input string should be in quotes")
except TypeError:
    print("input can not be a complex number")

#13 Write a program to add ,subtract,product and multiples of complex num
try:
    x=complex(input("enter 1st compllex num :"))
    y=complex(input("enter 2nd compllex num :"))
    print("sum:" ,x+y)
    print("difference:",x-y)
    print("Product: ",x*y)
    print("Division: ",x/y)
except:
    print("input should be a complex num")
    
#14 Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try: 
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except :
    print("input should be integer")

#15 Write a program to convert celsius to temperature to farenhit and vice-versa
try:
    ch = int(input("enter 1 to covert celsius to forenhit and 2 to convert foenhit to celsius :"))
    if ch == 1:
        c = float(input("Enter celsius temperature :"))
        print("Fahrenheit equivalent : ",1.8*c+32)
    elif ch==2:
        f = float(input("Enter fahrenheit temperature : "))
        print(F"celsius equivalent : {(f-32)/1.8:.2f}")
    else:
        print("Invalid input")
except:
    print("input should ba a number")

#16 Write a program fo =r x and y axis
try:
    x = int(input("Enter value of x co-ordinate : "))
    y = int(input("Enter value of y co-ordinate : "))
    if x>=1 and y >= 1:
        print("1st Quadrant")
    elif -1>=x and y >= 1:
        print("2nd Quadrant")
    elif -1>=x and -1 >= y:
        print("3rd Quadrant")
    elif x >= 1 and -1 >= y:
        print("4th Quadrant")
    elif x != 0 and y ==0 :
        print("5th Quadrant")
    elif x ==0 and y != 0:
        print("6th Quadrant")
    elif x==0 and y ==0 :
        print("Origin")
except:
    print("incorrect input")

#17 Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
try:
    a = int(input("Enter first input :" ))
    b = int(input("Enter second input :" ))
    c = int(input("Enter third input :" ))
    max = a
    if b > max: 
        max = b
    if  c > max:
        max = c
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    mid = (a+b+c)-(max+min)
    print("Largest input : ",max)
    print("smallest input : ",min)
    print("middle input : ",mid)
except:
    print("enter a valid input")
