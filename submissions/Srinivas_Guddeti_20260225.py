a = complex(input("enter 1st complex number : "))
b = complex(input("enter 2nd complex number : "))

sum = a + b
difference = a - b
product = a * b
division = a / b

print(f"sum : {sum}")
print(f"difference : {difference}")
print(f"product : {product}")
print(f"division : {division}")




import math
l=eval(input("enter the length  :"))
b=eval(input("enter the breadth:"))
perimeter = 2*(l+b);
area = l*b ;
print(f"the perimeter of the given lenghth and breadth is : {perimeter}")
print(f"the area of the given length and breadth is :{area}")



import math
r = float(input("enter the radius  : "))
volume = 4/3 * math.pi * r**3
print(f"the volume of the sphere is : {volume:.2f}")




import math
p=int(input("enter the principal ammount   :"))
t=int(input("enter the time:"))
r=float(input("enter the rate:"))
simpleIntrest = p * t * r / 100
compoundIntrest = p * (1  +  r  /  100)**t  -  p
print(f"simple Intrest : {simpleIntrest}")
print(f"compound Intrest :{compoundIntrest:.3f}")


# ...........(Home  work)
# Write  a  program  to  swap  values  of  two   objects   using  3rd  object

# Let  x = 10  and  y = Hyd
# What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

x=10 
y=hyd 
z=temp
x= input("enter 1st input :")
y= input("enter 2nd input :")
