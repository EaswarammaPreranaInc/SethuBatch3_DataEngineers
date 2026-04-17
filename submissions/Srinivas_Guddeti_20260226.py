





# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
# Center  is  origin  and  radius  is  'r'

# 1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

# 2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

# 3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

# 4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle

import math

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
r = float(input("Enter radius: "))

# Distance from origin
distance = math.sqrt(x**2 + y**2)

print("Distance from origin =", distance)

if distance > r:
    print("Point is Outside the circle")

elif distance < r:
    print("Point is Inside the circle")

else:
    print("Point is On the circle")