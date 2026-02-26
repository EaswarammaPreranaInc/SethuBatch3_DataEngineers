
import math

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))



if(a+b > c or b+c > c or c+a >b):
    if(a == b and b == c and a == c):
        print("Eqilateral triangle ")
        print(f'Area = {sqrt(3)/4*a**2:.2f}')
    elif(a == b or b ==c or c ==a):
        print("Isoscles triangle")
        print(f'Area : {a+b+c:.2f}')
    elif( a != b and b != c and c!=a):
        s = (a+b+c)/2
        print("Scalene triangle")
        print(f'Area of scalene : abs.{math.sqrt(s * (s-a) * (s-b) * (s-c))}')
        print(f'Perimeter : {a+b+c}')
else:
    print("not a triangle")
        



